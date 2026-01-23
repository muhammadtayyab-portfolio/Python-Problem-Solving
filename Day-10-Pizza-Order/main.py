price = 0
print("Small Pizza: $15")
print("Medium Pizza: $20")
print("Large Pizza: $25")
size =  input("please enter the size of pizza (S,M,L) : ")
print("Pepperoni for Small pizza: +$2")
print("Pepperoni for Medium or Large Pizza: +$3")
add_pepperoni = input("Type Y/N : ")
add_cheese = input("Extra cheese for any size pizza: + $1 : ")

if size in ["S","s"]:
    price = 15
    if add_pepperoni in ["Y","y"]:
        price += 2
    if add_cheese in ["Y","y"]:
        price += 1
    
elif size in ["M","m"]:
    price = 20
    if add_pepperoni in ["Y","y"]:
        price += 3
    if add_cheese in ["Y","y"]:
        price += 1
elif size in ["L","l"]:
    price = 25
    if add_pepperoni in ["Y","y"]:
        price += 3
    if add_cheese in ["Y","y"]:
        price += 1

print(f"Your final bill is: ${price}.")


