# User se string input lo aur character count ke hisaab se descending print karo.

s = input("please enter anything : ")
p = ""
for i in s:
    if i not in p:
        print(i," : ",s.count(i))
        p += i