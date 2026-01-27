def prime_num_find(n):
    if n <= 1:
        print("It's not a prime number.")
        return
    count = 2
    while count < n:
        if n % count == 0:
            print("It's not a prime number.")
            return
        count+=1
    
    print("It's a prime number.")


num = int(input("Please enter the number : "))

prime_num_find(num)