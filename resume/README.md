# 简历

刘祎铭的简历源码，中英文各一份。模板来自 [billryan/resume](https://github.com/billryan/resume)
（MIT，见 `LICENSE`），中文字体随仓库提交，任何机器上编译结果一致。

## 编译

```sh
make              # 两份都编译
make zh_CN        # 只编中文
make en           # 只编英文
make publish      # 编完并同步到主页的下载位置
```

需要 XeLaTeX（TeX Live / MacTeX 均可）。

## 文件

| 文件 | 说明 |
|---|---|
| `resume-zh_CN.tex` | 中文简历正文 |
| `resume-en.tex` | 英文简历正文，改一份时记得同步另一份 |
| `resume.cls` | 模板类：版式、`\datedsubsection` 等命令 |
| `zh_CN-Adobefonts_external.sty` | 中文字体配置，指向 `fonts/zh_CN-Adobe/` |
| `photo.jpg` | 证件照 |
| `fonts/` | 正文西文字体、FontAwesome、Adobe 中文字体 |

两份正文开头都覆盖了模板的页边距和章节间距，用来把内容压在一页内；加内容超页时优先精简
文字，其次再调 `\geometry` 和 `\titlespacing`。英文比中文占版面，所以它的间距更紧一档。
