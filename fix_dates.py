import os
import re
from pathlib import Path

notes_dir = Path("_notes")
fixed = 0

print("🔍 启动逐行核对模式，无视 BOM 与换行符差异...\n")

for file_path in notes_dir.rglob("*.*"):
    # 只扫描 Markdown 和 HTML 文件
    if file_path.suffix.lower() not in ['.md', '.markdown', '.html']:
        continue
        
    try:
        # 强制使用 utf-8-sig，消除所有隐形的 BOM 开头字符
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()
    except Exception:
        continue
        
    if not lines:
        continue
        
    # 严格判断第一行是不是 ---
    if lines[0].strip() != '---':
        continue
        
    in_yaml = True
    new_lines = []
    changed = False
    
    new_lines.append(lines[0])
    
    for i in range(1, len(lines)):
        line = lines[i]
        
        # 遇到第二个 --- 结束 YAML 区域
        if in_yaml and line.strip() == '---':
            in_yaml = False
            new_lines.append(line)
            continue
            
        # 不区分大小写地寻找 date 字段
        if in_yaml and line.strip().lower().startswith('date:'):
            # 获取 date 后面的值
            raw_val = line.split(':', 1)[1].strip()
            # 暴力扒掉所有的单引号、双引号
            clean_val = raw_val.replace('"', '').replace("'", "").strip()
            
            # 正则提取前10位标准的 YYYY-MM-DD
            match = re.search(r'(\d{4}-\d{2}-\d{2})', clean_val)
            if match:
                clean_date = match.group(1)
                correct_line = f"date: {clean_date}\n"
                
                # 如果原来的行带有引号、空格或格式不对，就会被判定为需要修改
                if line.strip() != correct_line.strip():
                    changed = True
                    print(f"🛠️ 修复格式冲突: [{raw_val}] -> [{clean_date}] (文件: {file_path.name})")
                new_lines.append(correct_line)
            else:
                # 根本没有合规日期的（比如 "未知", "2024"），直接删除这一行！
                changed = True
                print(f"⚠️ 删除无效日期: [{raw_val}] (文件: {file_path.name})")
        else:
            new_lines.append(line)
            
    if changed:
        # 重新保存为干净的 utf-8 编码
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        fixed += 1

print(f"\n🎉 深度扫描结束！共修复了 {fixed} 个文件的日期雷区。")