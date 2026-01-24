# User se 2 numbers le aur check karo agar unke sum ka square even hai ya odd.

num1 = int(input("Enter the number 1 : "))
num2 = int(input("Enter the number 2 : "))
sum_squr = (num1 + num2)**2
if sum_squr %2 == 0:
    print("sum ka square even hai : ", sum_squr)
else:
    print("sum ka square odd hai : ", sum_squr)

