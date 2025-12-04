# _Examination Attendance and Answer Script Issure Register Generation using Python and Latex_

### Initially it is made for Linux OS.
- Python 3
- Texlive (for Latex)
- Libreoffice Calc or other office management application to open .csv file as excel sheet for better experience.

### Instructions
- For fresh PDF generate, delete `generated_registers` directory if previously created.
- Fill the _courses-db.csv_ file and _student-db.csv_ file with data. You may understand through column header.
- In the _student-db.csv_ file, the course code should be the column header after the 'Program' column header.
- A value of 1 or more indicates that the student is enrolled in the course, while 0 or a blank cell indicates that the student is not enrolled.
- In the _courses-db.csv_ file, the course codes will represent the the rows and the corresponding data should be filled through row wise horizontally arranged.
- Run the shell file _run.sh_ using 
    ``` bash
    sh run.sh
    ```
 -  _or_
    ``` bash
    sudo chmod +x run.sh
    ./run.sh
    ```
- Go to the `generated_registers` folder and see the PDFs......
- Or _You may run manually one by one. Like...._
    ``` bash
    python3 main-python-program.py
    cd generated_registers
    ```
- Inside the `generated_registers` directory
    ``` bash
    sh compile_all.sh
    ```
- All PDF files will be created....

