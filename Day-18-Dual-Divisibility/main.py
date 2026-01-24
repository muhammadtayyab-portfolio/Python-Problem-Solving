# 1 se n tak numbers print karo, lekin numbers divisible by 2 aur 3 ek sath print kare.

n = int(input("Please enter the ending number : "))

for i in range(1,n+1):
    if i %2 == 0 and i %3 == 0:
        print(i)
