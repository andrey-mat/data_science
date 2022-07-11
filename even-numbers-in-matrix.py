# Напишите функцию def even_numbers_in_matrix(), 
# которая получает на вход матрицу (список из списков) 
# и возвращает количество четных чисел в ней.

matrix_example = [
          [1, 5, 4],
          [4, 2, -2],
          [7, 65, 88]
]

def even_numbers_in_matrix(matrix):
    counter = 0
    for raw in matrix:
        for x in raw:
            if x%2 == 0: counter+=1
    return counter

print(even_numbers_in_matrix(matrix_example))
