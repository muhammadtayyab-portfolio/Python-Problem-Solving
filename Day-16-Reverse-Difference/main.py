# Ek number input lo aur print karo reverse number aur original number ka difference.

num = int(input("Please enter the number : "))
or_num = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10 
     


print('orignal = ' ,or_num )
print('reverse = ' ,rev )
print("Difference =", or_num - rev)