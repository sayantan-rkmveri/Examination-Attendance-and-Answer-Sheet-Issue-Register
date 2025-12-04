@echo off
echo Compiling LaTeX files...
cd /d "%~dp0"
echo.

echo Compiling CS101 (standard template)...
pdflatex -interaction=nonstopmode "CS101_register.tex"
if exist "CS101_register.pdf" (
  echo   Success!
) else (
  echo   Failed - check .log file
)
echo.
echo Compiling CS102 (standard template)...
pdflatex -interaction=nonstopmode "CS102_register.tex"
if exist "CS102_register.pdf" (
  echo   Success!
) else (
  echo   Failed - check .log file
)
echo.
echo Compiling CS103 (standard template)...
pdflatex -interaction=nonstopmode "CS103_register.tex"
if exist "CS103_register.pdf" (
  echo   Success!
) else (
  echo   Failed - check .log file
)
echo.
echo Compiling CS104 (standard template)...
pdflatex -interaction=nonstopmode "CS104_register.tex"
if exist "CS104_register.pdf" (
  echo   Success!
) else (
  echo   Failed - check .log file
)
echo.
echo Compiling CS105 (standard template)...
pdflatex -interaction=nonstopmode "CS105_register.tex"
if exist "CS105_register.pdf" (
  echo   Success!
) else (
  echo   Failed - check .log file
)
echo.
echo Compiling CS106 (standard template)...
pdflatex -interaction=nonstopmode "CS106_register.tex"
if exist "CS106_register.pdf" (
  echo   Success!
) else (
  echo   Failed - check .log file
)
echo.
echo Compiling CS107 (standard template)...
pdflatex -interaction=nonstopmode "CS107_register.tex"
if exist "CS107_register.pdf" (
  echo   Success!
) else (
  echo   Failed - check .log file
)
echo.
echo All compilations attempted!
pause