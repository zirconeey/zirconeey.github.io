---
name: recipe
description: 在 zirconeey.github.io 站新建一篇符合 `_layouts/recipe.html` 强制 schema 的菜谱文章。当用户说"写菜谱 / 加道菜 / 新菜谱 / 把这道菜做成菜谱"等时使用。菜谱有专属布局和严格的 front-matter 字段，不能用 /new-post 替代。
---

# recipe — 新建菜谱

仓库根：`/Users/zhourui/Desktop/zirconeey.github.io`
菜谱目录：`_notes/life/recipes/<slug>.md`
图片目录：`/files/images/recipes/<slug>/`（cover 图必须存在，可先放占位 svg）

## 内容要求（来自 memory feedback_recipe_generation，**必须遵守**）

1. **公制单位**：g / ml / cm / ℃ 为主；为美国读者方便可在购物指引部分附 ℉ 或 lb 双标
2. **拒绝模糊**：禁用“少许、适量、约、稍微、看情况”。所有用量精确到个位 g/ml；时间精确到分钟；温度精确到 ℃
3. **品牌精确**：超市名 / 货架名 / 推荐品牌一定写出（Walmart 的 Kikkoman、亚超的 Pearl River Bridge / Lee Kum Kee、Kerrygold butter 等）
4. **备菜显式并行**：在 prep 段必须用粗体标出“备菜约 X 分钟，核心并行点是……”，把可同时做的事情显式列出
5. **失败诊断**：小贴士里要给出常见失败模式的判断方法和补救（如“太淡补 5 ml 生抽；太咸加 20 ml 热水 + 5 g 冰糖再煮 2 分钟”）

## Front-matter（layout `recipe.html` 强制读取，不可省）

```yaml
---
layout: recipe
title: "<中文菜名>"
slug: "<kebab-case 拼音或英文>"
date: <YYYY-MM-DD>
author: "Zircon"
main_category: "生活攻略"
sub_category: "菜谱"
permalink: "/life/recipes/<slug>"

cover: "/files/images/recipes/<slug>/cover.svg"  # 或 .jpg

cuisine: "<中餐 / 西餐 / 日料 / 烘焙 / ...>"
category: "<主菜 / 凉菜 / 汤 / 主食 / 甜点 / 早餐 / ...>"
total_time: <整数分钟>
difficulty: <1-5 整数>

ingredients:
  - { name: "<食材名>",   amount: "<数字 + 单位>" }
  - { name: "<食材名>",   amount: "<数字 + 单位>（可加括注用途）" }

prep: |
  备菜总用时约 <X> 分钟，核心并行点是**<具体并行项>**可以同时<具体动作>。

  **1. 先切（开火前完成）**

  - <具体食材> 切 <具体尺寸>（说明尺寸为何重要）
  - ...

  **2. <下一阶段名>（约 <X> 分钟）**

  - ...

  **3. 该阶段同步进行（这是唯一的并行窗口）**

  - ...

steps:
  - "第 1 步精确描述。**全程小火**，约 X 分钟后<具体可观察判据>立刻下一步。"
  - "第 2 步……"

tags: ["<2-4 个标签>"]
published: true
featured: false  # 可省略；置 true 让这道菜永远占据 /life/recipes/ 主页前排（在「最近 10 道」section 内置顶）
---
```

## 置顶（`featured`）

`/life/recipes/` 主页只显示 10 道菜：先按 date 倒序，但 `featured: true` 的菜会**钉在最前**（多个 featured 之间也按 date 倒序）。

- 不需要置顶 → 字段不写或写 `featured: false`，效果一样
- 想让这道菜不被新菜挤掉 → `featured: true`
- featured 数 > 10 时，主页只显示最近 10 个 featured 的，其它在 `/life/recipes/all/` 找
- 如果用户说“把这道菜置顶 / 钉到主页”，就给现有菜谱加这一行

## `---` 之下的正文（两段，按顺序）

### 1. 购物指引（美国超市）

强制表格：

```markdown
## 购物指引（美国超市）

| 食材 | Walmart 货架 | 亚超（H-Mart / 99 Ranch / 大华）| 备注 |
|------|-------------|-----------------------------|------|
| <食材> | <Walmart 上具体的货架名/英文名/价格区间> | <亚超推荐品牌> | <注意事项 / 替代品> |
```

每一行都要写实，不能写“自行寻找”。Walmart 没有的食材标 ❌，少见的标 ⚠️。

### 2. 小贴士

bullet 列表，覆盖：
- 关键尺寸/温度的灵敏度（“切到 3 cm 要炖 70 分钟”）
- 关键判据（“糖色判断：盯住颜色，**不看时间**”）
- 替代锅具的注意点
- 口味微调（咸淡补救）

## 字段含义对照（layout 实际渲染）

读 `_layouts/recipe.html` 第 64-127 行：
- `ingredients` → 食材网格（双列）
- `prep` → 备菜段（markdownify 渲染粗体/列表）
- `steps` → 做法段（圆形数字徽章 + markdownify）
- `cover` → 顶部封面图（圆角）
- `total_time` → 顶部 `⏱ X min`
- `difficulty` → 顶部星级（★☆）
- `cuisine` + `category` → 顶部 `🍜 <cuisine> · <category>`
- 正文 markdown 内容 → 底部“备注/购物指引/小贴士”区域
- `tags` → 顶部圆角标签

## 写完后

1. 让 cover 图存在（必要时让用户提供，或从已有菜的 cover.svg 复制一个临时占位）
2. 跑 `/fix-quotes _notes/life/recipes/<slug>.md` 把直引号转中文弯引号
3. 自动 `git add <files> && git commit -m "add recipe: <菜名>" && git push`

## 参考样板

- `_notes/life/recipes/hongshaorou.md`（红烧肉，结构最完整）
- `_notes/life/recipes/tangcujixiong.md`
- `_notes/life/recipes/heijiaoyangcongniupai.md`

打开任意一篇照着结构写，30 篇零漂移。

## 索引页

`/life/recipes/index.html` 是聚合页，新菜会自动出现，不用手工注册。
