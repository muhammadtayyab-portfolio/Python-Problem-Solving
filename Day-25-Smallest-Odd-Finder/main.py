# User se 5 numbers input lo aur print karo smallest odd number.
num1 = int(input("Please enter Num1 : "))
num2 = int(input("Please enter Num2 : "))
num3 = int(input("Please enter Num3 : "))
num4 = int(input("Please enter Num4 : "))
num5 = int(input("Please enter Num5 : "))


smallest_odd = None  

for num in [num1, num2, num3, num4, num5]:
    if num % 2 != 0:   
        if smallest_odd == None or num < smallest_odd:
            smallest_odd = num

if smallest_odd is None:
    print("No odd number found")
else:
    print("Smallest odd number is:", smallest_odd)

