# 3. Remove Duplicates without set()
# Write a function remove_duplicates(lst: list) -> list that removes duplicates from a list while preserving the order of elements.


def remove_duplicates(lst):
    unique_list = []
    for i in lst:
        if i not in unique_list:
            unique_list.append(i)
    
    return unique_list

user = input("Enter numbers separated by space: ").split()
result = remove_duplicates(user)
print("After removing duplicates:", result)
