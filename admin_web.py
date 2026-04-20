#!/usr/bin/env python3
"""
Zircon 知识库控制台 V8.0 (数字花园架构版)
新增：四大专栏独立路由、动态 YAML 字段生成、双规建站模式
"""

import os, time, webbrowser, threading
from pathlib import Path
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename

try:
    from ruamel.yaml import YAML
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.indent(mapping=2, sequence=4, offset=2)
except ImportError:
    print("\n[错误] 缺少依赖包！请先在终端运行: pip install ruamel.yaml\n")
    exit(1)

app = Flask(__name__)

NOTES_DIR = Path("_notes").resolve()
CONFIG_FILE = Path("_config.yml").resolve()
UPLOAD_DIR = Path("files/images").resolve()

# 核心架构映射表
MAIN_CATE_MAP = {
    "courses": "课程资料",
    "research": "科研妙招",
    "life": "生活攻略",
    "essays": "随笔漫谈"
}

# 字段扩充，加入了大类和子类
FIELDS = ['title', 'main_category', 'sub_category', 'published', 'discipline', 'course', 'material_type', 'date', 'author', 'permalink', 'pdf_url']

def is_safe_path(base_dir, target_path):
    try:
        target = Path(target_path).resolve()
        return target.is_relative_to(base_dir)
    except Exception:
        return False

def parse_note(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    info = {field: "" for field in FIELDS}
    info['published'] = "true"
    body = content

    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            yaml_str = parts[1]
            body = parts[2]
            try:
                parsed = yaml.load(yaml_str)
                if parsed:
                    for k, v in parsed.items():
                        info[k] = str(v).lower() if isinstance(v, bool) else str(v)
            except Exception:
                pass
                
    return info, body

@app.route("/api/notes")
def api_notes():
    if not NOTES_DIR.exists(): return jsonify({"tree": []})
    
    # 初始化完整的树状图骨架
    tree_dict = {
        k: {"main_id": k, "main_name": v, "subfolders": {}} 
        for k, v in MAIN_CATE_MAP.items()
    }
    
    for md_file in sorted(NOTES_DIR.rglob("*.md")):
        rel_path = md_file.relative_to(NOTES_DIR)
        parts = rel_path.parts
        if len(parts) == 0: continue
        
        main_id = parts[0]
        if main_id not in tree_dict:
            tree_dict[main_id] = {"main_id": main_id, "main_name": main_id, "subfolders": {}}
            
        info, _ = parse_note(md_file)
        
        # 归类到子文件夹
        if len(parts) >= 3:
            sub_id = parts[1]
        elif len(parts) == 2:
            sub_id = "default" # 直接放在大类下的文件
        else:
            continue
            
        sub_name = info.get('course') or info.get('sub_category') or (sub_id if sub_id != "default" else "未分类")
        
        if sub_id not in tree_dict[main_id]["subfolders"]:
            tree_dict[main_id]["subfolders"][sub_id] = {"sub_id": sub_id, "sub_name": sub_name, "files": []}
            
        tree_dict[main_id]["subfolders"][sub_id]["files"].append({
            "path": str(md_file),
            "title": info.get('title', md_file.stem),
            "published": info.get('published', 'true').lower() == 'true'
        })

    # 格式化给前端
    result = []
    for m_id, m_data in tree_dict.items():
        subs = []
        for s_id, s_data in m_data["subfolders"].items():
            subs.append(s_data)
        result.append({
            "main_id": m_id,
            "main_name": m_data["main_name"],
            "subfolders": subs
        })
        
    return jsonify({"tree": result})

@app.route("/api/note")
def api_get_note():
    filepath = request.args.get("path", "")
    if not filepath or not Path(filepath).exists() or not is_safe_path(NOTES_DIR, filepath):
        return jsonify({"error": "File not found or access denied"}), 404
    info, body = parse_note(filepath)
    return jsonify({"info": info, "body": body.lstrip("\n")})

@app.route("/api/note", methods=["POST"])
def api_save_note():
    data = request.json
    filepath = data.get("path", "")
    new_info = data.get("info", {})
    new_body = data.get("body", "")
    
    if not filepath or not Path(filepath).exists() or not is_safe_path(NOTES_DIR, filepath):
        return jsonify({"error": "File not found"}), 404
        
    with open(filepath, 'r', encoding='utf-8') as f: content = f.read()

    parsed_yaml = {}
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try: parsed_yaml = yaml.load(parts[1]) or {}
            except Exception: pass

    for f_name in FIELDS:
        val = new_info.get(f_name, "")
        if val:
            if val.lower() == "true": parsed_yaml[f_name] = True
            elif val.lower() == "false": parsed_yaml[f_name] = False
            else: parsed_yaml[f_name] = val
        else:
            if f_name in parsed_yaml: del parsed_yaml[f_name]

    import io
    buf = io.StringIO()
    yaml.dump(parsed_yaml, buf)
    
    body = new_body if new_body.startswith("\n") else "\n" + new_body
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("---\n" + buf.getvalue() + "---" + body)
        
    return jsonify({"ok": True})

@app.route("/api/note/rename", methods=["POST"])
def api_rename_note():
    data = request.json
    old_path = data.get("old_path", "")
    new_name = data.get("new_name", "").strip()
    if not old_path or not new_name or not Path(old_path).exists() or not is_safe_path(NOTES_DIR, old_path):
        return jsonify({"error": "无效的路径"}), 400
    if not new_name.endswith('.md'): new_name += '.md'
    old_file = Path(old_path)
    new_file = old_file.parent / new_name
    if new_file.exists(): return jsonify({"error": "该文件名已存在！"}), 400
    old_file.rename(new_file)
    return jsonify({"ok": True, "new_path": str(new_file)})

@app.route("/api/note/delete", methods=["POST"])
def api_delete_note():
    data = request.json
    filepath = data.get("path", "")
    if not filepath or not Path(filepath).exists() or not is_safe_path(NOTES_DIR, filepath):
        return jsonify({"error": "无效的路径"}), 400
    file_to_del = Path(filepath)
    folder = file_to_del.parent
    file_to_del.unlink()
    if folder.exists() and not any(folder.iterdir()): folder.rmdir()
    return jsonify({"ok": True})

@app.route("/api/note/new", methods=["POST"])
def api_new_note():
    data = request.json
    main_cat_id = data.get("main_cat_id", "courses").strip()
    sub_folder = secure_filename(data.get("sub_folder", "").strip())
    filename = data.get("filename", "").strip()
    title = data.get("title", "").strip()
    permalink = data.get("permalink", "").strip()
    pdf_url = data.get("pdf_url", "").strip()
    
    if not sub_folder or not filename: return jsonify({"error": "子分类和文件名不能为空"}), 400
    if not filename.endswith('.md'): filename += '.md'

    target_dir = NOTES_DIR / main_cat_id / sub_folder
    target_dir.mkdir(parents=True, exist_ok=True)
    filepath = target_dir / filename
    if not is_safe_path(NOTES_DIR, filepath): return jsonify({"error": "非法路径"}), 403
    if filepath.exists(): return jsonify({"error": "该文件已存在！"}), 400

    import datetime
    today = datetime.date.today().strftime("%Y-%m-%d")
    clean_title = title if title else filename.replace('.md', '')
    main_category_name = MAIN_CATE_MAP.get(main_cat_id, "未分类")
    
    # --- 动态构建 YAML 头部 ---
    content_lines = [
        "---",
        "layout: post",
        f'title: "{clean_title}"',
        f'main_category: "{main_category_name}"'
    ]
    
    # 针对不同大类的特定字段分流
    if main_cat_id == "courses":
        content_lines.extend([
            'discipline: "经济学"',  # 默认值，可在页面修改
            f'course: "{sub_folder}"',
            'material_type: "Notes"'
        ])
    else:
        content_lines.append(f'sub_category: "{sub_folder}"')

    content_lines.extend([
        f"date: {today}",
        'author: "Zircon"',
        "published: true"
    ])
    
    if permalink: content_lines.append(f'permalink: "{permalink}"')
    if pdf_url: content_lines.append(f'pdf_url: "{pdf_url}"')
    content_lines.append("---")
    
    # 针对 PDF 和正文的动态拼接
    if pdf_url and main_cat_id == "courses":
        preview_snippet = """
## 讲义在线预览与下载
> 手机端和平板端可能不能获得最佳的预览效果，请点击下方按钮下载

<style>
  .pdf-preview { display: block; }
  @media (max-width: 768px) {
    .pdf-preview { display: none !important; }
  }
</style>

<div class="pdf-container" style="margin: 2rem 0;">
  <div class="pdf-preview">
    <iframe src="{{ page.pdf_url }}" width="100%" height="600px" style="border: 1px solid var(--color-border); border-radius: 8px;">
      您的浏览器不支持内嵌预览，请通过下方链接下载。
    </iframe>
  </div>

  <div style="margin-top: 1rem; text-align: center;">
    <a href="{{ page.pdf_url }}" download style="padding: 10px 20px; border: 1px solid var(--color-ink); text-decoration: none; color: var(--color-ink); font-family: var(--font-display); transition: 0.3s;">
      📥 下载完整版附件
    </a>
  </div>
</div>

在这里开始书写你的笔记吧...
"""
        content_lines.append(preview_snippet)
    else:
        content_lines.append("\n\n在这里开始书写你的文章正文吧...\n")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("\n".join(content_lines))

    return jsonify({"ok": True, "path": str(filepath)})

@app.route("/api/upload", methods=["POST"])
def api_upload():
    if 'image' not in request.files: return jsonify({"error": "没有找到图片"}), 400
    file = request.files['image']
    if file.filename == '': return jsonify({"error": "图片格式无效"}), 400
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    ext = Path(file.filename).suffix
    if not ext: ext = '.png'
    new_filename = f"img_{int(time.time())}{ext}"
    file.save(UPLOAD_DIR / new_filename)
    return jsonify({"url": f"/files/images/{new_filename}"})

@app.route("/api/courses")
def api_get_courses():
    # 只扫描 courses 文件夹里的内容，不干扰随笔
    courses_dir = NOTES_DIR / "courses"
    folder_to_info = {}
    if courses_dir.exists():
        for md_file in courses_dir.rglob("*.md"):
            info, _ = parse_note(md_file)
            folder = md_file.parent.name
            if folder not in folder_to_info:
                folder_to_info[folder] = {"name": info.get('course', '') or folder, "discipline": info.get('discipline', '') or '未分类'}
    courses = []
    if CONFIG_FILE.exists():
        in_block = False
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith("course_order:"):
                    in_block = True
                    continue
                if in_block:
                    if line.strip().startswith("-"):
                        raw = line.strip()[1:].strip()
                        info = folder_to_info.get(raw, {"name": raw, "discipline": "未分类"})
                        courses.append({"folder": raw, "name": info["name"], "discipline": info["discipline"]})
                    elif line.strip() == "" or line.strip().startswith("#"): continue
                    elif not line.startswith(" ") and not line.startswith("\t"): break
    return jsonify({"courses": courses, "all_folders": {k: v["name"] for k, v in folder_to_info.items()}})

@app.route("/api/courses", methods=["POST"])
def api_save_courses():
    data = request.json
    folders = data.get("folders", [])
    if not CONFIG_FILE.exists(): return jsonify({"error": "Config not found"}), 404
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f: lines = f.readlines()
    out, in_block, replaced = [], False, False
    for line in lines:
        if line.startswith("course_order:"):
            in_block, replaced = True, True
            out.append(line)
            for c in folders: out.append(f"  - {c}\n")
            continue
        if in_block:
            if line.strip().startswith("-") or line.strip() == "" or line.strip().startswith("#"): continue
            elif not line.startswith(" ") and not line.startswith("\t"):
                in_block = False
                out.append(line)
        else: out.append(line)
    if not replaced:
        out.append("\ncourse_order:\n")
        for c in folders: out.append(f"  - {c}\n")
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f: f.writelines(out)
    return jsonify({"ok": True})

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    port = 9090
    print(f"\n{'='*50}")
    print(f"  Zircon 知识库控制台 V8.0 (数字花园架构版)")
    print(f"  浏览器打开: http://localhost:{port}")
    print(f"  按 Ctrl+C 退出")
    print(f"{'='*50}\n")
    threading.Timer(1.0, lambda: webbrowser.open(f"http://localhost:{port}")).start()
    app.run(debug=False, port=port)