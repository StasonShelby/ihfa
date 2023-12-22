#def find_min_element(row):
   # min_element = row[0]
    #for element in row:
     #   if element < min_element:
      #      min_element = element
    #return min_element

#def sort_rows_by_min_element(matrix):
 #   for i in range(len(matrix)):
  #      for j in range(len(matrix[i])):
   #         min_index = j
    #        for k in range(j+1, len(matrix[i])):
     #           if matrix[i][k] < matrix[i][min_index]:
      #              min_index = k
       #     if min_index != j:
        #        matrix[i][j], matrix[i][min_index] = matrix[i][min_index], matrix[i][j]
    #return matrix

#N = 3
#M = 4
#matrix = [[5, 3, 8, 2],
         # [1, 7, 6, 4],
          #[9, 0, 3, 5]]

#sorted_matrix = sort_rows_by_min_element(matrix)
#print(sorted_matrix)




import random


N = int(input("Введите количество строк: "))
M = int(input("Введите количество столбцов: "))
matrix = [[random.randint(1, 100) for j in range(M)] for i in range(N)]

sorted_matrix = sorted(matrix, key=lambda row: min(row))

print("Исходная матрица:")
for row in matrix:
    print(row)

print("\nОтсортированная матрица:")
for row in sorted_matrix:
    print(row)

