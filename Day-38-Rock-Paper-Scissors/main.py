import random

print("Let's start Rock Paper Scissors game : ")
print("1 - Rock")
print("2 - Paper")
print("3 - Scissors")

user = int(input("Enter your choice (1-3): "))
cpu = random.randint(1, 3)

if cpu == 1:
    print("CPU chose: Rock")
elif cpu == 2:
    print("CPU chose: Paper")
else:
    print("CPU chose: Scissors")

if user == cpu:
    print("Match was draw...")
elif (user == 1 and cpu == 3) or (user == 2 and cpu == 1) or (user == 3 and cpu == 2):
    print("User wins the match!")
else:
    print("CPU wins the match!")
