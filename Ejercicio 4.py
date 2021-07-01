import numpy as np

def swag(a, b):
    for i in range(0, len(a)):
        t = a[i]
        a[i] = b[i]
        b[i] = t

#Implementación de la matriz
def print_matrix( info, matrix ):
    print (info)
    for i in range( 0, matrix.shape[0]):
        print('[', end='')
        for j in range( 0, matrix.shape[1]):
            if(j == matrix.shape[1] - 1):
                print( '|', end=''),
            print("%5.2f" %matrix[i][j], end=' ')
            if j == matrix.shape[1] - 1:
                print(']', end=' ')
                print('\n')

#vefificación de que la matriz este completa
def check(matrix, i, row, col):
    if 0.00 in set(matrix[i]) and len(set(matrix[i])) == 1:
        for j in range(row - 1, i ,-1):
            try:
                if not(0.00 in set(matrix[j]) and len(set(matrix[j])) == 1):
                    swag(matrix[i], matrix[j])
                    select(matrix, i, col)
                    break
            except:
                return

#Selección de filas para la solución
def select(matrix, i, col):
    if 0.00 in set(matrix[i]) and len(set(matrix[i])) == 1:
        return
    for k in range(0, i):
        temp = matrix[i][k] / matrix[k][k]
        if temp == 0:
            continue
        for j in range(0, col):
            matrix[i][j] = matrix[i][j]-matrix[k][j] * temp

#Solución por eliminación gaussiana
def solve(matrix):
    row = matrix.shape[0]
    col = matrix.shape[1]
    for i in range(0, row):
        if matrix[i][i] == 0:
            for j in range(i + 1, row):
                if matrix[j][i] != 0:
                    swag(matrix[i], matrix[j])
                    break
        select(matrix, i, col)
        check(matrix, i, row, col)

#Escalonamiento
def to_one(matrix):
    row = matrix.shape[0]
    col = matrix.shape[1]
    for i in range(0, row):
        temp = matrix[i][i]
        for j in range(i, col):
            matrix[i][j] = matrix[i][j] / temp
    for i in range(0, row - 1):
        for j in range(i + 1, col - 1):
            temp = matrix[i][j]
            for k in range(j, col):
                matrix[i][k] = matrix[i][k] - matrix[j][k] * temp

#Instrucciones
def judge(matrix):
    row = matrix.shape[0]
    col = matrix.shape[1]
    vanumlist = []
    for i in range(0, col):
        if matrix[row - 1][i] != 0:
            vanumlist.append(matrix[row - 1][i])
    if len(vanumlist) == 1:
        print('')
        print( 'La matriz no tiene solución')
    elif len(vanumlist) == 2:
        to_one(matrix)
        print('')
        print_matrix('La solución de la matriz es:', matrix)
        print('')
        for i in range(0, row):
            print("x%d = %4.2f" %(i,matrix[i][col - 1]), end="  ")
            print('')
    else:
        print('')
        print( 'Múltiples soluciones de ecuaciones')


matrix = np.array([[4,-1,-1,0,30],
                   [-1,4,0,-1,60],
                   [-1,0,4,-1,40],
                   [0,-1,-1,4,70]],dtype=float)
print('')
print_matrix('La matriz inicial es:', matrix)
print('')
solve(matrix)
print('')
print_matrix('La matriz escalonada:', matrix)
print('')
judge(matrix)

