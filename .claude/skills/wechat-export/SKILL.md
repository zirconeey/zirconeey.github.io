---
name: wechat-export
description: 把 zirconeey.github.io 站的源 markdown 文章转换成适合粘贴到 https://md.doocs.org/（公众号 markdown 排版工具）的版本，并自动拷到剪贴板。当用户说"导出公众号 / 发公众号 / 转一下排版 / wechat 版 / 转 doocs"等时使用。仅适用于 layout=post 的文章；菜谱（layout=recipe）有结构化 YAML 字段，不适用此 skill。
---

# wechat-export — 导出公众号版 markdown

把 zirconeey 站的一篇博客文章转成适合贴进 [md.doocs.org](https://md.doocs.org/) 的版本。

## 它做什么

调用 `scripts/wx_render.py`，输入源 `.md` 文件，做三件事：

1. **剥掉 YAML front-matter**（doocs/md 不识别）
2. **图片相对路径 → 绝对 URL**：`/files/images/{slug}/01.jpg` → `https://zirconeey.github.io/files/images/{slug}/01.jpg`。GitHub Pages 充当图床，公众号粘贴后会自动转存到腾讯 CDN
3. **保留图片配文样式**：站点的 `<p class="img-caption">…</p>` → 等价的 inline style 版（居中、13 px、`#9ca3af` 灰）。doocs/md 原样保留这段 HTML，复制到公众号后 inline style 也保留，**视觉和站点一致**

转换后内容写到 stdout，并自动 `pbcopy` 到 macOS 剪贴板。

## 调用流程

1. **定位目标文件**：用户给路径直接用；否则取当前会话最近编辑/新建的 `_notes/**/*.md`；都不明确就问
2. **跑脚本**：

   ```bash
   python3 scripts/wx_render.py <md 文件路径>
   ```

   stderr 会打印 `[✓ 已拷贝 N 字到剪贴板。打开 https://md.doocs.org/ 粘贴即可。]`

3. **指引用户后续步骤**（**这一步必须明确告诉用户**）：

   1. 打开 [md.doocs.org](https://md.doocs.org/)
   2. **Cmd+V** 粘贴左侧编辑器
   3. 顶部选一个主题（用户的常用主题可以让他自己选；如果没指定，建议从默认开始）
   4. 点击右上角“复制”按钮 → 切到公众号编辑器粘贴
   5. 公众号里再做最后微调（如有需要）

## 选项

- `--no-copy`：只输出 stdout，不动剪贴板。用于调试或把输出重定向到文件

## 不适用范围

- **菜谱**（`layout: recipe`）：`ingredients` / `prep` / `steps` 在 YAML 里，剥掉 YAML 后会丢失。需要单独处理（暂未实现）
- **跨 zirconeey 链接**：文章里若有指向 `/notes/...` 的内部链接，转换后是 zirconeey.github.io 域，公众号读者点击会跳到本站；这是预期行为
- **代码块语法高亮**：doocs/md 自己处理，不需要 skill 干预

## 配套文件

- `scripts/wx_render.py` —— 实际转换器
- 颜色 / 字号常量在脚本顶部，可按需调整

## 常见小坑

- 图片在 doocs/md 预览时如果加载慢，是 GitHub Pages 全球 CDN 边缘节点缓存问题，等几秒会出来；公众号那边粘贴时会重新拉取并转存
- 如果配文有换行（`<br>`），inline style 版本同样支持
- 文章里如果用了未定义的 Liquid 标签（如 `{% ... %}`），脚本不会处理 —— 建议博客文章里就不要写 Liquid 模板

## 后续可扩展（暂未实现，用到再说）

- 给菜谱专门写一个 `wx_render_recipe.py`，把 `ingredients`/`prep`/`steps` 渲染成 markdown 表格 + 列表
- 自动检查文章里有没有 `<p class="img-caption">` 漏写的图（即“图后面没有配文的”），提示用户补
