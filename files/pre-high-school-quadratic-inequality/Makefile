Main.pdf: Main.tex theorems.tex commands.tex $(wildcard chapters/*.tex)
	latexmk -xelatex -interaction=nonstopmode Main.tex

clean:
	latexmk -C

.PHONY: clean
