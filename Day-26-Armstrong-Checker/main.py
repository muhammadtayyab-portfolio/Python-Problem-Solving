# Ek number input lo aur check karo agar wo Armstrong number hai ya nahi.
num = input("please enter the number : ")
total = 0
for i in num:
    total += int(i)**len(num)
if total == int(num):
    print("Armstrong number hai")
else:
    print("Armstrong number nahi hai")
