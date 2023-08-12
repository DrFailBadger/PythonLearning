# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆



#Write your code below this row 👇
student = 0
heightsSum = 0
for i in student_heights:
    heightsSum += i
    student += 1
Average = round(heightsSum / student)

print(Average)


# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

max = 0
min = 1000000000000000000000000000
for i in student_scores:
    if i > max:
        max = i
    if i < min:
        min = i

print(f"The highest score in the class is : {max}")
print(f"The Lowest score in the class is : {min}")



