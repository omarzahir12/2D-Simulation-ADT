# Adapted from doxygen generated Makefile

LATEX_CMD=pdflatex

all: report.pdf

pdf: report.pdf

report.pdf: clean report.tex
	$(LATEX_CMD) report
	latex_count=8 ; \
	while egrep -s 'Rerun (LaTeX|to get cross-references right)' report.log && [ $$latex_count -gt 0 ] ;\
	    do \
	      echo "Rerunning latex...." ;\
	      $(LATEX_CMD) report ;\
	      latex_count=`expr $$latex_count - 1` ;\
	    done
	$(LATEX_CMD) report


clean:
	rm -f *.ps *.dvi *.aux *.toc *.idx *.ind *.ilg *.log *.out *.brf *.blg *.bbl report.pdf
