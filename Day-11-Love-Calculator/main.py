name_1 = input("please enter the name-1 : ").lower()
name_2 = input("please enter the name-2 : ").lower()
add_name = name_1 + name_2
side_1 = 0
side_2 = 0
for i in add_name:
    if i in ["t","r","u","e"]:
        side_1 += 1
    if i in ["l","o","v","e"]:
        side_2 += 1

total = str(side_1) + str(side_2)

if 10 > int(total) > 90:
    print(f"Your score is {total}, you go together like coke and mentos .")
elif 40 <= int(total) <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")