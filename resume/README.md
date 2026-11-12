# 简历

刘祎铭的中文简历源码。模板来自 [billryan/resume](https://github.com/billryan/resume)（MIT，见 `LICENSE`），
中文字体和排版配置已随仓库提交，任何机器上编译结果一致。

## 编译

```sh
make zh_CN        # 或者： xelatex resume-zh_CN.tex
```

需要 XeLaTeX（TeX Live / MacTeX 均可）。产物是 `resume-zh_CN.pdf`。

更新后记得把 PDF 同步到主页的下载位置：

```sh
cp resume-zh_CN.pdf ../assets/cv/Yiming_Liu_CV.pdf
```

## 文件

| 文件 | 说明 |
|---|---|
| `resume-zh_CN.tex` | 简历正文，改这个 |
| `resume.cls` | 模板类：版式、`\datedsubsection` 等命令 |
| `zh_CN-Adobefonts_external.sty` | 中文字体配置，指向 `fonts/zh_CN-Adobe/` |
| `photo.jpg` | 证件照 |
| `fonts/` | 正文西文字体、FontAwesome、Adobe 中文字体 |

正文开头覆盖了模板的页边距和章节间距，用来把内容压在一页内；加内容超页时优先精简文字，
其次再调 `\geometry` 和 `\titlespacing`。
