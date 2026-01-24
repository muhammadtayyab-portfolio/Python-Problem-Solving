# Ek number input lo aur check karo agar even digit ka sum odd hai, ya nahi.

num = input("Enter the number stream : ")
sum = 0

for i in num:
    if int(i) % 2 == 0:
        sum += int(i)

if sum % 2 == 0:
    print("Ther sum is Even ",sum)
else:
    print("Ther sum is odd ",sum)
