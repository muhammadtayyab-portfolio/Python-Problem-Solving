# Ek string input lo aur palindrome ignoring case check karo.

str = input("Please enter palindrome : ")
rev_str = ""
count = len(str)-1
while count >= 0:
    rev_str += str[count]
    count -=1

if str == rev_str:
    print("Palindrome")
else:
    print("Not a palindrome")
