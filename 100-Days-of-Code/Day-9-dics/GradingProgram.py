student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}



    

#TODO-2: Write your code below to add the grades to student_grades.👇
#print(student_scores)
for students in student_scores:
    if student_scores[students] <= 70 :
        student_grades[students] = "Fail"
    elif student_scores[students] <= 80:
        student_grades[students] = "Acceptable"
    elif student_scores[students] <= 90:
        student_grades[students] = "Exceeds Expectations"
    elif student_scores[students] <= 100:
        student_grades[students] = "Outstanding"


# 🚨 Don't change the code below 👇
#print(student_grades)
print(student_grades)