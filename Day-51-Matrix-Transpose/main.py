# 10. Matrix Transpose
# Write a function transpose_matrix(matrix: list) -> list that takes a 2D list (matrix) and returns its transpose.

def transpose_matrix(matrix: list):
    new_list = []
    
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(cols):
        inner_row = []
        for j in range(rows):
            inner_row.append(matrix[j][i])
        new_list.append(inner_row)
    return new_list
row1 = input("Please enter row 1 : ").split()
row2 = input("Please enter row 2 : ").split()
list_r1_r2 = [row1,row2]
result = transpose_matrix(list_r1_r2)
print("transpose of a matrix : ")

for i in result:
    print(i)
