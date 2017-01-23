all: python.pdf data_analysis.pdf anaconda.pdf

python.pdf: python.tex
	pdflatex python.tex
	pdflatex python.tex
	-evince python.pdf

data_analysis.pdf: data_analysis.tex
	pdflatex data_analysis.tex
	pdflatex data_analysis.tex

anaconda.pdf: anaconda.tex
	pdflatex anaconda.tex
	pdflatex anaconda.tex

clean:
	-@/bin/rm -f *.aux *.log *.out *.nav *.toc *.vrb *.snm

realclean: clean
	-@/bin/rm -f *.pdf
