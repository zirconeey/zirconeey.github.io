#!/usr/bin/env python3
"""
Zircon 知识库控制台 V7.0 (Web版)
用法: cd ~/Desktop/zirconeey.github.io && python admin_web.py
然后浏览器打开 http://localhost:9090
"""

import os, json, webbrowser, threading
from pathlib import Path
from flask import Flask, request, jsonify, Response

app = Flask(__name__)

NOTES_DIR = Path("_notes")
CONFIG_FILE = Path("_config.yml")
FIELDS = ['title', 'published', 'discipline', 'course', 'material_type', 'date', 'author', 'permalink', 'pdf_url']

# ==================== 后端 API ====================

def parse_note(filepath):
    """解析一个markdown文件，返回YAML字段和正文"""
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
                        info[field] = line.split(":", 1)[1].strip().strip('"').strip("'")
        else:
            body_lines.append(line)
    return info, yaml_lines, "".join(body_lines)

@app.route("/api/notes")
def api_notes():
    """返回文件树结构"""
    if not NOTES_DIR.exists():
        return jsonify({"tree": []})
    tree = {}
    folder_to_course = {}
    for md_file in sorted(NOTES_DIR.rglob("*.md")):
        info, _, _ = parse_note(md_file)
        folder = md_file.parent.name
        course_name = info.get('course', '') or folder
        if folder not in folder_to_course and course_name:
            folder_to_course[folder] = course_name
        if folder not in tree:
            tree[folder] = {"name": course_name, "files": []}
        published = info.get('published', 'true').lower() == 'true'
        tree[folder]["files"].append({
            "path": str(md_file),
            "title": info.get('title', md_file.stem),
            "published": published,
        })
    result = [{"folder": k, "name": v["name"], "files": v["files"]} for k, v in tree.items()]
    return jsonify({"tree": result})

@app.route("/api/note")
def api_get_note():
    """获取单篇文章的YAML和正文"""
    filepath = request.args.get("path", "")
    if not filepath or not Path(filepath).exists():
        return jsonify({"error": "File not found"}), 404
    info, _, body = parse_note(filepath)
    return jsonify({"info": info, "body": body.lstrip("\n")})

@app.route("/api/note", methods=["POST"])
def api_save_note():
    """保存文章 (YAML + 正文)"""
    data = request.json
    filepath = data.get("path", "")
    new_info = data.get("info", {})
    new_body = data.get("body", "")
    if not filepath or not Path(filepath).exists():
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
                        out_yaml.append(f"{f}: {v}\n" if v in ["true","false"] else f'{f}: "{v}"\n')
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
                        out_yaml.append(f"{f}: {v}\n" if v in ["true","false"] else f'{f}: "{v}"\n')
                    break
            if not matched:
                out_yaml.append(line)
    body = new_body if new_body.startswith("\n") else "\n" + new_body
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("".join(out_yaml) + body)
    return jsonify({"ok": True})

@app.route("/api/courses")
def api_get_courses():
    """获取课程排序"""
    folder_to_course = {}
    if NOTES_DIR.exists():
        for md_file in NOTES_DIR.rglob("*.md"):
            info, _, _ = parse_note(md_file)
            folder = md_file.parent.name
            course_name = info.get('course', '') or folder
            if folder not in folder_to_course:
                folder_to_course[folder] = course_name
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
                        name = folder_to_course.get(raw, raw)
                        courses.append({"folder": raw, "name": name})
                    elif line.strip() == "" or line.strip().startswith("#"):
                        continue
                    elif not line.startswith(" ") and not line.startswith("\t"):
                        break
    return jsonify({"courses": courses, "all_folders": folder_to_course})

@app.route("/api/courses", methods=["POST"])
def api_save_courses():
    """保存课程排序到 _config.yml"""
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
            out.append(line)
            for c in folders:
                out.append(f"  - {c}\n")
            replaced = True
            continue
        if in_block:
            if line.strip().startswith("-") or line.strip() == "" or line.strip().startswith("#"):
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

# ==================== 前端页面 ====================

HTML = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Zircon 知识库控制台 V7.0</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/theme/nord.min.css">
<style>
:root {
  --bg: #fafaf9; --bg2: #f0efeb; --bg3: #e8e7e3;
  --ink: #1a1a2e; --text: #374151; --muted: #6b7280; --light: #9ca3af;
  --border: #d5d4cf; --accent: #1e3a5f; --accent2: #2d5a8e;
  --green: #16a34a; --green-bg: #dcfce7; --red: #dc2626; --gold: #c9a96e;
  --font: 'Source Sans 3', -apple-system, 'PingFang SC', sans-serif;
  --mono: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;
}
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family: var(--font); background: var(--bg); color: var(--text); height: 100vh; display: flex; flex-direction: column; }
button { font-family: var(--font); cursor: pointer; }

/* Top bar */
.topbar {
  background: var(--ink); color: #e8e6e3; padding: 0.6rem 1.5rem;
  display: flex; align-items: center; justify-content: space-between;
  flex-shrink: 0;
}
.topbar h1 { font-size: 1rem; font-weight: 500; letter-spacing: 0.02em; }
.topbar .tabs { display: flex; gap: 0; }
.topbar .tab {
  padding: 0.45rem 1.2rem; font-size: 0.85rem; color: #8a8680;
  background: none; border: none; border-bottom: 2px solid transparent;
  transition: all 0.2s;
}
.topbar .tab:hover { color: #e8e6e3; }
.topbar .tab.active { color: #e8e6e3; border-bottom-color: var(--gold); }

/* Panels */
.panel { display: none; flex: 1; overflow: hidden; }
.panel.active { display: flex; }

/* ===== NOTES PANEL ===== */
#panel-notes { display: flex; }

/* Sidebar */
.sidebar {
  width: 300px; min-width: 240px; border-right: 1px solid var(--border);
  display: flex; flex-direction: column; background: var(--bg2);
  flex-shrink: 0;
}
.sidebar-header {
  padding: 0.8rem 1rem; font-size: 0.8rem; font-weight: 600; color: var(--muted);
  text-transform: uppercase; letter-spacing: 0.08em;
  border-bottom: 1px solid var(--border);
  display: flex; justify-content: space-between; align-items: center;
}
.sidebar-header button {
  font-size: 0.75rem; background: none; border: 1px solid var(--border);
  padding: 0.2rem 0.6rem; border-radius: 4px; color: var(--muted);
}
.sidebar-header button:hover { border-color: var(--accent); color: var(--accent); }
.file-tree { flex: 1; overflow-y: auto; padding: 0.5rem 0; }
.folder-item {
  padding: 0.4rem 1rem; font-size: 0.85rem; font-weight: 600; color: var(--ink);
  cursor: pointer; user-select: none; display: flex; align-items: center; gap: 0.4rem;
}
.folder-item:hover { background: var(--bg3); }
.folder-item .arrow { font-size: 0.65rem; color: var(--muted); transition: transform 0.15s; display: inline-block; width: 12px; }
.folder-item .arrow.open { transform: rotate(90deg); }
.folder-children { display: none; }
.folder-children.open { display: block; }
.file-item {
  padding: 0.35rem 1rem 0.35rem 2.2rem; font-size: 0.84rem; color: var(--text);
  cursor: pointer; user-select: none; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
.file-item:hover { background: var(--bg3); }
.file-item.selected { background: #dbeafe; color: var(--accent); font-weight: 500; }
.file-item .status { font-size: 0.7rem; margin-right: 0.3rem; }

/* Editor area */
.editor-area { flex: 1; display: flex; flex-direction: column; overflow: hidden; }
.editor-toolbar {
  padding: 0.6rem 1.2rem; border-bottom: 1px solid var(--border);
  display: flex; align-items: center; justify-content: space-between; background: var(--bg);
  flex-shrink: 0;
}
.editor-toolbar .filename { font-size: 0.9rem; color: var(--muted); }
.btn-save {
  background: var(--green); color: white; border: none; padding: 0.5rem 1.5rem;
  border-radius: 6px; font-size: 0.85rem; font-weight: 500; transition: background 0.2s;
}
.btn-save:hover { background: #15803d; }
.btn-save:disabled { background: var(--light); cursor: not-allowed; }

/* YAML form */
.yaml-form {
  padding: 0.8rem 1.2rem; border-bottom: 1px solid var(--border);
  display: grid; grid-template-columns: auto 1fr auto 1fr auto 1fr;
  gap: 0.4rem 0.6rem; align-items: center; background: var(--bg2);
  flex-shrink: 0;
}
.yaml-form label { font-size: 0.78rem; color: var(--muted); text-align: right; font-weight: 500; }
.yaml-form input, .yaml-form select {
  font-family: var(--mono); font-size: 0.82rem; padding: 0.3rem 0.5rem;
  border: 1px solid var(--border); border-radius: 4px; background: white;
  color: var(--text); outline: none; transition: border-color 0.2s;
}
.yaml-form input:focus, .yaml-form select:focus { border-color: var(--accent); }
.yaml-form .full { grid-column: 2 / -1; }

/* CodeMirror wrapper */
.cm-wrapper { flex: 1; overflow: hidden; }
.cm-wrapper .CodeMirror { height: 100%; font-size: 14px; line-height: 1.6; }

/* Empty state */
.empty-state {
  flex: 1; display: flex; align-items: center; justify-content: center;
  color: var(--light); font-size: 1.1rem;
}

/* ===== COURSES PANEL ===== */
#panel-courses { padding: 2rem; flex-direction: column; align-items: center; }
.courses-container { width: 100%; max-width: 600px; }
.courses-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; }
.courses-header h2 { font-size: 1.1rem; color: var(--ink); }
.btn-scan {
  background: none; border: 1px solid var(--accent); color: var(--accent);
  padding: 0.4rem 1rem; border-radius: 6px; font-size: 0.82rem;
}
.btn-scan:hover { background: var(--accent); color: white; }
.course-list { list-style: none; border: 1px solid var(--border); border-radius: 8px; overflow: hidden; }
.course-item {
  padding: 0.7rem 1rem; background: white; border-bottom: 1px solid var(--border);
  display: flex; align-items: center; gap: 0.8rem; cursor: grab;
  font-size: 0.92rem; transition: background 0.15s;
}
.course-item:last-child { border-bottom: none; }
.course-item:hover { background: #f0f9ff; }
.course-item:active { cursor: grabbing; }
.course-item .drag-handle { color: var(--light); font-size: 1.1rem; cursor: grab; }
.course-item .course-name { flex: 1; color: var(--ink); }
.course-item .course-folder { font-size: 0.78rem; color: var(--light); font-family: var(--mono); }
.course-actions { margin-top: 1rem; display: flex; justify-content: flex-end; }

/* Toast notification */
.toast {
  position: fixed; bottom: 2rem; right: 2rem; padding: 0.8rem 1.5rem;
  background: var(--ink); color: white; border-radius: 8px; font-size: 0.88rem;
  opacity: 0; transform: translateY(10px); transition: all 0.3s;
  z-index: 999; pointer-events: none;
}
.toast.show { opacity: 1; transform: translateY(0); }
.toast.success { background: var(--green); }
.toast.error { background: var(--red); }

/* Keyboard shortcut hint */
.shortcut-hint { font-size: 0.72rem; color: #6b6762; margin-left: 0.5rem; }
</style>
</head>
<body>

<!-- Top bar -->
<div class="topbar">
  <h1>Zircon 知识库控制台</h1>
  <div class="tabs">
    <button class="tab active" onclick="switchTab('notes')">文章编辑器</button>
    <button class="tab" onclick="switchTab('courses')">课程排序</button>
  </div>
</div>

<!-- Notes Panel -->
<div id="panel-notes" class="panel active">
  <div class="sidebar">
    <div class="sidebar-header">
      <span>课程与文章</span>
      <button onclick="loadTree()">刷新</button>
    </div>
    <div class="file-tree" id="file-tree"></div>
  </div>
  <div class="editor-area" id="editor-area">
    <div class="empty-state" id="empty-state">← 从左侧选择一篇文章开始编辑</div>
    <div id="editor-content" style="display:none; flex:1; display:none; flex-direction:column; overflow:hidden;">
      <div class="editor-toolbar">
        <span class="filename" id="current-filename">—</span>
        <div>
          <button class="btn-save" id="btn-save" onclick="saveNote()">
            💾 保存 <span class="shortcut-hint">⌘S</span>
          </button>
        </div>
      </div>
      <div class="yaml-form" id="yaml-form">
        <label>title</label>    <input id="f-title" class="full" type="text">
        <label>published</label><select id="f-published"><option value="true">true</option><option value="false">false</option></select>
        <label>date</label>     <input id="f-date" type="text" placeholder="2026-04-17">
        <label>author</label>   <input id="f-author" type="text">
        <label>discipline</label><input id="f-discipline" type="text">
        <label>course</label>   <input id="f-course" type="text">
        <label>material_type</label><select id="f-material_type"><option value="">—</option><option>Notes</option><option>Exams</option><option>Script</option><option>Tool</option><option>Life</option></select>
        <label>permalink</label><input id="f-permalink" class="full" type="text">
        <label>pdf_url</label>  <input id="f-pdf_url" class="full" type="text">
      </div>
      <div class="cm-wrapper">
        <textarea id="md-editor"></textarea>
      </div>
    </div>
  </div>
</div>

<!-- Courses Panel -->
<div id="panel-courses" class="panel">
  <div class="courses-container">
    <div class="courses-header">
      <h2>课程排序（拖拽调整）</h2>
      <div>
        <button class="btn-scan" onclick="scanCourses()">自动导入新课程</button>
      </div>
    </div>
    <ul class="course-list" id="course-list"></ul>
    <div class="course-actions">
      <button class="btn-save" onclick="saveCourses()">💾 保存排序到 _config.yml</button>
    </div>
  </div>
</div>

<!-- Toast -->
<div class="toast" id="toast"></div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/markdown/markdown.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Sortable/1.15.0/Sortable.min.js"></script>
<script>
// ===== State =====
let currentFile = null;
let cleanInfo = {};
let cleanBody = "";
let editor = null;

// ===== Init =====
window.addEventListener('DOMContentLoaded', () => {
  editor = CodeMirror.fromTextArea(document.getElementById('md-editor'), {
    mode: 'markdown',
    lineNumbers: true,
    lineWrapping: true,
    tabSize: 2,
    theme: 'default',
  });
  loadTree();
  loadCourses();
  // Cmd+S / Ctrl+S to save
  document.addEventListener('keydown', e => {
    if ((e.metaKey || e.ctrlKey) && e.key === 's') {
      e.preventDefault();
      if (currentFile) saveNote();
    }
  });
});

// ===== Tabs =====
function switchTab(name) {
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
  document.querySelector(`.tab[onclick*="${name}"]`).classList.add('active');
  document.getElementById(`panel-${name}`).classList.add('active');
  if (name === 'courses') loadCourses();
}

// ===== Toast =====
function toast(msg, type='success') {
  const el = document.getElementById('toast');
  el.textContent = msg;
  el.className = 'toast show ' + type;
  setTimeout(() => el.className = 'toast', 2500);
}

// ===== File Tree =====
async function loadTree() {
  const res = await fetch('/api/notes');
  const data = await res.json();
  const tree = document.getElementById('file-tree');
  tree.innerHTML = '';
  data.tree.forEach(folder => {
    const folderDiv = document.createElement('div');
    const folderHeader = document.createElement('div');
    folderHeader.className = 'folder-item';
    folderHeader.innerHTML = `<span class="arrow">▶</span> 📚 ${folder.name}`;
    const children = document.createElement('div');
    children.className = 'folder-children';
    folderHeader.onclick = () => {
      children.classList.toggle('open');
      folderHeader.querySelector('.arrow').classList.toggle('open');
    };
    folder.files.forEach(f => {
      const item = document.createElement('div');
      item.className = 'file-item';
      item.dataset.path = f.path;
      const icon = f.published ? '👁️' : '🚫';
      item.innerHTML = `<span class="status">${icon}</span>${f.title || f.path}`;
      item.onclick = (e) => { e.stopPropagation(); selectFile(f.path, item); };
      children.appendChild(item);
    });
    folderDiv.appendChild(folderHeader);
    folderDiv.appendChild(children);
    tree.appendChild(folderDiv);
  });
}

// ===== Select & Load File =====
async function selectFile(path, el) {
  if (currentFile === path) return;
  if (currentFile && hasUnsavedChanges()) {
    if (!confirm('当前文章有未保存的修改，切换将丢弃更改。继续？')) return;
  }
  document.querySelectorAll('.file-item').forEach(i => i.classList.remove('selected'));
  el.classList.add('selected');
  const res = await fetch(`/api/note?path=${encodeURIComponent(path)}`);
  const data = await res.json();
  if (data.error) { toast(data.error, 'error'); return; }
  currentFile = path;
  document.getElementById('empty-state').style.display = 'none';
  const editorContent = document.getElementById('editor-content');
  editorContent.style.display = 'flex';
  document.getElementById('current-filename').textContent = path.split('/').pop();
  const fields = ['title','published','discipline','course','material_type','date','author','permalink','pdf_url'];
  fields.forEach(f => {
    const el = document.getElementById(`f-${f}`);
    if (el) el.value = data.info[f] || '';
  });
  editor.setValue(data.body || '');
  editor.refresh();
  cleanInfo = {...data.info};
  cleanBody = data.body || '';
}

// ===== Unsaved Changes =====
function hasUnsavedChanges() {
  if (!currentFile) return false;
  const fields = ['title','published','discipline','course','material_type','date','author','permalink','pdf_url'];
  for (const f of fields) {
    const el = document.getElementById(`f-${f}`);
    if (el && el.value !== (cleanInfo[f] || '')) return true;
  }
  if (editor.getValue().trim() !== cleanBody.trim()) return true;
  return false;
}

// ===== Save Note =====
async function saveNote() {
  if (!currentFile) return;
  const info = {};
  const fields = ['title','published','discipline','course','material_type','date','author','permalink','pdf_url'];
  fields.forEach(f => { info[f] = document.getElementById(`f-${f}`).value; });
  const body = editor.getValue();
  const res = await fetch('/api/note', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({path: currentFile, info, body})
  });
  const data = await res.json();
  if (data.ok) {
    cleanInfo = {...info};
    cleanBody = body;
    toast('保存成功！');
    loadTree();
  } else {
    toast('保存失败: ' + (data.error || '未知错误'), 'error');
  }
}

// ===== Courses =====
async function loadCourses() {
  const res = await fetch('/api/courses');
  const data = await res.json();
  const list = document.getElementById('course-list');
  list.innerHTML = '';
  data.courses.forEach(c => {
    const li = document.createElement('li');
    li.className = 'course-item';
    li.dataset.folder = c.folder;
    li.innerHTML = `<span class="drag-handle">⠿</span><span class="course-name">${c.name}</span><span class="course-folder">${c.folder}</span>`;
    list.appendChild(li);
  });
  if (typeof Sortable !== 'undefined') {
    Sortable.create(list, { animation: 150, handle: '.drag-handle', ghostClass: 'sortable-ghost' });
  }
}

async function scanCourses() {
  const res = await fetch('/api/courses');
  const data = await res.json();
  const existing = new Set(data.courses.map(c => c.folder));
  const list = document.getElementById('course-list');
  let added = 0;
  for (const [folder, name] of Object.entries(data.all_folders)) {
    if (!existing.has(folder) && folder !== 'output') {
      const li = document.createElement('li');
      li.className = 'course-item';
      li.dataset.folder = folder;
      li.innerHTML = `<span class="drag-handle">⠿</span><span class="course-name">${name}</span><span class="course-folder">${folder}</span>`;
      list.appendChild(li);
      added++;
    }
  }
  toast(added > 0 ? `已导入 ${added} 门新课程` : '没有新课程可导入');
}

async function saveCourses() {
  const items = document.querySelectorAll('#course-list .course-item');
  const folders = Array.from(items).map(li => li.dataset.folder);
  const res = await fetch('/api/courses', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({folders})
  });
  const data = await res.json();
  if (data.ok) toast('排序已保存到 _config.yml！');
  else toast('保存失败', 'error');
}

// Warn on page close if unsaved
window.addEventListener('beforeunload', e => {
  if (hasUnsavedChanges()) { e.preventDefault(); e.returnValue = ''; }
});
</script>
</body>
</html>'''

@app.route("/")
def index():
    return Response(HTML, content_type="text/html; charset=utf-8")

# ==================== 启动 ====================
if __name__ == "__main__":
    print("\n" + "="*50)
    print("  Zircon 知识库控制台 V7.0 (Web版)")
    print("  请在浏览器中打开: http://localhost:9090")
    print("  按 Ctrl+C 退出")
    print("="*50 + "\n")
    threading.Timer(1.0, lambda: webbrowser.open("http://localhost:9090")).start()
    app.run(debug=False, port=9090)
