---
layout: post
title: "优雅地用bruceR拿捏调节效应和中介效应"
main_category: "科研妙招"
date: "2023-05-01"
sub_category: "R 教程"
author: "Zircon"
permalink: "/research/r-tutorials/r-brucer-moderation-mediation"
published: true
---

这次的内容大不一样！上篇是《[博雅 | 优雅地用 R 拿捏调节效应和中介效应](https://mp.weixin.qq.com/s?__biz=Mzk0NTMxNjcxNg==&mid=2247488172&idx=1&sn=19cb14f51039d34ba7eb76f43241df64&chksm=c31664aff461edb91943a1dde2a68e189f32b523ae20a4937f79982f9190bf5fb23adf98ea1b&token=1698465383&lang=zh_CN&scene=21#wechat_redirect)》，这次不是优雅地用“R”了，而是优雅地用"bruceR"，比原先用R优雅地多！

当然，文末“**阅读原文**”必然是蓝色的~

站在巨人的肩膀上简单评价前人的成果是“不道德”的，但在进入正文之前，我还是想通过简单对比看看这次是有多优雅！在上篇介绍的，在调节效应显著后，简单斜率分析用到的代码是这样复杂：

![](/files/images/r-brucer-moderation-mediation/01.jpg)

不仅需要指定很繁杂的参数，还要**手动**设置中心化和标准差！而且这还没有考虑此前拟合模型所费的周章。而用了bruceR::PROCESS()，只要一句指令

![](/files/images/r-brucer-moderation-mediation/02.jpg)

就能给我返回部分模型、全模型，

![](/files/images/r-brucer-moderation-mediation/03.jpg)

还帮我顺带做了效应估计（在调节作用中即简单斜率分析）！

![](/files/images/r-brucer-moderation-mediation/04.jpg)

真的是有被"bruceR::PROCESS()"幸福到！🥰

调节效应和中介效应是因果分析中非常重要的两个板块。说白了，调节效应就是“调节”，干预自变量对因变量的作用，技术上就是在多元线性回归中添加了交互作用，中介效应就是“中介”，作为中介介入自变量到因变量的影响，技术上就是多元线性回归中的考虑“遗漏变量”情形。

对于更基础的知识和操作，可以参见上篇《[博雅 | 优雅地用 R 拿捏调节效应和中介效应](https://mp.weixin.qq.com/s?__biz=Mzk0NTMxNjcxNg==&mid=2247488172&idx=1&sn=19cb14f51039d34ba7eb76f43241df64&chksm=c31664aff461edb91943a1dde2a68e189f32b523ae20a4937f79982f9190bf5fb23adf98ea1b&token=1698465383&lang=zh_CN&scene=21#wechat_redirect)》，我已经迫不及待地想要介绍"bruceR::PROCESS()"是有多优雅了！正文开始！
![](/files/images/r-brucer-moderation-mediation/05.jpg)

![](/files/images/r-brucer-moderation-mediation/06.jpg)

![](/files/images/r-brucer-moderation-mediation/07.jpg)

![](/files/images/r-brucer-moderation-mediation/08.jpg)

![](/files/images/r-brucer-moderation-mediation/09.jpg)

![](/files/images/r-brucer-moderation-mediation/10.jpg)

![](/files/images/r-brucer-moderation-mediation/11.jpg)

![](/files/images/r-brucer-moderation-mediation/12.jpg)

![](/files/images/r-brucer-moderation-mediation/13.jpg)

![](/files/images/r-brucer-moderation-mediation/14.jpg)

![](/files/images/r-brucer-moderation-mediation/15.jpg)

![](/files/images/r-brucer-moderation-mediation/16.jpg)

![](/files/images/r-brucer-moderation-mediation/17.jpg)

![](/files/images/r-brucer-moderation-mediation/18.jpg)

![](/files/images/r-brucer-moderation-mediation/19.jpg)

![](/files/images/r-brucer-moderation-mediation/20.jpg)

![](/files/images/r-brucer-moderation-mediation/21.jpg)

![](/files/images/r-brucer-moderation-mediation/22.jpg)

![](/files/images/r-brucer-moderation-mediation/23.jpg)

![](/files/images/r-brucer-moderation-mediation/24.jpg)

![](/files/images/r-brucer-moderation-mediation/25.jpg)

![](/files/images/r-brucer-moderation-mediation/26.jpg)

![](/files/images/r-brucer-moderation-mediation/27.jpg)

![](/files/images/r-brucer-moderation-mediation/28.jpg)
