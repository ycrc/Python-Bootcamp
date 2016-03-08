all: python.pdf numpy.pdf

python.pdf: python.tex
	pdflatex python.tex
	pdflatex python.tex
	-xpdf -g 1200x800 -z page python.pdf

numpy.pdf: numpy.tex
	pdflatex numpy.tex
	pdflatex numpy.tex

clean:
	-@/bin/rm -f *.aux *.log *.out *.nav *.toc *.vrb *.snm

realclean: clean
	-@/bin/rm -f *.pdf
