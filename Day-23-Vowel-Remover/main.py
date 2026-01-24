# String input lo aur reverse me print karo, lekin vowels remove karke.

str = input("Please enter str : ")
str2 = ""
count = len(str)-1
while count >= 0:
    if str[count] not in ['a',"e","i","o","u","A",'E',"I","O","U"]:
        str2 += str[count]
    count -=1
print(str2)