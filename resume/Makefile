RESUMES = resume-zh_CN.pdf resume-en.pdf

all: $(RESUMES)

zh_CN: resume-zh_CN.pdf
en: resume-en.pdf

%.pdf: %.tex resume.cls
	xelatex -interaction=nonstopmode $<

# Copy the freshly built PDFs to where the homepage links to them.
publish: $(RESUMES)
	cp resume-en.pdf ../assets/cv/Yiming_Liu_CV_en.pdf
	cp resume-zh_CN.pdf ../assets/cv/Yiming_Liu_CV_zh.pdf

clean:
	rm -f *.aux *.log *.out *.synctex.gz

.PHONY: all zh_CN en publish clean
