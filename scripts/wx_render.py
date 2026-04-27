#!/usr/bin/env python3
"""
把 zirconeey.github.io 的源 markdown 转换成适合粘贴到 https://md.doocs.org/
（公众号排版工具）的版本。

转换规则：
  1. 剥掉 YAML front-matter
  2. 图片相对路径 / -> 绝对 URL https://zirconeey.github.io/...
  3. <p class="img-caption">…</p>
       -> <p style="text-align:center;font-size:13px;color:#9ca3af;
                    line-height:1.6;margin-top:6px;">…</p>
       （inline style，doocs/md 原样保留，公众号粘贴后样式也保留）

用法：
  python3 scripts/wx_render.py <md 文件>     # 输出到 stdout，并 pbcopy 到剪贴板
  python3 scripts/wx_render.py <md 文件> --no-copy   # 仅输出 stdout

仅适用于 layout=post 的文章。
菜谱（layout=recipe）的 ingredients/prep/steps 在 YAML 中，去掉 YAML 后会丢失，不适用。
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

SITE_BASE = "https://zirconeey.github.io"
CAPTION_STYLE = (
    "text-align:center;font-size:13px;color:#9ca3af;"
    "line-height:1.6;margin-top:6px;"
)


def strip_frontmatter(text: str) -> str:
    if not (text.startswith("---\n") or text.startswith("---\r\n")):
        return text
    lines = text.splitlines(keepends=True)
    end = None
    for i in range(1, len(lines)):
        if lines[i].rstrip("\r\n") == "---":
            end = i
            break
    if end is None:
        return text
    return "".join(lines[end + 1 :]).lstrip("\n")


def absolutize_images(text: str) -> str:
    def md_repl(m: re.Match) -> str:
        alt, src = m.group(1), m.group(2)
        if src.startswith("/"):
            return f"![{alt}]({SITE_BASE}{src})"
        return m.group(0)

    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", md_repl, text)

    def img_repl(m: re.Match) -> str:
        src = m.group(1)
        if src.startswith("/"):
            return m.group(0).replace(src, SITE_BASE + src)
        return m.group(0)

    text = re.sub(r'<img[^>]+src="([^"]+)"', img_repl, text)
    return text


def convert_caption(text: str) -> str:
    return re.sub(
        r'<p\s+class=["\']img-caption["\']>(.+?)</p>',
        f'<p style="{CAPTION_STYLE}">\\1</p>',
        text,
        flags=re.DOTALL,
    )


def render(md_path: Path) -> str:
    text = md_path.read_text(encoding="utf-8")
    text = strip_frontmatter(text)
    text = absolutize_images(text)
    text = convert_caption(text)
    return text


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="markdown 文件路径")
    ap.add_argument("--no-copy", action="store_true", help="不拷贝到剪贴板")
    args = ap.parse_args()

    src = Path(args.path)
    if not src.is_file():
        print(f"找不到文件: {src}", file=sys.stderr)
        return 1

    text = render(src)
    sys.stdout.write(text)

    if not args.no_copy:
        try:
            subprocess.run(
                ["pbcopy"], input=text.encode("utf-8"), check=True
            )
            print(
                f"\n\n[✓ 已拷贝 {len(text)} 字到剪贴板。"
                f"打开 https://md.doocs.org/ 粘贴即可。]",
                file=sys.stderr,
            )
        except (FileNotFoundError, subprocess.CalledProcessError) as e:
            print(f"\n\n[剪贴板拷贝失败: {e}]", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
