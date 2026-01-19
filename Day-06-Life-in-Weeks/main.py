const = 90 
age = int(input("please enter your age : "))
if age <= const:
    final = const - age
    x = final * 365
    y = final * 52
    z = final * 12
    print(f"You have {x} days, {y} weeks, and {z} months left.")