all: toslides 

toslides:
	jupyter nbconvert PythonNotebook.ipynb --to slides --post serve

clean:
	/bin/rm -f *.aux *.log *.out *.nav *.toc *.vrb *.snm
	/bin/rm -rf Ex2dir 
	/bin/rm -f myfile.fastq.gz
	cp -r Ex2dir.copy Ex2dir

realclean: clean
	-@/bin/rm -f *.pdf
