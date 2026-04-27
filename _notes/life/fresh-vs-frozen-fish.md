---
layout: post
title: "鲜鱼 vs 冷冻鱼到底差在哪？"
date: 2026-04-27
main_category: "生活攻略"
sub_category: "生活之问"
extra_categories:
  - 菜谱
permalink: "/life/fresh-vs-frozen-fish"
---

# 1. 问题

超市冷柜里的鱼分两栏：贵的“鲜鱼”和便宜的“冷冻鱼”。直觉上“鲜的好”——但为什么“刺身级三文鱼”包装上写着 “previously frozen”？为什么远洋捕捞的鱼明明几千公里运过来反而比本地“鲜”鱼便宜？冷冻鱼是不是营养流失？解冻为什么不能微波也不能室温化？

# 2. 结论先行

**很多情况下“冷冻鱼”反而比“鲜鱼”更新鲜**——这是反直觉但有充分科学依据的：

- **远洋捕捞**的鱼通常**在船上几小时内 -30 ℃ 急冻**（IQF, individual quick freezing），鲜度被锁住
- 超市标“鲜鱼”通常意味着**冷藏运输 5-7 天**，期间蛋白质降解、TVB-N 升高、口感已经下降
- **生食的寄生虫安全要求强制冷冻**（FDA：-20 ℃ × 7 天 / -35 ℃ × 15 hr）——所以美国超市的“刺身级”鱼**必然是冻过的**

冷冻鱼好不好，关键**不是“冻不冻”**，而是：

- **怎么冻**：IQF（小冰晶不破坏细胞）vs 家用冰箱慢冻（大冰晶刺穿细胞膜）
- **怎么解冻**：冷藏室 24 小时慢解冻（口感几乎不损失）vs 流水 / 微波 / 室温（细胞水分大量流失）

唯一**鲜鱼真有优势**的场景：本地新鲜上岸（沿海港口或本地渔市），24 小时内现宰现做。**绝大多数情况下，IQF 冷冻鱼应该是默认选择**。

# 3. 科学原理

## 3.1 鱼捕捞后的鲜度衰减时间表

鱼一离开水就开始**鲜度衰减**——这是一个连续的生化过程，主要靠两个指标量化：

**K 值**（核苷酸降解程度）：

肌肉中的 ATP（三磷酸腺苷）依次降解为 ADP → AMP → IMP → HxR（次黄苷）→ Hx（次黄嘌呤）。其中 IMP 是鲜味来源，HxR + Hx 越多越接近变质。

$$K = \frac{[HxR] + [Hx]}{[ATP] + [ADP] + [AMP] + [IMP] + [HxR] + [Hx]} \times 100\%$$

- K < 20% = 极鲜（刺身级）
- K = 20-40% = 鲜（清蒸 / 香煎）
- K = 40-60% = 一般（炖煮 / 煎炸）
- K > 60% = 不新鲜（不宜食用）

**TVB-N**（总挥发性盐基氮）：蛋白质降解产生的氨、二甲胺、三甲胺等碱性物质——有“腥臭味”。中国国标 GB 2733 规定海水鱼 TVB-N 限值 30 mg/100g。

**温度决定衰减速度**：

- 0 ℃ 冰水：每天 K 值上升约 5-10%
- 4 ℃ 冰箱：每天 K 值上升约 10-15%
- 室温 20 ℃：几小时就能从极鲜衰减到不能吃
- **-18 ℃ 冷冻**：生化反应几乎暂停（速率降至 1/100），K 值一周内仅小幅上升
- **-30 ℃ 急冻**：完全暂停

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 380" style="max-width:100%;height:auto;display:block;margin:1.2em auto;">
  <text x="360" y="22" text-anchor="middle" font-size="14" fill="#333" font-weight="600">三种处理方式下的鱼肉鲜度衰减（K 值）</text>
  <g transform="translate(100, 60)">
    <line x1="0" y1="0" x2="0" y2="240" stroke="#666" stroke-width="1.5"/>
    <line x1="0" y1="240" x2="560" y2="240" stroke="#666" stroke-width="1.5"/>
    <text x="-10" y="0" text-anchor="end" font-size="11" fill="#666">100%</text>
    <line x1="-3" y1="0" x2="3" y2="0" stroke="#666"/>
    <text x="-10" y="48" text-anchor="end" font-size="11" fill="#666">80%</text>
    <line x1="-3" y1="48" x2="3" y2="48" stroke="#666"/>
    <text x="-10" y="96" text-anchor="end" font-size="11" fill="#666">60%</text>
    <line x1="-3" y1="96" x2="3" y2="96" stroke="#666"/>
    <text x="-10" y="144" text-anchor="end" font-size="11" fill="#666">40%</text>
    <line x1="-3" y1="144" x2="3" y2="144" stroke="#666"/>
    <text x="-10" y="192" text-anchor="end" font-size="11" fill="#666">20%</text>
    <line x1="-3" y1="192" x2="3" y2="192" stroke="#666"/>
    <text x="-10" y="240" text-anchor="end" font-size="11" fill="#666">0%</text>
    <line x1="-3" y1="240" x2="3" y2="240" stroke="#666"/>
    <text x="0" y="258" text-anchor="middle" font-size="11" fill="#666">捕捞</text>
    <text x="80" y="258" text-anchor="middle" font-size="11" fill="#666">1 天</text>
    <line x1="80" y1="237" x2="80" y2="243" stroke="#666"/>
    <text x="240" y="258" text-anchor="middle" font-size="11" fill="#666">3 天</text>
    <line x1="240" y1="237" x2="240" y2="243" stroke="#666"/>
    <text x="400" y="258" text-anchor="middle" font-size="11" fill="#666">5 天</text>
    <line x1="400" y1="237" x2="400" y2="243" stroke="#666"/>
    <text x="560" y="258" text-anchor="middle" font-size="11" fill="#666">7 天</text>
    <line x1="560" y1="237" x2="560" y2="243" stroke="#666"/>
    <text x="-50" y="120" text-anchor="middle" font-size="11" fill="#333" font-weight="500" transform="rotate(-90, -50, 120)">K 值（越低越鲜）</text>
    <text x="280" y="278" text-anchor="middle" font-size="11" fill="#333" font-weight="500">捕捞后时间 →</text>
    <rect x="0" y="144" width="560" height="48" fill="#27ae60" opacity="0.1"/>
    <text x="555" y="166" text-anchor="end" font-size="10" fill="#27ae60" font-style="italic">极鲜（刺身级）</text>
    <rect x="0" y="96" width="560" height="48" fill="#f39c12" opacity="0.1"/>
    <text x="555" y="118" text-anchor="end" font-size="10" fill="#e67e22" font-style="italic">仍可清蒸 / 香煎</text>
    <rect x="0" y="48" width="560" height="48" fill="#e67e22" opacity="0.1"/>
    <text x="555" y="70" text-anchor="end" font-size="10" fill="#c0392b" font-style="italic">仅可炖煮 / 红烧</text>
    <rect x="0" y="0" width="560" height="48" fill="#c0392b" opacity="0.15"/>
    <text x="555" y="22" text-anchor="end" font-size="10" fill="#c0392b" font-style="italic">不宜食用</text>
    <path d="M 0 240 Q 30 215, 60 200 L 560 200" fill="none" stroke="#27ae60" stroke-width="3"/>
    <path d="M 0 240 L 80 204 L 240 156 Q 320 132, 400 108 L 560 60" fill="none" stroke="#c0392b" stroke-width="3" stroke-dasharray="6,3"/>
    <path d="M 0 240 L 80 192 Q 200 168, 320 156 L 560 144" fill="none" stroke="#e67e22" stroke-width="2.5"/>
  </g>
  <g transform="translate(120, 320)">
    <line x1="0" y1="0" x2="30" y2="0" stroke="#27ae60" stroke-width="3"/>
    <text x="40" y="4" font-size="11" fill="#333">远洋 IQF（船上 -30 ℃ 急冻）</text>
    <line x1="240" y1="0" x2="270" y2="0" stroke="#e67e22" stroke-width="2.5"/>
    <text x="280" y="4" font-size="11" fill="#333">家用冰箱 -18 ℃ 慢冻</text>
    <line x1="120" y1="20" x2="150" y2="20" stroke="#c0392b" stroke-width="3" stroke-dasharray="6,3"/>
    <text x="160" y="24" font-size="11" fill="#333">冷藏 0-4 ℃ 运输（「鲜鱼」标签）</text>
  </g>
</svg>
<p class="img-caption">远洋 IQF 的鱼在捕捞数小时内被冻到 -30 ℃ 以下，K 值停在极低水平；超市冷柜里标「鲜鱼」的，多半是冷藏运输 5-7 天的产品，K 值已显著上升。家用冰箱慢冻介于两者之间——好于持续冷藏，但远不及 IQF。</p>

## 3.2 IQF 急冻的物理：冰晶大小决定一切

冷冻鱼好坏的关键是**冰晶大小**。

水在结冰时，速度快的话产生**很多小冰晶**；速度慢的话产生**少而大的冰晶**。临界点在 -1 ℃ 到 -5 ℃ 之间——这就是所谓的“最大冰晶生成带”。

- **-30 ℃ IQF**：鱼通过这个温度区间只需要 **30 分钟以内**，产生的冰晶 < 50 μm，**比细胞还小**——不破坏细胞结构
- **-18 ℃ 家用慢冻**：鱼通过这个区间需要 **8-12 小时**，产生的冰晶 > 200 μm，**刺穿细胞膜**——解冻后细胞内汁水（含蛋白质、风味物质）大量流出

这就是为什么 IQF 解冻的鱼**口感几乎和新鲜的一样**，而家用慢冻的鱼解冻后会**显著出汁、发柴**。

> 工业 IQF 设备用的是 -40 ℃ 强风冷冻或液氮直接冷却，单条 fillet 几分钟内冻透。家用即使把冷冻室调到 -25 ℃ 最低档，也无法达到 IQF 的效果——温度梯度不够、风速不够、鱼厚度不够小。

## 3.3 冷冻对营养的影响：几乎没有

很多人担心“冷冻 = 营养流失”——这其实**基本不对**：

- **蛋白质**：变性极小，营养价值 99% 保留
- **omega-3 / EPA / DHA**：在 -18 ℃ 以下 6 个月内几乎不降解。氧化（rancidity）才是问题，但用真空包装可以避免
- **维生素 D / B12**：脂溶性 / 结合态，几乎不损失
- **矿物质（钙、磷、硒）**：完全不变

**真正的损失在口感和持水性**：

- 慢冻产生的大冰晶刺穿细胞 → 解冻后出汁 → 鱼肉变得略松散
- 冷冻不当（温度波动）会反复融化-冷冻 → 加重冰晶损伤
- 长时间冷冻会**轻微氧化脂肪**（即使在 -18 ℃ 下）→ 鱼肉颜色变暗、产生轻微哈喇味

**结论**：营养上 IQF 和鲜鱼几乎平手，口感上 IQF 略输于刚上岸的鲜鱼，但远好于“冷藏 5-7 天的鲜鱼”。

## 3.4 解冻：为什么慢解冻好

解冻和冷冻的物理是镜像的——冷冻速度决定**形成的冰晶大小**，解冻速度决定**冰晶融化对细胞的二次破坏**。

慢解冻（冷藏室 0-4 ℃，约 24 小时）：

- 内外温差小（< 5 ℃）→ 冰晶均匀逐步融化
- 化开的水有时间被细胞重新吸收
- 细胞结构损伤最小

快速解冻（流水 / 微波 / 室温）：

- 内外温差大（> 20 ℃）→ 表层化得很快，内层还冻着 → **二次冰晶**形成 + 蛋白质变性
- 化开的水来不及被细胞吸收 → 流出来形成“血水”
- 微波解冻最差：局部加热到 60 ℃+ 让蛋白质开始变性，鱼肉变成半生不熟的橡皮态

# 4. 实践建议

## 4.1 美国超市标签解读

美超鱼类区域常见标签和它们的真实含义：

| 标签 | 真实含义 |
|---|---|
| **Fresh** | 从未冻过，但通常意味着冷藏运输 5-7 天。**不一定比冷冻新鲜** |
| **Fresh, never frozen** | 真的没冻过。本地或近海捕捞 |
| **Previously frozen** | 之前冻过，现在解冻销售。**通常意味着 IQF 远洋鱼**——其实质量很好 |
| **Flash frozen** / **Quick frozen** | 急冻（接近 IQF 但不一定是工业级）。质量较好 |
| **IQF**（individual quick freezing） | 工业急冻。**质量最好的冷冻品** |
| **Sushi grade / Sashimi grade** | 满足 FDA 寄生虫冷冻要求的鱼。**几乎一定是 previously frozen 或当下冷冻状态** |
| **Wild caught** | 野生捕捞。omega-3 通常更高，但具体看品种 |
| **Farm raised** | 养殖。三文鱼大多是养殖；可持续性看认证 |

**关键判断**：标签上写 “previously frozen” 不是缺点——很多时候反而是品质保证。

## 4.2 哪些鱼买冷冻好

- **远洋鱼**（三文鱼、金枪鱼、鳕鱼、比目鱼）：买 IQF 几乎一定比“鲜”好——前者鲜度被锁住，后者已运输 5-7 天
- **虾蟹贝类**：基本所有都是 IQF 上市，“鲜虾”通常意味着解冻后摆放——直接买冷冻自己解冻反而更可控
- **远洋小型鱼**（沙丁鱼、凤尾鱼）：罐头是另一种保存方式，比新鲜更可靠
- **进口异国品种**（智利海鲈、英吉利海鳕）：本地“鲜”的就是空运冷藏 + 摆放，远不如 IQF

## 4.3 哪些鱼鲜的更好

- **本地浅海白肉鱼**（沿海地区当天上岸的鲈鱼、鲷鱼、鲽鱼）
- **本地养殖虹鳟、罗非**：从塘里现捞、24 小时内到超市
- **活鱼现宰**（粤式酒楼、亚超活鱼缸）—— 极致鲜，但要会处理
- **渔市直接买**（沿海地区，如 Seattle Pike Place、Boston Quincy Market、湾区 Half Moon Bay）

**反过来说**：在内陆城市（Phoenix、Denver、Pittsburgh、Pennsylvania State College），所谓“鲜鱼”几乎都是空运冷藏来的——这种情况下 IQF 几乎一定是更好的选择。

## 4.4 解冻方法对比

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 380" style="max-width:100%;height:auto;display:block;margin:1.2em auto;">
  <text x="360" y="22" text-anchor="middle" font-size="14" fill="#333" font-weight="600">四种解冻方法对比</text>
  <g transform="translate(60, 50)">
    <rect x="0" y="0" width="600" height="32" fill="#fafafa" stroke="#666" stroke-width="1.2"/>
    <text x="80" y="20" text-anchor="middle" font-size="12" fill="#333" font-weight="600">方法</text>
    <text x="220" y="20" text-anchor="middle" font-size="12" fill="#333" font-weight="600">速度</text>
    <text x="350" y="20" text-anchor="middle" font-size="12" fill="#333" font-weight="600">口感保持</text>
    <text x="470" y="20" text-anchor="middle" font-size="12" fill="#333" font-weight="600">食品安全</text>
    <text x="560" y="20" text-anchor="middle" font-size="12" fill="#333" font-weight="600">推荐</text>
    <line x1="160" y1="0" x2="160" y2="280" stroke="#ccc"/>
    <line x1="280" y1="0" x2="280" y2="280" stroke="#ccc"/>
    <line x1="420" y1="0" x2="420" y2="280" stroke="#ccc"/>
    <line x1="520" y1="0" x2="520" y2="280" stroke="#ccc"/>
    <rect x="0" y="32" width="160" height="60" fill="#e8f5e9" stroke="#666" stroke-width="1"/>
    <text x="80" y="56" text-anchor="middle" font-size="12" fill="#333" font-weight="600">冷藏室慢解冻</text>
    <text x="80" y="74" text-anchor="middle" font-size="11" fill="#666">放冰箱冷藏室</text>
    <rect x="160" y="32" width="120" height="60" fill="#fff8e1"/>
    <text x="220" y="56" text-anchor="middle" font-size="12" fill="#333" font-weight="600">慢</text>
    <text x="220" y="74" text-anchor="middle" font-size="11" fill="#666">12-24 小时</text>
    <rect x="280" y="32" width="140" height="60" fill="#c8e6c9"/>
    <text x="350" y="58" text-anchor="middle" font-size="14" fill="#27ae60" font-weight="700">★★★★★</text>
    <text x="350" y="78" text-anchor="middle" font-size="10" fill="#666">几乎无损失</text>
    <rect x="420" y="32" width="100" height="60" fill="#c8e6c9"/>
    <text x="470" y="58" text-anchor="middle" font-size="16" fill="#27ae60" font-weight="700">✓ 安全</text>
    <text x="470" y="78" text-anchor="middle" font-size="10" fill="#666">全程 &lt; 4 ℃</text>
    <rect x="520" y="32" width="80" height="60" fill="#c8e6c9"/>
    <text x="560" y="58" text-anchor="middle" font-size="14" fill="#27ae60" font-weight="700">★★★★★</text>
    <text x="560" y="76" text-anchor="middle" font-size="10" fill="#666">默认选择</text>
    <rect x="0" y="92" width="160" height="60" fill="#fff3e0" stroke="#666" stroke-width="1"/>
    <text x="80" y="116" text-anchor="middle" font-size="12" fill="#333" font-weight="600">流水包密封袋</text>
    <text x="80" y="134" text-anchor="middle" font-size="11" fill="#666">凉水冲 / 浸泡</text>
    <rect x="160" y="92" width="120" height="60" fill="#fff8e1"/>
    <text x="220" y="116" text-anchor="middle" font-size="12" fill="#333" font-weight="600">中</text>
    <text x="220" y="134" text-anchor="middle" font-size="11" fill="#666">1-2 小时</text>
    <rect x="280" y="92" width="140" height="60" fill="#fff8e1"/>
    <text x="350" y="118" text-anchor="middle" font-size="14" fill="#e67e22" font-weight="700">★★★★</text>
    <text x="350" y="138" text-anchor="middle" font-size="10" fill="#666">小损失</text>
    <rect x="420" y="92" width="100" height="60" fill="#c8e6c9"/>
    <text x="470" y="118" text-anchor="middle" font-size="16" fill="#27ae60" font-weight="700">✓ 安全</text>
    <text x="470" y="138" text-anchor="middle" font-size="10" fill="#666">水温 &lt; 21 ℃</text>
    <rect x="520" y="92" width="80" height="60" fill="#fff8e1"/>
    <text x="560" y="118" text-anchor="middle" font-size="14" fill="#e67e22" font-weight="700">★★★★</text>
    <text x="560" y="136" text-anchor="middle" font-size="10" fill="#666">应急用</text>
    <rect x="0" y="152" width="160" height="60" fill="#ffebee" stroke="#666" stroke-width="1"/>
    <text x="80" y="176" text-anchor="middle" font-size="12" fill="#333" font-weight="600">微波解冻</text>
    <text x="80" y="194" text-anchor="middle" font-size="11" fill="#666">用解冻档</text>
    <rect x="160" y="152" width="120" height="60" fill="#c8e6c9"/>
    <text x="220" y="176" text-anchor="middle" font-size="12" fill="#27ae60" font-weight="700">极快</text>
    <text x="220" y="194" text-anchor="middle" font-size="11" fill="#666">5-10 分钟</text>
    <rect x="280" y="152" width="140" height="60" fill="#ffcdd2"/>
    <text x="350" y="178" text-anchor="middle" font-size="14" fill="#c0392b" font-weight="700">★★</text>
    <text x="350" y="198" text-anchor="middle" font-size="10" fill="#666">明显劣化</text>
    <rect x="420" y="152" width="100" height="60" fill="#fff8e1"/>
    <text x="470" y="178" text-anchor="middle" font-size="14" fill="#e67e22" font-weight="700">⚠ 边缘</text>
    <text x="470" y="198" text-anchor="middle" font-size="10" fill="#666">局部&gt;60 ℃</text>
    <rect x="520" y="152" width="80" height="60" fill="#ffcdd2"/>
    <text x="560" y="178" text-anchor="middle" font-size="14" fill="#c0392b" font-weight="700">★</text>
    <text x="560" y="196" text-anchor="middle" font-size="10" fill="#666">不推荐</text>
    <rect x="0" y="212" width="160" height="60" fill="#ffebee" stroke="#666" stroke-width="1"/>
    <text x="80" y="236" text-anchor="middle" font-size="12" fill="#333" font-weight="600">室温化冻</text>
    <text x="80" y="254" text-anchor="middle" font-size="11" fill="#666">放厨房台面</text>
    <rect x="160" y="212" width="120" height="60" fill="#fff8e1"/>
    <text x="220" y="236" text-anchor="middle" font-size="12" fill="#333" font-weight="600">中</text>
    <text x="220" y="254" text-anchor="middle" font-size="11" fill="#666">1-3 小时</text>
    <rect x="280" y="212" width="140" height="60" fill="#fff8e1"/>
    <text x="350" y="238" text-anchor="middle" font-size="14" fill="#e67e22" font-weight="700">★★★</text>
    <text x="350" y="258" text-anchor="middle" font-size="10" fill="#666">中等损失</text>
    <rect x="420" y="212" width="100" height="60" fill="#ffcdd2"/>
    <text x="470" y="238" text-anchor="middle" font-size="14" fill="#c0392b" font-weight="700">✗ 不安全</text>
    <text x="470" y="258" text-anchor="middle" font-size="10" fill="#666">细菌增殖区</text>
    <rect x="520" y="212" width="80" height="60" fill="#ffcdd2"/>
    <text x="560" y="238" text-anchor="middle" font-size="14" fill="#c0392b" font-weight="700">✗</text>
    <text x="560" y="256" text-anchor="middle" font-size="10" fill="#666">绝对避免</text>
  </g>
  <text x="360" y="356" text-anchor="middle" font-size="11" fill="#888">"细菌增殖区" = 4-60 ℃，鱼肉表面达到这个温度后，沙门氏菌、李斯特菌等会快速繁殖（每 20 分钟翻倍）。</text>
</svg>
<p class="img-caption">默认就用冷藏室 24 小时慢解冻——口感几乎不损失。临时忘了拿出来的应急方案是流水包密封袋（必须包好密封袋，不能直接放水里）。微波和室温都不推荐。</p>

具体操作：

**冷藏室慢解冻（默认）**：

1. 把冷冻鱼从冷冻室移到冷藏室（0-4 ℃）
2. 放在盘子上（防止融出的水弄湿冰箱）
3. 等 12-24 小时，视厚度
4. 取出时鱼仍冰凉但已无冰碴 → 立即烹饪

**流水包密封袋（应急）**：

1. 鱼装进**密封塑料袋**（zip-lock 或保鲜膜紧裹），一定要密封防进水
2. 浸入**凉水**（不要超过 21 ℃ / 70 ℉）
3. 每 30 分钟换一次水，保持低温
4. 一般 1-2 小时化透
5. **不要用流动温水或热水**——直接进入细菌增殖区

## 4.5 寄生虫安全：生食必须冷冻

打算生食（刺身、寿司、carpaccio、ceviche）的鱼**必须先冷冻处理**——这是 FDA 明文规定的安全要求，目的是杀灭寄生虫（**异尖线虫 Anisakis、阔节裂头绦虫 Diphyllobothrium、华支睾吸虫 Clonorchis** 等）。

FDA 标准（21 CFR § 123.3）：

- **-20 ℃（-4 ℉）冷冻 ≥ 7 天**（适用于普通商用冷冻设备），或
- **-35 ℃（-31 ℉）冷冻 ≥ 15 小时**（急冻设备），或
- **-35 ℃ 冷冻至中心温度后保持 -20 ℃ ≥ 24 小时**

**所以美国超市标“sushi grade / sashimi grade”的鱼，几乎一定是 previously frozen**——这不是质量问题，反而是安全保证。

**例外**：

- **金枪鱼**（特别是黑鲔、长鳍）：FDA 豁免——金枪鱼在远洋大型温血鱼，体内基本没有人类寄生虫风险，可以生食不冷冻
- **本地野生淡水鱼绝对不要生吃**：含华支睾吸虫、棘口吸虫等多种寄生虫，加上汞和重金属富集
- **养殖三文鱼**：严格饲料管控的（如挪威、智利、加拿大主要养殖场）寄生虫风险极低，但仍建议遵守冷冻规则
- **野生太平洋三文鱼**：异尖线虫常见——强烈建议冷冻 ≥ 7 天再生食

# 5. 参考来源

1. **U.S. FDA.** *Fish and Fishery Products Hazards and Controls Guidance.* 4th ed (2022). Chapter 5: Parasites; Chapter 16: Listeria. ——刺身 / 生鱼安全的官方标准。
2. **Hultmann L, Rustad T.** **Iced storage of Atlantic salmon (Salmo salar) — effects on endogenous enzyme activity, protein and texture properties.** *Food Chemistry.* 2004;87(1):31-41. ——三文鱼冷藏过程蛋白质质构变化（高质量原始研究）。
3. **Tolstorebrov I, Eikevik TM, Bantle M.** **Effect of low and ultra-low temperature applications during freezing and frozen storage on quality parameters for fish.** *International Journal of Refrigeration.* 2016;63:37-47. ——IQF / ultra-low temperature 对鱼肉品质影响的综述。
4. **Erdoğdu F, Tutar M, Sarghini A, Skipnes D.** **Effects of advanced freezing techniques on the quality of fish.** *Food Engineering Reviews.* 2014;6(3):127-145. ——冷冻技术对鱼品质影响的工程综述。
5. **GB 2733-2015《食品安全国家标准 鲜、冻动物性水产品》**——中国国标对鲜冻水产品 TVB-N 等指标的规定（标准 / 监管文件）。
