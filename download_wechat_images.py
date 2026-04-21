#!/usr/bin/env python3
"""
下载微信文章中的所有图片，按顺序命名为 01.jpg, 02.jpg, ...
用法: python3 download_wechat_images.py <文章URL> <保存目录>
"""

import sys
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def download_wechat_images(url, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/120.0.0.0 Safari/537.36',
        'Referer': 'https://mp.weixin.qq.com/',
    }

    print(f"正在获取页面: {url}")
    resp = requests.get(url, headers=headers, timeout=15)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, 'html.parser')

    # 微信图片用 data-src 懒加载，也可能直接用 src
    imgs = soup.select('img[data-src], img[src]')

    # 过滤掉微信自身 UI 图标（头像、二维码等），只保留文章正文图片
    article_imgs = []
    for img in imgs:
        src = img.get('data-src') or img.get('src', '')
        if not src:
            continue
        # 微信文章图片域名
        if 'mmbiz.qpic.cn' in src or 'mmbiz.qlogo.cn' in src:
            # 跳过头像（通常很小，带 /0 后缀且尺寸参数为小值）
            if '/mmhead/' in src:
                continue
            article_imgs.append(src)

    if not article_imgs:
        print("未找到文章图片，尝试提取所有 img 标签...")
        for img in imgs:
            src = img.get('data-src') or img.get('src', '')
            if src and src.startswith('http'):
                article_imgs.append(src)

    print(f"找到 {len(article_imgs)} 张图片")

    for i, img_url in enumerate(article_imgs, 1):
        # 去掉微信的缩放参数，获取原图
        clean_url = img_url.split('?')[0] if '?' in img_url else img_url
        # 推断扩展名
        path = urlparse(clean_url).path
        ext = os.path.splitext(path)[1].lower()
        if ext not in ('.jpg', '.jpeg', '.png', '.gif', '.webp'):
            ext = '.jpg'

        filename = f"{i:02d}{ext}"
        filepath = os.path.join(output_dir, filename)

        print(f"  [{i:02d}/{len(article_imgs)}] 下载 {filename} ...", end=' ')
        try:
            r = requests.get(img_url, headers=headers, timeout=15)
            r.raise_for_status()
            with open(filepath, 'wb') as f:
                f.write(r.content)
            size_kb = len(r.content) // 1024
            print(f"✓ ({size_kb} KB)")
        except Exception as e:
            print(f"✗ 失败: {e}")

    print(f"\n完成！图片已保存到: {output_dir}")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("用法: python3 download_wechat_images.py <文章URL> <保存目录>")
        print("示例: python3 download_wechat_images.py 'https://mp.weixin.qq.com/s/xxx' files/images/birthday-21")
        sys.exit(1)

    download_wechat_images(sys.argv[1], sys.argv[2])
