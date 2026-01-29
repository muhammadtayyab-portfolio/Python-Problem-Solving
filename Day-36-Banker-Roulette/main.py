import random
name = input("Give me everybody's names, separated by a comma and space: ")

name_list = name.split(", ")
random_choice = random.randint(0,len(name_list)-1)
payer = name_list[random_choice]

print(f"{payer} is going to buy the meal today!")