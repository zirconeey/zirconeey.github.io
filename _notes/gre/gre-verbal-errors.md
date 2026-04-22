---
layout: post
title: "（个人向）GRE 语文填空题错题本"
date: 2024-08-17
discipline: "语言考试"
course: "GRE"
material_type: "错题本"
---

（8 月 16 日发的版本 LaTeX 代码忘了更新，本文附的是完整更新版。）

[裂开]

话不多说，第二次备考 GRE 了，很多的精力都放在了重过错题上（事实上第一次备考做的多而做不精，错题也只是错了）。上两篇分享过如何复刻和 GRE 考试界面一样的错题本，昨天分享了数学的错题本（发了之后意识到叫精选题更合适），这一篇就简单分享一下**语文填空题**错题本吧，算是给自己明天的考试攒点人品 🙏。

语文的填空题总结下来还是有不少套路的，第一阶段可能单词本身就是障碍（其实我到每个 section 的填空题还是免不了遇到关键信息甚至选项上的关键词），第二阶段要熟悉 GRE 的逻辑，有时候并不是逻辑不过关，单纯就是不熟练 GRE 的考题思路。第三阶段，也是这次备考的主要任务，就是形成一定的题感，并且保证高效的做题速度。事实证明多刷题还是有用的，但一定要精刷，也一定要集中刷，刷完一定要总结。如果你也是跟我一样比较细腻，做一个精题集是最好的实现手段。

语文填空题错题本前四页是精选题，主要是关乎逻辑理解；后四页是因字面含义理解而错的题；最后一页摘一些过程中的生词（甚至没有计入总页数，其实就是没背到但也懒得背了）。如果你也想用复刻这样的格式（而懒得补档上一篇），我也把 header 的代码放在图片之后了（不同于昨天的数学的代码），希望对大家有帮助～

![](/files/images/gre-verbal-errors/02.jpg)

![](/files/images/gre-verbal-errors/03.jpg)

![](/files/images/gre-verbal-errors/04.jpg)

![](/files/images/gre-verbal-errors/05.jpg)

![](/files/images/gre-verbal-errors/06.jpg)

![](/files/images/gre-verbal-errors/07.jpg)

![](/files/images/gre-verbal-errors/08.jpg)

![](/files/images/gre-verbal-errors/09.jpg)

![](/files/images/gre-verbal-errors/10.jpg)

{% raw %}
```latex
\usepackage{tabularx}

\newcommand{\note}[1]{{\heiti\textbf{注\hspace{1em}}}#1.}

\newcommand{\choices}[5]{%
    \ifx\relax#4\relax % 检查第四个参数是否未定义（即 \relax）
        % 如果第四个参数未定义，创建一个三参数的表格
        \begin{tabular}{|>{\centering\arraybackslash}m{0.7\linewidth}|}
        \hline
        #1 \\
        \hline
        #2 \\
        \hline
        #3 \\
        \hline
        \end{tabular}
    \else % 如果第四个参数已定义，创建一个五参数的表格
        \begin{tabular}{|>{\centering\arraybackslash}m{0.4\linewidth}|}
        \hline
        #1 \\
        \hline
        #2 \\
        \hline
        #3 \\
        \hline
        #4 \\
        \hline
        #5 \\
        \hline
        \end{tabular}
    \fi
}

\newcommand{\multiblank}[4]{%
    \ifnum#1=1
        \begin{center}
            \begin{tabularx}{0.4\textwidth}{*{1}{>{\centering\arraybackslash}X}}
            {#2}
            \end{tabularx}
        \end{center}
    \else
        \ifnum#1=2 % 如果第一个参数是 2
            \begin{center}
                \begin{tabularx}{0.4\textwidth}{*{2}{>{\centering\arraybackslash}X}}
                Blank (i) & Blank (ii) \\
                {#2} & {#3}
                \end{tabularx}
            \end{center}
        \else % 如果第一个参数不是 2
            \ifnum#1=3
                \begin{center}
                    \begin{tabularx}{0.4\textwidth}{*{3}{>{\centering\arraybackslash}X}}
                    Blank (i) & Blank (ii) & Blank (iii) \\
                    {#2} & {#3} & {#4}
                    \end{tabularx}
                \end{center}
            \fi
        \fi
    \fi
}

\newcommand{\senequiv}[6]{
\begin{center}
\begin{tabularx}{\linewidth}{>{\raggedleft\arraybackslash}p{0.4\linewidth} p{0.45\linewidth}}
    $\square$ & {#1} \\
    $\square$ & {#2} \\
    $\square$ & {#3} \\
    $\square$ & {#4} \\
    $\square$ & {#5} \\
    $\square$ & {#6} \\
\end{tabularx}
\end{center}
}
```
{% endraw %}
