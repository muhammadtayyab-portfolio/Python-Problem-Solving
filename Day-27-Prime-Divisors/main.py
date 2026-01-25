# Ek number input lo aur print karo us number ke all divisors jo prime hain.
num = int(input("Enter a number: "))

print("Prime divisors of", num, "are:")

for i in range(2, num + 1):  
    if num % i == 0:          
        is_prime = True
        for j in range(2, i): 
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i)
