# User se number input lo aur digits ko alternate multiply/add karke final result nikaalo.
s = input("Please enter the number: ")
count = 0
add = 0

while count < len(s):
    if count + 1 < len(s):
        add += int(s[count]) * int(s[count+1])
        count += 2
    else:
        add += int(s[count])
        count += 1

print("ans =", add)
