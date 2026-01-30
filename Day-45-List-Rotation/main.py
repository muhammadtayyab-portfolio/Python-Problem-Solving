# Write a function rotate_list(lst: list, k: int) -> list that rotates the list to the right by k steps.
#  Example: [1,2,3,4,5], k=2 → [4,5,1,2,3]

def rotate_list(lst, k):
    if not lst:
        return lst
    
    k = k % len(lst)
    return lst[-k:] + lst[:-k]


user = input("Enter numbers separated by space: ").split()
k = int(input("Enter k (steps to rotate): "))

result = rotate_list(user, k)
print("Rotated list:", result)


