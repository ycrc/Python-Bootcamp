all: data_analysis.pdf anaconda.pdf

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
	-@/bin/rm -rf Ex2dir 
	-@/bin/rm -f myfile.fastq.gz
	cp -r Ex2dir.copy Ex2dir

realclean: clean
	-@/bin/rm -f *.pdf
