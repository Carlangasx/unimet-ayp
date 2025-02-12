from typing import List

matrix: List[List[int]] =[
  [1,2,4,5],
  [1,3,4],
  [2,6]
]

# Your code

result = [1, 1, 2, 2, 3, 4]

len_of_lists = 0 # 3

for l in matrix:
  len_of_lists += len(l)

while len_of_lists > 0:
  i = 0
  min_of_columns = 1000000
  for row in range(len(matrix)): # 0,1,2
    if len(matrix[row]) == 0:
      continue
    if matrix[row][0] <= min_of_columns:
      min_of_columns = matrix[row][0]
      i = row # 1
  if (len(matrix[i]) > 0):
    matrix[i].pop(0)
    result.append(min_of_columns)

  for l in matrix:
    len_of_lists += len(l)

print(result)

# calcular min(lists[0][0], lists[1][0], lists[2][0])
# eliminar de la matriz
# insertar en la lista resultado
# repetir hasta que la matriz este vacia







print(result)
