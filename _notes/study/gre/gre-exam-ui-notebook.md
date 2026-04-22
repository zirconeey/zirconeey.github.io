---
layout: post
title: "我把 GRE 的考试界面搬到了错题本上"
date: 2024-08-09
discipline: "语言考试"
course: "GRE"
material_type: "错题本"
---

这是我第二次备考 GRE 了，他们都说**做得多不如做得精**，所以过去的三五天完全都在重做一遍第一次备考期间的错题，竟然也有好几百题值得精刷。考满分有很贴心的"错题本"功能，但错题本里看错题并不是很方便，我个人的习惯也是喜欢自己整理起来错题并加一些注释。另外，我对美观有算是比较独特的追求，也希望错题以考试同样的形式呈现；算是搞了小一会儿代码，故简单分享下。我会分 Verbal 填空题和 Quant 两部分分别介绍（阅读题整理到错题本就比较不必要了，更多是经验的积累）。

这篇内容可能很无聊，也可能挺有意思，但无论如何希望对大家有帮助 🌈

![](/files/images/gre-exam-ui-notebook/01.jpg)

![](/files/images/gre-exam-ui-notebook/02.jpg)

## Verbal 填空题

Verbal 填空题有三类题型：

- 五选一
- 多空题（两空和三空）
- 六选二

五选一和多空题本质上是一样的，都是把选项放在表格里，只不过是有几列、一列有几个选项之间的差别。

![](/files/images/gre-exam-ui-notebook/03.jpg)

<p class="img-caption">五选一</p>

![](/files/images/gre-exam-ui-notebook/04.jpg)

<p class="img-caption">双空题</p>

![](/files/images/gre-exam-ui-notebook/05.jpg)

<p class="img-caption">三空题</p>

为了把选项装在表格里，定义一个 `\choices` 命令，接收五个参数。如果五个参数都有，那么就放五行（相当于五选一题）；如果只有前三个参数有，后两个为空，则放三行（相当于多空题）。

```latex
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
```

之后需要根据题目类型决定放几列、怎么放。定义 `\multiblank` 命令，接收四个参数，第一个参数说明这道题有几空（为 1 即为五选一，2 或 3 就分别是两空和三空的多空题，六选二提醒后续会说），这会决定走哪套代码，即几个选项要怎么排布。后面三个参数就取决于具体题型往里头放 `\choices{}{}{}{}{}` 即可。

具体的实现就不在这里说了，有兴趣的可以看代码，其实并不算复杂，就是塞了 `tabularx` 环境，细节上设置选项陈列关于中间对齐，表格内的内容也要居中。

```latex
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
```

额外再定义一个下划线命令：

```latex
\newcommand{\blank}[1]{\underline{\tiankongdaan{\qquad~}}}
```

以及一个"注"命令用来写自己的解析：

```latex
\newcommand{\note}[1]{{\heiti\textbf{注\hspace{1em}}}#1.}
```

把整个错题本的正文都放在 `enumerate` 的环境之下，这样自然会有题号计数，每道题用 `\item` 打头。

### 五选一

```latex
\item Some biologists argue that each specific human trait must have arisen gradually and erratically, and that it is therefore difficult to isolate definite \blank{} in the evolution of the species.
\multiblank{1}{\choices{fluctuations}{generations}{predispositions}{milestones}{manifestations}}{}{}
```

呈现的效果如下

![](/files/images/gre-exam-ui-notebook/06.jpg)

### 双空题

```latex
\item It would be (i)\blank{} not to (ii)\blank{} these tabloid journalists for thriving in hard times: they deserve credit for doing well in a profession in financial straits.
\multiblank{2}{\choices{apropos}{churlish}{cagey}{}{}}{\choices{admire}{envy}{emulate}{}{}}{}
```

![](/files/images/gre-exam-ui-notebook/07.jpg)

### 三空题

```latex
\item By the end of the 1970s, the postmodern novel had degenerated from a bold attempt to (i)\blank{} the conventions of traditional narrative into a literary style as (ii)\blank{} as any other. There are, it seems, (iii)\blank{} number of ways to avoid telling a straightforward story.
\multiblank{3}{\choices{refine}{perpetuate}{subvert}{}{}}{\choices{predictable}{inescapable}{comprehensible}{}{}}{\choices{a limited}{a variable}{an inexhaustible}{}{}}{}{}
```

![](/files/images/gre-exam-ui-notebook/08.jpg)

### 六选二

因为呈现的形式不同于其它题，六选二题单独定义呈现命令。

![](/files/images/gre-exam-ui-notebook/09.jpg)

<p class="img-caption">六选二</p>

乍一眼来看，似乎用一个 `itemize` 环境（并且让其居中，然后再改变 bullet point 样式为 `\square`）就可以实现，但这样有一个问题，就是 bullet points 的位置可能因为选项的长度而有改变。我希望实现的是无论如何 bullet points 都在固定的位置（即有固定的横坐标），故还是用到了 `tabularx` 环境，相当于把方块和选项当作两列。如下定义六选二提醒的呈现命令 `\senequiv`（取这个名字是因为这类题实际上叫 sentence equivalence）：

```latex
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

使用起来效果如下：

```latex
\item Individuals interested in longevity have sought to fine-tune their bodies with all kinds of \blank{} diets: only raw foods; only plant; only the flesh, fruit, and nuts that prehistoric humans would have hunted and foraged.
\senequiv{eccentric}{meager}{salutary}{proscriptive}{trendy}{exacting}
```

![](/files/images/gre-exam-ui-notebook/10.jpg)

## Quant

数学大致来说有两类题型，一类是选择题，一类是填空题。

### 选择题

选择题可以再额外分出两小类：

- 比大小
- 一般的选择题

#### 一般选择题

一般的选择题里也有多选题，由于多选题比较少且一般不难，实现方法在上面的六选二也说过了，这边就不再额外介绍。

GRE 单选题选项的 bullet point 是一个椭圆，可惜的是 \LaTeX 里并没有直接的椭圆的命令，这里用到 `tikz` 包画一个就好。定义命令 `\oval` 为：

```latex
\usepackage{tikz}
\renewcommand{\oval}{
\begin{tikzpicture}
  \draw (0,0) ellipse (.15cm and .075cm);
\end{tikzpicture}
}
```

之后定义选项呈现的命令 `\options`（和 `\choices` 不同，但和 `\senequiv` 的思路基本相同，注意到一般选择题都是五个选项）：

```latex
\newcommand{\options}[5]{
\begin{center}
\begin{tabularx}{\linewidth}{>{\raggedleft\arraybackslash}p{0.45\linewidth} p{0.5\linewidth}}
    \oval & {#1} \\
    \oval & {#2} \\
    \oval & {#3} \\
    \oval & {#4} \\
    \oval & {#5}
\end{tabularx}
\end{center}
}
```

这样的效果如下：

```latex
\item The repeating decimal \( 1.\overline{ab} \), where \( a \) and \( b \) are different digits, is equivalent to the fraction \( \frac{n}{d} \), where \( n \) and \( d \) are positive integers whose greatest common factor is 1. What is the greatest possible value of \( n + d \) ?
\options{296}{297}{298}{299}{301}
```

![](/files/images/gre-exam-ui-notebook/11.jpg)

#### 比大小

比大小其实也是选择题的一种，它们出现频繁，格式都是固定的，选项也是一样的，所以单独定义一类以图方便。

![](/files/images/gre-exam-ui-notebook/12.jpg)

定义命令 `\quantities`，接收两个参数分别作为 Quantity A 和 Quantity B，用于比大小题从 Quantity A 一直到四个选项的呈现（题干信息额外写）：

```latex
\newcommand{\quantities}[2]{
\begin{center}
    \begin{tabularx}{\linewidth}{*{2}{>{\centering\arraybackslash}X}}
    \textbf{\underline{Quantity A}} & \textbf{\underline{Quantity B}}\\
    {#1} & {#2}
    \end{tabularx}
\end{center}

\begin{center}
\begin{tabularx}{\linewidth}{>{\raggedleft\arraybackslash}p{0.2\linewidth} p{0.8\linewidth}}
    \oval & Quantity A is greater. \\
    \oval & Quantity B is greater. \\
    \oval & The two quantities are equal. \\
    \oval & The relationship cannot be determined from the information given.
\end{tabularx}
\end{center}
}
```

呈现的效果如下：

```latex
\item $x^2+y^2 = 52$. Both $x$ and $y$ are integers and $x>y$.
\quantities{$x$}{$4$}
```

![](/files/images/gre-exam-ui-notebook/13.jpg)

### 填空题

填空题其实没有什么难度，题面的叙述就是一般的正文，只要考虑添加一个长方形框用来输入答案即可。

![](/files/images/gre-exam-ui-notebook/14.jpg)

这个长方形框还是用 `tikz` 画一个就好。定义一个命令 `\field` 用于生成长方形框：

```latex
\newcommand{\field}{
\begin{center}
\begin{tikzpicture}
  \draw (0,0) rectangle (3,.6);
\end{tikzpicture}
\end{center}
}
```

以上面那题为例，效果为：

```latex
\item If \( a \), \( b \), and \( c \) are positive integers such that \( \dfrac{a}{c} = 0.075 \), and \( \dfrac{b}{c} = 0.09 \), what is the least possible value of \( c \)?
\field
```

![](/files/images/gre-exam-ui-notebook/15.jpg)

希望对大家有帮助 🌈

![](/files/images/gre-exam-ui-notebook/16.jpg)
