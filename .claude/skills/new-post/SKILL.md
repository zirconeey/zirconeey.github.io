---
name: new-post
description: 在 zirconeey.github.io 站新建一篇博客文章。根据文章类型（essay / course-review / study-note）自动套用正确的目录、front-matter schema 和图片资源约定。当用户说"写一篇博客 / 新建文章 / 写新的 essay / 加一篇课程测评 / 加一篇错题本"等时使用。
---

# new-post — 新建博客文章

仓库根：`/Users/zhourui/Desktop/zirconeey.github.io`

## 第一步：确认文章类型

如果用户没有明确说，问一句他要写哪种：

| 类型 | 用途 | 目录 |
|---|---|---|
| `essay` | 个人随笔、生活感悟、生命故事 | `_notes/essays/` |
| `course-review` | 课程测评 | `_notes/course-reviews/` |
| `study-note` | 学习笔记、错题本、考试备考 | `_notes/<topic>/` 或 `_notes/study/<course>/` |

**菜谱不要用这个 skill，请用 `/recipe`。**

## 第二步：确认 slug、标题、日期、放图位置

- **slug**：kebab-case，从标题提炼（中文标题让用户给个英文 slug）
- **title**：保留中文原标题，用双引号包起来
- **date**：今天的日期，格式 `YYYY-MM-DD`（essay 用引号 `"2024-12-19"`，course-review/study-note 不带引号也行）
- **图片目录**：所有插图放 `/files/images/{slug}/`，文中用相对路径或 `/files/images/{slug}/01.jpg`

## 第三步：按类型生成 front-matter

### essay（`_notes/essays/{slug}.md`）

```yaml
---
layout: post
title: "<中文标题>"
main_category: "<如：随笔漫谈 / 思考记录 / 生活攻略>"
sub_category: "<如：生命故事 / 阅读笔记 / ...>"
date: "<YYYY-MM-DD>"
author: "Zircon"
permalink: "/essays/<slug>"
reactions: ["🎂", "🎉", "❤️"]   # 3-6 个 emoji，可让用户自选
published: true
---
```

### course-review（`_notes/course-reviews/{slug}.md`）

slug 推荐：`<course-name>-review-<year>`（如 `behavioral-econ-review-2023`）

```yaml
---
layout: post
title: "（个人向）<课程名>课程测评"
date: <YYYY-MM-DD>
discipline: "<如：经济学 / 数学 / 计算机>"
course: "<课程中文名>"
material_type: "课程测评"
review_category: "<同 discipline，用于聚合页归类>"
semester: "<如：2022 秋 / 2024 春>"
---
```

### study-note（位置取决于话题）

**目录约定（看 `_notes/` 既有结构）：**
- 语言考试 → `_notes/gre/<slug>.md` 或 `_notes/toefl/<slug>.md`
- 大学课程笔记 → `_notes/study/<course-slug>/<slug>.md`（如 `_notes/study/game-theory/lec01.md`）
- 科研类 → `_notes/research/<slug>.md`
- 生活攻略 → `_notes/life/<slug>.md`（**菜谱例外，去 `/recipe`**）

```yaml
---
layout: post
title: "<标题>"
date: <YYYY-MM-DD>
discipline: "<如：语言考试 / 经济学>"
course: "<如：GRE / 博弈论>"
material_type: "<如：错题本 / 课程笔记 / 备考心得>"
---
```

## 第四步：正文规则（所有类型通用）

- **标题前不要加 `---` 分割线**（front-matter 那个 `---` 已经是分隔符，正文里第一个标题前别再加）
- 引用 markdown 图片：`![](/files/images/{slug}/01.jpg)`，紧接着另起一行写图片配文：

  ```html
  <p class="img-caption">这里是配文</p>
  ```

  这是 zirconeey 站的固定格式，由 `_layouts/post.html` 的 CSS 渲染。**不要用 markdown 的 `*斜体*` 或 `> 引用` 充当图片配文。**
- 正文中文标点：用中文标点（“，。：；！？”“ 「」），西文术语/数字内部的标点保持半角

## 第五步：处理图片

如果用户提供了图片，新建目录 `/files/images/{slug}/`，把文件放进去（按 `01.jpg`、`02.jpg` 顺序命名）。

## 第六步：写完后

1. 提示用户回顾一下 front-matter（尤其是 essay 的 `main_category` / `sub_category` 是否合适）
2. 自动 `git add <new-files> && git commit -m "..." && git push`（按 memory 里 feedback_git_workflow 的约定）
3. commit message 用中文，简洁描述：”add essay: <标题>“ 之类

## 参考文件

- `_layouts/post.html` —— 渲染逻辑、caption CSS（第 186-195 行）
- `_notes/essays/birthday-21.md` —— essay 完整样板
- `_notes/course-reviews/behavioral-econ-review-2023.md` —— course-review 样板
- `_notes/gre/gre-verbal-errors.md` —— study-note 样板

## 写完后可选优化

- 跑 `/fix-quotes <new-file-path>` 把 ASCII 直引号统一成中文弯引号
