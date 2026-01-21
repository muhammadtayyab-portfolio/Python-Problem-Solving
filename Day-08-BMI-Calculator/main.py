weight = float(input("Please enter your weight : "))
height = float(input("Please enter your height : "))
bmi = round(weight / (height**2))

if bmi < 18.5:
    ans = "underweight"
elif bmi < 25:
    ans = "have a normal weight"
elif bmi < 30:
     ans = "are slightly overweight"
elif bmi < 35:
     ans = "are obese"
else:
     ans = "are clinically obese"

print(f"Your BMI is {bmi}, you {ans}.")