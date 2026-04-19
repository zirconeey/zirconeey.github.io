import os
from pathlib import Path

def generate_markdown_from_pdfs():
    # 设定基准文件夹
    files_dir = Path("/Users/zhourui/Desktop/zirconeey.github.io/files")
    notes_dir = Path("/Users/zhourui/Desktop/zirconeey.github.io/_notes")
    
    # 发布日期（可以写死，也可以用 datetime 获取当前日期）
    publish_date = "2026-04-18"
    
    if not files_dir.exists():
        print(f"❌ 找不到 {files_dir} 文件夹，请确认脚本运行路径。")
        return

    # rglob 递归遍历所有 pdf 文件
    pdf_files = list(files_dir.rglob("*.pdf"))
    count = 0

    for pdf_path in pdf_files:
        # 提取课程名（即 PDF 所在的一级子文件夹名）
        # 如果结构是 files/course_name/xxx.pdf，则 parent.name 就是 course_name
        course_name = pdf_path.parent.name
        
        # 提取 PDF 文件名（不含扩展名）
        pdf_name_stem = pdf_path.stem
        pdf_name_full = pdf_path.name
        
        # 智能判断 material_type：包含 mid 或 final 即为 Exams
        lower_name = pdf_name_stem.lower()
        if "mid" in lower_name or "final" in lower_name:
            material_type = "Exams"
        else:
            material_type = "Notes"
            
        # 构造目标 markdown 文件的路径
        target_note_dir = notes_dir / course_name
        target_note_dir.mkdir(parents=True, exist_ok=True)  # 如果子文件夹不存在则自动创建
        
        target_md_path = target_note_dir / f"{pdf_name_stem}.md"
        
        # 构造 URL 链接 (注意规避空格问题，如果文件名有空格，浏览器通常能解析，但最好保持命名规范)
        permalink = f"/notes/{course_name}/{pdf_name_stem}"
        pdf_url = f"/files/{course_name}/{pdf_name_full}"
        
        # 准备 Markdown 模板内容
        # 注意：Python 的 f-string 中，需要用 {{ 和 }} 来转义输出单个大括号 { 和 }
        # 所以 Jekyll 的 {{ page.pdf_url }} 在 f-string 里要写成 {{{{ page.pdf_url }}}}
        md_content = f"""---
layout: post
title: "{pdf_name_stem}"
discipline: "经济学"
course: "{course_name}"
material_type: "{material_type}"
date: {publish_date}
author: "Zircon"
permalink: {permalink}
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
        # 写入文件
        # 如果文件已经存在，你可以选择跳过或者覆盖。这里默认直接覆盖更新
        with open(target_md_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        
        count += 1
        print(f"✅ 已生成: {target_md_path}")

    print(f"\n🎉 运行完毕！共成功处理 {count} 个 PDF 文件。")

if __name__ == "__main__":
    generate_markdown_from_pdfs()