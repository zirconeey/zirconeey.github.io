---
layout: post
title: "美国签证完全指南：从 F-1 到绿卡，每种身份能做什么、不能做什么"
date: 2026-04-28
main_category: "生活攻略"
sub_category: "留学攻略"
permalink: "/life/us-visa-types"
---

# 1. 这篇文章给谁看

写给**中国大陆背景在美或将赴美的学生、学者、求职者**。文章的核心问题不是“怎么申请签证”——那是律师和官方的工作——而是**“我手里这张签证（或我即将申请的这张签证），到底允许我做什么、明确禁止我做什么”**。这个问题答错代价极大：轻则失去身份、重则永久不能再入境。

文章按身份阶段串联——从**短期访问 → 学生 → 学习期间的工作豁免 → 工作签证 → 绿卡**——每一类只挑中国读者最常用的几种讲清楚，**不堆全部 80 多种签证字母代码**。

> ⚠️ 签证规则会频繁变动，文中所有具体数字（配额、有效期、排期）以**美国国务院 / USCIS / 你所在学校的 ISSO 办公室**最新公告为准。复杂个案请咨询移民律师，本文不构成法律建议。

# 2. 全景图

绝大多数中国学生 / 学者 / 求职者的身份变化路径，就在下面这张图里。三条主流路径终点都是绿卡，差别是中间走多少弯路。

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" style="max-width:100%;height:auto;display:block;margin:1.2em auto;">
  <text x="380" y="20" text-anchor="middle" font-size="14" font-weight="600" fill="#333">中国学生赴美：从 F-1 到绿卡的三条主流路径</text>

  <!-- Path A: 工作主流 -->
  <text x="40" y="68" font-size="12" fill="#c0392b" font-weight="600">路径 A · 工作主流</text>
  <g transform="translate(60, 80)" font-family="sans-serif" font-size="11">
    <rect x="0" y="0" width="80" height="36" rx="6" fill="#fff8f0" stroke="#444"/>
    <text x="40" y="22" text-anchor="middle">F-1</text>
    <line x1="80" y1="18" x2="115" y2="18" stroke="#666" stroke-width="1.5" marker-end="url(#arr)"/>
    <rect x="115" y="0" width="80" height="36" rx="6" fill="#fff8f0" stroke="#444"/>
    <text x="155" y="14" text-anchor="middle" font-size="10">OPT</text>
    <text x="155" y="28" text-anchor="middle" font-size="9" fill="#888">12 mo</text>
    <line x1="195" y1="18" x2="230" y2="18" stroke="#666" stroke-width="1.5" marker-end="url(#arr)"/>
    <rect x="230" y="0" width="95" height="36" rx="6" fill="#fff8f0" stroke="#444"/>
    <text x="277" y="14" text-anchor="middle" font-size="10">STEM OPT</text>
    <text x="277" y="28" text-anchor="middle" font-size="9" fill="#888">+24 mo</text>
    <line x1="325" y1="18" x2="360" y2="18" stroke="#666" stroke-width="1.5" marker-end="url(#arr)"/>
    <rect x="360" y="0" width="80" height="36" rx="6" fill="#fdf0f0" stroke="#c0392b"/>
    <text x="400" y="14" text-anchor="middle" font-size="10" fill="#c0392b">H-1B</text>
    <text x="400" y="28" text-anchor="middle" font-size="9" fill="#888">需抽签</text>
    <line x1="440" y1="18" x2="475" y2="18" stroke="#666" stroke-width="1.5" marker-end="url(#arr)"/>
    <rect x="475" y="0" width="105" height="36" rx="6" fill="#fdf0f0" stroke="#c0392b"/>
    <text x="528" y="14" text-anchor="middle" font-size="10" fill="#c0392b">EB-2 / EB-3</text>
    <text x="528" y="28" text-anchor="middle" font-size="9" fill="#888">5-7 年排期</text>
    <line x1="580" y1="18" x2="620" y2="18" stroke="#666" stroke-width="1.5" marker-end="url(#arr)"/>
    <rect x="620" y="0" width="60" height="36" rx="6" fill="#27ae60"/>
    <text x="650" y="22" text-anchor="middle" fill="#fff" font-weight="600">绿卡</text>
  </g>

  <!-- Path B: PhD 自办 -->
  <text x="40" y="148" font-size="12" fill="#2980b9" font-weight="600">路径 B · PhD 自办（不走雇主担保）</text>
  <g transform="translate(60, 160)" font-family="sans-serif" font-size="11">
    <rect x="0" y="0" width="80" height="36" rx="6" fill="#fff8f0" stroke="#444"/>
    <text x="40" y="22" text-anchor="middle">F-1 (PhD)</text>
    <line x1="80" y1="18" x2="115" y2="18" stroke="#666" stroke-width="1.5" marker-end="url(#arr)"/>
    <rect x="115" y="0" width="95" height="36" rx="6" fill="#fff8f0" stroke="#444"/>
    <text x="162" y="14" text-anchor="middle" font-size="10">毕业前后</text>
    <text x="162" y="28" text-anchor="middle" font-size="9" fill="#888">一边 OPT 一边</text>
    <line x1="210" y1="18" x2="245" y2="18" stroke="#666" stroke-width="1.5" marker-end="url(#arr)"/>
    <rect x="245" y="0" width="135" height="36" rx="6" fill="#f0f8ff" stroke="#2980b9"/>
    <text x="312" y="14" text-anchor="middle" font-size="10" fill="#2980b9">EB-2 NIW（自办）</text>
    <text x="312" y="28" text-anchor="middle" font-size="9" fill="#888">不需要雇主担保</text>
    <line x1="380" y1="18" x2="415" y2="18" stroke="#666" stroke-width="1.5" marker-end="url(#arr)"/>
    <rect x="415" y="0" width="60" height="36" rx="6" fill="#27ae60"/>
    <text x="445" y="22" text-anchor="middle" fill="#fff" font-weight="600">绿卡</text>
    <text x="540" y="22" font-size="10" fill="#888">回避 H-1B 抽签 + 雇主依赖</text>
  </g>

  <!-- Path C: 杰出人才 -->
  <text x="40" y="228" font-size="12" fill="#8e44ad" font-weight="600">路径 C · 杰出人才（学术 / 工业 top 人才）</text>
  <g transform="translate(60, 240)" font-family="sans-serif" font-size="11">
    <rect x="0" y="0" width="80" height="36" rx="6" fill="#fff8f0" stroke="#444"/>
    <text x="40" y="22" text-anchor="middle">F-1</text>
    <line x1="80" y1="18" x2="115" y2="18" stroke="#666" stroke-width="1.5" marker-end="url(#arr)"/>
    <rect x="115" y="0" width="100" height="36" rx="6" fill="#f8f0fb" stroke="#8e44ad"/>
    <text x="165" y="14" text-anchor="middle" font-size="10" fill="#8e44ad">O-1</text>
    <text x="165" y="28" text-anchor="middle" font-size="9" fill="#888">不抽签 / 雇主灵活</text>
    <line x1="215" y1="18" x2="250" y2="18" stroke="#666" stroke-width="1.5" marker-end="url(#arr)"/>
    <rect x="250" y="0" width="135" height="36" rx="6" fill="#f8f0fb" stroke="#8e44ad"/>
    <text x="317" y="14" text-anchor="middle" font-size="10" fill="#8e44ad">EB-1A（自办）</text>
    <text x="317" y="28" text-anchor="middle" font-size="9" fill="#888">中国排期 ~2-3 年</text>
    <line x1="385" y1="18" x2="420" y2="18" stroke="#666" stroke-width="1.5" marker-end="url(#arr)"/>
    <rect x="420" y="0" width="60" height="36" rx="6" fill="#27ae60"/>
    <text x="450" y="22" text-anchor="middle" fill="#fff" font-weight="600">绿卡</text>
  </g>

  <!-- 备注 -->
  <text x="40" y="320" font-size="11" fill="#666" font-weight="600">其它常见走向：</text>
  <text x="40" y="338" font-size="10" fill="#666">· J-1 学者：通常需先回国 2 年（212(e)）才能 H-1B/绿卡，除非 waiver</text>
  <text x="40" y="354" font-size="10" fill="#666">· 婚姻绿卡：与美国公民结婚直接 IR-1 / CR-1，与绿卡持有者结婚走 F2A</text>
  <text x="40" y="370" font-size="10" fill="#666">· 转 J-1 / L-1 / E-3 / TN / 投资 EB-5：少数路径，下文各节简述</text>

  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto">
      <polygon points="0 0, 10 5, 0 10" fill="#666"/>
    </marker>
  </defs>
</svg>
<p class="img-caption">三条主流路径。**路径 A** 是大多数 STEM 硕士 / 工程师走的；**路径 B** 是 PhD 圈最近几年的"自助通道"——避开 H-1B 抽签；**路径 C** 是高引论文 / 顶会奖项 / 媒体报道齐全的少数人走的。</p>

# 3. 学生与学者签证（F、J）

## 3.1 F-1 学生签证（最常见）

**是什么：** 全日制学位学习（本科 / 硕士 / 博士）或全日制语言学习用的非移民签证。最常见的中国留学生身份。

**能做：**
- 在录取学校全日制读书
- **校内打工**（学期内 ≤ 20 小时/周；假期 ≤ 40 小时/周；TA / RA / 食堂 / 图书馆 / IT helpdesk 等都算校内）
- 一年后申 **CPT**（学期内课程相关实习）/ **OPT**（毕业后 12 个月）/ **STEM OPT**（再 +24 个月）—— 详见第 4 节
- 转学（提前办 transfer SEVIS record）
- 暑假回国 / 跨国旅行（带 I-20 + valid F-1 stamp）
- **被动投资**（股票、房产、定存）—— 不算“工作”

**不能做：**
- **校外打零工 / 自由职业 / 开公司经营** —— 违法工作直接终结身份
- 全日制工作（除 OPT/STEM OPT/CPT 期间）
- 兼职 unauthorized work（写文章拿稿费、做家教、代购、自媒体接广告等都算）
- **空 SEVIS 记录** —— 转学失败、退学、毕业后超过 60 天 grace period 不离境，身份立即失效

**常见陷阱：**
- 修课不够全日制（一般本科 12 学分 / 研究生 9 学分以上）= 身份违规
- 论坛发广告、Patreon 收赞助、TikTok 接推广 —— **算工作**，没 EAD 全部违法
- 实习用 CPT 但累积超 12 个月 —— **失去 OPT 资格**

## 3.2 F-2 家属签证

F-1 持有人的配偶 + 21 岁以下未婚子女。**最严格的家属身份之一**：

- ❌ **不能工作**（任何形式 EAD 都没有）
- ✅ **可以全日制读书**（2018 年规则放宽，但**不能**直接转 F-1，要换 status）
- ✅ 可以陪读 / 在美生活

很多 F-2 配偶因为不能工作选择换成自己的 F-1（自己读书）或 J-2（如果主申请人是 J-1）。

## 3.3 J-1 交换访问签证（学者 / 短期访问 / 暑期）

J-1 是个**伞形签证**——下面有十几个子类，最常见的是：

| 子类 | 用途 | 典型时长 |
|---|---|---|
| **Research Scholar** | 大学/研究所做研究 | 最多 5 年 |
| **Professor** | 大学任教 | 最多 5 年 |
| **Short-term Scholar** | 短期访问研究 | ≤ 6 个月 |
| **Student**（college/university） | 交换学生 / 联合培养 | 与学位长度匹配 |
| **Trainee / Intern** | 学位前后实习 | 12 / 18 个月 |
| **Physician** | 临床住院医师 | 7 年内 |

**J-1 能做：**
- 完成项目所列的研究 / 教学 / 培训
- **J-1 Academic Training (AT)**：类似 F-1 的 OPT，但更严格，需要 sponsor 批准；研究领域要和项目相关
- 短期校外讲座、会议（与项目相关）

**J-1 不能做：**
- 项目之外的工作
- 改变项目主轴（要先经 Responsible Officer 批）

**最大陷阱：212(e) 两年回国服务期**

J-1 持有人**只要符合下面任一条件**，就被打上 212(e) 标记：

1. 资金来源含**美国政府或本国（中国）政府资助**（即便是部分资助）
2. 所学技能在**中国 Skills List** 上（中国的 list 极广，多数 STEM、医学、工程都在内）
3. **临床医生 J-1**（physician category）

被打上 212(e) 的人，**必须先回国服务满 2 年**，才能：
- 申请 H-1B / L-1 等工作签证
- 申请绿卡（任何类别）
- 转换成永久居民

**绝大多数中国 J-1 学者都触发 212(e)**——因为国家留学基金委（CSC）资助、Fulbright 资助、Skills List 范围广。

**怎么办？申请 212(e) waiver**，常见五种路径：
1. **No Objection Statement (NORI)** —— 中国大使馆出具“不反对”信。**最常见**，但 CSC 资助的通常拿不到
2. **Conrad 30 / IGA waiver** —— 主要给医生
3. **Persecution waiver** —— 害怕回国受迫害
4. **Hardship waiver** —— 美国公民配偶/子女遭受 exceptional hardship
5. **Department of Defense / Government Agency waiver** —— 极少数政府 sponsor 的人

**所以 J-1 的核心建议**：来美前看清楚 DS-2019 表上 212(e) 条目是 “Subject” 还是 “Not Subject”。如果是 Subject，且你不打算长期留美，**这是个 feature**；如果你想留美工作，**要么提前规划 waiver，要么换成 F-1 / H-1B**。

## 3.4 J-2 家属签证

J-1 配偶 + 21 岁以下未婚子女。**比 F-2 友好得多**：

- ✅ **可以申请 EAD 工作**（J-2 EAD，I-765 表，处理周期 3-6 个月）
- ✅ 可以全日制读书
- ⚠️ J-2 EAD 收入**不能用于 J-1 的生活费**（理论上的限制，实务很少 enforce）
- ⚠️ **如果 J-1 触发 212(e)，J-2 也跟着触发**

很多家属的策略是：J-2 + EAD 期间一边工作一边换身份（比如转 H-1B，或自己读书转 F-1）。

# 4. 学习期间的工作豁免

F-1 / J-1 学生身份本身不能在校外工作，但 USCIS 提供了几个豁免通道。

## 4.1 CPT（Curricular Practical Training）

- **谁有：** F-1 学生
- **触发条件：** 学完一个学年（暑期到入学日满 1 年；少数项目允许 day-1 CPT，但深陷争议）
- **形式：** 全职或兼职，**必须与所学专业课程绑定**（一般是必修实习课、暑期 internship 课）
- **时长：** **累积超过 12 个月全职 CPT，失去 OPT 资格**——这是踩坑大户
- **典型用途：** 暑假实习、博士最后一年的 industry collaboration

## 4.2 OPT（Optional Practical Training）

- **谁有：** F-1 学生（每个学位级别一次：本科一次、硕士一次、博士一次）
- **形式：** 毕业后 12 个月的 EAD，可以全职、不限雇主、可以 unemployed 累积 ≤ 90 天
- **触发：** 毕业前 90 天 - 毕业后 60 天窗口里申请（USCIS 处理 2-3 个月）
- **限制：** 必须与所学专业相关；**不能 unauthorized self-employment**
- **典型陷阱：** OPT 期间累积失业 > 90 天 → 身份失效；雇主必须报到 SEVP Portal

## 4.3 STEM OPT（24 个月延长）

- **谁有：** OPT 持有人 + 学位是 STEM Designated Degree List 上的专业
- **形式：** 在 OPT 12 个月之后再加 24 个月 EAD（所以 STEM 学生总共有 36 个月毕业后工作时间）
- **关键限制：**
  - 雇主必须 **E-Verify enrolled**
  - 雇主必须签 I-983 培训计划书
  - 失业累积 ≤ 150 天（含原 OPT 90 天）
  - **不能在小公司 / startup 工作**（必须有 employer-employee relationship；contractor / 三方派遣不行）
- **典型用途：** 三年 STEM OPT 期间走 3 次 H-1B 抽签；中签之前可以一直工作

## 4.4 J-1 Academic Training (AT)

- **谁有：** J-1 student
- **形式：** 与 OPT 相似但更严
- **时长：** 最多 18 个月（PhD 毕业后可以 36 个月）
- **触发：** sponsor（DS-2019 上的）批准
- **限制：** 工作必须与学习领域 directly related

# 5. 工作签证（毕业后）

## 5.1 H-1B（最常见）

- **是什么：** “Specialty occupation” 工作签证。需要**雇主担保 + 本科以上学位 + 学位与岗位相关**
- **配额：** 65,000 + 20,000（美国硕士/博士额外）= 总共 85,000 个/年
- **抽签：** 每年 3 月 H-1B Cap Lottery 注册，4 月公布结果。**美国硕士/博士 + 普通池“双抽签”**，比纯本科有约 2 倍中签概率
- **能做：** 给担保雇主全职工作；**换工作要做 H-1B Transfer**
- **不能做：** Self-employed（除非自己公司有第三方监督）；任意 freelance；担保岗位之外的工作
- **时长：** 单次 3 年，可续到 6 年；**6 年后必须出境 1 年**（除非 I-140 已批 + EB pending → AC21 延期 indefinitely）
- **配偶：** H-4。**H-4 EAD 仅当 H-1B 持有者 I-140 已批**才能拿
- **关键豁免：** 学校 / 非营利研究所 / 政府研究机构是 **cap-exempt**（教授、博士后不抽签，可以随时申）

## 5.2 O-1 杰出人才

- **是什么：** 在科学 / 教育 / 商业 / 体育 / 艺术领域有 “extraordinary ability” 的人。USCIS 列了 8 项 criteria，满足 3 项即可。
- **能做：** 给担保雇主或经纪人工作；**multiple petitioners 允许**（比 H-1B 灵活）；可以做 self-employment（通过 agent / management company）
- **时长：** 单次 3 年，**可无限续**
- **不抽签** —— 这是 H-1B 抽不中或不想抽的人的最常见 plan B
- **配偶 O-3：** **不能工作**（比 H-4 严）

最近几年圈内热门趋势：**博士后 / 高引论文学术圈 + 顶级工业届工程师**很多走 O-1。8 项 criteria 包括：奖项、独立评审记录（peer review）、原创贡献、媒体报道、专业组织 membership、高薪、学术发表、主导/关键角色。**STEM PhD 满足 3-4 项不难。**

## 5.3 L-1 跨国公司内调

- **L-1A**（高管 / 经理）：单次最长 7 年
- **L-1B**（specialized knowledge）：最长 5 年
- **触发：** 必须在海外公司全职工作 ≥ 1 年（最近 3 年内）
- **典型路径：** 国内大厂 → 入职超过 1 年 → 公司派来美国分公司
- **配偶 L-2：** 自动拿 EAD（最友好的家属身份之一）

## 5.4 TN（加拿大、墨西哥专属）

- **谁有：** 加拿大 / 墨西哥公民
- **触发：** USMCA（前 NAFTA）类别表上的职业（律师、工程师、会计、心理学家、计算机系统分析师、科学家等）
- **时长：** 3 年可无限续；**程序最简单**——加拿大公民甚至可以在边境直接申请
- **不抽签**

中国国籍读者除非已经入籍加拿大或墨西哥，否则不适用。

## 5.5 E-3（澳大利亚专属）

- **谁有：** 澳大利亚公民
- **触发：** “Specialty occupation”（与 H-1B 类似）
- **配额：** 10,500/年（实际从未用完）
- **配偶 E-3D：** 可申 EAD

中国国籍读者除非入籍澳大利亚，否则不适用。

## 5.6 H-4 EAD（H-1B 配偶工作通道）

- **谁有：** H-1B 持有者的配偶 H-4
- **触发：** H-1B 持有者**已获得 I-140 批准**（绿卡申请第一阶段）
- **意义：** 让 H-4 配偶在等绿卡的漫长岁月里能合法工作

# 6. 绿卡路径

绿卡（Lawful Permanent Resident）是终极目的地。中国大陆出生的人，**主要瓶颈是排期（visa bulletin）而非批准率**。

## 6.1 雇主担保 EB 系列

- **EB-1A 杰出人才：** 自办（不需要雇主），**门槛比 O-1 高一档**——不仅要“extraordinary”，还要证明国际/全国声誉。中国排期 ~2-3 年
- **EB-1B 杰出研究员/教授：** 需要大学/研究所雇主，但程序比 EB-2 简单。**学术圈助理教授、终身研究员的主力路径**
- **EB-1C 跨国高管：** L-1A 升级版
- **EB-2 (PERM)：** 高级学位 + 雇主担保 + 劳工证（PERM）。**中国排期 ~5-7 年**
- **EB-2 NIW（National Interest Waiver）：** 自办，**不需要雇主担保 + 不需要 PERM**。STEM PhD 圈最近 3-4 年的爆款。三个 prong：substantial merit + well positioned + waiver benefits US。中国排期同 EB-2
- **EB-3：** 学士学位 + PERM。中国排期更长
- **EB-5：** 投资移民。$800K（targeted area）/ $1.05M（其他），创造 10 个就业岗位。中国排期 ~6-8 年

## 6.2 家庭团聚

- **IR 系列**（**美国公民**的配偶 / 21 岁以下未婚子女 / 父母）：**无配额、无排期** —— 如果你和美国公民结婚，理论上 6-12 个月就能拿到 GC
- **F2A**（**绿卡持有者**的配偶 / 21 岁以下未婚子女）：有排期但通常较短
- **F1 / F2B / F3 / F4**（公民/绿卡的成年子女、兄弟姐妹）：排期非常长（10-20+ 年）

## 6.3 抽签与人道

- **DV Diversity Lottery**（绿卡抽签）：每年 5 万张，**中国大陆出生不符合资格**（通常出生在低移民率国家才行）
- **庇护 / 难民**：基于 well-founded fear of persecution
- **VAWA / U / T**：家暴 / 犯罪受害者 / 人口贩卖受害者

# 7. 短期访问

## 7.1 B-1 商务 / B-2 旅游

- **B-1：** 商务（开会、签合同、谈判、参加培训），**不能拿美国雇主薪水**
- **B-2：** 旅游、探亲、短期医疗、参加非学位课程（< 18 小时/周）
- 实务中签证页通常合并为 **B-1/B-2**
- **典型停留：** 每次入境 6 个月（实际由海关定）；签证有效期 ≤ 10 年（中国十年签证就是 B-1/B-2）
- **能做：** 旅游、探亲、参加学术会议（不能拿薪水）、看病
- **不能做：** 拿美国雇主薪水；全日制学习（要换 F-1）；做志愿者超过名义上的范围；**坐月嫂工作**（实务高发陷阱）

**最大陷阱：B-1/B-2 转 F-1 / H-1B 的“intent 问题”** —— 入境时如果海关怀疑你“真实意图”是来读书或工作而非旅游，会拒绝入境。**B → F 转换尤其敏感**，建议最好回国直接办 F-1。

## 7.2 ESTA / VWP

- **VWP**（Visa Waiver Program）：免签 90 天的 41 个国家
- **中国大陆护照不在 VWP 名单**
- 持其他国家护照（如已入籍英国 / 日本 / 韩国）的中国背景读者可以用，每次入境 ESTA 申请 $21、有效 2 年

# 8. 横向对照速查表

| 签证 | 能工作？ | 哪种工作？ | 配偶能工作？ | 主要限制 |
|---|---|---|---|---|
| **F-1** | 是（受限） | 校内 + CPT/OPT/STEM | F-2 ❌ | 校外打工违法 |
| **F-2** | ❌ | — | — | 不能工作 |
| **J-1** | 是 | 项目 + AT | **J-2 EAD ✅** | 212(e) 大坑 |
| **H-1B** | ✅ | 担保雇主全职 | H-4 EAD（仅 I-140 后） | 抽签 + 6 年限 |
| **O-1** | ✅ | 多雇主灵活 | O-3 ❌ | 门槛高 |
| **L-1** | ✅ | 同公司美国分支 | **L-2 EAD 自动 ✅** | 海外公司必须 ≥1y |
| **TN** | ✅ | USMCA 列表岗位 | TD ❌ | 仅加/墨公民 |
| **E-3** | ✅ | Specialty occupation | E-3D ✅ | 仅澳公民 |
| **B-1/B-2** | ❌ | — | — | 不能拿美雇主钱 |
| **绿卡** | ✅ | 几乎无限 | 配偶有 | 出境时长有限制 |

# 9. 避坑清单 + 实践建议

- ❌ **不要相信“灰色地带”**：朋友圈代购、TikTok 接广告、Patreon 拿赞助、做家教收现金——**全部需要 EAD**，没有 EAD 全部违法。被发现轻则失去身份，重则永久不能再入境。
- ❌ **不要用“day-1 CPT”凑学位**：很多注水学校（特别是某些“硕士项目”）允许学生入学第一天就开 CPT 工作。这种 CPT 长期被 USCIS 警惕，**未来转 H-1B / 绿卡时被拒概率高**。
- ❌ **J-1 不要忽视 DS-2019 上的 212(e) 标记**：拿到签证那天就要查“Subject to”还是“Not Subject”，并提前规划。
- ❌ **不要在 OPT / STEM OPT 期间累积失业超过限额**（OPT 90 天 / STEM OPT 总计 150 天）—— 累积满即身份失效。
- ❌ **不要在 B-1/B-2 入境后立刻申请换 F-1 / H-1B**—— 海关 / USCIS 会怀疑你“misrepresented intent”，可能终身拒签。
- ✅ **每个学校都有 ISSO（International Student Services Office）—— 任何身份疑问先问 ISSO。** 他们处理过几千个同类案子，比知乎 / 小红书可靠。
- ✅ **复杂情况一定找移民律师**：换 status、申 NIW、Day-1 CPT 风险评估、I-140 前后跳槽时机。律师费 $3K-$10K 可能为你省掉一次永久拒签。
- ✅ **签证、I-94、I-20 / DS-2019、EAD 卡——四份文件 PDF 备份在云端**，丢一份省不止一千美金麻烦。
- ✅ **每次入境后立刻查 [I-94](https://i94.cbp.dhs.gov/)** —— 海关偶尔输错日期或类型，错了要在 30 天内 correction。
- ✅ **EB-2 NIW 是 STEM PhD 的“自助通道”**—— 别等到毕业才开始想，PhD 第 3-4 年就可以开始攒 evidence（论文、专利、独立 reviewer 记录）。

# 10. 参考来源

1. **[USCIS 官方网站](https://www.uscis.gov/)** —— 最权威；任何具体案件先查这里
2. **[U.S. Department of State - Visa Bulletin](https://travel.state.gov/content/travel/en/legal/visa-law0/visa-bulletin.html)** —— 每月更新的 EB 排期表，绿卡申请人必看
3. **[r/immigration on Reddit](https://www.reddit.com/r/immigration/)** —— 社区讨论，案例多但需要交叉验证
4. **[一亩三分地“美国移民”版块](https://www.1point3acres.com/bbs/forum-184-1.html)** —— 中文最大移民讨论社区，特别是 NIW / EB-1A 实战经验
5. **[Murthy Law Firm Newsletter](https://www.murthy.com/)** —— 移民律师事务所的免费 newsletter，政策异动追踪权威
6. **学校 ISSO 网站** —— 你所在学校的 International Student Services Office，**是这十个来源里第一应该看的**
7. **[Doctor of Credit“Tax for Resident Aliens”系列](https://www.doctorofcredit.com/)** —— 涉税身份相关
8. **NAFSA: Association of International Educators** —— 学校 ISSO 老师们的行业协会，他们的 advisory 是 ISSO 的内部参考

---

最后说一件**最重要的事**：**身份合规 > 任何工作 / 实习机会**。一份再好的 offer，如果用违法工作的方式接受，将来都可能成为绿卡 / 入籍审查里的炸弹。**违法工作的“被发现概率”逐年上升**——USCIS 现在审 H-1B / EB-2 / 绿卡时会调阅 IRS 报税记录、SSA 工资记录、社交媒体、学校 SEVIS 记录、海关入境记录。**心安理得地工作，是你能给自己的最重要的“长期主义”。**
