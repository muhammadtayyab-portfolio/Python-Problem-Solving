student_marks = input("Please enter student marks saprated by space : ").split()
max_num = int(student_marks[0])
for i in student_marks:
    if int(i) > max_num:
        max_num = int(i)

print(f"The highest score in the class is: {max_num}")