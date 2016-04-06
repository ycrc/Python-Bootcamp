all: python.pdf numpy.pdf anaconda.pdf

python.pdf: python.tex
	pdflatex python.tex
	pdflatex python.tex
	#-xpdf -g 1200x800 -z page python.pdf
	evince python.pdf

numpy.pdf: numpy.tex
	pdflatex numpy.tex
	pdflatex numpy.tex

anaconda.pdf: anaconda.tex
	pdflatex anaconda.tex
	pdflatex anaconda.tex

clean:
	-@/bin/rm -f *.aux *.log *.out *.nav *.toc *.vrb *.snm

realclean: clean
	-@/bin/rm -f *.pdf
