TEX=main.tex
PDF=main.pdf

.PHONY: all clean

all: $(PDF)

$(PDF): $(TEX)
	pdflatex $(TEX)
	pdflatex $(TEX)

clean:
	rm -f *.aux *.log *.out *.toc *.pdf
