# User se string input lo aur first and last character same hai ya nahi check karo.

user_str = input("Please enter anything: ")

if user_str[0] == user_str[-1]:
    print("First and last character are same : ",user_str[0]," = ",user_str[-1])
else:
    print("First and last character are different : ",user_str[0]," != ",user_str[-1])
