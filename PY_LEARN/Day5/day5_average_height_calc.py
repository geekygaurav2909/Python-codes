# Input a Python list of student heights
student_heights = input().split()
total_height = 0
total_student = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

#   total_height += student_heights[n]
#   total_student = n + 1
#   print(f"total_student: {total_student} \nN count: {n}")

# average = round(total_height / total_student)

# print(f"total height = {total_height}")
# print(f"number of students = {total_student}")
# print(f"average height = {average}")

#Alternate method
  
st_height = 0
for height in student_heights:
  st_height += height

print(f"total height = {st_height}")

studentCount = 0
for num_students in student_heights:
  studentCount += 1

print(f"number of students = {studentCount}")

averageFinder = round(st_height/studentCount)

print(f"average height : {averageFinder}")


