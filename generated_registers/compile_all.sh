#!/bin/bash
echo "Compiling LaTeX files..."
cd "$(dirname "$0")"
echo ""

echo "Compiling CS101 (standard template)..."
pdflatex -interaction=nonstopmode "CS101_register.tex"
if [ -f "CS101_register.pdf" ]; then
  echo "  Success!"
else
  echo "  Failed - check .log file"
fi
echo ""
echo "Compiling CS102 (standard template)..."
pdflatex -interaction=nonstopmode "CS102_register.tex"
if [ -f "CS102_register.pdf" ]; then
  echo "  Success!"
else
  echo "  Failed - check .log file"
fi
echo ""
echo "Compiling CS103 (standard template)..."
pdflatex -interaction=nonstopmode "CS103_register.tex"
if [ -f "CS103_register.pdf" ]; then
  echo "  Success!"
else
  echo "  Failed - check .log file"
fi
echo ""
echo "Compiling CS104 (standard template)..."
pdflatex -interaction=nonstopmode "CS104_register.tex"
if [ -f "CS104_register.pdf" ]; then
  echo "  Success!"
else
  echo "  Failed - check .log file"
fi
echo ""
echo "Compiling CS105 (standard template)..."
pdflatex -interaction=nonstopmode "CS105_register.tex"
if [ -f "CS105_register.pdf" ]; then
  echo "  Success!"
else
  echo "  Failed - check .log file"
fi
echo ""
echo "Compiling CS106 (standard template)..."
pdflatex -interaction=nonstopmode "CS106_register.tex"
if [ -f "CS106_register.pdf" ]; then
  echo "  Success!"
else
  echo "  Failed - check .log file"
fi
echo ""
echo "Compiling CS107 (standard template)..."
pdflatex -interaction=nonstopmode "CS107_register.tex"
if [ -f "CS107_register.pdf" ]; then
  echo "  Success!"
else
  echo "  Failed - check .log file"
fi
echo ""
echo "All compilations attempted!"
rm -rf *.aux *.log