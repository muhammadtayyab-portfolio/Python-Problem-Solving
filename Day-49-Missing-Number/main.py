# 8. Find Missing Number
# Write a function find_missing(nums: list) -> int that finds the missing number from a list containing numbers from 1 to n with one number missing.

def find_missing(nums):
    sum_orignal = 0
    for i in nums:
        sum_orignal += int(i)

    formula = (len(nums)+1) * ((len(nums)+1) + 1)//2
    return formula - sum_orignal  

user = input("please enter missing number stream : ").split()

result = find_missing(user)
print("The missing number is = ",result)