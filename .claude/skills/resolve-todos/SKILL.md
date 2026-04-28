---
name: resolve-todos
description: 系统化处理 LaTeX 讲义里的 \todo{...} 注解：先 grep 收集所有 todo + 上下文，按"知识/确认/可视化/格式"四类分组，给每条提出修改方案，等用户批准后再分组 commit 落盘。当用户说"解决我的 todo / 处理我的 todo / 把这章的 todo 收掉 / 清掉 todo / 把 todo 解决了"时使用。
---

# resolve-todos — 收掉 LaTeX 讲义里的 `\todo{...}`

## 适用范围

- 任何使用 `\todo{...}` 宏（定义在项目 `commands.tex` 中）的 LaTeX 讲义项目。
- 当前已知项目：`/Users/zhourui/Desktop/zirconeey.github.io/files/adv-micro-psu/`（ECON 521 高微讲义）。
- 编译命令固定为 `xelatex -synctex=1 -interaction=nonstopmode Micro.tex`（项目里有中文章节，pdflatex 不行）。

## 流程总览（六步）

1. **定位** 所有 `\todo{...}` 行
2. **提取** 每条 todo 的上下文（前后 5–10 行）
3. **分类** 成 A/B/C/D 四类
4. **提案** 一次性把所有方案 dump 给用户
5. **等批** 用户回 OK / 调整后才动手
6. **落地** 按类别分 3–4 个 commit，每组结束 `xelatex` 验证

⚠️ 绝对不要省略第 4–5 步直接改文件。用户的 todo 经常是反思性的、“我自己也没想清楚”，不能假设你的方案默认正确。

## Step 1 — 定位

```bash
grep -rn "\\todo{" chapters/
```

把每行编号。注意：**一行可能有多条 `\todo{...}`**（在同一段里塞了两个问题）；分别计数。

## Step 2 — 提取上下文

每条 todo：
- 用 `Read` 取所在文件的 ±5 行（句子边界要清楚）
- 必要时取整个 `\rmkb{...}` / `\propp{...}{...}{...}` / `\thmpf{}` 块

可以并行批量 Read 多个 offset。

## Step 3 — 分类（核心，必须照做）

### A 类 — 知识题
用户在 todo 里问 “X 是什么 / 这句话啥意思 / 为什么 Y / Z 怎么定义”。

**处理动作**：先在回复里给用户一个清晰解答（用中文，简明扼要，必要时带公式）。再决定是否把解答塞进正文：
- 概念性术语澄清 → 加 `\rmkb[Title]{...}` 块或新 `\defn{...}{...}`
- 短脚注能讲清楚的 → 加 `\footnote{...}`
- 一句话能补 → 改成 inline parenthetical 或换词
- 用户的疑问其实暴露了原文写得绕 → 重写那句话

### B 类 — 自我确认
用户在 todo 里**已经把答案写出来了**，只是不确定。例：
- “i think basically X. is that right?”
- “so this is Y, namely Z.”

识别信号：todo 文本以 “i think” / “so” / “namely” / “is this correct” / “is it because” 开头大概率是 B 类。

**处理动作**：直接确认正确（如果对），把 todo 删掉。可选：把那句话精炼后落到正文做澄清。错的话照 A 类处理。

### C 类 — 可视化 / 结构补充
用户提议加图、加节、加表、画时间轴、用 automaton 表示 ……

**处理动作**：评估值不值得加，给具体 tikz/tabular 草稿（不要只说“加个图”）。如果加 subsection，明确插入位置和结构（标题、若干 ex/rmkb 块、forward reference）。

### D 类 — 格式统一
关于 `\smallskip` / `\medskip` 用法、定义环境间距、命名约定 ……

**处理动作**：默认**只在本章统一**，不动 `theorems.tex` / `commands.tex`（避免 blast radius 影响其他章节）。如果用户明确要全局改，再考虑动 preamble。

## Step 4 — 提案

把所有 todo 的处理方案一次性 dump 给用户，格式：

```
## A 类（N 个）
### 1. ch11:8 — 用户问 "stage game 是什么 + S_i 行动还是策略"
**回答**：[简明解释]
**改动**：在 §11.1 setup 后插入 `\rmkb[Terminology]{...}`，删 todo。

### 2. ...

## B 类（M 个）
...

## C 类（K 个）
...

## D 类（L 个）
...
```

每条都要有 location + 问题 + 答案 + 改动方案。**不要边写边改文件。**

最后给一个 commit 分组建议，让用户确认。

## Step 5 — 等批

等用户回复。常见回应：
- “全 OK，开做” → 进入 Step 6
- “X、Y 不要改，其它照做” → 删除对应方案，剩下的进入 Step 6
- “Y 解释一下” → 补充解释，再等批
- “改成 Z 这样” → 调整方案后再等批

## Step 6 — 落地

**默认 4 个 commit**（commit 1+2+3 处理 todo 本身，commit 4 是 SKILL/工具改动 ；如果没碰 SKILL 就 3 个 commit）：

| commit | 内容 | 范围 |
|---|---|---|
| 1 | A + B 类 | 文字解释、`\rmkb`/`\defn` 插入、删 todo |
| 2 | C 类 | tikz 图、新 subsection、表格补充 |
| 3 | D 类 | 格式审计、移除多余 spacing |

每组结束：
```bash
cd /path/to/project && xelatex -synctex=1 -interaction=nonstopmode Micro.tex
```
确认页数符合预期、无 error。Overfull hbox 警告可以忽略；Missing character 警告（Chinese 字符）可以忽略——这些是项目固有的。

Commit 后：
```bash
git add chapters/<file>.tex Micro.pdf Micro.synctex.gz [Micro.tex if changed]
git commit -m "$(cat <<'EOF'
<concise subject line>

<bullet body explaining the resolution>

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
git push
```

⚠️ commit 子集要点：
- `Micro.pdf` / `Micro.synctex.gz` 跟 chapters 一起提交（项目仓库版本化 PDF）
- **不要**提交 `.aux` / `.log` / `.fls` / `.out` / `.toc` / `.fdb_latexmk`（项目根 `.gitignore` 已排除）
- 编译失败不要 force-commit，先 fix

最后一组 commit 结束后 `grep -rn "\\todo{" chapters/` 应该返回空。

## 关键约定

1. **绝不静默改 todo**——必须先 dump 全部方案给用户看。
2. **B 类识别**：用户写“i think / so / namely”开头的 todo 大概率是自我确认，不要再啰嗦解释。
3. **改正文三档**（按侵入性从轻到重）：换词 / parenthetical → footnote → `\rmkb`/`\defn` 块。能用轻量的就别用重量的。
4. **不要破坏证明结构**：`\thmpf{}` 内部的 Step 1/2/3 顺序、变量命名、引用编号都要保留。
5. **编译失败排错先于 commit**：unicode 错（中文字符）→ 用 `xelatex` 不是 `pdflatex`；missing tikz library → 在 `Micro.tex` 加 `\usetikzlibrary{...}`；undefined control sequence → 检查是否拼错 `\rmkb` 之类的环境名。
6. **跨章节统一**：本 skill 默认 batch 处理“当前 batch 的所有 todo”——可以 cross-chapter，不限制单文件。

## 触发短语

- 解决我的 todo
- 处理我的 todo
- 收掉这章的 todo
- 清掉 todo
- 把 todo 解决了
- 跑 resolve-todos

英文：resolve my todos / clear the todos / handle my todos.

## 微示例（一条 A 类 todo 的完整生命周期）

**grep 行**：
```
ch11:8: ...$S = \prod_{i=1}^n S_i$.\todo{what does the term ``stage game'' mean? ... $S_i$ defined as action set, but earlier we called it strategy set ...}
```

**Read 上下文**：发现是 §11.1 Setup 段，刚定义 $G$ 之后的位置。

**分类**：A 类（用户问两个概念问题）。

**提案给用户**：

> 1. ch11:8 — 用户问“stage game” + “$S_i$ 行动还是策略”。
> **回答**：stage game = 反复重复的那个 one-shot normal-form game；这里的 $S_i$ 是 action set。在 one-shot 里行动=策略，但在重复博弈里 strategy 是 history→action 的映射，跟 action 分开。
> **改动**：在 §11.1 Setup 段后插入 `\rmkb[Terminology: ``Stage Game'' and ``Action vs. Strategy'']{...}`；删 todo。

**等批**：用户回“OK”。

**落地**：
```latex
% 删除 \todo{...} 部分
% 在原段后插入：
\rmkb[Terminology: ``Stage Game'' and ``Action vs.\ Strategy'']{
  ...
}
```

跟 commit 1 一起 push。

## 参考实施记录

- 2026-04-28：首次成功执行此流程，处理了 adv-micro-psu 仓库 ch10/ch11 的 20 条 todo（A 类 11 条 + B 类 5 条 + C 类 3 条 + D 类 1 条），分 3 个 commit 落地（33aa268、895be0b、73cfbc7）。这次执行直接催生了本 SKILL。
