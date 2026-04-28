---
layout: post
title: "WiFi 为什么隔一面墙就掉？2.4G 和 5G 该怎么选？"
date: 2026-04-28
main_category: "生活攻略"
sub_category: "生活之问"
permalink: "/life/wifi-through-walls"
---

# 1. 问题

明明路由器就在隔壁一墙之隔，WiFi 信号却从满格掉到一格、视频卡成 PPT。手机里的 2.4G 和 5G 双频到底该选哪个？路由器放哪里最好？「Mesh」「中继器」「电力猫」是不是真的有用？

# 2. 结论先行

WiFi 是电磁波，**频率越高、波长越短，穿墙时损耗越大**：

- **2.4 GHz**：波长 12.5 cm，穿透好——但住宅楼里邻居 + 蓝牙 + 微波炉全挤在这；只有 **3 个非重叠信道**（1 / 6 / 11）
- **5 GHz**：波长 6 cm，速率快、信道多（20+）——但隔一堵承重墙就大幅衰减
- **6 GHz**（WiFi 6E / WiFi 7 用）：更快、更不拥堵，但穿透更弱

实操简版：

| 场景 | 选哪个 |
|---|---|
| 同一房间、视距内 | 5 GHz（速度优先） |
| 隔 1 堵承重墙 | 大多数情况 5 GHz 仍可，5G 不行再切 2.4G |
| 隔 2 堵以上 / 跨楼层 | 走 2.4 GHz，或加 Mesh / 网线 |
| 楼内 WiFi 极拥挤 | 优先 5 GHz（信道多）|

路由器摆放三件事：**居中、抬高、远离金属和水**。装在金属机柜里、塞鞋柜里、紧挨微波炉，再贵的路由器也救不回来。

# 3. 科学原理

## 3.1 WiFi 是电磁波，关键变量是频率

WiFi 信号是无线电波，本质和广播、5G 移动信号、微波炉发出的 2.45 GHz 微波是同类东西，只是频率（也就是波长）不同。

电磁波在真空中的速度是固定的光速 c ≈ 3 × 10⁸ m/s。频率 f 和波长 λ 的关系是：

> **λ = c / f**

代入：

- 2.4 GHz WiFi → λ ≈ **12.5 cm**
- 5 GHz WiFi → λ ≈ **6 cm**
- 6 GHz WiFi → λ ≈ **5 cm**
- FM 广播（100 MHz） → λ ≈ 3 m
- 4G LTE（700 MHz 频段） → λ ≈ 43 cm

**为什么频率高穿墙差？** 一个直观理解：电磁波要“挤过”墙体材料的分子结构，波长越短，越容易被墙里的水分、钢筋、金属网“看见”和吸收 / 反射。波长长的电波更倾向于绕过或直接穿透小障碍。

这就是为什么 FM 广播能轻松穿一栋楼，4G 信号在地下室仍能用，而 5 GHz WiFi 隔两堵墙就所剩无几。

## 3.2 不同建筑材料的衰减，一目了然

不同材料对 WiFi 的衰减差距非常大。下面是基于 ITU-R P.2040 模型 + NIST 实测综合的典型数值：

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 460" style="max-width:100%;height:auto;display:block;margin:1.2em auto;">
  <text x="360" y="22" text-anchor="middle" font-size="14" fill="#333" font-weight="600">穿过单层材料的 WiFi 信号衰减（dB）</text>
  <text x="360" y="42" text-anchor="middle" font-size="11" fill="#666">每 10 dB ≈ 信号强度衰减到原来的 1/10</text>
  <line x1="180" y1="60" x2="180" y2="430" stroke="#888" stroke-width="1"/>
  <line x1="180" y1="430" x2="700" y2="430" stroke="#888" stroke-width="1"/>
  <g font-size="10" fill="#888">
    <text x="180" y="445" text-anchor="middle">0</text>
    <text x="284" y="445" text-anchor="middle">5</text>
    <text x="388" y="445" text-anchor="middle">10</text>
    <text x="492" y="445" text-anchor="middle">15</text>
    <text x="596" y="445" text-anchor="middle">20</text>
    <text x="700" y="445" text-anchor="middle">25 dB</text>
  </g>
  <g font-size="11" fill="#333">
    <text x="170" y="80" text-anchor="end">人体</text>
    <rect x="180" y="70" width="63" height="14" fill="#3498db" opacity="0.85"/>
    <text x="248" y="80" font-size="10" fill="#666">3 dB</text>
    <rect x="180" y="86" width="83" height="14" fill="#e74c3c" opacity="0.85"/>
    <text x="268" y="96" font-size="10" fill="#666">4 dB</text>
  </g>
  <g font-size="11" fill="#333">
    <text x="170" y="118" text-anchor="end">普通木门</text>
    <rect x="180" y="108" width="42" height="14" fill="#3498db" opacity="0.85"/>
    <text x="227" y="118" font-size="10" fill="#666">2 dB</text>
    <rect x="180" y="124" width="63" height="14" fill="#e74c3c" opacity="0.85"/>
    <text x="248" y="134" font-size="10" fill="#666">3 dB</text>
  </g>
  <g font-size="11" fill="#333">
    <text x="170" y="156" text-anchor="end">石膏板隔墙</text>
    <rect x="180" y="146" width="63" height="14" fill="#3498db" opacity="0.85"/>
    <text x="248" y="156" font-size="10" fill="#666">3 dB</text>
    <rect x="180" y="162" width="105" height="14" fill="#e74c3c" opacity="0.85"/>
    <text x="290" y="172" font-size="10" fill="#666">5 dB</text>
  </g>
  <g font-size="11" fill="#333">
    <text x="170" y="194" text-anchor="end">普通玻璃窗</text>
    <rect x="180" y="184" width="63" height="14" fill="#3498db" opacity="0.85"/>
    <text x="248" y="194" font-size="10" fill="#666">3 dB</text>
    <rect x="180" y="200" width="105" height="14" fill="#e74c3c" opacity="0.85"/>
    <text x="290" y="210" font-size="10" fill="#666">5 dB</text>
  </g>
  <g font-size="11" fill="#333">
    <text x="170" y="232" text-anchor="end">砖墙（24 cm）</text>
    <rect x="180" y="222" width="125" height="14" fill="#3498db" opacity="0.85"/>
    <text x="310" y="232" font-size="10" fill="#666">6 dB</text>
    <rect x="180" y="238" width="208" height="14" fill="#e74c3c" opacity="0.85"/>
    <text x="393" y="248" font-size="10" fill="#666">10 dB</text>
  </g>
  <g font-size="11" fill="#333">
    <text x="170" y="270" text-anchor="end">混凝土承重墙</text>
    <rect x="180" y="260" width="250" height="14" fill="#3498db" opacity="0.85"/>
    <text x="435" y="270" font-size="10" fill="#666">12 dB</text>
    <rect x="180" y="276" width="375" height="14" fill="#e74c3c" opacity="0.85"/>
    <text x="560" y="286" font-size="10" fill="#666">18 dB</text>
  </g>
  <g font-size="11" fill="#333">
    <text x="170" y="308" text-anchor="end">low-e 镀膜玻璃</text>
    <rect x="180" y="298" width="208" height="14" fill="#3498db" opacity="0.85"/>
    <text x="393" y="308" font-size="10" fill="#666">10 dB</text>
    <rect x="180" y="314" width="333" height="14" fill="#e74c3c" opacity="0.85"/>
    <text x="518" y="324" font-size="10" fill="#666">16 dB</text>
  </g>
  <g font-size="11" fill="#333">
    <text x="170" y="346" text-anchor="end">瓷砖墙 / 镜子</text>
    <rect x="180" y="336" width="250" height="14" fill="#3498db" opacity="0.85"/>
    <text x="435" y="346" font-size="10" fill="#666">12 dB</text>
    <rect x="180" y="352" width="375" height="14" fill="#e74c3c" opacity="0.85"/>
    <text x="560" y="362" font-size="10" fill="#666">18 dB</text>
  </g>
  <g font-size="11" fill="#333">
    <text x="170" y="384" text-anchor="end">金属门 / 防盗门</text>
    <rect x="180" y="374" width="500" height="14" fill="#3498db" opacity="0.85"/>
    <text x="685" y="384" font-size="10" fill="#666">24 dB</text>
    <rect x="180" y="390" width="520" height="14" fill="#e74c3c" opacity="0.85"/>
    <text x="685" y="400" font-size="10" fill="#666">25+ dB</text>
  </g>
  <g transform="translate(540,75)" font-size="11">
    <rect x="0" y="0" width="14" height="12" fill="#3498db" opacity="0.85"/>
    <text x="22" y="10" fill="#333">2.4 GHz</text>
    <rect x="0" y="20" width="14" height="12" fill="#e74c3c" opacity="0.85"/>
    <text x="22" y="30" fill="#333">5 GHz</text>
  </g>
</svg>
<p class="img-caption">**dB 是对数刻度**：每 +10 dB 信号强度衰减 10 倍、+20 dB 衰减 100 倍。一堵混凝土承重墙（5G ≈ 18 dB）就能把信号衰减到原来的 1/63。两堵承重墙叠加 36 dB，相当于 1/4000——这就是为什么穿两堵墙基本就什么都不剩了。**5 GHz 的衰减普遍是 2.4 GHz 的 1.5-2 倍**。</p>

## 3.3 信道：2.4G 拥挤、5G 宽敞

光看穿透，2.4G 是赢家。但住宅楼里 2.4G 经常“满格但卡”——问题不在距离，在**信道拥堵**。

WiFi 把频段切成多个信道。2.4 GHz 频段总共只有 83.5 MHz 带宽，被切成 11-13 个信道，但每个信道有 20 MHz 宽，相邻信道严重重叠。**真正不重叠的只有 3 个：信道 1、6、11**。

5 GHz 频段则有 500+ MHz 可用带宽，能切出 25 个左右非重叠信道（不同国家略有差别）。

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 320" style="max-width:100%;height:auto;display:block;margin:1.2em auto;">
  <text x="360" y="22" text-anchor="middle" font-size="14" fill="#333" font-weight="600">2.4 GHz vs 5 GHz 信道分布</text>
  <g transform="translate(0,40)">
    <text x="40" y="14" font-size="12" fill="#333" font-weight="600">2.4 GHz：只有 3 个非重叠信道</text>
    <line x1="40" y1="80" x2="680" y2="80" stroke="#888" stroke-width="1"/>
    <text x="40" y="98" font-size="10" fill="#888">2400 MHz</text>
    <text x="680" y="98" font-size="10" fill="#888" text-anchor="end">2483 MHz</text>
    <ellipse cx="120" cy="60" rx="80" ry="22" fill="#27ae60" opacity="0.55"/>
    <text x="120" y="64" text-anchor="middle" font-size="12" fill="#fff" font-weight="700">信道 1</text>
    <ellipse cx="200" cy="60" rx="80" ry="22" fill="#3498db" opacity="0.4"/>
    <text x="200" y="64" text-anchor="middle" font-size="11" fill="#666">2</text>
    <ellipse cx="280" cy="60" rx="80" ry="22" fill="#3498db" opacity="0.4"/>
    <text x="280" y="64" text-anchor="middle" font-size="11" fill="#666">3-5</text>
    <ellipse cx="360" cy="60" rx="80" ry="22" fill="#27ae60" opacity="0.55"/>
    <text x="360" y="64" text-anchor="middle" font-size="12" fill="#fff" font-weight="700">信道 6</text>
    <ellipse cx="440" cy="60" rx="80" ry="22" fill="#3498db" opacity="0.4"/>
    <text x="440" y="64" text-anchor="middle" font-size="11" fill="#666">7</text>
    <ellipse cx="520" cy="60" rx="80" ry="22" fill="#3498db" opacity="0.4"/>
    <text x="520" y="64" text-anchor="middle" font-size="11" fill="#666">8-10</text>
    <ellipse cx="600" cy="60" rx="80" ry="22" fill="#27ae60" opacity="0.55"/>
    <text x="600" y="64" text-anchor="middle" font-size="12" fill="#fff" font-weight="700">信道 11</text>
    <text x="360" y="120" text-anchor="middle" font-size="11" fill="#666">每个信道 20 MHz 宽，相邻信道严重重叠</text>
  </g>
  <g transform="translate(0,170)">
    <text x="40" y="14" font-size="12" fill="#333" font-weight="600">5 GHz：25+ 个非重叠信道</text>
    <line x1="40" y1="60" x2="680" y2="60" stroke="#888" stroke-width="1"/>
    <text x="40" y="78" font-size="10" fill="#888">5170 MHz</text>
    <text x="680" y="78" font-size="10" fill="#888" text-anchor="end">5835 MHz</text>
    <g fill="#27ae60" opacity="0.7">
      <rect x="50" y="48" width="22" height="14"/>
      <rect x="74" y="48" width="22" height="14"/>
      <rect x="98" y="48" width="22" height="14"/>
      <rect x="122" y="48" width="22" height="14"/>
      <rect x="146" y="48" width="22" height="14"/>
      <rect x="170" y="48" width="22" height="14"/>
      <rect x="194" y="48" width="22" height="14"/>
      <rect x="218" y="48" width="22" height="14"/>
      <rect x="242" y="48" width="22" height="14"/>
      <rect x="266" y="48" width="22" height="14"/>
      <rect x="290" y="48" width="22" height="14"/>
      <rect x="314" y="48" width="22" height="14"/>
      <rect x="338" y="48" width="22" height="14"/>
      <rect x="362" y="48" width="22" height="14"/>
      <rect x="386" y="48" width="22" height="14"/>
      <rect x="410" y="48" width="22" height="14"/>
      <rect x="434" y="48" width="22" height="14"/>
      <rect x="458" y="48" width="22" height="14"/>
      <rect x="482" y="48" width="22" height="14"/>
      <rect x="506" y="48" width="22" height="14"/>
      <rect x="530" y="48" width="22" height="14"/>
      <rect x="554" y="48" width="22" height="14"/>
      <rect x="578" y="48" width="22" height="14"/>
      <rect x="602" y="48" width="22" height="14"/>
      <rect x="626" y="48" width="22" height="14"/>
    </g>
    <text x="360" y="100" text-anchor="middle" font-size="11" fill="#666">信道之间不重叠，邻居用了一个我用另一个，互不干扰</text>
  </g>
</svg>
<p class="img-caption">2.4 GHz 像一条只有 3 个车道的小路，整栋楼几百户人家都在抢；5 GHz 像 25 车道的高速。这就是为什么 2.4G 信号看着满格、实际下载速率却慢——不是信号弱，是**车道堵**。</p>

## 3.4 多径效应：为什么屋里有 WiFi 死角

WiFi 信号不只走直线。墙壁、家具、金属表面都会**反射**信号，多条反射波到达手机时相位不同——有些地方相互加强（信号好），有些地方相互抵消（**死角**）。

特别要注意的反射 / 吸收源：

- **大型金属面**：冰箱、金属机柜、不锈钢厨具、镜子（背面是金属箔）
- **大型水体**：鱼缸、热水器、装满水的容器——水对 2.4 GHz 吸收强（因为微波炉就是利用这一点）
- **人体**：人 60% 是水，**会显著吸收 WiFi**（一屋子人开会时 WiFi 变慢有这个因素）

## 3.5 干扰源：微波炉真的会干扰 WiFi

家用微波炉工作频率正好是 2.45 GHz——和 2.4 GHz WiFi 是同频段。理论上微波炉是密封屏蔽的，但实际泄漏的微弱微波足以**短暂淹没附近 WiFi 信号**。

观察过这个现象的人都知道：开微波炉时刷视频经常卡几秒，关掉就恢复。这不是错觉，是物理。

其他 2.4 GHz 干扰源：

- 蓝牙耳机 / 鼠标 / 键盘（同频段，但功率低、跳频协议会避让）
- 老式无线电话（已经基本淘汰）
- 婴儿监视器
- 邻居 WiFi（楼里 50 个 2.4G 路由器分 3 个信道）

5 GHz 因为频段独占性强、家电少有这个频率，**几乎不受这些干扰**——这是它最大的优势之一。

## 3.6 为什么 6 GHz / WiFi 6E / WiFi 7 出现

简短：5 GHz 也开始拥挤了，需要更多频谱。

- **6 GHz 频段**（5925-7125 MHz）：FCC 在 2020 年开放给 WiFi 6E / WiFi 7 使用，新增 1200 MHz 带宽
- 优点：信道更多（59 个 20 MHz 信道）、几乎没有遗留设备占用
- 缺点：穿透更弱（波长更短）；只有近 2-3 年的新设备支持

如果你新买路由器，**WiFi 6E 或 WiFi 7 的 6 GHz 频段** 会显著改善近距离体验，但隔墙后仍要靠 2.4 GHz 兜底。

# 4. 实践建议

## 4.1 路由器位置：三件事

> **居中、抬高、远离金属和水**

具体：

- **居中**：放在房子几何中心位置，让信号往四周扩散；不要塞在户型一角
- **抬高**：离地至少 1 m，最好 1.2-1.8 m。WiFi 主辐射方向是水平的，离地太低被家具挡死
- **远离**：金属机柜内 / 鞋柜里 / 抽屉里 = 自带屏蔽箱，**直接削掉一半信号**；远离冰箱、鱼缸、微波炉、热水器、镜子至少 1 m

加分项：

- 天线**外置**的型号，把天线竖直立起来（不是水平摆着）；2 根以上天线可以一根竖直一根斜 45°，覆盖更全
- 有 WAN 口的房间是路由器位置的硬约束——如果它不在房子中心，考虑走网线把路由器牵到中心位置

## 4.2 双频段怎么选

现代手机 / 笔记本基本都默认开“智能 WiFi”，自动在 2.4G 和 5G 之间切换。但有些设备需要手动指定：

- **客厅、书房、近距离 → 5 GHz**（速度优先）
- **卧室、阳台、跨墙 → 2.4 GHz**（穿透优先）
- **打游戏 / 视频会议 → 5 GHz**（延迟稳定，干扰少）
- **智能家居（灯、扫地机、空调）→ 2.4 GHz**（多数只支持 2.4G）

很多路由器默认把 2.4G 和 5G 用**同一个 SSID**（让设备自动选）——这通常是最方便的。但如果你发现某些设备老黏在 2.4G 不切换，可以**拆成两个 SSID**（如 `MyWiFi-2G` 和 `MyWiFi-5G`），手动指定。

## 4.3 信道选择：避开邻居

下载一个 WiFi Analyzer 类 App（手机端：「WiFi Analyzer」「NetSpot」；电脑端：macOS 内置「无线诊断」、Windows 用 WiFi Analyzer），扫一下周围 WiFi 都用了哪些信道。

- **2.4 GHz**：在 1 / 6 / 11 里挑一个空的。如果三个都被占了，挑信号最弱（dBm 数值最负）的那个邻居所在信道——至少打架对手少
- **5 GHz**：信道多，路由器自动选信道通常 OK；但如果发现 DFS 信道（52-144）连接不稳，可以手动锁到非 DFS 信道（36 / 40 / 44 / 48 / 149+）

## 4.4 隔墙怎么办

按效果排序：

1. **走网线 + 增加 AP**：最稳；如果墙里没有预埋网线，可以走墙边或踢脚线藏明线
2. **Mesh 路由器**（一主多从，统一 SSID）：现代家庭最优解；从节点和主路由通过专用回程信号通信，性能远好于普通中继器
3. **电力猫**：通过家里的电线传数据；**同一相位电路稳定，跨相位会大幅衰减**——效果取决于家里电路质量，靠运气
4. **中继器 / 信号放大器**：最便宜但最差——它接收一遍再发一遍，**实际带宽通常只有原来的一半**；能用但别期望太多
5. **更换更强路由器**：边际收益低；家用路由发射功率受 FCC 限制，“更强”的型号大多是天线和处理性能更好，对穿墙提升有限

跨楼层经验：

- 一栋两层小楼：路由器放楼梯口或一楼天花板附近，信号上下都能照顾
- 三层以上 / 大平层：基本必须 Mesh 或多 AP

## 4.5 三个常见误区

**误区 1：「路由器越贵穿墙越强」**——错。家用路由器最大发射功率被 FCC / 工信部限制（2.4 GHz 通常 100 mW = 20 dBm，5 GHz 200 mW = 23 dBm），所有合规产品基本一样。贵的差别在天线设计、芯片性能、并发能力。

**误区 2：「换 WiFi 7 就能解决卡顿」**——只解决一部分。WiFi 7 提升的是峰值速率和并发，**穿墙物理还是那个物理**。如果是隔两堵承重墙的问题，换 WiFi 7 不如加一个 Mesh 节点。

**误区 3：「关掉 2.4G 只用 5G 更快」**——对部分场景对，对大部分家庭错。2.4G 是穿墙兜底；关了它意味着远距离设备直接掉线。除非你已经有 Mesh 全屋覆盖、所有设备都支持 5G，否则别关。

# 5. 参考来源

1. **IEEE 802.11 standard** (current revision)：WiFi 协议族的官方技术规范，定义了所有频段、信道、调制方式。最权威的源头文档。
2. **ITU-R Recommendation P.2040.** *Effects of building materials and structures on radiowave propagation above about 100 MHz.* International Telecommunication Union; 2023. ——建筑材料对电磁波穿透 / 反射 / 衰减的官方模型，本文衰减值的主要参考。
3. **Stone WC.** *Electromagnetic Signal Attenuation in Construction Materials.* NIST Construction Automation Program Report No. 3; 1997. ——美国国家标准与技术研究院的实测衰减数据。
4. **FCC Office of Engineering and Technology.** *Code of Federal Regulations Title 47, Part 15.* ——美国 ISM / U-NII 频段的法定划分和功率限制。
5. **Wi-Fi Alliance.** *Wi-Fi 6E / Wi-Fi 7 technical specifications.* ——6 GHz 频段、WiFi 6E / 7 的最新技术文档。
