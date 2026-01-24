# Ek program jo user se 3 numbers le aur largest number print kare, without max().

num1 = int(input("Enter the 1st number : "))
num2 = int(input("Enter the 2st number : "))
num3 = int(input("Enter the 3st number : "))
large = num1
if num2 > large:
    large = num2
if num3 > large:
    large = num3
else:
    print("Numbers are equal")

print("max number is = ",large)