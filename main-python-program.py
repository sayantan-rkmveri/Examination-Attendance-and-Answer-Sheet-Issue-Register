import pandas as pd
import os
from datetime import datetime

def escape_latex(text):
    """Simple LaTeX escaping function"""
    if pd.isna(text):
        return ""
    
    text = str(text)
    
    # Replace special characters
    replacements = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
    }
    
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    
    return text

def create_latex_document(course_info, students_df, course_code):
    """Create LaTeX document for a specific course"""
    
    # Filter students enrolled in this course
    if course_code in students_df.columns:
        enrolled_students = students_df[
            students_df[course_code].notna() & 
            (students_df[course_code].astype(str).str.strip() != '')
        ].copy()
        
        # Try to filter numeric values >= 1
        try:
            numeric_values = pd.to_numeric(enrolled_students[course_code], errors='coerce')
            enrolled_students = enrolled_students[numeric_values >= 1]
        except:
            pass  # Keep all non-empty entries if conversion fails
    else:
        enrolled_students = pd.DataFrame()
    
    # Get program from first enrolled student
    program = "MSc Program"
    if not enrolled_students.empty:
        program = enrolled_students['Program'].iloc[0]
    
    # Escape LaTeX special characters
    course_name = escape_latex(course_info['Course_Name'])
    instructor = escape_latex(course_info['Instructor'])
    exam_type = escape_latex(course_info['Exam_type']) if pd.notna(course_info['Exam_type']) else ""
    exam_date = escape_latex(course_info['Exam_Date']) if pd.notna(course_info['Exam_Date']) else ""
    semester = escape_latex(course_info['Semester']) if pd.notna(course_info['Semester']) else ""
    session = escape_latex(course_info['Session']) if pd.notna(course_info['Session']) else ""
    
    # Handle empty fields - create LaTeX spacing commands
    exam_type_field = exam_type if exam_type else r'\hspace{2cm}'
    semester_field = semester if semester else r'\hspace{1cm}'
    session_field = session if session else r'\hspace{4cm}'
    exam_date_field = exam_date if exam_date else r'\hspace{2cm}'
    
    # Start building LaTeX document
    latex_parts = []
    
    # Document header with standard packages
    latex_parts.extend([
        r"\documentclass[a4paper]{article}",
        r"\usepackage[utf8]{inputenc}",
        r"\usepackage{amsmath, amsfonts, amssymb}",
        r"\usepackage[margin=1cm]{geometry}",
        r"\usepackage{longtable}",
        r"\usepackage{tabularx}",
        r"\usepackage{tabularray}",
        r"\usepackage{array}",
        r"\usepackage{booktabs}",
        r"",
        r"\thispagestyle{empty}",
        r"",
        r"\begin{document}",
        r"\begin{center}",
        r"\Large\textbf{Ramakrishna Mission Vivekananda Educational and Research Institute}\\",
        rf"\large Programme: {program}\\",
        rf"\large Course Name: {course_name} ({course_info['Course_Code']})\\",
        rf"\large Instructor: {instructor}",
        r"",
        r"\begin{tabular}{llllllll}",
        rf"Exam: & {exam_type_field} & Semester: & {semester_field} & Session: & {session_field} & Date: & {exam_date_field}\\",
        r"\end{tabular}",
        r"\vspace{-1em}",
        r"\large",
        r"\begin{longtblr}[",
        r"caption = {\textbf{\underline{Attendance and Answer Script Issue Register}}},",
        r"]{",
        r"width = \textwidth,",
        r"colspec = {%",
        r">{\centering\arraybackslash}p{0.5cm}",
        r">{\raggedright\arraybackslash}p{4.75cm}",
        r">{\centering\arraybackslash}p{1.8cm}",
        r">{\centering\arraybackslash}p{3cm}",
        r">{\centering\arraybackslash}p{2cm}",
        r">{\centering\arraybackslash}X",
        r"},",
        r"rowhead = 1,",
        r"row{1} = {font=\bfseries},",
        r"row{2-Z} = {ht=7mm},",
        r"hline{1,Z} = {1pt},",
        r"hline{2} = {0.8pt},",
        r"vlines,",
        r"rows = {m},",
        r"}",
        r"\textbf{Sl No} & \textbf{Name} & \textbf{ID} & \textbf{Answer Script Booklet No} & \textbf{Loose Sheet No} & \textbf{Signature with Date} \\",
    ])
    
    # Add student rows
    if not enrolled_students.empty:
        enrolled_students = enrolled_students.sort_values('Sl')
        
        for idx, (_, student) in enumerate(enrolled_students.iterrows(), 1):
            student_name = escape_latex(student['Name'])
            student_id = escape_latex(str(student['ID']))
            latex_parts.append(rf"{idx} & {student_name} & {student_id} & & & \\ \hline")
    else:
        latex_parts.append(r"\multicolumn{6}{|c|}{\textbf{No students enrolled in this course}} \\ \hline")
    
    # Close the table and document
    latex_parts.extend([
        r"\end{longtable}",
        r"\end{center}",
        r"\vspace{0.25cm}",
        r"\textbf{Invigilators' Signature(s):} \underline{\hspace{14cm}}",
        r"",
        r"\end{document}"
    ])
    
    return "\n".join(latex_parts)

def main():
    """Main function to generate LaTeX registers"""
    
    # Read CSV files
    try:
        courses_df = pd.read_csv("courses-db.csv")
        students_df = pd.read_csv("student-db.csv")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please make sure 'courses-db.csv' and 'student-db.csv' are in the same directory.")
        return
    
    # Create output directory
    output_dir = "generated_registers"
    os.makedirs(output_dir, exist_ok=True)
    
    print("=" * 60)
    print("RKMVERI - Answer Script Register Generator")
    print("=" * 60)
    print(f"Found {len(courses_df)} courses")
    print(f"Found {len(students_df)} students")
    print()

    # Always use standard template now
    use_simple = False
    
    # Generate LaTeX file for each course
    generated_files = []
    
    for idx, course in courses_df.iterrows():
        course_code = course['Course_Code']
        course_name = course['Course_Name']
        
        print(f"\nGenerating register for: {course_code} - {course_name}")
        
        # Always use standard template
        latex_content = create_latex_document(course, students_df, course_code)
        template_type = "standard"
        
        # Save to file
        filename = f"{course_code}_register.tex"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(latex_content)
        
        generated_files.append((course_code, filepath, template_type))
        
        # Count enrolled students
        if course_code in students_df.columns:
            enrolled_count = students_df[
                students_df[course_code].notna() & 
                (students_df[course_code].astype(str).str.strip() != '')
            ].shape[0]
            print(f"  → {enrolled_count} students enrolled")
        else:
            print(f"  → 0 students enrolled")
    
    print("\n" + "=" * 60)
    print("GENERATION COMPLETE!")
    print("=" * 60)
    
    # Create compilation instructions
    compile_bat = """@echo off
echo Compiling LaTeX files...
cd /d "%~dp0"
echo.

"""
    
    compile_sh = """#!/bin/bash
echo "Compiling LaTeX files..."
cd "$(dirname "$0")"
echo ""

"""
    
    # Test compilation with pdflatex
    if generated_files:
        first_course_code, first_filepath, template_type = generated_files[0]
        
        print(f"\nTesting compilation with {first_course_code}...")
        test_file = os.path.join(output_dir, "test_compile.bat" if os.name == 'nt' else "test_compile.sh")
        
        with open(test_file, 'w') as f:
            if os.name == 'nt':
                f.write(f'@echo off\ncd /d "%~dp0"\npdflatex -interaction=nonstopmode "{first_course_code}_register.tex"\nif exist "{first_course_code}_register.pdf" (\n  echo Success! PDF created: {first_course_code}_register.pdf\n  pause\n) else (\n  echo Compilation failed. Check {first_course_code}_register.log for errors.\n  pause\n)')
            else:
                f.write(f'#!/bin/bash\ncd "$(dirname "$0")"\npdflatex -interaction=nonstopmode "{first_course_code}_register.tex"\nif [ -f "{first_course_code}_register.pdf" ]; then\n  echo "Success! PDF created: {first_course_code}_register.pdf"\nelse\n  echo "Compilation failed. Check {first_course_code}_register.log for errors."\nfi')
        
        if os.name != 'nt':
            os.chmod(test_file, 0o755)
        
        print(f"Test compilation script created: {test_file}")
    
    # Create main compilation script
    for course_code, filepath, template_type in generated_files:
        filename = os.path.basename(filepath)
        compile_bat += f'echo Compiling {course_code} ({template_type} template)...\npdflatex -interaction=nonstopmode "{filename}"\nif exist "{course_code}_register.pdf" (\n  echo   Success!\n) else (\n  echo   Failed - check .log file\n)\necho.\n'
        compile_sh += f'echo "Compiling {course_code} ({template_type} template)..."\npdflatex -interaction=nonstopmode "{filename}"\nif [ -f "{course_code}_register.pdf" ]; then\n  echo "  Success!"\nelse\n  echo "  Failed - check .log file"\nfi\necho ""\n'
    
    compile_bat += 'echo All compilations attempted!\npause'
    compile_sh += 'echo "All compilations attempted!"\n'
    compile_sh += 'rm -rf *.aux *.log'
    
    # Save scripts
    with open(os.path.join(output_dir, "compile_all.bat"), 'w') as f:
        f.write(compile_bat)
    
    with open(os.path.join(output_dir, "compile_all.sh"), 'w') as f:
        f.write(compile_sh)
    
    try:
        os.chmod(os.path.join(output_dir, "compile_all.sh"), 0o755)
    except:
        pass
    
    # README
    readme_content = f"""# Generated Answer Script Registers
# ABC University
# Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Template used: Standard

This folder contains LaTeX files for answer script issue registers.

## Files Generated:
{chr(10).join([f"- {code} (standard): {os.path.basename(path)}" for code, path, ttype in generated_files])}

## Required LaTeX Packages:
- longtable
- array
- booktabs
- tabularray

## To Compile:
Run test script, then compile_all script.
"""
    
    with open(os.path.join(output_dir, "README.txt"), 'w') as f:
        f.write(readme_content)
    
    print(f"\nGenerated {len(generated_files)} LaTeX files in '{output_dir}' folder.")

if __name__ == "__main__":
    main()

