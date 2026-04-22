---
layout: post
title: "优雅地用 R 拿捏相关与距离"
main_category: "科研妙招"
date: "2023-04-29"
sub_category: "R 教程"
author: "Zircon"
permalink: "/research/r-tutorials/r-correlation-distance"
published: true
---

文末“**阅读原文**”是蓝色的噢~

本节的“相关”将会在之前讲的参数相关、非参相关之外讨论考虑分组时的相关，以及偏相关（partial correlation）和半偏相关（部分相关, part correlation）。有意思的是，之前在多元线性回归时也讨论过偏相关和半偏相关，但此处的概念得到了一般化，不必局限于多元线性回归的领域。不过，用回归和残差的思路理解偏相关能收获独特的见解！

本节的“距离”并不是物理意义上的距离，而是用来刻画相关的距离。实际上，我们学习的所有相关都是“距离”的一种刻画。在此基础上，介绍了欧氏距离、切比雪夫距离和余弦距离。代码中给出了计算欧氏距离和余弦相似性的方法。同时，注意“距离”的概念有区分是观测之间的距离，还是变量之间的距离。两者在含以上有很大的差距，但在计算上只要将矩阵（或数据框）转置即可。

本次笔记用到了“stargazer()”函数（来自stargazer包），它能帮助输出很漂亮的结果，下次重点聊聊（挖坑 ing）~

![](/files/images/r-correlation-distance/01.jpg)

![](/files/images/r-correlation-distance/02.jpg)

![](/files/images/r-correlation-distance/03.jpg)

![](/files/images/r-correlation-distance/04.jpg)

![](/files/images/r-correlation-distance/05.jpg)

![](/files/images/r-correlation-distance/06.jpg)

![](/files/images/r-correlation-distance/07.jpg)

![](/files/images/r-correlation-distance/08.jpg)

![](/files/images/r-correlation-distance/09.jpg)

![](/files/images/r-correlation-distance/10.jpg)

![](/files/images/r-correlation-distance/11.jpg)

![](/files/images/r-correlation-distance/12.jpg)

![](/files/images/r-correlation-distance/13.jpg)

![](/files/images/r-correlation-distance/14.jpg)
