# 2. Second Largest Number
# Write a function second_largest(numbers: list) -> int that returns the second largest number from a list of integers.

def second_largest(numbers):
    numbers_2 = []
    
    for i in numbers:
        numbers_2.append(int(i))

    max_num = max(numbers)
    numbers.remove(max_num)
    second = max(numbers)
    return second


user = input("Please enter the numbers separated by space: ").split()
result = second_largest(user)

print("This is the second largest number:", result)