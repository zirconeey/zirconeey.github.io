#!/usr/bin/env python3
"""
微信公众号文章转 Markdown 工具
运行目录: 博客根目录 (zirconeey.github.io/)

用法:
  python3 download_wechat_images.py <URL> <slug>
  python3 download_wechat_images.py <URL> <slug> -c 随笔漫谈
  python3 download_wechat_images.py <URL> <slug> --images-only

输出:
  files/images/<slug>/01.jpg, 02.jpg, ...
  <slug>.md  （当前目录，之后手动移入对应的 _notes/ 子目录）
"""

import sys, os, re, argparse
from pathlib import Path
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup, NavigableString, Tag

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://mp.weixin.qq.com/',
}


# ── 网络工具 ────────────────────────────────────────────────────────────────

def fetch_soup(url: str) -> BeautifulSoup:
    print(f"正在获取: {url}")
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    resp.encoding = 'utf-8'
    return BeautifulSoup(resp.text, 'html.parser')


def ext_from_url(url: str) -> str:
    path = urlparse(url.split('?')[0]).path
    ext = os.path.splitext(path)[1].lower()
    return ext if ext in ('.jpg', '.jpeg', '.png', '.gif', '.webp') else '.jpg'


# ── 图片下载 ─────────────────────────────────────────────────────────────────

def collect_and_download_images(content_div, img_dir: Path, slug: str) -> dict:
    """
    只抓取正文区（#js_content）内的图片，自然跳过封面图。
    返回 {原始URL: 本地文件名} 映射。
    """
    img_dir.mkdir(parents=True, exist_ok=True)

    imgs = content_div.select('img[data-src], img[src]') if content_div else []
    article_imgs = []
    for img in imgs:
        src = img.get('data-src') or img.get('src', '')
        if not src:
            continue
        if 'mmbiz.qpic.cn' in src or 'mmbiz.qlogo.cn' in src:
            if '/mmhead/' in src:
                continue  # 跳过头像
            article_imgs.append(src)
        elif src.startswith('http'):
            article_imgs.append(src)

    print(f"找到 {len(article_imgs)} 张正文图片（已排除封面）")
    url_to_local = {}

    for i, src in enumerate(article_imgs, 1):
        ext = ext_from_url(src)
        filename = f'{i:02d}{ext}'
        dest = img_dir / filename
        print(f"  [{i:02d}/{len(article_imgs)}] {filename} ...", end=' ', flush=True)
        try:
            r = requests.get(src, headers=HEADERS, timeout=15)
            r.raise_for_status()
            dest.write_bytes(r.content)
            print(f"✓ ({len(r.content) // 1024} KB)")
        except Exception as e:
            print(f"✗ {e}")
        url_to_local[src] = filename

    return url_to_local


# ── HTML → Markdown 转换 ────────────────────────────────────────────────────

def inline_md(node) -> str:
    """提取节点的内联 Markdown（文字格式，不含块级图片）。"""
    if isinstance(node, NavigableString):
        return str(node)

    tag = (node.name or '').lower()
    children = ''.join(inline_md(c) for c in node.children)

    if tag in ('script', 'style'):
        return ''
    if tag in ('strong', 'b'):
        t = children.strip()
        return f'**{t}**' if t else ''
    if tag in ('em', 'i'):
        t = children.strip()
        return f'*{t}*' if t else ''
    if tag in ('s', 'del', 'strike'):
        t = children.strip()
        return f'~~{t}~~' if t else ''
    if tag == 'code':
        return f'`{children}`'
    if tag == 'br':
        return '\n'
    if tag == 'a':
        href = node.get('href', '')
        t = children.strip()
        if href and not href.startswith('javascript') and t:
            return f'[{t}]({href})'
        return t
    if tag == 'span':
        style = node.get('style', '').replace(' ', '').lower()
        t = children
        if 'font-weight:bold' in style or 'font-weight:700' in style:
            stripped = t.strip()
            t = f'**{stripped}**' if stripped else t
        if 'font-style:italic' in style:
            stripped = t.strip()
            t = f'*{stripped}*' if stripped else t
        return t
    if tag == 'img':
        return ''  # 图片在块级层处理

    return children


def block_to_lines(node, url_map: dict, slug: str, list_depth: int = 0) -> list:
    """将节点递归转为行列表（每行不含尾部换行符）。"""
    if isinstance(node, NavigableString):
        t = str(node).strip()
        return [t] if t else []

    tag = (node.name or '').lower()

    if tag in ('script', 'style', 'head'):
        return []

    # 图片
    if tag == 'img':
        src = node.get('data-src') or node.get('src', '')
        if src in url_map:
            return [f'![](/files/images/{slug}/{url_map[src]})']
        return []

    # 标题
    if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
        text = inline_md(node).strip()
        return [f'{"#" * int(tag[1])} {text}'] if text else []

    # 无序列表
    if tag == 'ul':
        lines = []
        for li in node.find_all('li', recursive=False):
            # 先提取 li 内的内联文字（跳过子列表）
            li_text = ''.join(
                inline_md(c) for c in li.children
                if not (isinstance(c, Tag) and c.name in ('ul', 'ol'))
            ).strip()
            lines.append('  ' * list_depth + f'- {li_text}')
            for child in li.children:
                if isinstance(child, Tag) and child.name in ('ul', 'ol'):
                    lines.extend(block_to_lines(child, url_map, slug, list_depth + 1))
        return lines

    # 有序列表
    if tag == 'ol':
        lines = []
        for idx, li in enumerate(node.find_all('li', recursive=False), 1):
            li_text = ''.join(
                inline_md(c) for c in li.children
                if not (isinstance(c, Tag) and c.name in ('ul', 'ol'))
            ).strip()
            lines.append('  ' * list_depth + f'{idx}. {li_text}')
            for child in li.children:
                if isinstance(child, Tag) and child.name in ('ul', 'ol'):
                    lines.extend(block_to_lines(child, url_map, slug, list_depth + 1))
        return lines

    # 引用
    if tag == 'blockquote':
        inner = []
        for child in node.children:
            inner.extend(block_to_lines(child, url_map, slug))
        return ['> ' + line for line in inner] if inner else []

    # 段落：处理文字和内嵌图片（含 <span><img/></span> 等包裹形式）
    if tag == 'p':
        lines = []
        text_parts = []

        def flush_text():
            if text_parts:
                combined = ''.join(text_parts).strip()
                if combined:
                    lines.append(combined)
                text_parts.clear()

        for child in node.children:
            if isinstance(child, Tag) and child.name == 'img':
                flush_text()
                src = child.get('data-src') or child.get('src', '')
                if src in url_map:
                    lines.append(f'![](/files/images/{slug}/{url_map[src]})')
            elif isinstance(child, Tag):
                # 检查是否是纯图片包裹容器（无文字，只含 img）
                imgs = child.find_all('img')
                if imgs and not child.get_text(strip=True):
                    flush_text()
                    for img in imgs:
                        src = img.get('data-src') or img.get('src', '')
                        if src in url_map:
                            lines.append(f'![](/files/images/{slug}/{url_map[src]})')
                else:
                    text_parts.append(inline_md(child))
            else:
                text_parts.append(str(child))

        flush_text()
        return lines

    # section / div 等透明容器：递归子节点，段间插空行
    if tag in ('section', 'div', 'article', 'main', 'figure', 'figcaption', 'body'):
        lines = []
        for child in node.children:
            child_lines = block_to_lines(child, url_map, slug)
            if child_lines:
                if lines and lines[-1] != '':
                    lines.append('')
                lines.extend(child_lines)
        return lines

    # 其他标签：降级为内联文字
    text = inline_md(node).strip()
    return [text] if text else []


def html_to_markdown(content_div, url_map: dict, slug: str) -> str:
    lines = []
    for child in content_div.children:
        child_lines = block_to_lines(child, url_map, slug)
        if child_lines:
            if lines and lines[-1] != '':
                lines.append('')
            lines.extend(child_lines)

    md = '\n'.join(lines)
    md = re.sub(r'\n{3,}', '\n\n', md)  # 最多两个连续空行
    return md.strip()


# ── 元数据提取 ───────────────────────────────────────────────────────────────

def extract_meta(soup: BeautifulSoup) -> tuple:
    """返回 (title, date_str)，date_str 为 YYYY-MM-DD 格式。"""
    title = ''
    date = ''

    # 标题
    for selector in ('#activity-name', 'h1.rich_media_title', 'h2.rich_media_title'):
        el = soup.select_one(selector)
        if el:
            title = el.get_text(strip=True)
            break

    # 去掉专栏前缀，如 "随风｜"、"博雅 | "、"Advanced Micro | " 等
    title = re.sub(r'^.+?\s*[|｜]\s*', '', title).strip()

    # 日期
    for selector in ('#publish_time', 'em#publish_time', 'span#publish_time'):
        el = soup.select_one(selector)
        if el:
            raw = el.get_text(strip=True)
            # 转换 "2024年1月1日" → "2024-01-01"
            m = re.search(r'(\d{4})年(\d{1,2})月(\d{1,2})日', raw)
            if m:
                date = f'{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}'
            else:
                # 已经是 YYYY-MM-DD 或类似格式
                m2 = re.search(r'\d{4}-\d{2}-\d{2}', raw)
                date = m2.group(0) if m2 else raw
            break

    if not date:
        meta = soup.find('meta', attrs={'property': 'article:published_time'})
        if meta:
            date = (meta.get('content', '') or '')[:10]

    return title, date


def generate_frontmatter(title: str, date: str, category: str) -> str:
    lines = ['---', 'layout: post']
    if title:
        lines.append(f'title: "{title.replace(chr(34), chr(92)+chr(34))}"')
    if date:
        lines.append(f'date: {date}')
    if category:
        lines.append(f'main_category: "{category}"')
    lines += ['---', '']
    return '\n'.join(lines) + '\n'


# ── 主流程 ───────────────────────────────────────────────────────────────────

def run(url: str, slug: str, category: str = '', images_only: bool = False):
    soup = fetch_soup(url)
    title, date = extract_meta(soup)
    print(f"标题: {title or '(未找到)'}")
    print(f"日期: {date or '(未找到)'}")

    content_div = soup.find(id='js_content')
    if not content_div:
        print("⚠️  未找到 #js_content，尝试全 body（可能含多余内容）")
        content_div = soup.find('body')

    img_dir = Path('files') / 'images' / slug
    url_map = collect_and_download_images(content_div, img_dir, slug)

    if images_only:
        print(f"\n完成！图片已保存到 {img_dir}/")
        return

    print("\n正在转换 HTML → Markdown ...")
    md_body = html_to_markdown(content_div, url_map, slug)
    frontmatter = generate_frontmatter(title, date, category)

    out_path = Path(f'{slug}.md')
    out_path.write_text(frontmatter + md_body + '\n', encoding='utf-8')

    print(f"\n完成！")
    print(f"  Markdown: {out_path}")
    print(f"  图片目录: {img_dir}/  ({len(url_map)} 张)")
    print(f"\n下一步：将 {slug}.md 移入对应的 _notes/ 子目录，检查并补充 frontmatter。")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='微信公众号文章转 Markdown（在博客根目录运行）'
    )
    parser.add_argument('url', help='微信文章 URL')
    parser.add_argument('slug', help='文章 slug，用于文件名和图片目录，如 my-article-2024')
    parser.add_argument('-c', '--category', default='', metavar='分类',
                        help='主分类，如 随笔漫谈 / 科研妙招 / 生活攻略')
    parser.add_argument('--images-only', action='store_true',
                        help='仅下载图片，不生成 Markdown')
    args = parser.parse_args()
    run(args.url, args.slug, args.category, args.images_only)
