本程序的目的是为了方便将 Optech newsletter 的中文译本生成出适配 Optech Github 库和 PrimitivesLane 的不同版本。

两者需要将超链接和一些网页表现写为不同的形式。

本程序的主要思想是：

- 为了兼容 Optech Github，我们使用它库中的源文件摘出其特殊的形式。并为每一个引用形成特殊的标记
- 在翻译之时，仅留下特殊的标记，在生成最后的文档时，将这些标题替换成有意义的超链接文字
- 超链接文字的翻译在专门的文件内补充
- 最后，根据译本中的标记，将标记替换为被翻译的超链接文字，得到兼容 Optech 的版本
- 根据 Optech 原文件底部的明文参考，辨别哪些超链接需要转写并附加明文链接，得到兼容 PrimitivesLane 的版本

程序使用步骤：

1. 在 Optech Github 库内找到要翻译的原文件，复制到程序同文件夹内保存
2. 使用  ` Main-function.py ` 执行指令 1，生成 final_form.md、links_and_table.md、references.md 三个文件
3. 在 final_form.md 文件内输入中文翻译。对于所有超链接文字，仅留下 “%#n%#” 形式的标记，其余都删去
4. 在 links_and_table.md 文件内按行提供被超链接的文字的翻译。行内文字用逗号分割，每行的第二段文字就是被超链接的文字；翻译在句末直接输入；如无必要翻译，可不输入
5. 复制 Optech 网站对应页面的文档（其中包含了最终的 html 信息），粘贴到兼容 markdown 的编辑器内（作者使用 Typora），保存到文件夹内。注意，不应复制 “PR 审核俱乐部” 的特殊格式部分
6. 运行 ` Main-function.py ` 执行指令 2，得到最终的版本，分别为 optech_comptabile.md 和 primitives_comptabile.md

文件夹内的 #201.md、#201-web.md 和 #201-trans-test.md 是用于演示的。第一个是 optech 的原文（用于指令 1），第二个是其网页版（用于指令 2），第三个是翻译，可复制到 final_form.md 内方便执行指令 2。

### 2022-05-21 Update

- 减少了微量的重复计算
- 使之能处理 Optech Newslatter 中的 “Bitcoin Stack Exchange 精选问答” 内的引用（ ` []() ` 格式）

### 2022-06-16 Update

- 增加了为加粗格式和“Bitcoin Stack Exchange 精选问答” 内的引用（ ` []() ` 格式）增加形如 “<!--eng-words-->” 的注释的功能，这些注释将为 Optech 程序的自动处理提供帮助
- 尚不能为 “Bitcoin Core PR 审核俱乐部” 栏目自动添加注释（此前也不能为 PrimitivesLane 版本自动转换其中的内容）。需要考虑专门写一个程序来处理
- 增加了一个 “easy-note-generator” 程序，输入英文字符串即可生成需要添加的注释，是对上一条所述局限性的缓兵之计

### 2022-09-06 Update

- 增加了对 ` [XXX][] ` 形式的引用的处理：如果 ` XXX ` 具有翻译，则将 ` XXX ` 放入后面的方括号中，以保证原文文末的超链信息依然有效

### 2022-09-24 Update

- 修复代码，真正完成 2022-09-06 更新中的目标