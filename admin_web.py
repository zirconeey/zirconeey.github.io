#!/usr/bin/env python3
"""
Zircon 知识库控制台 V7.1 (Web版)
用法: cd ~/Desktop/zirconeey.github.io && python3 admin_web.py
"""

import os, json, webbrowser, threading
from pathlib import Path
from flask import Flask, request, jsonify, Response

app = Flask(__name__)

NOTES_DIR = Path("_notes")
CONFIG_FILE = Path("_config.yml")
FIELDS = ['title', 'published', 'discipline', 'course', 'material_type', 'date', 'author', 'permalink', 'pdf_url']

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
                        info[field] = line.split(":", 1)[1].strip().strip('"').strip("'")
        else:
            body_lines.append(line)
    return info, yaml_lines, "".join(body_lines)

@app.route("/api/notes")
def api_notes():
    if not NOTES_DIR.exists():
        return jsonify({"tree": []})
    tree = {}
    for md_file in sorted(NOTES_DIR.rglob("*.md")):
        info, _, _ = parse_note(md_file)
        folder = md_file.parent.name
        course_name = info.get('course', '') or folder
        discipline = info.get('discipline', '') or '未分类'
        if folder not in tree:
            tree[folder] = {"name": course_name, "discipline": discipline, "files": []}
        published = info.get('published', 'true').lower() == 'true'
        tree[folder]["files"].append({
            "path": str(md_file),
            "title": info.get('title', md_file.stem),
            "published": published,
        })
    result = [{"folder": k, "name": v["name"], "discipline": v["discipline"], "files": v["files"]} for k, v in tree.items()]
    return jsonify({"tree": result})

@app.route("/api/note")
def api_get_note():
    filepath = request.args.get("path", "")
    if not filepath or not Path(filepath).exists():
        return jsonify({"error": "File not found"}), 404
    info, _, body = parse_note(filepath)
    return jsonify({"info": info, "body": body.lstrip("\n")})

@app.route("/api/note", methods=["POST"])
def api_save_note():
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
    folder_to_info = {}
    if NOTES_DIR.exists():
        for md_file in NOTES_DIR.rglob("*.md"):
            info, _, _ = parse_note(md_file)
            folder = md_file.parent.name
            if folder not in folder_to_info:
                folder_to_info[folder] = {
                    "name": info.get('course', '') or folder,
                    "discipline": info.get('discipline', '') or '未分类'
                }
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
                    elif line.strip() == "" or line.strip().startswith("#"):
                        continue
                    elif not line.startswith(" ") and not line.startswith("\t"):
                        break
    return jsonify({"courses": courses, "all_folders": {k: v["name"] for k, v in folder_to_info.items()}})

@app.route("/api/courses", methods=["POST"])
def api_save_courses():
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

HTML = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Zircon 知识库控制台</title>
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
.sidebar{width:300px;min-width:240px;border-right:1px solid var(--border);display:flex;flex-direction:column;background:var(--bg2);flex-shrink:0}
.sidebar-header{padding:.8rem 1rem;font-size:.8rem;font-weight:600;color:var(--muted);text-transform:uppercase;letter-spacing:.08em;border-bottom:1px solid var(--border);display:flex;justify-content:space-between;align-items:center}
.sidebar-header button{font-size:.75rem;background:none;border:1px solid var(--border);padding:.2rem .6rem;border-radius:4px;color:var(--muted)}
.sidebar-header button:hover{border-color:var(--accent);color:var(--accent)}
.file-tree{flex:1;overflow-y:auto;padding:.5rem 0}
.folder-item{padding:.4rem 1rem;font-size:.85rem;font-weight:600;color:var(--ink);cursor:pointer;user-select:none;display:flex;align-items:center;gap:.4rem}
.folder-item:hover{background:var(--bg3)}
.folder-item .arrow{font-size:.65rem;color:var(--muted);transition:transform .15s;display:inline-block;width:12px}
.folder-item .arrow.open{transform:rotate(90deg)}
.folder-children{display:none}
.folder-children.open{display:block}
.file-item{padding:.35rem 1rem .35rem 2.2rem;font-size:.84rem;color:var(--text);cursor:pointer;user-select:none;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.file-item:hover{background:var(--bg3)}
.file-item.selected{background:#dbeafe;color:var(--accent);font-weight:500}
.editor-area{flex:1;display:flex;flex-direction:column;overflow:hidden}
.editor-toolbar{padding:.6rem 1.2rem;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;background:var(--bg);flex-shrink:0}
.filename{font-size:.9rem;color:var(--muted)}
.btn-save{background:var(--green);color:#fff;border:none;padding:.5rem 1.5rem;border-radius:6px;font-size:.85rem;font-weight:500;transition:background .2s}
.btn-save:hover{background:#15803d}
.yaml-form{padding:.8rem 1.2rem;border-bottom:1px solid var(--border);display:grid;grid-template-columns:auto 1fr auto 1fr auto 1fr;gap:.4rem .6rem;align-items:center;background:var(--bg2);flex-shrink:0}
.yaml-form label{font-size:.78rem;color:var(--muted);text-align:right;font-weight:500}
.yaml-form input,.yaml-form select{font-family:var(--mono);font-size:.82rem;padding:.3rem .5rem;border:1px solid var(--border);border-radius:4px;background:#fff;color:var(--text);outline:none}
.yaml-form input:focus,.yaml-form select:focus{border-color:var(--accent)}
.yaml-form .full{grid-column:2/-1}
.cm-wrapper{flex:1;overflow:hidden}
.cm-wrapper .CodeMirror{height:100%;font-size:14px;line-height:1.6}
.empty-state{flex:1;display:flex;align-items:center;justify-content:center;color:var(--light);font-size:1.1rem}
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
.course-item{padding:.55rem 1rem .55rem 2rem;border-bottom:1px solid var(--border);display:flex;align-items:center;gap:.8rem;cursor:grab;font-size:.9rem;transition:background .1s}
.course-item:last-child{border-bottom:none}
.course-item:hover{background:#f0f9ff}
.course-item:active{cursor:grabbing}
.course-name{flex:1;color:var(--ink)}
.course-folder{font-size:.75rem;color:var(--light);font-family:var(--mono)}
.sortable-ghost{opacity:.4;background:#dbeafe}
.toast{position:fixed;bottom:2rem;right:2rem;padding:.8rem 1.5rem;background:var(--ink);color:#fff;border-radius:8px;font-size:.88rem;opacity:0;transform:translateY(10px);transition:all .3s;z-index:999;pointer-events:none}
.toast.show{opacity:1;transform:translateY(0)}
.toast.success{background:var(--green)}
.toast.error{background:var(--red)}
</style>
</head>
<body>

<div class="topbar">
  <h1>Zircon 知识库控制台</h1>
  <div class="tabs">
    <button class="tab active" data-tab="notes" onclick="switchTab('notes')">文章编辑器</button>
    <button class="tab" data-tab="courses" onclick="switchTab('courses')">课程排序</button>
  </div>
</div>

<div id="panel-notes" class="panel active">
  <div class="sidebar">
    <div class="sidebar-header"><span>课程与文章</span><button onclick="loadTree()">刷新</button></div>
    <div class="file-tree" id="file-tree"></div>
  </div>
  <div class="editor-area">
    <div class="empty-state" id="empty-state">← 从左侧选择一篇文章开始编辑</div>
    <div id="editor-content" style="display:none;flex-direction:column;overflow:hidden;flex:1">
      <div class="editor-toolbar">
        <span class="filename" id="current-filename">—</span>
        <button class="btn-save" onclick="saveNote()">💾 保存 <span style="font-size:.72rem;color:rgba(255,255,255,.7);margin-left:.3rem">⌘S</span></button>
      </div>
      <div class="yaml-form">
        <label>title</label><input id="f-title" class="full" type="text">
        <label>published</label><select id="f-published"><option value="true">true</option><option value="false">false</option></select>
        <label>date</label><input id="f-date" type="text" placeholder="2026-04-17">
        <label>author</label><input id="f-author" type="text">
        <label>discipline</label><input id="f-discipline" type="text">
        <label>course</label><input id="f-course" type="text">
        <label>material_type</label><select id="f-material_type"><option value="">—</option><option>Notes</option><option>Exams</option><option>Script</option><option>Tool</option><option>Life</option></select>
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
        <h2>拖拽调整课程与分类顺序</h2>
        <div class="btns">
          <button class="btn-outline" onclick="scanCourses()">自动导入新课程</button>
          <button class="btn-save" onclick="saveCourses()">💾 保存排序</button>
        </div>
      </div>
      <div id="disc-list"></div>
    </div>
  </div>
</div>

<div class="toast" id="toast"></div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/markdown/markdown.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Sortable/1.15.0/Sortable.min.js"></script>
<script>
let currentFile=null, cleanInfo={}, cleanBody="", editor=null, initialSnap="";

window.addEventListener('DOMContentLoaded', ()=>{
  editor=CodeMirror.fromTextArea(document.getElementById('md-editor'),{mode:'markdown',lineNumbers:true,lineWrapping:true,tabSize:2});
  loadTree();
  document.addEventListener('keydown', e=>{if((e.metaKey||e.ctrlKey)&&e.key==='s'){e.preventDefault();if(currentFile)saveNote();}});
});

function switchTab(name){
  if(currentFile&&hasUnsavedNoteChanges()){if(!confirm('当前文章有未保存的修改，切换将丢弃更改。继续？'))return;}
  if(hasUnsavedCourseChanges()){if(!confirm('课程排序有未保存的修改，切换将丢弃更改。继续？'))return;}
  document.querySelectorAll('.tab').forEach(t=>t.classList.remove('active'));
  document.querySelectorAll('.panel').forEach(p=>p.classList.remove('active'));
  document.querySelector(`.tab[data-tab="${name}"]`).classList.add('active');
  document.getElementById(`panel-${name}`).classList.add('active');
  if(name==='courses')loadCourses();
}

function toast(msg,type='success'){const el=document.getElementById('toast');el.textContent=msg;el.className='toast show '+type;setTimeout(()=>el.className='toast',2500);}

async function loadTree(){
  const res=await fetch('/api/notes');const data=await res.json();
  const tree=document.getElementById('file-tree');tree.innerHTML='';
  data.tree.forEach(folder=>{
    const div=document.createElement('div');
    const hdr=document.createElement('div');hdr.className='folder-item';
    hdr.innerHTML=`<span class="arrow">▶</span> 📚 ${folder.name}`;
    const ch=document.createElement('div');ch.className='folder-children';
    hdr.onclick=()=>{ch.classList.toggle('open');hdr.querySelector('.arrow').classList.toggle('open');};
    folder.files.forEach(f=>{
      const item=document.createElement('div');item.className='file-item';item.dataset.path=f.path;
      item.innerHTML=`<span style="font-size:.7rem;margin-right:.3rem">${f.published?'👁️':'🚫'}</span>${f.title||f.path}`;
      item.onclick=e=>{e.stopPropagation();selectFile(f.path,item);};
      ch.appendChild(item);
    });
    div.appendChild(hdr);div.appendChild(ch);tree.appendChild(div);
  });
}

async function selectFile(path,el){
  if(currentFile===path)return;
  if(currentFile&&hasUnsavedNoteChanges()){if(!confirm('当前文章有未保存的修改，切换将丢弃更改。继续？'))return;}
  document.querySelectorAll('.file-item').forEach(i=>i.classList.remove('selected'));
  el.classList.add('selected');
  const res=await fetch(`/api/note?path=${encodeURIComponent(path)}`);const data=await res.json();
  if(data.error){toast(data.error,'error');return;}
  currentFile=path;
  document.getElementById('empty-state').style.display='none';
  document.getElementById('editor-content').style.display='flex';
  document.getElementById('current-filename').textContent=path.split('/').pop();
  ['title','published','discipline','course','material_type','date','author','permalink','pdf_url'].forEach(f=>{
    const el=document.getElementById(`f-${f}`);if(el)el.value=data.info[f]||'';
  });
  editor.setValue(data.body||'');editor.refresh();
  cleanInfo={...data.info};cleanBody=data.body||'';
}

function hasUnsavedNoteChanges(){
  if(!currentFile)return false;
  for(const f of['title','published','discipline','course','material_type','date','author','permalink','pdf_url']){
    const el=document.getElementById(`f-${f}`);if(el&&el.value!==(cleanInfo[f]||''))return true;
  }
  if(editor&&editor.getValue().trim()!==cleanBody.trim())return true;
  return false;
}

async function saveNote(){
  if(!currentFile)return;
  const info={};
  ['title','published','discipline','course','material_type','date','author','permalink','pdf_url'].forEach(f=>{info[f]=document.getElementById(`f-${f}`).value;});
  const body=editor.getValue();
  const res=await fetch('/api/note',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({path:currentFile,info,body})});
  const data=await res.json();
  if(data.ok){cleanInfo={...info};cleanBody=body;toast('保存成功！');loadTree();}
  else toast('保存失败','error');
}

async function loadCourses(){
  const res=await fetch('/api/courses');const data=await res.json();
  const container=document.getElementById('disc-list');container.innerHTML='';
  const groups={};
  data.courses.forEach(c=>{const d=c.discipline||'未分类';if(!groups[d])groups[d]=[];groups[d].push(c);});

  for(const[disc,courses]of Object.entries(groups)){
    const group=document.createElement('div');group.className='disc-group';group.dataset.discipline=disc;
    const header=document.createElement('div');header.className='disc-header';
    header.innerHTML=`<span class="disc-arrow">▶</span><span class="disc-label">${disc}</span><span class="disc-count">${courses.length} 门课</span>`;

    const body=document.createElement('div');body.className='disc-body';

    // Click arrow or label to toggle, not the whole header (so drag still works)
    header.querySelector('.disc-arrow').addEventListener('click',e=>{e.stopPropagation();body.classList.toggle('open');header.querySelector('.disc-arrow').classList.toggle('open');});
    header.querySelector('.disc-label').addEventListener('click',e=>{e.stopPropagation();body.classList.toggle('open');header.querySelector('.disc-arrow').classList.toggle('open');});

    courses.forEach(c=>{
      const item=document.createElement('div');item.className='course-item';item.dataset.folder=c.folder;
      item.innerHTML=`<span class="course-name">${c.name}</span><span class="course-folder">${c.folder}</span>`;
      body.appendChild(item);
    });
    group.appendChild(header);group.appendChild(body);container.appendChild(group);
    Sortable.create(body,{animation:150,ghostClass:'sortable-ghost',group:'courses'});
  }
  Sortable.create(container,{animation:200,handle:'.disc-header',ghostClass:'sortable-ghost'});
  initialSnap=getSnap();
}

function getSnap(){
  return Array.from(document.querySelectorAll('#disc-list .course-item')).map(li=>li.dataset.folder).join(',');
}
function hasUnsavedCourseChanges(){
  if(!initialSnap)return false;
  return getSnap()!==initialSnap;
}

async function scanCourses(){
  const res=await fetch('/api/courses');const data=await res.json();
  const existing=new Set(data.courses.map(c=>c.folder));
  let n=0;for(const f of Object.keys(data.all_folders)){if(!existing.has(f)&&f!=='output')n++;}
  if(n>0){await loadCourses();toast(`已导入 ${n} 门新课程`);}
  else toast('没有新课程可导入');
}

async function saveCourses(){
  const folders=Array.from(document.querySelectorAll('#disc-list .course-item')).map(li=>li.dataset.folder);
  const res=await fetch('/api/courses',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({folders})});
  const data=await res.json();
  if(data.ok){initialSnap=getSnap();toast('排序已保存到 _config.yml！');}
  else toast('保存失败','error');
}

window.addEventListener('beforeunload',e=>{if(hasUnsavedNoteChanges()||hasUnsavedCourseChanges()){e.preventDefault();e.returnValue='';}});
</script>
</body></html>'''

@app.route("/")
def index():
    return Response(HTML, content_type="text/html; charset=utf-8")

if __name__ == "__main__":
    port = 9090
    print(f"\n{'='*50}")
    print(f"  Zircon 知识库控制台 V7.1")
    print(f"  浏览器打开: http://localhost:{port}")
    print(f"  按 Ctrl+C 退出")
    print(f"{'='*50}\n")
    threading.Timer(1.0, lambda: webbrowser.open(f"http://localhost:{port}")).start()
    app.run(debug=False, port=port)
