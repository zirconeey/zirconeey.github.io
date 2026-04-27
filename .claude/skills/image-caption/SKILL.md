---
name: image-caption
description: 在 zirconeey.github.io 的 markdown 文件里给某张图片下面追加标准的 `<p class="img-caption">` 配文。当用户说"给这张图加配文 / 加 caption / 这张图下面写一句"等时使用。zirconeey 站的固定格式，由 `_layouts/post.html` 的 CSS 渲染。
---

# image-caption — 给图片加标准配文

## 固定格式（**唯一允许的写法**）

```html
<p class="img-caption">这里是配文文字</p>
```

紧跟在 markdown 图片或 HTML `<img>` 之后另起一行。多行配文用 `<br>` 分行：

```html
<p class="img-caption">第一行<br>第二行</p>
```

## 不允许的写法

- ❌ markdown 斜体充当配文：`*这是配文*`
- ❌ 引用块充当配文：`> 这是配文`
- ❌ HTML 但用别的 class：`<p class="caption">` / `<figcaption>`
- ❌ 把配文写在图片同一行后面

## 何时使用此 skill

用户在文章里加了一张图，想配上说明文字。典型触发：

- “给这张图加个配文：……”
- “图下面写一句：……”
- “这张图加 caption：……”

## 调用方式

最简形式：用户直接给配文文字即可：

```
/image-caption 自洽的安定，何以寻？
```

如果当前会话上下文里有最近编辑的图片位置，直接在那张图后面插入 `<p class="img-caption">…</p>`。

如果有歧义（多张图、不清楚加在哪张），先问用户加在哪张图后。

## 实施步骤

1. 定位目标 markdown 文件（通常是当前会话刚编辑过的那篇）
2. 找到目标图片所在行（最近一张 `![...](...)` 或 `<img ...>`）
3. 在该图片**后**插入新行：`<p class="img-caption">{配文}</p>`
4. 如果图片后已经有空行，配文紧贴图片下一行（中间不留空行也行，看相邻样式）
5. 保留写完，建议跑 `/fix-quotes <file>` 一并把配文里的直引号转中文弯引号

## 参考

- 渲染 CSS：`_layouts/post.html` 第 186-195 行（`.markdown-content .img-caption`）
- 真实样板：`_notes/essays/birthday-21.md` 用了 20+ 处
