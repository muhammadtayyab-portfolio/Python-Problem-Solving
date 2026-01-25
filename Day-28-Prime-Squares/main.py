# 1 se n tak numbers print karo, lekin prime numbers ke square print karo aur baki normal.

num = int(input("Please enter the number: "))

for i in range(1, num + 1):
    is_prime = True
    
    if i == 1:
        is_prime = False 
    
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
            
    if is_prime:
        print("Prime numbers k squares:", i ** 2)
    else:
        print("Simple numbers:", i)
    