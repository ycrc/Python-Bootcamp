all: python.pdf

python.pdf: python.tex
	pdflatex python.tex
	pdflatex python.tex

clean:
	-@/bin/rm -f *.aux *.log *.out *.nav *.toc *.vrb *.snm

realclean: clean
	-@/bin/rm -f *.pdf
