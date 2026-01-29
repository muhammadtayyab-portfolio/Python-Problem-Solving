import random

q1 = int(input("How many letters would you like in your password? : "))
q2 = int(input("How many symbols would you like? : "))
q3 = int(input("How many numbers would you like? : "))
new_letter = ""
new_symbol = ""
new_number = ""
password = ""
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', 
    '(', ')', '_', '+', '-', '=', '{', '}', 
    '[', ']', ':', ';', '"', "'", '<', '>', 
    ',', '.', '?', '/', '\\', '|', '~', '`'
]
lowercase_letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
uppercase_letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
all_letters = lowercase_letters + uppercase_letters
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in range(0,q1):
    random_letter = random.randint(0,q1) 
    new_letter += all_letters[random_letter]  

for i in range(0,q2):
    random_symbol = random.randint(0,q2)
    new_symbol += symbols[random_symbol]

for i in range(0,q3):
    random_number = random.randint(0,q3)
    new_number += numbers[random_number]

password_list = list(new_letter + new_symbol + new_number)

shuffled_password = ""  
while password_list:  
    index = random.randint(0, len(password_list) - 1)  
    shuffled_password += password_list.pop(index)      

print(f"Your password (hard version): {shuffled_password}")

