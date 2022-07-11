# Напишите функцию def matrix_sum(), которая получает на вход две матрицы 
# и возвращает их сумму.

# Примечание: чтобы найти сумму двух матриц, нужно просуммировать 
# их соответствующие элементы. Но перед этим необходимо проверить, что размеры 
# матриц одинаковы (одинаковое количество столбцов и одинаковое количество строк)

# Например:

# 1 2 3   2 3 4   3 5 7
# 2 3 4 + 4 5 6 = 6 8 10
# 5 6 7   4 3 2   9 9 9

matrix_example = [
          [1, 5, 4],
          [4, 2, -2],
          [7, 65, 88]
]


def matrix_sum(matrix1, matrix2):
  mat_eq = True
  if len(matrix1) != len(matrix2):
    mat_eq = False
    print('Error! Matrices dimensions are different!')
    return    
  for i in range(len(matrix1)):
    if len(matrix1[i]) != len(matrix2[i]):
      mat_eq = False
  if mat_eq == False:
    print('Error! Matrices dimensions are different!')
    return
  
  res = []
  for i in range(len(matrix1)):
    new_line = []
    for j in range(len(matrix1[i])):
      new_line.append(matrix1[i][j] + matrix2[i][j])
    res.append(new_line)
  
  return res
  

print(matrix_sum(matrix_example, matrix_example))
