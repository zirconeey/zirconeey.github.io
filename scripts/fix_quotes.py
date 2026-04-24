#!/usr/bin/env python3
"""
把 .md 文件正文里 ASCII 直引号 (") 按出现顺序交替替换为中文弯引号
(U+201C "" 左 / U+201D "" 右)。

跳过：
  - YAML frontmatter（首个 --- 到下一个 ---）
  - fenced code blocks（``` 或 ~~~）
  - inline code（行内 ` ... `）
  - 内嵌 HTML 标签所在行（整行 strip 后以 `<` 开头，例如 `<img src="...">`、`<div ...>`）

用法：
  python3 scripts/fix_quotes.py --all             # 扫描 _notes/ 下全部 .md
  python3 scripts/fix_quotes.py --all --dry-run   # 预览：列出每文件将改多少处
  python3 scripts/fix_quotes.py --staged          # 只处理 git 暂存区的 .md
  python3 scripts/fix_quotes.py <path1> <path2>   # 显式指定文件
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

LQUO = "“"  # "
RQUO = "”"  # "

REPO_ROOT = Path(__file__).resolve().parent.parent


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return "", text
    # 找到第二个 --- 行
    lines = text.splitlines(keepends=True)
    if not lines or not lines[0].startswith("---"):
        return "", text
    end = None
    for i in range(1, len(lines)):
        if lines[i].rstrip("\r\n") == "---":
            end = i
            break
    if end is None:
        return "", text
    fm = "".join(lines[: end + 1])
    body = "".join(lines[end + 1 :])
    return fm, body


def convert_body(body: str) -> tuple[str, int]:
    """
    扫描 body，跳过 fenced code + inline code，对其余区域按配对顺序替换 ASCII "
    返回 (新文本, 替换处数)
    """
    out: list[str] = []
    i = 0
    n = len(body)
    quote_idx = 0  # 0 → 下一个用 "，1 → 下一个用 "
    changes = 0

    in_fence = False
    fence_marker = None  # "```" or "~~~"

    def at_line_start(pos: int) -> bool:
        return pos == 0 or body[pos - 1] == "\n"

    while i < n:
        ch = body[i]

        # —— 内嵌 HTML 标签行（行首 strip 后以 `<` 开头）整行原样输出 ——
        if at_line_start(i) and not in_fence:
            j = i
            while j < n and body[j] in " \t":
                j += 1
            if j < n and body[j] == "<" and j + 1 < n and (body[j + 1].isalpha() or body[j + 1] == "/"):
                line_end = body.find("\n", j)
                if line_end == -1:
                    line_end = n
                else:
                    line_end += 1
                out.append(body[i:line_end])
                i = line_end
                continue

        # —— fenced code block 检测（```  或 ~~~，行首）——
        if at_line_start(i) and not in_fence:
            # 读取该行前导空白（允许 0-3 空格缩进，4+ 是代码块缩进，本处不处理）
            j = i
            leading_spaces = 0
            while j < n and body[j] == " " and leading_spaces < 4:
                j += 1
                leading_spaces += 1
            if leading_spaces < 4:
                if body.startswith("```", j):
                    in_fence = True
                    fence_marker = "```"
                    # 找到行尾，把整行（带 info string 和换行）原样输出
                    line_end = body.find("\n", j)
                    if line_end == -1:
                        line_end = n
                    else:
                        line_end += 1
                    out.append(body[i:line_end])
                    i = line_end
                    continue
                if body.startswith("~~~", j):
                    in_fence = True
                    fence_marker = "~~~"
                    line_end = body.find("\n", j)
                    if line_end == -1:
                        line_end = n
                    else:
                        line_end += 1
                    out.append(body[i:line_end])
                    i = line_end
                    continue

        # —— 处于 fenced code 内 —— 原样输出直到闭合围栏 ——
        if in_fence:
            if at_line_start(i):
                j = i
                leading_spaces = 0
                while j < n and body[j] == " " and leading_spaces < 4:
                    j += 1
                    leading_spaces += 1
                if leading_spaces < 4 and body.startswith(fence_marker, j):
                    # 检查 fence 行后面除了可选空白只能是换行
                    k = j + len(fence_marker)
                    while k < n and body[k] in " \t":
                        k += 1
                    if k == n or body[k] == "\n":
                        line_end = body.find("\n", j)
                        if line_end == -1:
                            line_end = n
                        else:
                            line_end += 1
                        out.append(body[i:line_end])
                        i = line_end
                        in_fence = False
                        fence_marker = None
                        continue
            # 非围栏闭合：原样输出当前字符
            out.append(ch)
            i += 1
            continue

        # —— inline code（行内反引号）——
        if ch == "`":
            # 计算本组连续反引号数量
            start = i
            while i < n and body[i] == "`":
                i += 1
            ticks = body[start:i]
            # 在后续寻找等长的闭合组
            close_idx = body.find(ticks, i)
            if close_idx != -1:
                # 出现等长闭合组 —— 把 `…` 原样输出（但闭合组后不能紧跟更多反引号）
                # 简化处理：直接匹配第一次等长出现
                after = close_idx + len(ticks)
                out.append(body[start:after])
                i = after
                continue
            else:
                # 没有闭合组——当作普通字符
                out.append(ticks)
                continue

        # —— ASCII " 替换 ——
        if ch == '"':
            # 英寸 / 尺寸符号：数字紧跟 " （如 12"、6.5"），不替换
            if i > 0 and body[i - 1].isdigit():
                out.append(ch)
                i += 1
                continue
            if quote_idx % 2 == 0:
                out.append(LQUO)
            else:
                out.append(RQUO)
            quote_idx += 1
            changes += 1
            i += 1
            continue

        out.append(ch)
        i += 1

    return "".join(out), changes


def process_file(path: Path, dry_run: bool = False) -> int:
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError) as e:
        print(f"  ! 跳过 {path}: {e}", file=sys.stderr)
        return 0

    fm, body = split_frontmatter(text)
    new_body, changes = convert_body(body)
    if changes == 0:
        return 0

    new_text = fm + new_body
    if not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return changes


def collect_all_md() -> list[Path]:
    notes_dir = REPO_ROOT / "_notes"
    return sorted(notes_dir.rglob("*.md"))


def collect_staged() -> list[Path]:
    out = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    files = []
    for line in out.stdout.splitlines():
        line = line.strip()
        if line.endswith(".md"):
            p = REPO_ROOT / line
            if p.is_file():
                files.append(p)
    return files


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="scan _notes/ recursively")
    ap.add_argument("--staged", action="store_true", help="only staged .md files")
    ap.add_argument("--dry-run", action="store_true", help="preview, don't write")
    ap.add_argument("paths", nargs="*", help="explicit file paths")
    args = ap.parse_args()

    if args.all:
        files = collect_all_md()
    elif args.staged:
        files = collect_staged()
    elif args.paths:
        files = [Path(p) for p in args.paths]
    else:
        ap.print_help()
        return 1

    if not files:
        print("（没有需要处理的文件）")
        return 0

    total_changes = 0
    total_files = 0
    for f in files:
        c = process_file(f, dry_run=args.dry_run)
        if c > 0:
            total_files += 1
            total_changes += c
            rel = f.relative_to(REPO_ROOT) if f.is_absolute() else f
            mark = "(dry-run) " if args.dry_run else ""
            print(f"  {mark}{rel}: {c} 处")

    verb = "将改" if args.dry_run else "已改"
    print(f"\n共 {total_files} 个文件 {verb} {total_changes} 处。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
