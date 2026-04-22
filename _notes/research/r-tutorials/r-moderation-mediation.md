---
layout: post
title: "优雅地用 R 拿捏调节效应和中介效应"
main_category: "科研妙招"
date: "2023-04-28"
sub_category: "R 教程"
author: "Zircon"
permalink: "/research/r-tutorials/r-moderation-mediation"
published: true
---

调节效应和中介效应是因果分析中非常重要的两个板块。我仍然很清晰地记得去年《社会心理学》的助教学姐锐评我们搭建的漏洞百出的模型时，“调节效应”“中介效应”信口拈来，而那时连听到“IV”和“DV”都要反应一会儿的我真的完全懵了，只敢连声应下并事后偷偷补了补课。

说白了，调节效应就是“调节”，干预自变量对因变量的作用，技术上就是在多元线性回归中添加了交互作用，中介效应就是“中介”，作为中介介入自变量到因变量的影响，技术上就是多元线性回归中的考虑“遗漏变量”情形。调节作用在上周的一篇小文章样本结构与调节作用中简单谈过。

我后来发现在编译的PDF中显示代码结果是一件很烦人的事情，于是索性这回直接把所有的代码输出都隐藏了——结果从Rmd到PDF的编译速度简直飞起——往常我可以打开朋友圈点个赞的功夫 PDF 才会自动生成（10s 左右），这回没等我把手从键盘挪到鼠标就生成了！此外，《心理统计 II》现在越来越工具性了——我不像也没法像前几节课那样对所有的原理都做到完全消化，尤其是一些很复杂的技术性的检验——因此现在我除了放上最基本的理解外，文档整体上还是工具性更强一些，相信对于有实战需要的朋友能提供更直接的帮助。

![](/files/images/r-moderation-mediation/01.jpg)

![](/files/images/r-moderation-mediation/02.jpg)

![](/files/images/r-moderation-mediation/03.jpg)

![](/files/images/r-moderation-mediation/04.jpg)

![](/files/images/r-moderation-mediation/05.jpg)

![](/files/images/r-moderation-mediation/06.jpg)

![](/files/images/r-moderation-mediation/07.jpg)

![](/files/images/r-moderation-mediation/08.jpg)

![](/files/images/r-moderation-mediation/09.jpg)

![](/files/images/r-moderation-mediation/10.jpg)

![](/files/images/r-moderation-mediation/11.jpg)

![](/files/images/r-moderation-mediation/12.jpg)

![](/files/images/r-moderation-mediation/13.jpg)

![](/files/images/r-moderation-mediation/14.jpg)
