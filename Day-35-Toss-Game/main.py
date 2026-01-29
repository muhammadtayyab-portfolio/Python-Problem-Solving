import random
print("Lets Tose...")

user1 =input("Heads or Tails : ").lower()
if user1 == "heads":
    user2 = "Tails"
else:
    user2 = "Heads"

r = random.randint(0,1)

if r == 0 :
    print("Winner is : Heads")
else:
    print("Winner is : Tails")