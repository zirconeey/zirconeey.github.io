---
name: new-post
description: 在 zirconeey.github.io 站新建一篇博客文章。先运行时发现仓库现有的分类和样板，再按对应 schema 生成 front-matter；如果用户要的是全新一级分类，引导走"添加新分类"流程并补齐 landing 页和主页入口。当用户说"写一篇博客 / 新建文章 / 写一篇随笔 / 加一篇生活攻略 / 加一篇科研妙招 / 加一篇课程测评 / 加一篇错题本"等时使用。菜谱用 /recipe，不用此 skill。
---

# new-post — 新建博客文章

仓库根：`/Users/zhourui/Desktop/zirconeey.github.io`

> **设计原则**：本 skill **不写死分类清单**。每次调用先扫一遍仓库实际状态（目录 + main_category 取值 + landing 页 + 已有样板），用现实而非记忆做决定。仓库变化了 skill 自动跟随。

---

## 第一步：扫描仓库实际状态

每次调用 skill 都先跑：

```bash
# 1. _notes/ 一级目录
ls _notes/

# 2. 现存的 main_category 取值
grep -rh "^main_category:" _notes/ | sort -u

# 3. 哪些一级目录有 landing 页
for d in essays life research notes; do [ -f "$d/index.html" ] && echo "$d/index.html ✓"; done

# 4. 主页 cat-card 列表
grep -E 'cat-card.*href' index.html
```

读出当前真实分布。如下是写本文档时（2026-04-26）观察到的状态，仅作参考基线，**实际以现场扫描为准**：

| `main_category` | 目录 | landing 页 | 主页 cat-card |
|---|---|---|---|
| `随笔漫谈` | `_notes/essays/` | `essays/index.html` | ✓ |
| `生活攻略` | `_notes/life/` | `life/index.html`（菜谱被 sub_category 排除） | ✓ |
| `科研妙招` | `_notes/research/` | `research/index.html` | ✓ |

外加 2 种**特殊 schema**（不是 main_category 体系）：
- 课程测评：`_notes/course-reviews/`，由 `notes/index.html` 一类汇总页接管
- 学习笔记：`_notes/<exam>/`（gre, toefl, pre-high-school）、`_notes/study/<course>/`、`_notes/research/<sub>/`

---

## 第二步：判断文章归属

按以下决策树走，**不要硬套**：

1. **是菜谱？** → 退出本 skill，让用户用 `/recipe`
2. **是课程测评？** → 走 [Schema: course-review](#schema-course-review)
3. **是某门课/某次考试的学习笔记/错题本/讲义？** → 走 [Schema: study-note](#schema-study-note)
4. **是某个一级 main_category 下的内容？**
   - 匹配第一步扫描出的现有 main_category（如 `随笔漫谈` / `生活攻略` / `科研妙招`） → 走 [Schema: main-category 通用模板](#schema-main-category-通用模板)
   - **不匹配任何现有分类**（用户要开一个全新一级分类，比如“影视摘记”“旅行笔记”） → 走 [流程：添加新一级分类](#流程添加新一级分类)

**问用户**：如果他没说清楚，就用第一步扫描结果当选项让他选；或描述他这篇文章想表达什么、想出现在哪个 landing 页里。

---

## 第三步：读至少 1 篇同类样板

**写之前必须做**。每个分类下随便挑一篇近期文章 `head -20`，看它的 front-matter 实际用了哪些字段。schema 可能比文档记的还演进过；以现场样板为准。

```bash
ls -t _notes/<目标目录>/*.md | head -3   # 找最近的 3 篇
head -20 _notes/<目标目录>/<最新一篇>.md
```

---

## Schema: main-category 通用模板

适用于 **`随笔漫谈` / `生活攻略` / `科研妙招`** 这种“一级分类 + landing 页”模式，未来添加的新一级分类也用这套。

### 公共字段

```yaml
---
layout: post
title: "<中文标题>"
date: "<YYYY-MM-DD>"
author: "Zircon"
main_category: "<分类的中文 label，如 随笔漫谈 / 生活攻略 / 科研妙招>"
permalink: "<见下方>"
published: true
---
```

### 各分类的差异（按现场样板对齐，下表只是 2026-04-26 观察）

| 分类 | 目录 | permalink | 额外字段 | 样板 |
|---|---|---|---|---|
| 随笔漫谈 | `_notes/essays/<slug>.md` | `/essays/<slug>` | `sub_category`（如 生命故事 / 阅读笔记）<br>`reactions: ["🎂", "🎉", "❤️"]`（3-6 个 emoji） | `_notes/essays/birthday-21.md` |
| 生活攻略 | `_notes/life/<slug>.md` | `/life/<slug>` | `extra_categories: [科研妙招]`（可选，跨分类聚合）<br>`sub_category`（可选） | `_notes/life/vpn-setup-ios.md` |
| 科研妙招 | `_notes/research/<topic>/<slug>.md` | `/research/<topic>/<slug>` | `sub_category`（如 R 教程 / LaTeX） | `_notes/research/r-tutorials/r-pca.md` |

> **permalink 默认值**：`_config.yml` 给 `_notes/` collection 设了默认 `/notes/:path/`。但**生活攻略**有专属 URL 前缀 `/life/<slug>`（不带 notes/，因为分类名就是 life，notes/ 多余）——必须**手写 permalink 覆盖默认**。其它分类（essays 用 `/essays/`、research 用 `/research/<topic>/<slug>`）也都各自手写 permalink。看那个分类的 landing 页里 Liquid 用什么 URL 链接到文章，就跟它对齐。

---

## Schema: course-review

```yaml
---
layout: post
title: "（个人向）<课程中文名>课程测评"
date: <YYYY-MM-DD>
discipline: "<如 经济学 / 数学 / 计算机>"
course: "<课程中文名>"
material_type: "课程测评"
review_category: "<同 discipline，用于聚合页归类>"
semester: "<如 2022 秋 / 2024 春>"
---
```

- 目录：`_notes/course-reviews/<course-slug>-review-<year>.md`
- 不用 main_category；由 `notes/index.html` 等汇总页接管
- 样板：`_notes/course-reviews/behavioral-econ-review-2023.md`

---

## Schema: study-note

```yaml
---
layout: post
title: "<标题>"
date: <YYYY-MM-DD>
discipline: "<如 语言考试 / 经济学 / 心理学>"
course: "<如 GRE / 博弈论 / 行为经济学>"
material_type: "<如 错题本 / 课程笔记 / 备考心得 / 讲义>"
---
```

**目录由话题决定**（看 `_notes/` 现有划分）：
- 大型考试 → `_notes/<exam>/<slug>.md`（gre, toefl, pre-high-school）
- 大学课程笔记 → `_notes/study/<course-slug>/<slug>.md`
- 科研工具/方法 → `_notes/research/<sub-topic>/<slug>.md`

样板：`_notes/gre/gre-verbal-errors.md`

---

## 流程：添加新一级分类

用户想开一个**全新**的 main_category（既有“随笔漫谈/生活攻略/科研妙招”之外，例如“影视摘记”“旅行笔记”），不只是写一篇文章。这一节告诉你怎么做。

### 1. 与用户确认 4 个参数

| 参数 | 例 | 说明 |
|---|---|---|
| 一级分类的中文 label | 影视摘记 | 即 `main_category` 字段值 |
| 目录名（kebab-case） | `films` | `_notes/films/` |
| permalink 前缀 | `/films/` 或默认 `/notes/films/` | 决定要不要在文章 front-matter 里写 permalink |
| 主页 cat-card 图标和描述 | 🎬 / “Film Notes” | 给 `index.html` 加入口用 |

### 2. 创建目录和占位

```bash
mkdir -p _notes/<dirname>
mkdir -p files/images/<dirname>   # 文章图片用
```

### 3. 创建 landing 页 `<dirname>/index.html`

**复制 `life/index.html` 当模板**（它的 Liquid 过滤逻辑最完整：`where: main_category` ∪ `extra_categories contains` − 排除特定 sub_category）。修改 4 处：

1. `front-matter title` → 新分类的中文 label
2. `<h1>` 文字 → 新分类的中文 label
3. `<p>` 副标题 → 英文副标题
4. `where: "main_category", "<旧值>"` → `<新值>`（改两处：main 过滤 + extra_categories 过滤）
5. （可选）如果要把某 sub_category 排除（参考 life 排除“菜谱”），保留那行 `where_exp` 并改值；否则删掉

### 4. 给主页 `index.html` 加一张 cat-card

参考 `index.html` 里现有的 `.cat-card` 写法。一般是：

```html
<a href="/<dirname>/" class="cat-card">
  <span class="cat-icon">🎬</span>
  <div>
    <div class="cat-name"><新中文 label></div>
    <div class="cat-count">{{ site.notes | where: "main_category", "<新中文 label>" | size }} 篇</div>
  </div>
</a>
```

### 5. （可选）登记到 `_config.yml`

目前 `_config.yml` 里**没有集中分类清单**，所以一般不用动它。除非你要给这个分类加专属 collection 或排序，否则跳过。

### 6. 写第一篇文章

回到 [Schema: main-category 通用模板](#schema-main-category-通用模板)，把 `main_category` 设成新建的 label。

---

## 通用正文规则（不论哪种 schema）

- **slug**：kebab-case，从标题提炼；中文标题让用户给一个英文/拼音 slug
- **date**：今天的日期，`YYYY-MM-DD`。essay 的样板用引号包住，其他可不带引号，YAML 解析都通过
- **图片目录**：`/files/images/<slug>/`（菜谱例外，那是 `/files/images/recipes/<slug>/`）
- **图片引用**：

  ```markdown
  ![](/files/images/<slug>/01.jpg)
  <p class="img-caption">这里是配文</p>
  ```

  配文**必须**用 `<p class="img-caption">`，由 `_layouts/post.html` CSS 渲染。**别用斜体或引用块替代。**
- **标题前不要 `---`**：YAML front-matter 那两道 `---` 之外，正文里第一个标题前别加分割线
- **中文标点**：用中文标点（“，。：；！？「」”），西文术语/数字内部保持半角

---

## 写完后

1. 让用户回顾 front-matter（特别是新一级分类时，确认主页 cat-card 和 landing 页都补到位）
2. 跑 `/fix-quotes <new-file-path>` 把 ASCII 直引号转中文弯引号
3. 自动 `git add <new-files> && git commit -m "<中文 commit msg>" && git push`
   - 单文章：`add <type>: <标题>`
   - 新分类：`category: bootstrap <中文 label>`（带 landing 页 + cat-card + 第一篇）

---

## 参考文件

- `_config.yml` —— `collections.notes` 默认 permalink `/notes/:path/`
- `_layouts/post.html` —— 渲染逻辑、caption CSS（第 186-195 行）
- `<category>/index.html`（如 `life/index.html`、`essays/index.html`） —— landing 页 Liquid 过滤模板
- `index.html` —— 主页 cat-card 入口位置
- 各 schema 的样板文件见上文每节脚注
