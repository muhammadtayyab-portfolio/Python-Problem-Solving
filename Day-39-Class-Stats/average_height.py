input_heights = input("Enter student heights separated by spaces: ").split()
student_heights = []
for height in input_heights:
    student_heights.append(int(height))

total_height = 0
number_of_students = 0

for height in student_heights:
    total_height += height
    number_of_students += 1

ave_height = round(total_height / number_of_students)

print(f"Average height: {ave_height}")
