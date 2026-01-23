price = 0
height  = int(input("Please enter your height in cm : "))
if height > 120:
    print("Can ride")
    age = int(input("Please enter your age : "))
    if age > 18:
        price = 12
    elif age < 12:
        price = 5  
    elif age >= 12 and age <=18:
        price = 7

    if age >=45 and age <=55:
        price = 0
    
    photos = input("want photos : ")
    if photos == "Yes" or photos == "yes":
        price += 3
    print(f"The total bill is ${price}") 
else:
    print("Can't ride")