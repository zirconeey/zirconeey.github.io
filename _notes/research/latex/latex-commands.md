---
layout: post
title: "我常用的LaTeX快捷键大全"
main_category: "科研妙招"
sub_category: "LaTex相关"
date: "2026-04-20"
author: "Zircon"
permalink: "/research/latex/latex-commands"
published: true
---

不知道大家有没有过这样的体验：在上课听讲或者推导作业时，思路明明正如泉涌，却被冗长繁琐的 LaTeX 代码硬生生打断。为了敲出一个多行对齐的公式，或者一个带上下标的求和符号，手指在键盘上翻飞，结果一不小心漏掉一个大括号，编译报错，思路也跟着烟消云散了。

曾经我也是个头铁的“硬核”玩家，觉得既然要写 LaTeX，那就老老实实把每一个 `\begin{aligned}` 和 `\mathbb{R}` 都敲完整。但随着学业的深入，尤其是在应对高宏、高微这类充满复杂公式的课程时，我开始反思这种“苦力活”的意义。我忽然意识到，我似乎在把自己当作排版的工具奴役，而忘记了做笔记的“第一性原理”——**记录和推导思想，而不是去默写代码。**

于是，我开始学着偷懒，建立了自己的 `commands.tex` 快捷键库。今天就和大家聊聊，我们为什么需要构建自己的 LaTeX 快捷键，以及如何利用 `\newcommand` 和 `\renewcommand` 打造一个真正趁手的科研利器。

完整的Latex快捷键大全放在下一个章节，方便有需要的读者朋友自取。更具体的解释在更下一个章节，有兴趣的朋友可以继续阅读。

## 我的`commands.tex`全部命令

```
% ============================================================
%  commands.tex — Custom macros for Econ PhD lecture notes
%  Last updated: April 2026
% ============================================================

% ------------------------------------------------------------
%  1. Packages (loaded here to keep main .tex clean)
% ------------------------------------------------------------
\usepackage{amsmath}

% ------------------------------------------------------------
%  2. Environment shortcuts
% ------------------------------------------------------------
\newcommand{\ba}{\begin{aligned}}
\newcommand{\ea}{\end{aligned}}
\newcommand{\bc}{\begin{cases}}
\newcommand{\ec}{\end{cases}}

% ------------------------------------------------------------
%  3. Blackboard bold (number sets)
% ------------------------------------------------------------
\newcommand{\RR}{\mathbb{R}}
\newcommand{\QQ}{\mathbb{Q}}
\newcommand{\ZZ}{\mathbb{Z}}
\newcommand{\CC}{\mathbb{C}}
\newcommand{\NN}{\mathbb{N}}
\newcommand{\FF}{\mathbb{F}}

% ------------------------------------------------------------
%  4. Calligraphic letters (collections, spaces, etc.)
% ------------------------------------------------------------
\renewcommand{\P}{\mathcal{P}}
\renewcommand{\S}{\mathcal{S}}   % overwrites §
\newcommand{\T}{\mathcal{T}}
\newcommand{\A}{\mathcal{A}}
\newcommand{\B}{\mathcal{B}}
\newcommand{\C}{\mathcal{C}}
\renewcommand{\L}{\mathcal{L}}

% ------------------------------------------------------------
%  5. Bold vectors  (single-letter shortcuts)
%     For ad-hoc vectors, use \vb{symbol} instead.
% ------------------------------------------------------------
\newcommand{\vb}[1]{\mathbf{#1}}          % general bold vector
\newcommand{\x}{\mathbf{x}}
\newcommand{\y}{\mathbf{y}}
\newcommand{\z}{\mathbf{z}}
\newcommand{\w}{\mathbf{w}}
\newcommand{\e}{\mathbf{e}}
\renewcommand{\b}{\mathbf{b}}             % overwrites bar-under accent
\newcommand{\p}{\mathbf{p}}
\newcommand{\q}{\mathbf{q}}
\newcommand{\0}{\mathbf{0}}
\newcommand{\1}{\mathbf{1}}
\newcommand{\I}{\mathbf{I}}
\newcommand{\X}{\mathbf{X}}

% ------------------------------------------------------------
%  6. Greek letter shortcuts
% ------------------------------------------------------------
\newcommand{\ve}{\varepsilon}
\newcommand{\s}{\sigma}
\renewcommand{\l}{\lambda}                % overwrites Polish ł

% ------------------------------------------------------------
%  7. Delimiters (auto-sizing)
% ------------------------------------------------------------
\newcommand{\br}[1]{\left[#1\right]}                 % brackets
\newcommand{\pr}[1]{\left(#1\right)}                  % parentheses
\renewcommand{\brace}[1]{\left\{#1\right\}}           % braces
\newcommand{\abs}[1]{\left|#1\right|}                  % absolute value
\newcommand{\norm}[2][1]{\|{#2}\|_{#1}}               % norm
\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor} % floor
\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}    % ceiling

% ------------------------------------------------------------
%  8. Operators (proper math-operator spacing)
% ------------------------------------------------------------
\DeclareMathOperator*{\argmax}{arg\,max}
\DeclareMathOperator*{\argmin}{arg\,min}
\DeclareMathOperator{\plim}{plim}
\DeclareMathOperator{\supp}{supp}
\DeclareMathOperator{\mnull}{null}
\DeclareMathOperator{\mspan}{span}

% ------------------------------------------------------------
%  9. Probability, expectation, variance
%     Usage:  \Pr{A \given B},  \E{X \given Y},  \Var{X}
% ------------------------------------------------------------
\newcommand{\given}{\;\middle|\;}                     % conditional bar
\renewcommand{\Pr}[1]{\operatorname{Pr}\!\left(#1\right)}
\newcommand{\E}[2][]{\mathbb{E}_{#1}\!\pr{#2}}
\newcommand{\Var}[2][]{\operatorname{Var}_{#1}\!\br{#2}}
\newcommand{\Cov}[2]{\operatorname{Cov}\!\br{#1,#2}}

% ------------------------------------------------------------
%  10. Convergence and asymptotics
% ------------------------------------------------------------
\newcommand{\dto}{\overset{d}{\to}}                   % convergence in distribution
\newcommand{\pto}{\overset{p}{\to}}                   % convergence in probability
\newcommand{\asim}{\overset{\text{a}}{\sim}}           % asymptotically distributed

% ------------------------------------------------------------
%  11. Calculus and analysis
% ------------------------------------------------------------
\renewcommand{\d}{\text{d}}                           % upright differential d
\newcommand{\dd}[2]{\frac{\d #1}{\d #2}}              % total derivative
\newcommand{\pd}[2]{\frac{\partial #1}{\partial #2}}  % partial derivative
\newcommand{\inv}[1]{{#1}^{-1}}                       % inverse

% ------------------------------------------------------------
%  12. Relations and logic
% ------------------------------------------------------------
\newcommand{\se}{\subseteq}
\newcommand{\bs}{\setminus}                           % set difference (use \bs not \c)
\newcommand{\st}{\text{ s.t. }}
\newcommand{\mif}{\text{ if }}

% ------------------------------------------------------------
%  13. Summation / union / intersection shortcuts
% ------------------------------------------------------------
\newcommand{\add}[1][i]{\sum_{#1 = 1}^n}
\newcommand{\ply}[1][i]{\prod_{#1 = 1}^n}
\newcommand{\sinf}[1][k]{\sum_{{#1} = 1}^{\infty}}
\newcommand{\uinf}[1][k]{\bigcup_{{#1} = 1}^{\infty}}
\newcommand{\iinf}[1][k]{\bigcap_{{#1} = 1}^{\infty}}

% ------------------------------------------------------------
%  14. Game theory / mechanism design
% ------------------------------------------------------------
\newcommand{\pref}{\succsim}                          % weak preference
\newcommand{\meet}{\wedge}                            % lattice meet
\newcommand{\join}{\vee}                              % lattice join

% ------------------------------------------------------------
%  15. Complex analysis (keep if needed)
% ------------------------------------------------------------
\renewcommand{\Re}{\operatorname{Re}}
\renewcommand{\Im}{\operatorname{Im}}

% ------------------------------------------------------------
%  16. Draft utilities
% ------------------------------------------------------------
\newif\ifdraft
\drafttrue   % set \draftfalse to hide all TODOs

\newcommand{\todo}[1]{%
  \ifdraft{\textcolor{red}{\textbf{[TODO: #1]}}}{}\fi
}

% ------------------------------------------------------------
%  17. Highlighting (for lecture notes)
% ------------------------------------------------------------
\newcommand{\match}[1]{\textcolor{ForestGreen}{$\boldsymbol{#1}$}}

```

从最初的零星几个设定，到现在慢慢攒出一个完整的 `commands.tex`，我发现建立快捷键本质上是为了满足以下三种需求：

### 1. 极致的偷懒：用“语义”替代“物理按键”
这是最直观的需求。写数学笔记时，$\mathbb{R}$、$\varepsilon$ 这种符号几乎满天飞。每次敲 `\mathbb{R}` 实在太反人类了。通过建立快捷键，我们可以把操作压缩到极致。更重要的是，我们是在用“语义”写作：`\RR` 代表实数集，`\ba` 代表 aligned 环境开始。这种缩写不仅让代码更整洁，也让脑子在敲击键盘时少转一个弯。

### 2. 全局的统一：应对未来可能的“反悔”
有时候我们写到一半，或者文章快写完了，突然觉得期望的符号用 $\text{E}[X]$ 不好看，想改成黑斜体的 $\mathbb{E}[X]$。如果没有快捷键，你可能需要用查找替换功能把整个文档翻一遍，还容易改错。如果我们一开始就定义了 `\E{X}`，那么到时候只需要在导言区改一行代码，全篇的样式就会瞬间统一。**这其实就是解耦——把“内容”和“格式”分开。**

### 3. 强迫症的救星：搞定那些烦人的排版细节
LaTeX 虽然强大，但默认的一些设定并不完美。比如微积分里的微分符号“d”，按照规范它应该是直立体（upright），而不是默认的斜体 $d$。又比如求最大值时的 $\arg\max$，如果直接写 `arg \max`，它们之间的间距和下标的位置通常会很别扭。快捷键能帮我们把这些排版规范封装起来，调用时完全不需要再操心细节。

---

## 我的`commands.tex`核心用法解析

下面我挑出我的 `commands.tex` 中一些比较有代表性的部分，和大家分享一下具体的实现逻辑。特别是对于一些带有可选参数的复杂用法，一旦掌握，你会发现新世界的大门被打开了。

### 1. 极简主义：能省则省的基础替换

最基础的用法就是单纯的字符替换。比如环境的缩写和常用符号：

```latex
% 环境缩写
\newcommand{\ba}{\begin{aligned}}
\newcommand{\ea}{\end{aligned}}

% 希腊字母与常用集合
\newcommand{\RR}{\mathbb{R}}
\newcommand{\ve}{\varepsilon}
```

这里值得一提的是 `\renewcommand`。LaTeX 原本已经定义了很多命令，比如 `\l` 是用来打出波兰语字母 ł 的，`\Re` 默认是有点古典的哥特体 $\Re$。如果你确信自己这辈子都不会在经济学笔记里用到波兰语，也不喜欢那个古典的实部符号，那就果断覆盖掉它们：

```latex
\renewcommand{\l}{\lambda}                % 覆盖波兰语 ł
\renewcommand{\Re}{\operatorname{Re}}     % 改用现代的罗马体 Re
```

### 2. 自动伸缩的括号：告别排版刺客

遇到分式或者大矩阵时，普通的左右括号 $()$ 会显得极度不协调，我们需要用 `\left(` 和 `\right)` 来让括号自动匹配内部内容的高度。但这两个词敲起来极其费劲，我们可以这样封装：

```latex
\newcommand{\pr}[1]{\left(#1\right)}                  % 圆括号
\newcommand{\br}[1]{\left[#1\right]}                  % 方括号
\renewcommand{\brace}[1]{\left\{#1\right\}}           % 大括号
\newcommand{\abs}[1]{\left|#1\right|}                 % 绝对值
```

这里的 `[1]` 表示这个命令接收 **1个参数**。调用时只需要写 `\pr{\frac{1}{2}}`，LaTeX 就会把它展开成 `\left(\frac{1}{2}\right)`，完美生成自适应大小的 $\left(\frac{1}{2}\right)$。

### 3. 进阶魔法：带有默认值的可选参数

这是我觉得最优雅的一部分！`\newcommand` 其实支持设置“可选参数”（用方括号传入）。
它的语法是：`\newcommand{\命令名}[参数个数][第一个参数的默认值]{具体的定义}`。

**案例 A：范数（Norm）**
范数一般有 1-范数、2-范数、无穷范数等。我们可以这样定义：
```latex
\newcommand{\norm}[2][1]{\|{#2}\|_{#1}}
```
这里 `[2]` 表示共有 2 个参数，`[1]` 表示**第一个参数是可选的，且默认值为 1**。
- 如果我正常输入 `\norm{x}`，它等价于第一个参数缺省（采用默认值 1），第二个参数传入 $x$，最终渲染出 $\|x\|_1$。
- 如果我想表达 2-范数，我只需要显式给出第一个参数：`\norm[2]{x}`，就能得到 $\|x\|_2$。
- 想表达无穷范数：`\norm[\infty]{x}`，得到 $\|x\|_\infty$。

**案例 B：求和符号的极致偷懒**
在统计或宏观笔记里，连加符号 $\sum_{i=1}^n$ 出现频率极高。
```latex
\newcommand{\add}[1][i]{\sum_{#1 = 1}^n}
```
- 直接敲 `\add`，默认用 $i$ 做指标，得到 $\sum_{i = 1}^n$。
- 如果遇到双重求和，内部那一层换个指标 $j$，只需要敲 `\add[j]`，就会变成 $\sum_{j = 1}^n$。

**案例 C：期望与方差**
同理，我们经常遇到带下标的期望（比如对某个分布 $F$ 求期望）。
```latex
\newcommand{\E}[2][]{\mathbb{E}_{#1}\!\pr{#2}}
```
- 不带下标：`\E{X}` $\rightarrow \mathbb{E}(X)$
- 带特定分布下标：`\E[\theta]{X}` $\rightarrow \mathbb{E}_\theta(X)$

*(注：这里的 `\!` 是一个小小的负间距，用来微调 $\mathbb{E}$ 和括号之间的距离，这也属于一点强迫症的修饰。)*

### 4. 算子（Operators）的正规化

对于 `plim`、`argmax` 这种数学算子，如果直接当成普通文本敲，前后间距会很丑，而且不能像 `\lim` 那样把下标放在正下方。我们需要借助 `amsmath` 宏包提供的 `\DeclareMathOperator`：

```latex
\DeclareMathOperator*{\argmax}{arg\,max}
\DeclareMathOperator{\plim}{plim}
```
带星号的 `\DeclareMathOperator*` 意味着它可以在独立公式环境中像 $\max$ 或 $\sum$ 一样，把上下标写在正上方和正下方。

### 5. 给自己留点余地：草稿与 TODO 模式

做学术往往是一个不断推翻再重来的过程。笔记里经常会有一些不确定、待补充的地方。为了不让这些内容混杂在正文里难以寻找，我定义了一个 Draft 开关：

```latex
\newif\ifdraft
\drafttrue   % 设置为 \draftfalse 即可隐藏所有 TODO

\newcommand{\todo}[1]{%
  \ifdraft{\textcolor{red}{\textbf{[TODO: #1]}}}{}\fi
}
```
`\newif\ifdraft` 定义了一个布尔变量。当你处于编写阶段时，保持 `\drafttrue`，文中的 `\todo{查阅某某文献}` 就会变成刺眼的红色粗体警告你。当你准备导出最终版（或者给导师看）时，只需要把上面那行改成 `\draftfalse`，全文所有的 TODO 标记就会像魔法一样瞬间消失，一点痕迹都不留。

---

## 结语

我的 `commands.tex` 就是这样一点点积累起来的。它就像是一个不断在进化的外脑，记录着我在不同阶段对于排版、对于效率，甚至对于学科逻辑的理解。

刚来留学时，我总觉得自己在奔走于各种繁杂的“短期目标”之中，甚至会因为一个排版错误内耗半天。但后来我发现，**获得自洽的密码之一，就是把那些能够标准化的东西交给机器和规则，把最宝贵的注意力留给真正的思考。**

希望这份笔记能给你一些启发，让你也能早日脱离枯燥的重复劳动，搭建出最契合你思维习惯的快捷键体系。去享受那种在键盘上运笔如飞的感觉吧！
