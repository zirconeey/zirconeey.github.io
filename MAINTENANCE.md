# 维护手册

这份文档是给未来的自己（或下一次改站的人）写的。核心问题：**为什么有两个站？日常怎么改？出问题怎么排？**

## 架构速览

一人维护两个 GitHub Pages 用户站，面向两类读者：

- `zirconeey.github.io` — 中文博客 / 公众号存档，Jekyll 动态站
- `ruizhou03.github.io` — 英文学术主页，adcom / 同行专用

由于 `USERNAME.github.io` 必须属于同名账号，两个站不能用同一个仓库。所以本仓库是**唯一源**，另一个仓库是**只读镜像**。

```
本仓库 (zirconeey/zirconeey.github.io)  <<< 唯一改动入口 >>>
├── 中文博客所有内容 (_notes, _essays, ...)    → 部署到 zirconeey.github.io
├── en/index.html                              → 同步到 ↓
├── files/en/**                                → 同步到 ↓
└── .github/workflows/sync-english-site.yml    → 每次 push 后跑

ruizhou03/ruizhou03.github.io  <<< 不要手改，会被覆盖 >>>
├── index.html        ← 从 en/index.html 脱掉 Jekyll frontmatter 后覆盖写入
├── files/en/**       ← 整个目录 rm -rf 后 cp 覆盖
└── drafts/CV/        ← 本地 LaTeX 源，不参与同步（这里是历史遗留）
```

关键约束：**adcom 键入 `ruizhou03.github.io` 看到的 URL 永不跳转**，专业形象 0 损伤。

## 日常：改英文主页

全部在**本仓库**操作：

1. 编辑 [`en/index.html`](en/index.html)（顶部的 Jekyll frontmatter `permalink: /en/` 必须保留）
2. 若改到资产（CV PDF、头像等）：放进 [`files/en/`](files/en/)，HTML 里用绝对路径 `/files/en/xxx.pdf`
3. `git commit && git push`
4. 等约 1–2 分钟，刷新 <https://ruizhou03.github.io/>（可能需要清缓存）

Action 只在 push 改动了 `en/**`、`files/en/**`、或 workflow 文件本身时才触发（paths filter）。改中文博客内容不会触发同步，这是节省资源的去重设计。

## 日常：改中文博客

和合并前完全一样——Jekyll 正常流程。笔记进 `_notes/`，随笔进 `_essays/` 等等，push 后 GitHub Pages 自动构建。不会触发英文站同步。

## 验证同步是否成功

三种查法（推荐前两种）：

```bash
# 1. 查最近几次 Action 状态（无需登录）
curl -s "https://api.github.com/repos/zirconeey/zirconeey.github.io/actions/workflows/sync-english-site.yml/runs?per_page=3" \
  | python3 -c "import json,sys; [print(f\"#{r['run_number']} {r['head_sha'][:7]} {r['conclusion']} - {r['display_title']}\") for r in json.load(sys.stdin)['workflow_runs']]"

# 2. 查 ruizhou03 仓库最近的 sync bot commit
cd /Users/zhourui/Desktop/ruizhou03.github.io && git fetch && git log origin/main --oneline -5
```

3. 浏览器打开 <https://github.com/zirconeey/zirconeey.github.io/actions/workflows/sync-english-site.yml> 看详细日志。

Action 输出 `No changes to sync.` 是正常的——说明你这次 push 没改到英文站内容，不是失败。

## 初次配置 / 迁机 checklist

如果要在新机器上操作，或者整个 setup 要重建：

### SSH key（给 zirconeey 账号 push 权限）

```bash
# 看本机是否已有
cat ~/.ssh/id_rsa.pub    # 或 id_ed25519.pub
# 没有就生成
ssh-keygen -t ed25519 -C "your_email@example.com"
```

把 pubkey 贴到 <https://github.com/settings/ssh/new>（登录 zirconeey）。

本仓库的 remote 走 SSH：

```bash
git remote set-url origin git@github.com:zirconeey/zirconeey.github.io.git
```

### 跨账号 PAT（给 Action 写 ruizhou03 的权限）

1. 登录 **ruizhou03** 账号 → <https://github.com/settings/personal-access-tokens/new>
2. Fine-grained token，Resource owner = `ruizhou03`，Repository access = `ruizhou03/ruizhou03.github.io`
3. Permissions → Contents: **Read and write**（只要这一个，别给多）
4. 生成后复制 token
5. 切回 **zirconeey** 账号 → <https://github.com/zirconeey/zirconeey.github.io/settings/secrets/actions/new>
6. Name: `RUIZHOU03_PAT`（拼写必须一致，workflow 里引用这个名字）
7. Value: 粘贴 token

## PAT 轮换（1 年一次，或泄露时立即）

Token 有效期通常设 1 年，到期前 GitHub 会邮件提醒。轮换流程：

1. ruizhou03 账号 → Settings → Developer settings → Personal access tokens → 找到旧 token → **Regenerate token**（新 token 立即生效，旧的同时失效）
2. 复制新 token
3. zirconeey 账号 → `RUIZHOU03_PAT` secret 页面 → Update → 粘贴新 token
4. 触发一次 Action（改个小东西 push，或在 Actions 页点 “Run workflow”）验证

## 故障排查

### Action failure: Checkout ruizhou03 target 步骤挂了

十有八九是 `RUIZHOU03_PAT` 过期、被撤销、或权限不足。去 ruizhou03 账号的 tokens 页看状态，按“PAT 轮换”流程重建即可。

### Action failure: push 步骤挂了（403 / 404）

PAT 还在，但权限 scope 错了。确认 token 只给了 ruizhou03/ruizhou03.github.io 仓库的 Contents:write，没有别的。

### 英文页改了，ruizhou03 没更新

按“验证同步是否成功”第 1 步查 Action。如果 Action 根本没跑——检查你改的路径是否在 paths 过滤里（`en/**`、`files/en/**`）；如果 Action 跑了但说 “No changes to sync”——检查 `en/index.html` 的 Jekyll frontmatter 是不是和上次完全一样（frontmatter 内容变了但 body 没变也会被识别为“无变化”，因为同步前会 strip）。

### 手贱在 ruizhou03 仓库 commit 了

下次 zirconeey push 触发的 sync 会把你的修改覆盖掉。如果想挽救：先把 ruizhou03 的手改同步回 zirconeey 的 `en/index.html`，再 push zirconeey。

### 忘记哪个账号对哪个站

- **zirconeey** → 中文站 + 两个站的源仓库（动的那个）
- **ruizhou03** → 英文站的部署镜像（只读的那个）
- SSH key 绑定：zirconeey（因为 push 的只能是 zirconeey 源仓库）
- PAT 来源：ruizhou03（因为 Action 要从 zirconeey 写到 ruizhou03，token 要能被 ruizhou03 接受）

## 关键文件速查

| 路径 | 作用 |
|---|---|
| [`en/index.html`](en/index.html) | 英文主页源文件（Jekyll 处理），改这里 |
| [`en/sitemap.xml`](en/sitemap.xml) | 同步后挂在 ruizhou03 根目录，给 Google 索引用 |
| [`en/robots.txt`](en/robots.txt) | 同步后挂在 ruizhou03 根目录，告诉爬虫 sitemap 位置 |
| [`files/en/`](files/en/) | 英文页引用的所有资产（CV、头像、PDF）|
| [`.github/workflows/sync-english-site.yml`](.github/workflows/sync-english-site.yml) | 同步 Action 定义 |
| ruizhou03 repo 的 `README.md` | 说明镜像状态、禁止手改 |
| zirconeey 的 `index.html`（中文首页） | 包含指向英文站的 notice box |
| zirconeey 的 `_layouts/default.html` | nav 包含 `← 英文主页` 链接（非笔记页才显示）|

## SEO：让搜“Rui Zhou”能搜到本站

站内已经做了的（`en/index.html` head + 两个 root 文件）：

- `<link rel="canonical" href="https://ruizhou03.github.io/">` — 告诉 Google ruizhou03 是首选 URL，避免和 zirconeey/en/ 镜像分摊权重
- Schema.org `Person` JSON-LD — 用 affiliation/alumniOf/sameAs 把“Rui Zhou”消歧到具体的 PSU 经济系学生
- Open Graph + Twitter card — LinkedIn / 微信 / Slack 分享时能出预览图
- `sitemap.xml` + `robots.txt` 同步到 ruizhou03 根目录，由 sync workflow 自动 hoist 上来

需要你**手动**做的（站外 / 注册类，1 次性）：

1. **Google Search Console**：<https://search.google.com/search-console> → Add property → 选 URL prefix → 填 `https://ruizhou03.github.io/` → 用 HTML tag 验证（把 meta tag 加到 [`en/index.html`](en/index.html) 的 `<head>` 里 push 一次，验证通过后可以删，但留着也没坏处）→ 在 Sitemaps 里提交 `https://ruizhou03.github.io/sitemap.xml`
2. **加更多 `sameAs` 链接**：研究 profile 越多，“是哪一个 Rui Zhou”消歧越准。建议至少补：
   - Google Scholar（去 <https://scholar.google.com> 注册一个）
   - LinkedIn
   - ORCID（<https://orcid.org>，ORCID 是学界最权威的 ID 系统，2 分钟注册）
   - PSU 经济系 people page（如果有）
   补完之后把 URL 填到 [`en/index.html`](en/index.html) JSON-LD 的 `sameAs` 数组里
3. **反向链接（最关键、最慢）**：让以下页面 link 回 `https://ruizhou03.github.io/`：
   - PSU 经济系个人 profile 页（联系系办挂上）
   - 导师 / co-author 主页的“students”区
   - LinkedIn / Scholar / ORCID 的 personal website 字段
   - GitHub profile bio
   - 任何会议、talk、workshop 的 speaker bio 链接
   反向链接是排名最强的信号，但 Google 重新爬通常要 2–3 个月才看到效果

每次更新内容后，记得手动改一下 [`en/sitemap.xml`](en/sitemap.xml) 的 `<lastmod>` 日期，提示 Google 重新爬。

## 延后 / 未做的事

- **`_data/profile.yml` 抽共享元信息**：两边页面内容重叠几乎为零（中文首页是博客风自我介绍，英文是 CV 风），现在抽共享 YAML 没有可抽的。等哪天中文站加“关于我/CV”正式页再说。
- **买自定义域名统一入口**（如 `ruizhou.xyz`）：架构支持直接升级——把 zirconeey 仓库 CNAME 到新域，两个 github.io 都变成 redirect。花 ~$15/yr，现在没必要。
