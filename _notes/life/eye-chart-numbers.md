---
layout: post
title: "视力表上的 5.0 / 1.0 / 4.8 / 20/20 都是什么意思？"
date: 2026-04-27
main_category: "生活攻略"
sub_category: "生活之问"
permalink: "/life/eye-chart-numbers"
---

# 1. 问题

体检视力表上有人念 5.0，验光单写 1.0，电影里美国医生说 20/20，朋友圈里还有人晒 4.8——这些数字都在量同一件事吗？

# 2. 结论先行

它们量的是**同一件事**——你眼睛能分辨多细的细节——只是用三种不同的“刻度”在表达：

- **20/20 制**（Snellen，欧美主流）：分数形式，分母越大视力越差。
- **小数制**（Decimal，亚洲常用）：直接把分数算成小数，1.0 = 20/20。
- **五分制**（中国国标 GB 11533-2011）：把视力**取对数**再用 5 减一下，5.0 = 1.0 = 20/20。

**哪个更科学？**——五分制和它背后的 logMAR 是国际眼科公认的金标准，因为它是**等距对数刻度**，可以做加减、求平均、做统计；小数制和 20/20 不能。日常看大概值哪个都行；做研究、手术评估、跟踪近视进展，认 logMAR / 五分制。

# 3. 科学原理

## 3.1 视力到底在量什么：最小分辨角（MAR）

人眼能不能“看清”，取决于两个相邻的细节在视网膜上能不能被分开。眼科里用一个标准量来描述：**MAR**（Minimum Angle of Resolution，最小分辨角），单位是**角分**（1° = 60 角分）。

一个“标准好眼”的 MAR 是 **1 角分**——也就是说，相距 1 角分的两条线能被分开。视力表上一个标准视标（E 字、C 字或 Snellen 字母）整体高度占 **5 角分**，其中每一笔的粗细恰好是 1 角分。这是国际通用的设计约定，所有视力表都按这个几何来定义视标尺寸。

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 240" style="max-width:100%;height:auto;display:block;margin:1.2em auto;">
  <g transform="translate(70,120)">
    <ellipse cx="0" cy="0" rx="28" ry="17" fill="none" stroke="#333" stroke-width="2"/>
    <circle cx="0" cy="0" r="8" fill="#333"/>
    <text x="0" y="42" text-anchor="middle" font-size="13" fill="#666">观察者</text>
  </g>
  <line x1="110" y1="120" x2="430" y2="120" stroke="#999" stroke-width="1" stroke-dasharray="5,5"/>
  <text x="270" y="113" text-anchor="middle" font-size="12" fill="#666">5 米 / 20 英尺</text>
  <g transform="translate(460,60)">
    <rect x="0" y="0" width="100" height="20" fill="#222"/>
    <rect x="0" y="40" width="80" height="20" fill="#222"/>
    <rect x="0" y="80" width="100" height="20" fill="#222"/>
    <rect x="0" y="0" width="20" height="100" fill="#222"/>
  </g>
  <line x1="575" y1="60" x2="575" y2="160" stroke="#c0392b" stroke-width="1.5"/>
  <line x1="569" y1="60" x2="581" y2="60" stroke="#c0392b" stroke-width="1.5"/>
  <line x1="569" y1="160" x2="581" y2="160" stroke="#c0392b" stroke-width="1.5"/>
  <text x="595" y="115" font-size="13" fill="#c0392b">整体 5 角分</text>
  <line x1="460" y1="180" x2="480" y2="180" stroke="#27ae60" stroke-width="1.5"/>
  <line x1="460" y1="174" x2="460" y2="186" stroke="#27ae60" stroke-width="1.5"/>
  <line x1="480" y1="174" x2="480" y2="186" stroke="#27ae60" stroke-width="1.5"/>
  <text x="470" y="205" text-anchor="middle" font-size="13" fill="#27ae60">单笔 1 角分</text>
</svg>
<p class="img-caption">视标的标准几何：整体高 5 角分，单笔粗 1 角分。1 角分约等于 5 米外 1.5 毫米的细节。所谓「看到 1.0」，在物理上就是这种粒度的细节你的眼睛能分开。</p>

## 3.2 三种制式的换算

设 MAR = m（单位角分），则：

- **小数制**：V = 1/m。MAR=1 → 1.0；MAR=2 → 0.5；MAR=10 → 0.1。
- **20/20 制**：V = 20/(20m)。20/40 表示别人 40 英尺能看清的，你要走到 20 英尺才看清，MAR=2，等价于小数 0.5。
- **logMAR**：logMAR = log₁₀(m)。MAR=1 → 0；MAR=2 → 0.30；MAR=10 → 1.0。
- **五分制**：V₅ = 5 - log₁₀(m) = 5 - logMAR。

写成对照表（背一张就够用）：

| 五分制 | logMAR | 小数 | 20/20 制 |
|:---:|:---:|:---:|:---:|
| 5.3 | -0.3 | 2.0 | 20/10 |
| 5.2 | -0.2 | 1.58 | 20/12.5 |
| 5.1 | -0.1 | 1.26 | 20/16 |
| **5.0** | **0.0** | **1.0** | **20/20** |
| 4.9 | 0.1 | 0.79 | 20/25 |
| 4.8 | 0.2 | 0.63 | 20/32 |
| 4.7 | 0.3 | 0.5 | 20/40 |
| 4.6 | 0.4 | 0.4 | 20/50 |
| 4.5 | 0.5 | 0.32 | 20/63 |
| 4.0 | 1.0 | 0.1 | 20/200（中国法定盲下限附近） |

所以体检表上看到 4.8，意思是你的 MAR 是 10⁰·² ≈ 1.58 角分，相当于小数 0.63、20/32——比 1.0 略差但远没到要配镜的程度。

## 3.3 为什么 logMAR / 五分制更科学：等距对数刻度

视力表每往下一行，字号都按一个固定**比例**缩小，而不是按固定**差值**。国际标准（Bailey-Lovie 1976、ETDRS 1982）规定的比例是 10⁰·¹ ≈ 1.2589——每一行字大约是上一行的 1.26 倍，也就是 logMAR 每增加 0.1 一档。

这个设计基于一个朴素观察：**人眼对“难度”的感受是对数的**。从小数 0.1 到 0.2 的提升，远比从 0.9 到 1.0 显著得多——前者把 MAR 从 10 减到 5（少了 5 角分），后者只把 MAR 从 1.11 减到 1.0（只少了 0.11 角分）。

下面这张图把“同一组 11 个视力档位”画在两种坐标轴上，一眼就能看出区别：

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 360" style="max-width:100%;height:auto;display:block;margin:1.2em auto;">
  <text x="350" y="22" text-anchor="middle" font-size="14" fill="#333" font-weight="600">同样 11 个视力档位，画在两种刻度上</text>
  <text x="50" y="68" font-size="13" fill="#333" font-weight="500">小数制（线性轴）</text>
  <line x1="50" y1="100" x2="650" y2="100" stroke="#444" stroke-width="1.5"/>
  <g stroke="#c0392b" stroke-width="2.2">
    <line x1="650" y1="92" x2="650" y2="118"/>
    <line x1="526" y1="92" x2="526" y2="118"/>
    <line x1="429" y1="92" x2="429" y2="118"/>
    <line x1="351" y1="92" x2="351" y2="118"/>
    <line x1="289" y1="92" x2="289" y2="118"/>
    <line x1="240" y1="92" x2="240" y2="118"/>
    <line x1="201" y1="92" x2="201" y2="118"/>
    <line x1="170" y1="92" x2="170" y2="118"/>
    <line x1="145" y1="92" x2="145" y2="118"/>
    <line x1="126" y1="92" x2="126" y2="118"/>
    <line x1="110" y1="92" x2="110" y2="118"/>
  </g>
  <text x="110" y="138" text-anchor="middle" font-size="11" fill="#888">小数 0.1</text>
  <text x="350" y="138" text-anchor="middle" font-size="11" fill="#888">小数 0.5</text>
  <text x="650" y="138" text-anchor="middle" font-size="11" fill="#888">小数 1.0</text>
  <text x="380" y="170" text-anchor="middle" font-size="12" fill="#c0392b" font-style="italic">↑ 视力越好越往右挤；高视力区分辨率被压缩</text>
  <text x="50" y="220" font-size="13" fill="#333" font-weight="500">logMAR / 五分制（对数轴 = 看起来线性）</text>
  <line x1="50" y1="252" x2="650" y2="252" stroke="#444" stroke-width="1.5"/>
  <g stroke="#27ae60" stroke-width="2.2">
    <line x1="50" y1="244" x2="50" y2="270"/>
    <line x1="110" y1="244" x2="110" y2="270"/>
    <line x1="170" y1="244" x2="170" y2="270"/>
    <line x1="230" y1="244" x2="230" y2="270"/>
    <line x1="290" y1="244" x2="290" y2="270"/>
    <line x1="350" y1="244" x2="350" y2="270"/>
    <line x1="410" y1="244" x2="410" y2="270"/>
    <line x1="470" y1="244" x2="470" y2="270"/>
    <line x1="530" y1="244" x2="530" y2="270"/>
    <line x1="590" y1="244" x2="590" y2="270"/>
    <line x1="650" y1="244" x2="650" y2="270"/>
  </g>
  <text x="50" y="290" text-anchor="middle" font-size="11" fill="#888">logMAR 1.0</text>
  <text x="50" y="304" text-anchor="middle" font-size="11" fill="#888">五分 4.0</text>
  <text x="350" y="290" text-anchor="middle" font-size="11" fill="#888">logMAR 0.5</text>
  <text x="350" y="304" text-anchor="middle" font-size="11" fill="#888">五分 4.5</text>
  <text x="650" y="290" text-anchor="middle" font-size="11" fill="#888">logMAR 0.0</text>
  <text x="650" y="304" text-anchor="middle" font-size="11" fill="#888">五分 5.0</text>
  <text x="350" y="335" text-anchor="middle" font-size="12" fill="#27ae60" font-style="italic">↑ 11 个档位等距铺开；可加减、可平均、可做统计</text>
</svg>
<p class="img-caption">同一组视力档位（小数 1.00、0.79、0.63、0.50、0.40、0.32、0.25、0.20、0.16、0.13、0.10）画在两种轴上。小数轴下「好视力」的档位全都挤在右端；logMAR / 五分制下则均匀铺开——这就是为什么眼科研究只认后者。</p>

把这种非线性关系直接做成线性的，就是 logMAR：

- 每一行恰好是 0.1 logMAR；
- 每一行恰好 5 个视标（标准 ETDRS 表），认对 1 个就是 0.02 logMAR；
- 两次测量可以**直接相减**得到“进步/恶化了多少”。

而小数制和 20/20 不行。常见的错误做法是把两眼小数视力直接平均：左眼 0.1、右眼 1.0，于是报一个“平均下来差不多 0.55 的视力”——这是错的。Holladay (1997, 2004) 反复强调：视力的正确平均必须先转 logMAR 再算（左眼 logMAR=1.0、右眼 logMAR=0.0，平均 logMAR=0.5，对应小数 0.32），否则严重高估那只视力差的眼睛对整体的贡献。

## 3.4 中国五分制的来历

五分制由温州医学院（现温州医科大学）的**缪天荣**教授于 1958 年提出，比 Bailey-Lovie 的 logMAR 表早了近 20 年。它的精妙在于：

- 数字大 = 视力好（符合直觉，1.0 反而不直观）；
- 5.0 是常人正常值，“5 分”听起来像满分但实际能到 5.3；
- 本质就是 5 - logMAR，等距、可统计。

1979 年定为中国国家标准，2011 年修订为现行的 GB 11533-2011。**所以中国国标的对数视力表，和国际通用的 logMAR 表，本质是同一件事的两种写法。**——这件事说出来不少眼科医生自己也觉得“原来如此”。

# 4. 实践建议

- **看体检报告的换算锚点**：记住 5.0 = 1.0 = 20/20 这一条等式，其他档位查上面那张表。
- **1.0 不是“满分”**：很多年轻人裸眼能到 1.5（= 五分制 5.2）。验光单上的 1.5 / 2.0 不是仪器出错。
- **跟踪近视进展时一定换算**：如果医生给的是小数视力，**先在心里换成 logMAR / 五分制再比**。从 0.6 掉到 0.4，听起来掉了 0.2，其实在 logMAR 上掉了 0.18（约两行）；从 1.0 掉到 0.8，听起来也掉了 0.2，但 logMAR 上只掉了 0.1（一行）——后者远没前者严重。
- **跨制式沟通**：跟欧美医生沟通直接报 20/x 或 logMAR；跟中国医生报五分制最不容易出错。
- **测视力的环境敏感度**：照度、距离、视标种类（E 字 / C 字 / 字母 / Landolt 环）都会影响结果，**复查请尽量用同一类视标和同一距离**，否则 0.1 的差别可能只是测量噪声。

# 5. 参考来源

1. Bailey IL, Lovie JE. **New design principles for visual acuity letter charts.** *Am J Optom Physiol Opt.* 1976;53(11):740-745. ——logMAR 表的开创性论文，奠定“等比例缩小 + 每行等数量字符”的现代视力表设计（系统综述前的奠基方法学论文）。
2. Ferris FL 3rd, Kassoff A, Bresnick GH, Bailey I. **New visual acuity charts for clinical research.** *Am J Ophthalmol.* 1982;94(1):91-96. ——ETDRS 表标准化论文，目前临床研究的金标准（高质量原始研究）。
3. Holladay JT. **Visual acuity measurements.** *J Cataract Refract Surg.* 2004;30(2):287-290. ——综述，详细论证为什么必须用 logMAR 而非小数视力做统计平均（专家共识 / 综述）。
4. **GB 11533-2011《标准对数视力表》**——中国国家标准，五分制的法定依据，原始设计来自缪天荣 1958 年的工作（标准 / 指南）。
5. Kaiser PK. **Prospective evaluation of visual acuity assessment: a comparison of Snellen versus ETDRS charts in clinical practice (An AOS Thesis).** *Trans Am Ophthalmol Soc.* 2009;107:311-324. ——临床实证：ETDRS（logMAR）测量比 Snellen 更可重复、更敏感（高质量原始研究）。
