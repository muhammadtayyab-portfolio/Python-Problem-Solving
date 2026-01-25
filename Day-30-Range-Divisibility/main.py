# User se 2 numbers input lo aur numbers ke beech ke all numbers divisible by either print karo.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

start = min(num1, num2)
end = max(num1, num2)

print("Numbers divisible by either", num1, "or", num2, "are:")

for i in range(start, end + 1):
    if i % num1 == 0 or i % num2 == 0:
        print(i, end=" ")
