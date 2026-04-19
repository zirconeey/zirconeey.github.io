import os
from pathlib import Path
import urllib.parse  # <--- 新增：用于 URL 编码

def generate_markdown_from_pdfs():
    # 设定基准文件夹
    files_dir = Path("/Users/zhourui/Desktop/zirconeey.github.io/files")
    notes_dir = Path("/Users/zhourui/Desktop/zirconeey.github.io/_notes")
    
    # 发布日期
    publish_date = "2026-04-18"
    
    if not files_dir.exists():
        print(f"❌ 找不到 {files_dir} 文件夹，请确认脚本运行路径。")
        return

    # rglob 递归遍历所有 pdf 文件
    pdf_files = list(files_dir.rglob("*.pdf"))
    count = 0

    for pdf_path in pdf_files:
        # 提取课程名与文件名
        course_name = pdf_path.parent.name
        pdf_name_stem = pdf_path.stem
        pdf_name_full = pdf_path.name
        
        # 智能判断 material_type
        lower_name = pdf_name_stem.lower()
        if "mid" in lower_name or "final" in lower_name:
            material_type = "Exams"
        else:
            material_type = "Notes"
            
        # 构造目标 markdown 文件的路径
        target_note_dir = notes_dir / course_name
        target_note_dir.mkdir(parents=True, exist_ok=True)
        target_md_path = target_note_dir / f"{pdf_name_stem}.md"
        
        # 【关键修复区：URL 编码处理】
        # 将路径中的空格和括号等特殊字符转译为安全的 URL 格式（如 %20）
        safe_course_name = urllib.parse.quote(course_name)
        safe_pdf_name_stem = urllib.parse.quote(pdf_name_stem)
        safe_pdf_name_full = urllib.parse.quote(pdf_name_full)
        
        permalink = f"/notes/{safe_course_name}/{safe_pdf_name_stem}"
        pdf_url = f"/files/{safe_course_name}/{safe_pdf_name_full}"
        
        # 【关键修复区：YAML 加双引号】
        # permalink: "{permalink}" 确保 YAML 解析器不会因为特殊字符崩溃
        md_content = f"""---
layout: post
title: "{pdf_name_stem}"
discipline: "经济学"
course: "{course_name}"
material_type: "{material_type}"
date: {publish_date}
author: "Zircon"
permalink: "{permalink}"
pdf_url: "{pdf_url}"
# reactions: ['👍', '🎓', '📝', '🔥']
---

## 讲义在线预览与下载
> 手机端和平板端可能不能获得最佳的预览效果，请点击下方按钮下载

<style>
  .pdf-preview {{ display: block; }}
  @media (max-width: 768px) {{
    .pdf-preview {{ display: none !important; }}
  }}
</style>

<div class="pdf-container" style="margin: 2rem 0;">
  <div class="pdf-preview">
    <iframe src="{{{{ page.pdf_url }}}}" width="100%" height="600px" style="border: 1px solid var(--color-border); border-radius: 8px;">
      您的浏览器不支持内嵌 PDF，请通过下方链接下载。
    </iframe>
  </div>
  
  <div style="margin-top: 1rem; text-align: center;">
    <a href="{{{{ page.pdf_url }}}}" download style="padding: 10px 20px; border: 1px solid var(--color-ink); text-decoration: none; color: var(--color-ink); font-family: var(--font-display); transition: 0.3s;">
      📥 下载完整版 PDF 讲义
    </a>
  </div>
</div>
"""
        with open(target_md_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        
        count += 1
        print(f"✅ 已生成: {target_md_path}")

    print(f"\n🎉 运行完毕！共成功处理 {count} 个 PDF 文件。URL 现已全部安全编码！")

if __name__ == "__main__":
    generate_markdown_from_pdfs()