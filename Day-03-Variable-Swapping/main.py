# Day 3 - Variable Swapping Logic
# Concept: Using a temporary variable to exchange values

# Input: Taking two values from the user
a = input("Enter the value of a: ")
b = input("Enter the value of b: ")

print(f"\nBefore swapping: a = {a}, b = {b}")

# Swapping Logic:
# 1. Put value of 'a' into a temporary storage
temp = a
# 2. Assign value of 'b' to 'a'
a = b
# 3. Assign value of 'temp' (original 'a') back to 'b'
b = temp

# Output: Displaying the results using f-strings
print(f"After swapping:  a = {a}, b = {b}")