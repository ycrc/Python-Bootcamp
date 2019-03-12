all: toslides 

html:   PythonNotebook.ipynb
	jupyter nbconvert --to slides PythonNotebook.ipynb --output-dir ./docs/ --reveal-prefix "https://cdn.jsdelivr.net/npm/reveal.js@3.6.0 "
	cp docs/PythonNotebook.slides.html docs/index.html

clean:
	/bin/rm -f *.aux *.log *.out *.nav *.toc *.vrb *.snm
	/bin/rm -rf Ex2dir 
	/bin/rm -f myfile.fastq.gz
	cp -r Ex2dir.copy Ex2dir

realclean: clean
	-@/bin/rm -f *.pdf
