---
layout: post
title: "美国手机话费完全指南：从选运营商到保留中国号码"
date: 2026-04-28
main_category: "生活攻略"
sub_category: "留学攻略"
permalink: "/life/us-phone-plans"
---

# 1. 这篇文章给谁看

写给三类人：

- **刚来美国一两个月**，还在用国内号漫游 / 不知道挑哪家运营商，被 mall 里的 Verizon 销售反复推销 $80+ 套餐
- **已经有美国号但每月被坑 $80+** ——账单上写满 surcharges、taxes、device protection、autopay discount 的人
- **中美两边跑** ——既不想丢国内号（要收银行 / 12306 / 政务验证码），又要在美国用一个本地号

我自己刚来时被 Verizon 实体店销售一通推销，差点签了 $90/月的“无限套餐”，最后冷静下来选了 $20/月的 MVNO——**信号一模一样，每月省 $70**。这篇文章把这套逻辑摊开讲清楚。

> ⚠️ 各运营商套餐价格 / 福利会**频繁变动**，文中价格以**运营商官网**最新公告为准。

# 2. 结论先行

**单身留学生最优路径**：选 **Mint Mobile / Visible / US Mobile** 三家之一，月费 **$15-$30**——信号、覆盖和三大运营商一模一样（它们租用主网络），但价格只有 1/3。

**家庭多人**：4 人及以上一起办 T-Mobile / Verizon 家庭计划，**人均反而比 MVNO 便宜**。

**最大三个坑**：
1. 实体店销售对 postpaid 有提成——他们会反复劝你选 $80+ 月费
2. 广告 $25/月的 postpaid 套餐，账单出来 $32+（10-30% 隐形税费）—— **Mint / Visible 标的是“含税价”**
3. “免费 iPhone”是 36 个月话费分期，提前解约要赔几百美刀

**中国号码**：保留 + 接收短信即可（每月 8-10 元保号套餐），**不要在美国漫游打电话**。eSIM iPhone 让你能同时拥有美国号 + 中国号。

# 3. 美国手机生态：主网络 + MVNO 双轨

> 这是理解美国手机价格差异的**核心一张图**：美国其实只有 **3 个真正的“网络”**——基站、频谱、信号塔都是它们的。其他几十家“运营商”都是租用这三家网络的“虚拟运营商”（MVNO，Mobile Virtual Network Operator）。**信号完全一样，价格便宜 50-70%**。

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 360" style="max-width:100%;height:auto;display:block;margin:1.2em auto;">
  <text x="380" y="22" text-anchor="middle" font-size="14" font-weight="600" fill="#333">美国手机生态：3 个主网络 + 一群 MVNO</text>

  <!-- 三大网络 -->
  <g transform="translate(40, 50)">
    <rect width="200" height="80" rx="10" fill="#fdf0f0" stroke="#c0392b" stroke-width="2"/>
    <text x="100" y="30" text-anchor="middle" font-size="13" fill="#c0392b" font-weight="700">Verizon 网络</text>
    <text x="100" y="50" text-anchor="middle" font-size="10" fill="#666">基站 + 频谱所有者</text>
    <text x="100" y="65" text-anchor="middle" font-size="10" fill="#666">全美覆盖最广</text>
  </g>

  <g transform="translate(280, 50)">
    <rect width="200" height="80" rx="10" fill="#f0fff4" stroke="#27ae60" stroke-width="2"/>
    <text x="100" y="30" text-anchor="middle" font-size="13" fill="#27ae60" font-weight="700">T-Mobile 网络</text>
    <text x="100" y="50" text-anchor="middle" font-size="10" fill="#666">5G 速度最快</text>
    <text x="100" y="65" text-anchor="middle" font-size="10" fill="#666">国际漫游最友好</text>
  </g>

  <g transform="translate(520, 50)">
    <rect width="200" height="80" rx="10" fill="#f0f8ff" stroke="#2980b9" stroke-width="2"/>
    <text x="100" y="30" text-anchor="middle" font-size="13" fill="#2980b9" font-weight="700">AT&amp;T 网络</text>
    <text x="100" y="50" text-anchor="middle" font-size="10" fill="#666">乡村覆盖好</text>
    <text x="100" y="65" text-anchor="middle" font-size="10" fill="#666">中规中矩</text>
  </g>

  <!-- 连接线 -->
  <line x1="140" y1="130" x2="140" y2="160" stroke="#888" stroke-width="1.5"/>
  <line x1="380" y1="130" x2="380" y2="160" stroke="#888" stroke-width="1.5"/>
  <line x1="620" y1="130" x2="620" y2="160" stroke="#888" stroke-width="1.5"/>

  <!-- 自营 + MVNO -->
  <g transform="translate(40, 165)">
    <text x="100" y="14" text-anchor="middle" font-size="11" fill="#888" font-weight="600">自营 + 主要 MVNO</text>
    <rect x="0" y="22" width="200" height="135" rx="8" fill="#fff" stroke="#c0392b" stroke-width="1" stroke-dasharray="4,2"/>
    <text x="14" y="42" font-size="11" fill="#c0392b" font-weight="600">Verizon</text>
    <text x="60" y="42" font-size="9" fill="#888">$80+ / 主品牌</text>
    <text x="14" y="62" font-size="11" fill="#444" font-weight="600">Visible</text>
    <text x="60" y="62" font-size="9" fill="#888">$25 / Verizon 子品牌</text>
    <text x="14" y="82" font-size="11" fill="#444" font-weight="600">Total Wireless</text>
    <text x="100" y="82" font-size="9" fill="#888">$25-$50</text>
    <text x="14" y="102" font-size="11" fill="#444" font-weight="600">Straight Talk</text>
    <text x="100" y="102" font-size="9" fill="#888">$35-$55</text>
    <text x="14" y="122" font-size="11" fill="#444" font-weight="600">Spectrum Mobile</text>
    <text x="110" y="122" font-size="9" fill="#888">$30 / Charter 旗下</text>
    <text x="14" y="146" font-size="9" fill="#888" font-style="italic">(Visible 是同一家 Verizon</text>
    <text x="14" y="156" font-size="9" fill="#888" font-style="italic">的便宜版子品牌)</text>
  </g>

  <g transform="translate(280, 165)">
    <text x="100" y="14" text-anchor="middle" font-size="11" fill="#888" font-weight="600">自营 + 主要 MVNO</text>
    <rect x="0" y="22" width="200" height="135" rx="8" fill="#fff" stroke="#27ae60" stroke-width="1" stroke-dasharray="4,2"/>
    <text x="14" y="42" font-size="11" fill="#27ae60" font-weight="600">T-Mobile</text>
    <text x="60" y="42" font-size="9" fill="#888">$70+ / 主品牌</text>
    <text x="14" y="62" font-size="11" fill="#444" font-weight="600">Mint Mobile</text>
    <text x="100" y="62" font-size="9" fill="#888">$15-$30</text>
    <text x="14" y="82" font-size="11" fill="#444" font-weight="600">Metro by T-Mobile</text>
    <text x="120" y="82" font-size="9" fill="#888">$30+</text>
    <text x="14" y="102" font-size="11" fill="#444" font-weight="600">Google Fi</text>
    <text x="80" y="102" font-size="9" fill="#888">$20-$65</text>
    <text x="14" y="122" font-size="11" fill="#444" font-weight="600">Mint / Ultra Mobile</text>
    <text x="120" y="122" font-size="9" fill="#888">$15+</text>
    <text x="14" y="146" font-size="9" fill="#888" font-style="italic">(Mint 已被 T-Mobile</text>
    <text x="14" y="156" font-size="9" fill="#888" font-style="italic">收购，独立运营)</text>
  </g>

  <g transform="translate(520, 165)">
    <text x="100" y="14" text-anchor="middle" font-size="11" fill="#888" font-weight="600">自营 + 主要 MVNO</text>
    <rect x="0" y="22" width="200" height="135" rx="8" fill="#fff" stroke="#2980b9" stroke-width="1" stroke-dasharray="4,2"/>
    <text x="14" y="42" font-size="11" fill="#2980b9" font-weight="600">AT&amp;T</text>
    <text x="50" y="42" font-size="9" fill="#888">$75+ / 主品牌</text>
    <text x="14" y="62" font-size="11" fill="#444" font-weight="600">Cricket</text>
    <text x="65" y="62" font-size="9" fill="#888">$30-$60 / AT&amp;T 子品牌</text>
    <text x="14" y="82" font-size="11" fill="#444" font-weight="600">Consumer Cellular</text>
    <text x="120" y="82" font-size="9" fill="#888">$20+ / 老年人友好</text>
    <text x="14" y="102" font-size="11" fill="#444" font-weight="600">Boost Mobile</text>
    <text x="100" y="102" font-size="9" fill="#888">$25+ / 多网</text>
    <text x="14" y="122" font-size="11" fill="#444" font-weight="600">H2O Wireless</text>
    <text x="100" y="122" font-size="9" fill="#888">$20+ / 国际通话</text>
    <text x="14" y="146" font-size="9" fill="#888" font-style="italic">(Cricket 是同一家 AT&amp;T</text>
    <text x="14" y="156" font-size="9" fill="#888" font-style="italic">的便宜版子品牌)</text>
  </g>

  <!-- US Mobile 横跨 -->
  <g transform="translate(40, 320)">
    <rect width="680" height="30" rx="8" fill="#fff8f0" stroke="#f39c12" stroke-width="2"/>
    <text x="340" y="20" text-anchor="middle" font-size="12" fill="#f39c12" font-weight="700">US Mobile（可在三家网络间切换：Warp = Verizon / GSM = T-Mobile / Dark Star = AT&amp;T）</text>
  </g>
</svg>
<p class="img-caption">三大网络是基础设施所有者，下面挂着各自的"主品牌"和一群 MVNO。MVNO 信号 = 主网络信号，因为它们租的就是同一个网络。**Verizon = Visible，T-Mobile = Mint，AT&T = Cricket** 是最常见的"同信号，半价"配对。</p>

**两个关键结论从这张图里读出来：**

1. **想用 Verizon 网络但不付 $80**：选 **Visible（$25）** 或 **US Mobile Warp（$25-$35）**——同一根信号
2. **想用 T-Mobile 网络但不付 $70**：选 **Mint Mobile（$15-$30 年付）** 或 **Google Fi（$20）**——同一根信号

# 4. 主流运营商对比（一张大表）

下面这张表只列**留学生 / 工作族最值得考虑**的 8 家，按月费从低到高排（基础套餐价）：

| 运营商 | 类型 | 网络 | 起步月费 | 流量 | 关键特点 |
|---|---|---|---|---|---|
| **US Mobile Pooled** | MVNO | 三网可切 | **$10** | 2 GB | 灵活度最高，按需付费 |
| **Mint Mobile** | MVNO | T-Mobile | **$15**（年付）| 5 GB | 留学生最爱，年付预付 |
| **Mint Mobile Unlimited** | MVNO | T-Mobile | **$30**（年付）| 无限* | * 35 GB 后限速 |
| **Google Fi Simply Unlimited** | MVNO | T-Mobile | **$20**（多线下降）| 35 GB | 国际漫游 / 多设备友好 |
| **Visible Basic** | MVNO（Verizon 子品牌） | Verizon | **$25** | 无限* | * 25 GB 后可能限速 |
| **US Mobile Warp Unlimited** | MVNO | Verizon | **$25-35** | 无限 | Verizon 信号最便宜方案 |
| **Visible+ Pro** | MVNO（Verizon 子品牌） | Verizon | **$45** | 无限 + 优先 | 含 Premium 数据 + 国际通话 |
| **T-Mobile Go5G** | 主网 | T-Mobile | **$70** | 无限 | Netflix / Apple TV+ 含 |
| **Verizon Unlimited Plus** | 主网 | Verizon | **$80** | 无限 + 优先 | Disney+ / Hulu / ESPN+ 含 |
| **AT&T Unlimited Premium** | 主网 | AT&T | **$85** | 无限 + 优先 | Max / Cricket 大型机会 |

> **价格统一注释**：以上都是**单线**（1 个号码）价格，多人 / 多线办通常每条线降 $5-$15。**MVNO 标价通常含税；主网标价 + 10-25% taxes & fees 才是实际账单。**

**重点解读：**

- **$15-$30 区间**：MVNO 主战场，覆盖 95% 留学生需求
- **$30-$50 区间**：MVNO 高端版（Visible+、US Mobile premium 等），加了“优先级数据” + 国际功能
- **$70+ 区间**：主网 + 流媒体 bundle——**只有当你真的会看 Disney+ / Netflix 才划算**

# 5. 怎么选？按身份 + 使用场景

下面这个决策树覆盖 90% 的留学生 / 工作族场景：

| 场景 | 推荐方案 | 月费 |
|---|---|---|
| **单身留学生 + 校园 WiFi 多 + 流量需求一般（< 5 GB/月）** | **Mint Mobile $15** 年付（5GB）| $15 |
| **PhD / 工作族 + 校外多 + 想要无限流量** | **Visible $25** 或 **Mint Unlimited $30** | $25-$30 |
| **重度用户 + 视频流 + 直播 + 共享热点** | **Visible+ $45** 或 **US Mobile Warp Unlimited Premium $35** | $35-$45 |
| **多设备 / 国际出差 / 商务党** | **Google Fi**（一个套餐多设备 + 200+ 国家漫游同价）| $20-$50 |
| **家庭 4 人及以上一起办** | **T-Mobile / Verizon 家庭计划**（人均 $25-$35）| 总 $100-$140 |
| **实体店党 / 不想线上自助** | **Cricket（AT&T 旗下）/ Metro（T-Mobile 旗下）** | $30-$50 |
| **来美国 < 1 个月 / 试用期** | **prepaid eSIM**（Mint 7 天免费试用 / US Mobile 月付）| < $15 |
| **长期保留中国号 + 美国号双卡党** | iPhone 上 eSIM 美国号 + 物理 SIM / eSIM 中国号 | 详见 §6 |

**信号覆盖差异（实务）**：

- **大学城 / 大城市**：三网都好，差距 < 5%
- **乡村 / 高速公路 / 国家公园**：**Verizon > AT&T > T-Mobile**——所以喜欢 road trip 的人选 Verizon 系（Visible / US Mobile Warp）
- **校园里室内**：**T-Mobile 5G 速度最快**，但深室内信号偶尔弱
- **搬家 / 换城市前**：先查 [FCC 信号地图](https://www.fcc.gov/BroadbandData/MobileMaps/mobile-map) 或问邻居

# 6. 中国号码怎么办？

这是中国背景留学生第一年最纠结的问题之一。三种方案：

## 6.1 方案 A：完全放弃（不推荐）

不是不可行，但**国内很多服务（银行、12306、医保、政务、微信好友找回密码）只能用国内手机号收验证码**。完全注销国内号意味着**回国办事会到处碰墙**。

## 6.2 方案 B：保号 + 用国内备用机收验证码（推荐）

**核心思路**：把国内号转到 **8-10 元/月的“保号套餐”**，插在一个国内备用机里，每月偶尔开机收一下验证码。

**具体步骤：**

1. **办保号套餐**（出国前 / 临回国时办最方便）：
   - **中国移动**：8 元/月「8 元保号套餐」（30 分钟通话 + 100 MB 流量）
   - **中国联通**：8 元/月「沃 8 套餐」类似
   - **中国电信**：10 元/月「飞 Young」保号
2. **备用机插着**：把这张 SIM 插在国内的备用机（旧 iPhone / 红米都行），交给父母 / 信任的人保管
3. **每月开机一次**：让信号有“活动”，避免长时间无网络被销号
4. **重要服务收码时**：让家人 / 朋友把短信转发给你（**微信图片转发即可**）
5. **不要在美国开漫游打电话**：每分钟 ¥3-5，几通电话就破百

## 6.3 方案 C：双卡 / eSIM 同时持有

**iPhone eSIM 时代的最优解**：

- iPhone XS 之后所有美版 iPhone 支持双 SIM（1 物理 + 1 eSIM 或 2 eSIM）
- **iPhone 14 及之后的美版只支持 eSIM**（无 SIM 卡槽）—— 但仍可装多个 eSIM
- 配置：**eSIM 1 = 美国号（Mint / Visible / US Mobile）+ eSIM 2 / 物理 SIM = 中国号（保号套餐）**
- 在中国号 eSIM / SIM 上**关闭“漫游”**——只接收短信，不打电话也不上网，**0 漫游费**
- 收到银行 / 12306 短信即可看到内容
- **缺点**：中国号码必须**先在国内办好 eSIM**才能带过来；如果办的是物理 SIM 卡，要带卡过来插着

**实战配置**：

```
iPhone 设置：
  ├─ 主线：美国号（接电话 / 用流量 / iMessage）
  ├─ 副线：中国号（仅接收短信，关闭蜂窝数据 + 关闭漫游）
  └─ 来电显示 / 短信 / 通讯录可以分开管理
```

## 6.4 WiFi calling（国内号在美国接电话）

**WiFi calling**（Wi-Fi 通话）是个救命功能：当你手机连了 WiFi，**可以直接用国内号在美国打 / 接电话**——网络走 WiFi，**只算国内通话费**（不算漫游）。

但前提：

- 你的中国号运营商支持 WiFi calling（中国移动 / 联通的国际版套餐部分支持）
- 你的手机支持（iPhone 全系支持，Android 看品牌）
- 这个功能在国内被运营商限制——**不是所有套餐都开**，建议出国前打客服开通

# 7. eSIM vs 实体 SIM

| 维度 | 实体 SIM | eSIM |
|---|---|---|
| 安装速度 | 快递寄卡 1-3 天 | **5 分钟内激活** |
| 换手机 | 取出插新机 | **重新申请激活**（部分运营商收 $0-$25 费） |
| 多 SIM 同机 | iPhone 最多 1 物理 + 1 eSIM | **iPhone 可装 8 个 eSIM**，活跃 2 个 |
| 出国旅行 | 换卡麻烦 | **直接装目的地国家 eSIM**，不撤美国号 |
| 丢卡 / 损坏 | 需要补卡 | **不会丢** |
| 美版 iPhone 14+ | 不支持 | **唯一选项** |

**主流 MVNO 都支持 eSIM**：Mint / Visible / Google Fi / US Mobile 都可以全 eSIM。**强烈推荐 eSIM**——除非你买二手手机不支持。

# 8. 几个隐藏坑

## 8.1 “免费 iPhone”分期套路

实体店销售常说：“Sign up for our $80/mo plan and get a free iPhone 16!”

实际上：

- iPhone 16 售价 $799 → 分摊到 36 个月 = **$22/mo 自动加到账单**
- 你看到的“$80/mo”实际上是 **$80 + $22 = $102/mo**
- 提前解约（换 carrier）= 必须**一次性付清剩余手机分期**
- 36 个月 = **3 年绑定**

**怎么避坑**：

- 想要新 iPhone 就**直接 Apple Store 全款 / 信用卡分期**买（24 期 0 利率）
- 然后用 **unlocked 手机** 配 MVNO 套餐——**完全自由切换运营商**

## 8.2 Taxes & Fees（隐形税费）

主网 postpaid 套餐广告 $80/mo，账单出来 $95+。多出来的是：

- **Federal Universal Service Fund**：~3-7%
- **State Sales Tax**：3-9%（看州）
- **911 Surcharge**：$0.50-$1.00/线
- **Regulatory Recovery Fee**：$1-$3
- **Administrative Fee**：$1-$3

**总计 10-25% 隐形费**。所以广告 $80 → 账单 $95-$100。

**MVNO（Mint / Visible / US Mobile）通常标含税价**——所以“$25 = $25"，没有隐形费。这是它们便宜的另一层原因。

## 8.3 自动续费陷阱

- **Mint 年付套餐**：到期自动续费——记得在到期前 1 周决定要不要继续
- **Postpaid 自动 autopay**：很多套餐”autopay $5 折扣“诱导你绑卡，但 autopay 中的卡过期后会**自动改用账户余额扣**——你以为没绑实际仍在扣

## 8.4 信号覆盖差异

不同运营商在不同地区差距大。**前做选择前先查**：

- [FCC Mobile Coverage Map](https://www.fcc.gov/BroadbandData/MobileMaps/mobile-map)
- 问同小区 / 实验室的同事手机信号怎样（最直接）

**实战**：T-Mobile 在大城市好，乡村差；Verizon 全美最稳。在你的具体地区，问问邻居。

## 8.5 实体店销售提成话术

实体店销售对 **postpaid 套餐有提成**（约 $20-$50/单），对 **prepaid / MVNO 几乎没提成**。所以——

- 销售一定推 postpaid 套餐
- 会反复”建议“你选 $80+ 的”无限套餐“
- 会说 MVNO ”信号差 / 不稳定“——**这是销售话术，不是事实**

**应对**：在网上自助办，不去实体店。Mint / Visible / US Mobile / Google Fi 都是**全线上自助**，eSIM 5 分钟激活。

## 8.6 国际漫游高额账单

去欧洲一周回来收 $200 的账单是常事——主网 postpaid 套餐**多数不含国际漫游**，每天 $5-$10 + 流量 $5-$10/MB。

**避坑**：

- **出国前手动关漫游 + 蜂窝数据**
- 或换 **Google Fi**（200+ 国家漫游同价同流量，$0 加价）
- 或在目的地买当地 eSIM（[Airalo](https://www.airalo.com/) / [Holafly](https://esim.holafly.com/) 等）

# 9. 实战建议

## 9.1 新到美国第一周

**不要急着 commit 长期套餐**：

1. **先用 prepaid eSIM 试用**：Mint 7 天免费 / US Mobile 月付 / Google Fi 月付——**5 分钟在线激活**
2. **试用期间观察实际用量**：流量 / 通话量 / 短信量
3. **3-4 周后选定长期套餐**：基于实际用量选档位

## 9.2 半年回顾

每 6 个月做一次”账单审计“：

- 实际流量用了多少？（多数人远低于无限套餐）
- 通话和短信几乎没用？（iMessage / WhatsApp / 微信替代）
- 出过差 / 旅行没？

很多人办了 $80 无限套餐但实际只用 8 GB / 月——**降到 $20 套餐每月省 $60，一年省 $720**。

## 9.3 转网（Porting Number）

**保留号码换运营商**的标准流程：

1. **不要先关旧账户**——号码会被释放
2. 在新运营商网站开账户时选”**Bring your own number**“
3. 提供旧运营商的 **account number + transfer PIN**（旧运营商客服电话索要 / app 内申请）
4. 新运营商 24-48 小时内完成 porting，旧账户自动关闭
5. 期间手机可能短暂断信号 1-2 小时

**坑**：转网期间不要换 SIM 卡 / 重启手机，会卡住。

## 9.4 公司 / 学校话费补贴

**很多 PhD / 工程师工作有 $30-$50/月话费报销**——记得入职时问 HR。

- 大学：部分系会给 RA / TA 报销手机话费（实验室 PI 申请）
- 公司：很多大企业（Google / Meta / 金融业）有月度话费报销
- 校友 / 学术会议：偶尔有”会员价“折扣

# 10. 参考来源

1. **[r/NoContract](https://www.reddit.com/r/NoContract/)** —— Reddit 上 MVNO / prepaid 讨论最大的社区，新政策 / 折扣第一时间
2. **[BestMVNO.com](https://bestmvno.com/)** —— MVNO 大全 + 比较工具，每月更新
3. **[Mint Mobile / Visible / US Mobile / Google Fi 官网]**：直接看价格 + 套餐
4. **[FCC Mobile Coverage Map](https://www.fcc.gov/BroadbandData/MobileMaps/mobile-map)** —— 信号覆盖官方查询
5. **[一亩三分地”美国生活“版块](https://www.1point3acres.com/bbs/forum-178-1.html)** —— 中文圈实战经验
6. **[Doctor of Credit 手机话费 promo](https://www.doctorofcredit.com/)** —— 偶尔有”开卡送 $500 / 转入送 $400"等大力度活动追踪

---

最后一个观察——**手机话费这件事，一年下来一个人能省的钱可能比想象的多得多**。从 $80 主网套餐换到 $20 MVNO，**每月省 $60，一年 $720，五年 $3,600**。这笔钱够你回国 2-3 次往返机票，或者交一个学期的健康保险。**最值得花的 30 分钟是研究一下 MVNO，最不值得花的时间是每月默默被多扣 $60**。
