import random

def sum_above_diagonal(matrix):
    n = len(matrix)
    total_sum = 0
    for i in range(n):
        for j in range(i+1, n):
            total_sum += abs(matrix[i][j])
    return total_sum
matrix = [[random.randint(-10, 10) for x in range(5)] for j in range(5)]

for row in matrix:
    print(row)


