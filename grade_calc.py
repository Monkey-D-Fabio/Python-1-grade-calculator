nbr_lab_problems = input("Enter the number of labs completed: ")
nbr_quizzes = input("Enter the number of quizzes completed: ")grade_assignment_1 = input("Enter grade for Assignment 1: ")
grade_assignment_2 = input("Enter grade for Assignment 2: ") 
grade_assignment_3 = input("Enter grade for Assignment 3: ") 
grade_assignment_4 = input("Enter grade for Assignment 4: ") 
grade_midterm_1 = input("Enter grade for Midterm 1: ") 
grade_midterm_2 = input("Enter grade for Midterm 2: ")
grade_final = input("Enter grade for Final Exam: ")
grade_midterm_final = input("Enter grade for Midterms and Final Preparation: ")

# Calculations Labs & Quizzes 

if nbr_lab_problems > 6:
    lab_weight = 20
else:
    lab_weight = nbr_lab_problems * (10/3) 

if nbr_quizzes > 6:
    quizzes_weight = 20
else:
    quizzes_weight = nbr_quizzes * (10/3)

# Calc. Assignments & Midterms

assigments_weight = (grade_assignment_1 + grade_assignment_2 +grade_assignment_3 + grade_assignment_4) / 4 * 0.16 
midterms_weight = (grade_midterm_1 + grade_midterm_2) / 2  
