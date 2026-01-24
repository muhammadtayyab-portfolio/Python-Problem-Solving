# String input lo aur print karo vowels ki position.

str = input("Please enter any string : ")
cout = 0
while cout < len(str):
    if str[cout] == "a" or str[cout] == "A":
        print(str[cout],"at postion ",cout)
    elif str[cout] == "e" or str[cout] == "E":
        print(str[cout],"at postion ",cout)
    elif str[cout] == "i" or str[cout] == "I":
        print(str[cout],"at postion ",cout)
    elif str[cout] == "o" or str[cout] == "O":
        print(str[cout],"at postion ",cout)
    elif str[cout] == "u" or str[cout] == "U":
        print(str[cout],"at postion ",cout)
    cout += 1