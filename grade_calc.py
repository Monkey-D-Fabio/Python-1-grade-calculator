# Input for different grades

nbr_lab_problems = int(input("Enter the number of labs completed: "))
nbr_quizzes = int(input("Enter the number of quizzes completed: "))
grade_assignment_1 = int(input("Enter grade for Assignment 1: "))
grade_assignment_2 = int(input("Enter grade for Assignment 2: "))
grade_assignment_3 = int(input("Enter grade for Assignment 3: ")) 
grade_assignment_4 = int(input("Enter grade for Assignment 4: ")) 
grade_midterm_1 = int(input("Enter grade for Midterm 1: ")) 
grade_midterm_2 = int(input("Enter grade for Midterm 2: "))
grade_final = int(input("Enter grade for Final Exam: "))
grade_midterm_final = int(input("Enter grade for Midterms and Final Preparation: "))

# Weight Labs & Quizzes 

if nbr_lab_problems > 6:
    lab_weight = 20
else:
    lab_weight = nbr_lab_problems * (10/3) 

if nbr_quizzes > 6:
    quizzes_weight = 15
else:
    quizzes_weight = nbr_quizzes * (10/3)

# Weight Assignments & Midterms

weight_assignments = 0.04 * (grade_assignment_1 + grade_assignment_2 +grade_assignment_3 + grade_assignment_4)
weight_midterms = 0.125 * (grade_midterm_1 + grade_midterm_2) 

# Weight Final & Midterm and Final prep.

weight_final = grade_final * 0.18
weight_midterm_final = grade_midterm_final * 0.06

# Total grade

total_grade = round(weight_midterm_final + weight_final + weight_midterms + weight_assignments + quizzes_weight + lab_weight, 2)

# Total grade output

print(f"Your grade is: {total_grade}")

