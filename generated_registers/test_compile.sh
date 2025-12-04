#!/bin/bash
cd "$(dirname "$0")"
pdflatex -interaction=nonstopmode "CS101_register.tex"
if [ -f "CS101_register.pdf" ]; then
  echo "Success! PDF created: CS101_register.pdf"
else
  echo "Compilation failed. Check CS101_register.log for errors."
fi