# LaTeX表格生成模板

> 使用 tabularray 包生成现代表格。

---

## 基础表

```latex
% 在导言区添加
\usepackage{tabularray}
\usepackage{siunitx}

% 基本表格
\begin{table}[H]
\centering
\caption{表格标题。}
\label{tab:example}
\begin{tblr}{
  colspec = {l S[table-format=3.0] S[table-format=2.1]},
  row{1} = {font=\bfseries},
  hline{1,Z} = {1pt},
  hline{2} = {0.5pt},
}
  催化剂 & 温度 (°C) & 转化率 (\%) \\
  Catalyst A & 250 & 95.2 \\
  Catalyst B & 250 & 88.7 \\
  Catalyst C & 300 & 92.4 \\
\end{tblr}
\end{table}
```

## 多行表头

```latex
\begin{tblr}{
  colspec = {l *{3}{c}},
  row{1-2} = {font=\bfseries},
  cell{1}{2-4} = {c}{halign=c},
  hline{1,Z} = {1pt},
  hline{2,3} = {0.5pt},
}
  & \SetCell[c=3]{c} 反应条件 \\
  催化剂 & 温度 (°C) & 空速 (h⁻¹) & 转化率 (\%) \\
  A & 250 & 30,000 & 95.2 \\
  B & 300 & 30,000 & 92.4 \\
\end{tblr}
```

## 注意事项

1. 表格在LaTeX中应使用 `\label{tab:xxx}` 和 `Table~\ref{tab:xxx}` 引用
2. Caption放在表格上方（这是学术惯例，与图的caption在下方不同）
3. 数值对齐：整数用 `S[table-format=3.0]`，1位小数用 `S[table-format=2.1]`
