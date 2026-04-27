---
name: fix-quotes
description: 调用仓库内 `scripts/fix_quotes.py`，把 markdown 文件正文里的 ASCII 直引号 (`"`) 按出现顺序交替替换为中文弯引号（`"` / `"`）。当用户说"统一引号 / 修引号 / 把这篇的引号转中文 / 跑 fix_quotes"等时使用。脚本会自动跳过 YAML front-matter、代码块和 HTML 标签行，安全。
---

# fix-quotes — 统一中文弯引号

仓库根：`/Users/zhourui/Desktop/zirconeey.github.io`
脚本路径：`scripts/fix_quotes.py`

## 脚本能力（不要重写它）

- 把 ASCII `"` 按配对顺序替换为 `"` / `"`（U+201C / U+201D）
- **自动跳过**：YAML front-matter、围栏代码块（``` 或 ~~~）、行内反引号、HTML 标签所在行（如 `<img src="...">`、`<p class="img-caption">`）
- **保留英寸符号**：数字紧跟 `"`（如 `12"`、`6.5"`）不会被替换

## 调用方式（4 种）

### 1. 处理指定文件（最常用）

```bash
python3 scripts/fix_quotes.py <path1> [<path2> ...]
```

例：`python3 scripts/fix_quotes.py _notes/essays/birthday-21.md`

### 2. 仅处理 git 暂存区的 .md（commit 前 hook 风格）

```bash
python3 scripts/fix_quotes.py --staged
```

### 3. 全仓扫描

```bash
python3 scripts/fix_quotes.py --all
```

### 4. 预览（不写盘）

任何模式加 `--dry-run`：

```bash
python3 scripts/fix_quotes.py --all --dry-run
```

## 何时该跑

- 用 `/new-post` 或 `/recipe` 写完一篇新文章，**结束之前**跑一次（指定那个新文件）
- 用户从 Word / 微信 / VSCode 复制的内容里有大量直引号
- commit 前批量整理：`--staged --dry-run` 先看，再正式跑

## 实施步骤（skill 被调起来时怎么做）

1. **定位目标文件**：
   - 用户给了路径 → 直接用
   - 用户没给 → 看当前会话最近编辑/新建的 markdown 文件
   - 都不明确 → 问用户：单文件 / 暂存区 / 全仓扫描？
2. **先 dry-run 看预期改动**（除非用户明确说“直接跑”）：
   ```bash
   python3 scripts/fix_quotes.py <path> --dry-run
   ```
3. 输出“X 个文件将改 Y 处”，让用户确认
4. **正式跑**（去掉 `--dry-run`）
5. 跑完用 `git diff <path>` 给用户看实际变化
6. 如果是接在 `/new-post` 或 `/recipe` 后面，可以顺手把这次修改合进上一次的 commit（feedback_git_workflow 的一部分），或者另起一个小 commit

## 注意

- 这个脚本**只处理直引号**，不处理别的标点（不转 `,` → `，` 之类）。文件名虽然叫 fix-quotes 但范围窄。
- 脚本原文档在 `scripts/fix_quotes.py` 头部，有完整说明。
