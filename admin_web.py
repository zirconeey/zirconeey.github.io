#!/usr/bin/env python3
"""
Zircon 知识库控制台 V8.3
"""

import os, json, time, webbrowser, threading, re, sys, traceback
from pathlib import Path
from flask import Flask, request, jsonify, Response
from werkzeug.utils import secure_filename

app = Flask(__name__)

WORK_DIR = Path.cwd().resolve()
NOTES_DIR = (WORK_DIR / "_notes").resolve()
CONFIG_FILE = (WORK_DIR / "_config.yml").resolve()
UPLOAD_DIR = (WORK_DIR / "files" / "images").resolve()

MAIN_CATE_MAP = {
    "courses":  "🎒 课程资料",
    "research": "🔬 科研妙招",
    "life":     "☕ 生活攻略",
    "essays":   "✒️ 随笔漫谈",
}

FIELDS = ['title', 'main_category', 'sub_category', 'published', 'discipline',
          'course', 'material_type', 'date', 'author', 'permalink', 'pdf_url']


def parse_note(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    info = {field: "" for field in FIELDS}
    info['published'] = "true"
    yaml_lines, body_lines = [], []
    dash_count = 0
    for line in lines:
        if dash_count < 2:
            yaml_lines.append(line)
            if line.strip() == "---":
                dash_count += 1
            if dash_count == 1 and ":" in line:
                for field in FIELDS:
                    if line.startswith(f"{field}:"):
                        val = line.split(":", 1)[1].strip()
                        # 只有当两端都是同种引号且长度>=2才脱引号
                        if len(val) >= 2 and (
                            (val[0] == '"' and val[-1] == '"') or
                            (val[0] == "'" and val[-1] == "'")
                        ):
                            val = val[1:-1]
                        info[field] = val
        else:
            body_lines.append(line)
    return info, yaml_lines, "".join(body_lines)


def is_safe_path(base_dir, target_path):
    try:
        base = Path(base_dir).resolve()
        target = Path(target_path).resolve()
        # 兼容 Python 3.8 (用 startswith 而不是 is_relative_to)
        return str(target).startswith(str(base))
    except Exception:
        return False


def log_exception(endpoint, e):
    """打印异常到终端"""
    print(f"\n━━━━ ❌ 异常在 {endpoint} ━━━━", file=sys.stderr)
    traceback.print_exc()
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━\n", file=sys.stderr)


# =================== API ===================

@app.errorhandler(Exception)
def handle_any_error(e):
    """全局兜底：任何未捕获的异常都返回 JSON 而不是 HTML"""
    tb = traceback.format_exc()
    print(f"\n━━━━ ❌ 未捕获异常 ━━━━\n{tb}━━━━━━━━━━━━━━━━━\n", file=sys.stderr)
    return jsonify({
        "error": str(e),
        "type": type(e).__name__,
        "traceback": tb.split("\n")[-4] if tb else "",
    }), 500


@app.route("/api/notes")
def api_notes():
    try:
        buckets = {k: {"main_id": k, "main_name": v, "subfolders": {}}
                   for k, v in MAIN_CATE_MAP.items()}

        if not NOTES_DIR.exists():
            return jsonify({"tree": list(buckets.values())})

        for md_file in sorted(NOTES_DIR.rglob("*.md")):
            try:
                rel = md_file.relative_to(NOTES_DIR)
            except Exception:
                continue
            parts = rel.parts
            if not parts:
                continue

            if parts[0] in MAIN_CATE_MAP:
                main_id = parts[0]
                sub_parts = parts[1:]
            else:
                main_id = "courses"
                sub_parts = parts

            if len(sub_parts) >= 2:
                sub_id = sub_parts[0]
            elif len(sub_parts) == 1:
                sub_id = "_root"
            else:
                continue

            try:
                info, _, _ = parse_note(md_file)
            except Exception as e:
                print(f"  ⚠️ parse_note 失败 {md_file}: {e}", file=sys.stderr)
                info = {"title": md_file.stem, "published": "true",
                        "course": "", "sub_category": ""}

            sub_name = info.get('course') or info.get('sub_category') \
                       or (sub_id if sub_id != "_root" else "(根目录)")

            subs = buckets[main_id]["subfolders"]
            if sub_id not in subs:
                subs[sub_id] = {"sub_id": sub_id, "sub_name": sub_name, "files": []}

            subs[sub_id]["files"].append({
                "path": str(md_file),
                "title": info.get('title') or md_file.stem,
                "published": info.get('published', 'true').lower() == 'true',
            })

        result = []
        for main_id, bucket in buckets.items():
            result.append({
                "main_id": bucket["main_id"],
                "main_name": bucket["main_name"],
                "subfolders": list(bucket["subfolders"].values()),
            })
        return jsonify({"tree": result})
    except Exception as e:
        log_exception("/api/notes", e)
        return jsonify({"error": str(e), "tree": []}), 500


@app.route("/api/note")
def api_get_note():
    try:
        filepath = request.args.get("path", "")
        print(f"📖 读取文件: {filepath}", file=sys.stderr)

        if not filepath:
            return jsonify({"error": "path 参数为空"}), 400
        if not Path(filepath).exists():
            return jsonify({"error": f"文件不存在: {filepath}"}), 404
        if not is_safe_path(NOTES_DIR, filepath):
            return jsonify({"error": f"路径不在 _notes 目录下: {filepath}"}), 403

        info, _, body = parse_note(filepath)
        return jsonify({"info": info, "body": body.lstrip("\n")})
    except Exception as e:
        log_exception("/api/note", e)
        return jsonify({"error": f"{type(e).__name__}: {str(e)}"}), 500


@app.route("/api/note", methods=["POST"])
def api_save_note():
    try:
        data = request.json
        filepath = data.get("path", "")
        new_info = data.get("info", {})
        new_body = data.get("body", "")

        if not filepath or not Path(filepath).exists() or not is_safe_path(NOTES_DIR, filepath):
            return jsonify({"error": "File not found"}), 404

        _, old_yaml_lines, _ = parse_note(filepath)
        out_yaml = []
        dash_count = 0
        written = set()

        for line in old_yaml_lines:
            if line.strip() == "---":
                dash_count += 1
                if dash_count == 2:
                    for f in FIELDS:
                        if f not in written and new_info.get(f):
                            v = new_info[f]
                            if v in ["true", "false"]:
                                out_yaml.append(f"{f}: {v}\n")
                            else:
                                out_yaml.append(f'{f}: "{v}"\n')
                out_yaml.append(line)
                continue
            if dash_count == 1:
                matched = False
                for f in FIELDS:
                    if line.startswith(f"{f}:"):
                        matched = True
                        written.add(f)
                        v = new_info.get(f, "")
                        if v:
                            if v in ["true", "false"]:
                                out_yaml.append(f"{f}: {v}\n")
                            else:
                                out_yaml.append(f'{f}: "{v}"\n')
                        break
                if not matched:
                    out_yaml.append(line)

        body = new_body if new_body.startswith("\n") else "\n" + new_body
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("".join(out_yaml) + body)
        return jsonify({"ok": True})
    except Exception as e:
        log_exception("/api/note POST", e)
        return jsonify({"error": f"{type(e).__name__}: {str(e)}"}), 500


@app.route("/api/note/new", methods=["POST"])
def api_new_note():
    try:
        data = request.json
        main_id = data.get("main_id", "courses").strip()
        sub_folder = secure_filename(data.get("sub_folder", "").strip())
        filename = data.get("filename", "").strip()
        title = data.get("title", "").strip() or filename
        has_pdf = data.get("has_pdf", False)

        if main_id not in MAIN_CATE_MAP:
            return jsonify({"error": "无效的大类"}), 400
        if not sub_folder or not filename:
            return jsonify({"error": "子分类和文件名不能为空"}), 400
        if not filename.endswith('.md'):
            filename += '.md'

        target_dir = NOTES_DIR / main_id / sub_folder
        target_dir.mkdir(parents=True, exist_ok=True)
        filepath = target_dir / filename
        if filepath.exists():
            return jsonify({"error": "文件已存在"}), 400

        import datetime
        today = datetime.date.today().strftime("%Y-%m-%d")
        main_display = MAIN_CATE_MAP[main_id].split(" ", 1)[-1]
        file_stem = filename.replace('.md', '')
        route_map = {"courses": "notes", "research": "research",
                     "life": "life", "essays": "essays"}
        permalink = f"/{route_map[main_id]}/{sub_folder}/{file_stem}"
        pdf_url = f"/files/{sub_folder}/{file_stem}.pdf" if has_pdf else ""

        yaml_lines = ["---\n", "layout: post\n", f'title: "{title}"\n',
                      f'main_category: "{main_display}"\n']
        if main_id == "courses":
            yaml_lines.extend([
                'discipline: "经济学"\n',
                f'course: "{sub_folder}"\n',
                'material_type: "Notes"\n',
            ])
        else:
            yaml_lines.append(f'sub_category: "{sub_folder}"\n')
        yaml_lines.extend([
            f"date: {today}\n",
            'author: "Zircon"\n',
            f'permalink: "{permalink}"\n',
        ])
        if pdf_url:
            yaml_lines.append(f'pdf_url: "{pdf_url}"\n')
        yaml_lines.append('published: true\n')
        yaml_lines.append("---\n\n")

        if has_pdf and main_id == "courses":
            body = """## 讲义在线预览与下载
> 手机端和平板端可能不能获得最佳的预览效果，请点击下方按钮下载

<div class="pdf-container" style="margin: 2rem 0;">
  <div class="pdf-preview">
    <iframe src="{{ page.pdf_url }}" width="100%" height="600px" style="border: 1px solid var(--color-border); border-radius: 8px;"></iframe>
  </div>
  <div style="margin-top: 1rem; text-align: center;">
    <a href="{{ page.pdf_url }}" download>📥 下载完整版 PDF 讲义</a>
  </div>
</div>
"""
        else:
            body = "\n在这里开始书写你的文章正文吧...\n"

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("".join(yaml_lines) + body)
        return jsonify({"ok": True, "path": str(filepath)})
    except Exception as e:
        log_exception("/api/note/new", e)
        return jsonify({"error": f"{type(e).__name__}: {str(e)}"}), 500


@app.route("/api/note/rename", methods=["POST"])
def api_rename_note():
    try:
        data = request.json
        old_path = data.get("old_path", "")
        new_name = data.get("new_name", "").strip()
        if not old_path or not new_name or not Path(old_path).exists() \
           or not is_safe_path(NOTES_DIR, old_path):
            return jsonify({"error": "无效的路径"}), 400
        if not new_name.endswith('.md'):
            new_name += '.md'
        old_file = Path(old_path)
        new_file = old_file.parent / new_name
        if new_file.exists():
            return jsonify({"error": "新文件名已存在"}), 400
        old_file.rename(new_file)
        return jsonify({"ok": True, "new_path": str(new_file)})
    except Exception as e:
        log_exception("/api/note/rename", e)
        return jsonify({"error": str(e)}), 500


@app.route("/api/note/delete", methods=["POST"])
def api_delete_note():
    try:
        data = request.json
        filepath = data.get("path", "")
        if not filepath or not Path(filepath).exists() \
           or not is_safe_path(NOTES_DIR, filepath):
            return jsonify({"error": "无效的路径"}), 400
        file_to_del = Path(filepath)
        folder = file_to_del.parent
        file_to_del.unlink()
        try:
            if folder.exists() and not any(folder.iterdir()):
                folder.rmdir()
        except Exception:
            pass
        return jsonify({"ok": True})
    except Exception as e:
        log_exception("/api/note/delete", e)
        return jsonify({"error": str(e)}), 500


@app.route("/api/upload", methods=["POST"])
def api_upload():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "没有图片"}), 400
        file = request.files['image']
        if not file.filename:
            return jsonify({"error": "文件名无效"}), 400
        UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
        ext = Path(file.filename).suffix or ".png"
        new_name = f"img_{int(time.time())}{ext}"
        file.save(UPLOAD_DIR / new_name)
        return jsonify({"url": f"/files/images/{new_name}"})
    except Exception as e:
        log_exception("/api/upload", e)
        return jsonify({"error": str(e)}), 500


@app.route("/api/courses")
def api_get_courses():
    try:
        print(f"📋 读取课程列表", file=sys.stderr)
        folder_to_info = {}

        courses_dir = NOTES_DIR / "courses"
        print(f"   courses_dir: {courses_dir} (exists={courses_dir.exists()})", file=sys.stderr)

        if courses_dir.exists():
            md_count = 0
            for md_file in courses_dir.rglob("*.md"):
                md_count += 1
                try:
                    info, _, _ = parse_note(md_file)
                except Exception as e:
                    print(f"   ⚠️ parse 失败 {md_file.name}: {e}", file=sys.stderr)
                    continue
                folder = md_file.parent.name
                if folder not in folder_to_info:
                    folder_to_info[folder] = {
                        "name": info.get('course', '') or folder,
                        "discipline": info.get('discipline', '') or '未分类',
                    }
            print(f"   courses/ 下找到 {md_count} 个 md 文件, {len(folder_to_info)} 个课程文件夹", file=sys.stderr)

        # 旧结构兼容
        if NOTES_DIR.exists():
            for p in NOTES_DIR.iterdir():
                if p.is_dir() and p.name not in MAIN_CATE_MAP:
                    for md_file in p.rglob("*.md"):
                        try:
                            info, _, _ = parse_note(md_file)
                        except Exception:
                            continue
                        folder = md_file.parent.name
                        if folder not in folder_to_info:
                            folder_to_info[folder] = {
                                "name": info.get('course', '') or folder,
                                "discipline": info.get('discipline', '') or '未分类',
                            }

        courses = []
        if CONFIG_FILE.exists():
            print(f"   读取 {CONFIG_FILE}", file=sys.stderr)
            in_block = False
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.startswith("course_order:"):
                        in_block = True
                        continue
                    if in_block:
                        s = line.strip()
                        if s.startswith("-"):
                            raw = s[1:].strip()
                            info = folder_to_info.get(raw,
                                                       {"name": raw, "discipline": "未分类"})
                            courses.append({"folder": raw, "name": info["name"],
                                             "discipline": info["discipline"]})
                        elif s == "" or s.startswith("#"):
                            continue
                        elif not line.startswith(" ") and not line.startswith("\t"):
                            break
        else:
            print(f"   ⚠️ {CONFIG_FILE} 不存在", file=sys.stderr)

        print(f"   返回 {len(courses)} 门课程", file=sys.stderr)
        return jsonify({"courses": courses,
                        "all_folders": {k: v["name"] for k, v in folder_to_info.items()}})
    except Exception as e:
        log_exception("/api/courses", e)
        return jsonify({"error": str(e), "courses": [], "all_folders": {}}), 500


@app.route("/api/courses", methods=["POST"])
def api_save_courses():
    try:
        data = request.json
        folders = data.get("folders", [])
        if not CONFIG_FILE.exists():
            return jsonify({"error": "Config not found"}), 404

        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        out, in_block, replaced = [], False, False
        for line in lines:
            if line.startswith("course_order:"):
                in_block = True
                replaced = True
                out.append(line)
                for c in folders:
                    out.append(f"  - {c}\n")
                continue
            if in_block:
                s = line.strip()
                if s.startswith("-") or s == "" or s.startswith("#"):
                    continue
                elif not line.startswith(" ") and not line.startswith("\t"):
                    in_block = False
                    out.append(line)
            else:
                out.append(line)

        if not replaced:
            out.append("\ncourse_order:\n")
            for c in folders:
                out.append(f"  - {c}\n")

        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            f.writelines(out)
        return jsonify({"ok": True})
    except Exception as e:
        log_exception("/api/courses POST", e)
        return jsonify({"error": str(e)}), 500


def diagnose():
    print("\n" + "━"*60)
    print("📊 启动诊断")
    print("━"*60)
    print(f"  工作目录:   {WORK_DIR}")
    print(f"  _notes 路径: {NOTES_DIR}")
    print(f"  _notes 存在: {'✅' if NOTES_DIR.exists() else '❌'}")
    print(f"  _config.yml: {'✅' if CONFIG_FILE.exists() else '❌'}")
    if NOTES_DIR.exists():
        for main_id in MAIN_CATE_MAP.keys():
            p = NOTES_DIR / main_id
            if p.exists():
                count = len(list(p.rglob("*.md")))
                print(f"    └─ {main_id}/: {count} 个 .md")
    print("━"*60 + "\n")


HTML = r'''<!DOCTYPE html>
<html lang="zh-CN"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Zircon V8.3</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.css">
<style>
:root{--bg:#fafaf9;--bg2:#f0efeb;--bg3:#e8e7e3;--ink:#1a1a2e;--text:#374151;--muted:#6b7280;--light:#9ca3af;--border:#d5d4cf;--accent:#1e3a5f;--green:#16a34a;--red:#dc2626;--gold:#c9a96e;--font:'Source Sans 3',-apple-system,'PingFang SC',sans-serif;--mono:'JetBrains Mono','Fira Code','Consolas',monospace}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:var(--font);background:var(--bg);color:var(--text);height:100vh;display:flex;flex-direction:column;overflow:hidden}
button{font-family:var(--font);cursor:pointer}
.topbar{background:var(--ink);color:#e8e6e3;padding:.6rem 1.5rem;display:flex;align-items:center;justify-content:space-between;flex-shrink:0}
.topbar h1{font-size:1rem;font-weight:500}
.tabs{display:flex}
.tab{padding:.45rem 1.2rem;font-size:.85rem;color:#8a8680;background:none;border:none;border-bottom:2px solid transparent;transition:all .2s}
.tab:hover{color:#e8e6e3}
.tab.active{color:#e8e6e3;border-bottom-color:var(--gold)}
.panel{display:none!important;flex:1;overflow:hidden}
.panel.active{display:flex!important}
.sidebar{width:320px;min-width:280px;border-right:1px solid var(--border);display:flex;flex-direction:column;background:var(--bg2);flex-shrink:0}
.sidebar-header{padding:.8rem 1rem;font-size:.8rem;font-weight:600;color:var(--muted);text-transform:uppercase;letter-spacing:.08em;border-bottom:1px solid var(--border);display:flex;justify-content:space-between;align-items:center;gap:.4rem}
.sidebar-header button{font-size:.75rem;background:none;border:1px solid var(--border);padding:.25rem .6rem;border-radius:4px;color:var(--muted)}
.sidebar-header button:hover{border-color:var(--accent);color:var(--accent);background:white}
.file-tree{flex:1;overflow-y:auto;padding:.3rem 0}
.main-cat{padding:.5rem 1rem;font-size:.9rem;font-weight:700;color:var(--accent);cursor:pointer;user-select:none;display:flex;align-items:center;gap:.4rem;background:var(--bg3);border-top:1px solid var(--border)}
.main-cat:first-child{border-top:none}
.main-cat .arrow{font-size:.65rem;color:var(--muted);transition:transform .15s;display:inline-block;width:12px}
.main-cat .arrow.open{transform:rotate(90deg)}
.main-cat-children{display:none}
.main-cat-children.open{display:block}
.main-cat-empty{padding:.5rem 1rem .5rem 2.5rem;font-size:.8rem;color:var(--light);font-style:italic}
.sub-folder{padding:.4rem 1rem .4rem 2rem;font-size:.85rem;font-weight:600;color:var(--ink);cursor:pointer;user-select:none;display:flex;align-items:center;gap:.4rem}
.sub-folder:hover{background:var(--bg3)}
.sub-folder .arrow{font-size:.65rem;color:var(--muted);transition:transform .15s;display:inline-block;width:12px}
.sub-folder .arrow.open{transform:rotate(90deg)}
.sub-children{display:none}
.sub-children.open{display:block}
.file-item{padding:.35rem 1rem .35rem 3.2rem;font-size:.84rem;color:var(--text);cursor:pointer;user-select:none;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.file-item:hover{background:var(--bg3)}
.file-item.selected{background:#dbeafe;color:var(--accent);font-weight:500}
.editor-area{flex:1;display:flex;flex-direction:column;overflow:hidden}
.editor-toolbar{padding:.6rem 1.2rem;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;background:var(--bg);flex-shrink:0}
.filename{font-size:.88rem;color:var(--muted);font-family:var(--mono);display:flex;align-items:center;gap:.5rem}
.btn-icon{background:none;border:none;font-size:1rem;cursor:pointer;opacity:.55;transition:opacity .2s}
.btn-icon:hover{opacity:1}
.btn-save{background:var(--green);color:#fff;border:none;padding:.5rem 1.5rem;border-radius:6px;font-size:.85rem;font-weight:500}
.btn-save:hover{background:#15803d}
.yaml-form{padding:.8rem 1.2rem;border-bottom:1px solid var(--border);display:grid;grid-template-columns:auto 1fr auto 1fr auto 1fr;gap:.4rem .6rem;align-items:center;background:var(--bg2);flex-shrink:0}
.yaml-form label{font-size:.78rem;color:var(--muted);text-align:right;font-weight:500}
.yaml-form input,.yaml-form select{font-family:var(--mono);font-size:.82rem;padding:.3rem .5rem;border:1px solid var(--border);border-radius:4px;background:#fff;color:var(--text);outline:none;width:100%}
.yaml-form input:focus,.yaml-form select:focus{border-color:var(--accent)}
.yaml-form .full{grid-column:2/-1}
.cm-wrapper{flex:1;overflow:hidden}
.cm-wrapper .CodeMirror{height:100%;font-size:14px;line-height:1.6}
.empty-state{flex:1;display:flex;align-items:center;justify-content:center;color:var(--light);font-size:1.05rem}
.courses-page{flex:1;overflow-y:auto;padding:1.5rem 2rem}
.courses-inner{max-width:700px;margin:0 auto}
.courses-topbar{display:flex;justify-content:space-between;align-items:center;position:sticky;top:0;background:var(--bg);padding:.6rem 0 1rem;z-index:10}
.courses-topbar h2{font-size:1rem;color:var(--ink);margin:0}
.courses-topbar .btns{display:flex;gap:.6rem}
.btn-outline{background:none;border:1px solid var(--accent);color:var(--accent);padding:.4rem 1rem;border-radius:6px;font-size:.82rem}
.btn-outline:hover{background:var(--accent);color:#fff}
.disc-group{margin-bottom:1rem;border:1px solid var(--border);border-radius:8px;overflow:hidden;background:#fff}
.disc-header{padding:.55rem 1rem;background:var(--bg2);font-size:.85rem;font-weight:600;color:var(--ink);cursor:grab;user-select:none;display:flex;align-items:center;gap:.6rem;border-bottom:1px solid var(--border)}
.disc-header:active{cursor:grabbing}
.disc-arrow{font-size:.6rem;color:var(--muted);transition:transform .2s;display:inline-block;cursor:pointer}
.disc-arrow.open{transform:rotate(90deg)}
.disc-label{flex:1;cursor:pointer}
.disc-count{font-size:.75rem;color:var(--light);font-weight:400}
.disc-body{display:none}
.disc-body.open{display:block}
.course-item{padding:.55rem 1rem .55rem 2rem;border-bottom:1px solid var(--border);display:flex;align-items:center;gap:.8rem;cursor:grab;font-size:.9rem}
.course-item:last-child{border-bottom:none}
.course-item:hover{background:#f0f9ff}
.course-item:active{cursor:grabbing}
.course-name{flex:1;color:var(--ink)}
.course-folder{font-size:.75rem;color:var(--light);font-family:var(--mono)}
.sortable-ghost{opacity:.4;background:#dbeafe}
.toast{position:fixed;bottom:2rem;right:2rem;padding:.8rem 1.5rem;background:var(--ink);color:#fff;border-radius:8px;font-size:.88rem;opacity:0;transform:translateY(10px);transition:all .3s;z-index:999;pointer-events:none;max-width:500px}
.toast.show{opacity:1;transform:translateY(0)}
.toast.success{background:var(--green)}
.toast.error{background:var(--red)}
.modal-overlay{display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,.5);z-index:1000;align-items:center;justify-content:center}
.modal-box{background:white;padding:2rem;border-radius:8px;width:460px;max-width:90vw}
.modal-box h3{margin-bottom:1.2rem;color:var(--ink);text-align:center;border-bottom:1px solid var(--border);padding-bottom:.8rem}
.modal-box label{display:block;margin:.8rem 0 .3rem;font-size:.85rem;font-weight:600;color:var(--text)}
.modal-box .hint{font-size:.75rem;color:var(--muted);font-weight:400;margin-left:.4rem}
.modal-box input,.modal-box select{width:100%;padding:.55rem;border:1px solid var(--border);border-radius:4px;font-family:var(--mono);font-size:.85rem}
.modal-box input:focus,.modal-box select:focus{border-color:var(--accent);outline:none}
.modal-box .preview{margin-top:.8rem;padding:.6rem .8rem;background:var(--bg2);border-radius:4px;font-family:var(--mono);font-size:.78rem;color:var(--accent);min-height:1.8em}
.modal-btns{margin-top:1.5rem;display:flex;justify-content:flex-end;gap:.5rem}
.modal-btns button{padding:.5rem 1.2rem;border-radius:4px;border:none;font-weight:500}
.btn-cancel{background:#e5e7eb;color:var(--text)}
.btn-cancel:hover{background:#d1d5db}
.pdf-check{display:flex;align-items:center;gap:.5rem;margin-top:.8rem}
.pdf-check input{width:auto;margin:0}
</style></head>
<body>

<div class="topbar">
  <h1>Zircon 知识库控制台 V8.3</h1>
  <div class="tabs">
    <button class="tab active" data-tab="notes" onclick="switchTab('notes')">全站内容管理</button>
    <button class="tab" data-tab="courses" onclick="switchTab('courses')">课程专项排序</button>
  </div>
</div>

<div id="panel-notes" class="panel active">
  <div class="sidebar">
    <div class="sidebar-header">
      <span>数字花园树</span>
      <div>
        <button onclick="openModal()">➕ 新建</button>
        <button onclick="loadTree()">刷新</button>
      </div>
    </div>
    <div class="file-tree" id="file-tree"></div>
  </div>
  <div class="editor-area">
    <div class="empty-state" id="empty-state">← 从左侧选择一篇文章，或点击"新建"</div>
    <div id="editor-content" style="display:none;flex-direction:column;overflow:hidden;flex:1">
      <div class="editor-toolbar">
        <div class="filename">
          <span id="current-filename">—</span>
          <button class="btn-icon" onclick="renameFile()" title="重命名">✏️</button>
          <button class="btn-icon" onclick="deleteFile()" title="删除" style="color:var(--red)">🗑️</button>
        </div>
        <button class="btn-save" onclick="saveNote()">💾 保存 <span style="font-size:.72rem;color:rgba(255,255,255,.7);margin-left:.3rem">⌘S</span></button>
      </div>
      <div class="yaml-form">
        <label>title</label><input id="f-title" class="full" type="text">
        <label>main_category</label><select id="f-main_category"><option value=""></option><option>课程资料</option><option>科研妙招</option><option>生活攻略</option><option>随笔漫谈</option></select>
        <label>published</label><select id="f-published"><option value="true">true</option><option value="false">false</option></select>
        <label>date</label><input id="f-date" type="text">
        <label>discipline</label><input id="f-discipline" type="text">
        <label>course</label><input id="f-course" type="text">
        <label>sub_category</label><input id="f-sub_category" type="text">
        <label>material_type</label><select id="f-material_type"><option value="">—</option><option>Notes</option><option>Exams</option><option>Script</option><option>Tool</option><option>Life</option></select>
        <label>author</label><input id="f-author" type="text">
        <label>permalink</label><input id="f-permalink" class="full" type="text">
        <label>pdf_url</label><input id="f-pdf_url" class="full" type="text">
      </div>
      <div class="cm-wrapper"><textarea id="md-editor"></textarea></div>
    </div>
  </div>
</div>

<div id="panel-courses" class="panel">
  <div class="courses-page">
    <div class="courses-inner">
      <div class="courses-topbar">
        <h2>拖拽调整【课程资料】分类顺序</h2>
        <div class="btns">
          <button class="btn-outline" onclick="scanCourses()">自动导入新课程</button>
          <button class="btn-save" onclick="saveCourses()">💾 保存排序</button>
        </div>
      </div>
      <div id="disc-list"></div>
    </div>
  </div>
</div>

<div id="modal-new" class="modal-overlay">
  <div class="modal-box">
    <h3>➕ 新建文章</h3>
    <label>1. 选择所属大板块</label>
    <select id="new-main-id" onchange="updatePreview()">
      <option value="courses">🎒 课程资料</option>
      <option value="research">🔬 科研妙招</option>
      <option value="life">☕ 生活攻略</option>
      <option value="essays">✒️ 随笔漫谈</option>
    </select>
    <label>2. 文章标题</label>
    <input type="text" id="new-title" placeholder="如：宏观期中复习">
    <label id="lbl-sub">3. 子分类文件夹名</label>
    <input type="text" id="new-sub" placeholder="如：adv-macro" oninput="updatePreview()">
    <label>4. 文件名</label>
    <input type="text" id="new-filename" placeholder="如：mid-prep" oninput="updatePreview()">
    <div class="preview">
      <div style="font-size:.72rem;color:var(--muted);margin-bottom:.2rem">生成的 URL：</div>
      <div id="new-preview-url">—</div>
    </div>
    <div class="pdf-check">
      <input type="checkbox" id="new-has-pdf">
      <span style="font-size:.85rem;color:var(--text)">附带 PDF 下载模块</span>
    </div>
    <div class="modal-btns">
      <button class="btn-cancel" onclick="closeModal()">取消</button>
      <button class="btn-save" onclick="createNote()">🚀 创建</button>
    </div>
  </div>
</div>

<div class="toast" id="toast"></div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/markdown/markdown.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Sortable/1.15.0/Sortable.min.js"></script>
<script>
const FIELDS = ['title','main_category','sub_category','published','discipline','course','material_type','date','author','permalink','pdf_url'];
const ROUTE_MAP = {courses:'notes', research:'research', life:'life', essays:'essays'};
let currentFile=null, cleanInfo={}, cleanBody='', editor=null, initialSnap='';

window.addEventListener('DOMContentLoaded', ()=>{
  editor = CodeMirror.fromTextArea(document.getElementById('md-editor'),
    {mode:'markdown',lineNumbers:true,lineWrapping:true,tabSize:2});
  loadTree();
  document.addEventListener('keydown', e=>{
    if((e.metaKey||e.ctrlKey)&&e.key==='s'){e.preventDefault();if(currentFile)saveNote();}
  });
});

function toast(msg, type='success', duration=2500){
  const el=document.getElementById('toast');
  el.textContent=msg; el.className='toast show '+type;
  setTimeout(()=>el.className='toast', duration);
}

// 统一的 fetch 包装，返回 JSON + 错误友好处理
async function apiCall(url, options={}) {
  try {
    const res = await fetch(url, options);
    let data;
    try {
      data = await res.json();
    } catch(e) {
      // JSON 解析失败
      return {_error: `响应不是 JSON (HTTP ${res.status})`};
    }
    if (!res.ok && data.error) {
      return {_error: data.error, ...data};
    }
    if (!res.ok) {
      return {_error: `HTTP ${res.status}`};
    }
    return data;
  } catch (e) {
    return {_error: `网络错误: ${e.message}`};
  }
}

function switchTab(name){
  if(currentFile&&hasUnsavedNoteChanges() && !confirm('当前文章有未保存修改，继续？')) return;
  if(hasUnsavedCourseChanges() && !confirm('课程排序有未保存修改，继续？')) return;
  document.querySelectorAll('.tab').forEach(t=>t.classList.remove('active'));
  document.querySelectorAll('.panel').forEach(p=>p.classList.remove('active'));
  document.querySelector(`.tab[data-tab="${name}"]`).classList.add('active');
  document.getElementById(`panel-${name}`).classList.add('active');
  if(name==='courses') loadCourses();
}

async function loadTree(){
  const tree = document.getElementById('file-tree');
  tree.innerHTML = '<div style="padding:2rem 1rem;text-align:center;color:var(--light);font-size:.85rem">加载中...</div>';
  const data = await apiCall('/api/notes');
  if(data._error) {
    tree.innerHTML = `<div style="padding:1rem;color:var(--red);font-size:.8rem">加载失败：${data._error}</div>`;
    return;
  }
  tree.innerHTML = '';
  data.tree.forEach(mainNode => {
    const mainDiv = document.createElement('div');
    const mainHdr = document.createElement('div');
    mainHdr.className = 'main-cat';
    const hasContent = mainNode.subfolders.length > 0;
    mainHdr.innerHTML = `<span class="arrow ${hasContent?'open':''}">▶</span>${mainNode.main_name}`;
    const mainCh = document.createElement('div');
    mainCh.className = 'main-cat-children' + (hasContent?' open':'');
    mainHdr.onclick = () => {
      mainCh.classList.toggle('open');
      mainHdr.querySelector('.arrow').classList.toggle('open');
    };
    if(!hasContent) {
      const empty = document.createElement('div');
      empty.className = 'main-cat-empty';
      empty.textContent = '（暂无内容）';
      mainCh.appendChild(empty);
    } else {
      mainNode.subfolders.forEach(subNode => {
        const subHdr = document.createElement('div');
        subHdr.className = 'sub-folder';
        subHdr.innerHTML = `<span class="arrow">▶</span>📂 ${subNode.sub_name}`;
        const subCh = document.createElement('div');
        subCh.className = 'sub-children';
        subHdr.onclick = () => {
          subCh.classList.toggle('open');
          subHdr.querySelector('.arrow').classList.toggle('open');
        };
        subNode.files.forEach(f => {
          const item = document.createElement('div');
          item.className = 'file-item';
          item.dataset.path = f.path;
          if(currentFile === f.path) item.classList.add('selected');
          item.innerHTML = `<span style="font-size:.7rem;margin-right:.3rem">${f.published?'👁️':'🚫'}</span>${f.title}`;
          item.onclick = e => { e.stopPropagation(); selectFile(f.path, item); };
          subCh.appendChild(item);
        });
        mainCh.appendChild(subHdr);
        mainCh.appendChild(subCh);
      });
    }
    mainDiv.appendChild(mainHdr);
    mainDiv.appendChild(mainCh);
    tree.appendChild(mainDiv);
  });
}

async function selectFile(path, el){
  if(currentFile === path) return;
  if(currentFile && hasUnsavedNoteChanges() && !confirm('当前文章有未保存修改，继续？')) return;
  document.querySelectorAll('.file-item').forEach(i=>i.classList.remove('selected'));
  if(el) el.classList.add('selected');
  const data = await apiCall(`/api/note?path=${encodeURIComponent(path)}`);
  if(data._error) { toast('读取失败: '+data._error, 'error', 5000); return; }
  currentFile = path;
  document.getElementById('empty-state').style.display='none';
  document.getElementById('editor-content').style.display='flex';
  const parts = path.split(/[/\\]/);
  document.getElementById('current-filename').textContent = parts.slice(-2).join('/');
  FIELDS.forEach(f => {
    const elem = document.getElementById(`f-${f}`);
    if(elem) elem.value = data.info[f] || '';
  });
  editor.setValue(data.body || '');
  editor.refresh();
  cleanInfo = {...data.info};
  cleanBody = data.body || '';
}

function hasUnsavedNoteChanges(){
  if(!currentFile) return false;
  for(const f of FIELDS){
    const el = document.getElementById(`f-${f}`);
    if(el && el.value !== (cleanInfo[f]||'')) return true;
  }
  if(editor && editor.getValue().trim() !== cleanBody.trim()) return true;
  return false;
}

async function saveNote(){
  if(!currentFile) return;
  const info = {};
  FIELDS.forEach(f => { info[f] = document.getElementById(`f-${f}`).value; });
  const body = editor.getValue();
  const data = await apiCall('/api/note', {
    method:'POST', headers:{'Content-Type':'application/json'},
    body: JSON.stringify({path:currentFile, info, body})
  });
  if(data._error) { toast('保存失败: '+data._error,'error',5000); return; }
  cleanInfo={...info}; cleanBody=body; toast('保存成功！'); loadTree();
}

async function renameFile(){
  if(!currentFile) return;
  const parts = currentFile.split(/[/\\]/);
  const oldName = parts[parts.length-1].replace('.md','');
  const newName = prompt('新文件名（不含 .md）：', oldName);
  if(!newName || newName === oldName) return;
  const data = await apiCall('/api/note/rename', {
    method:'POST', headers:{'Content-Type':'application/json'},
    body: JSON.stringify({old_path:currentFile, new_name:newName})
  });
  if(data._error) { toast('重命名失败: '+data._error,'error',5000); return; }
  currentFile = data.new_path; toast('重命名成功！'); await loadTree(); selectFile(data.new_path, null);
}

async function deleteFile(){
  if(!currentFile) return;
  const name = currentFile.split(/[/\\]/).pop();
  if(!confirm(`⚠️ 彻底删除 "${name}"？无法恢复。`)) return;
  const data = await apiCall('/api/note/delete', {
    method:'POST', headers:{'Content-Type':'application/json'},
    body: JSON.stringify({path:currentFile})
  });
  if(data._error) { toast('删除失败: '+data._error,'error',5000); return; }
  currentFile = null;
  document.getElementById('editor-content').style.display='none';
  document.getElementById('empty-state').style.display='flex';
  toast('已删除'); loadTree();
}

function openModal(){
  document.getElementById('modal-new').style.display='flex';
  document.getElementById('new-title').focus();
  updatePreview();
}
function closeModal(){
  document.getElementById('modal-new').style.display='none';
  ['new-title','new-sub','new-filename'].forEach(id=>document.getElementById(id).value='');
  document.getElementById('new-has-pdf').checked=false;
  document.getElementById('new-main-id').value='courses';
}
function updatePreview(){
  const main = document.getElementById('new-main-id').value;
  const sub = document.getElementById('new-sub').value.trim();
  const file = document.getElementById('new-filename').value.trim();
  const prefix = ROUTE_MAP[main] || 'notes';
  document.getElementById('new-preview-url').textContent = (sub && file) ? `/${prefix}/${sub}/${file}` : '—';
  const lbl = document.getElementById('lbl-sub');
  if(main === 'courses') lbl.innerHTML = '3. 所属课程文件夹 <span class="hint">英文缩写</span>';
  else lbl.innerHTML = '3. 子分类文件夹名 <span class="hint">英文缩写</span>';
}
async function createNote(){
  const main_id = document.getElementById('new-main-id').value;
  const title = document.getElementById('new-title').value.trim();
  const sub = document.getElementById('new-sub').value.trim();
  const filename = document.getElementById('new-filename').value.trim();
  const has_pdf = document.getElementById('new-has-pdf').checked;
  if(!sub || !filename) return toast('子分类和文件名必填','error');
  const data = await apiCall('/api/note/new', {
    method:'POST', headers:{'Content-Type':'application/json'},
    body: JSON.stringify({main_id, sub_folder:sub, filename, title, has_pdf})
  });
  if(data._error) { toast('创建失败: '+data._error,'error',5000); return; }
  closeModal(); toast('创建成功'); await loadTree(); selectFile(data.path, null);
}

async function loadCourses(){
  const container = document.getElementById('disc-list');
  container.innerHTML = '<div style="padding:1rem;color:var(--muted)">加载中...</div>';
  const data = await apiCall('/api/courses');
  if(data._error) {
    container.innerHTML = `<div style="padding:1rem;color:var(--red)">加载失败：${data._error}</div>`;
    return;
  }
  if(!data.courses || data.courses.length === 0) {
    container.innerHTML = '<div style="padding:1rem;color:var(--muted)">没有课程。检查 _config.yml 的 course_order 字段。</div>';
    return;
  }
  container.innerHTML = '';
  const groups = {};
  data.courses.forEach(c => {
    const d = c.discipline || '未分类';
    if(!groups[d]) groups[d] = [];
    groups[d].push(c);
  });
  for(const [disc, courses] of Object.entries(groups)){
    const group = document.createElement('div');
    group.className = 'disc-group';
    const header = document.createElement('div');
    header.className = 'disc-header';
    header.innerHTML = `<span class="disc-arrow">▶</span><span class="disc-label">${disc}</span><span class="disc-count">${courses.length} 门课</span>`;
    const body = document.createElement('div');
    body.className = 'disc-body';
    header.querySelector('.disc-arrow').addEventListener('click', e=>{e.stopPropagation();body.classList.toggle('open');header.querySelector('.disc-arrow').classList.toggle('open');});
    header.querySelector('.disc-label').addEventListener('click', e=>{e.stopPropagation();body.classList.toggle('open');header.querySelector('.disc-arrow').classList.toggle('open');});
    courses.forEach(c => {
      const item = document.createElement('div');
      item.className = 'course-item';
      item.dataset.folder = c.folder;
      item.innerHTML = `<span class="course-name">${c.name}</span><span class="course-folder">${c.folder}</span>`;
      body.appendChild(item);
    });
    group.appendChild(header); group.appendChild(body); container.appendChild(group);
    Sortable.create(body, {animation:150, ghostClass:'sortable-ghost', group:'courses'});
  }
  Sortable.create(container, {animation:200, handle:'.disc-header', ghostClass:'sortable-ghost'});
  initialSnap = getSnap();
}
function getSnap(){ return Array.from(document.querySelectorAll('#disc-list .course-item')).map(li=>li.dataset.folder).join(','); }
function hasUnsavedCourseChanges(){ if(!initialSnap) return false; return getSnap() !== initialSnap; }
async function scanCourses(){
  const data = await apiCall('/api/courses');
  if(data._error) return toast('失败: '+data._error,'error');
  const existing = new Set(data.courses.map(c=>c.folder));
  let n=0;
  for(const f of Object.keys(data.all_folders)){ if(!existing.has(f)) n++; }
  if(n>0){ await loadCourses(); toast(`已导入 ${n} 门新课程`); }
  else toast('没有新课程');
}
async function saveCourses(){
  const folders = Array.from(document.querySelectorAll('#disc-list .course-item')).map(li=>li.dataset.folder);
  const data = await apiCall('/api/courses', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({folders})});
  if(data._error) { toast('失败: '+data._error,'error'); return; }
  initialSnap=getSnap(); toast('排序已保存');
}

window.addEventListener('beforeunload', e=>{
  if(hasUnsavedNoteChanges()||hasUnsavedCourseChanges()){ e.preventDefault(); e.returnValue=''; }
});
</script>
</body></html>'''

@app.route("/")
def index():
    return Response(HTML, content_type="text/html; charset=utf-8")


if __name__ == "__main__":
    port = 9090
    diagnose()
    print(f"🚀 启动服务器: http://localhost:{port}")
    print(f"按 Ctrl+C 退出\n")
    threading.Timer(1.0, lambda: webbrowser.open(f"http://localhost:{port}")).start()
    app.run(debug=False, port=port)
