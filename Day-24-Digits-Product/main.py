# User se number input lo aur digits ka product print karo.

num = input("Please enter numbers : ")
result = 1
for i in num:
    result *= int(i)

print(result)
