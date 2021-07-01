import numpy as np

A = np.array([[4,-1,-1,0],
              [-1,4,0,-1],
              [-1,0,4,-1],
              [0,-1,-1,4]])

B = np.array([[30],
              [60],
              [40],
              [70]])


casicero = 1e-15
# Evitar truncamiento
A = np.array(A, dtype=float)
AB = np.concatenate((A, B), axis=1)
AB0 = np.copy(AB)

# Pivoteo parcial por filas
tamano = np.shape(AB)
n = tamano[0]
m = tamano[1]

# Para cada fila en AB
for i in range(0, n - 1, 1):
    columna = abs(AB[i:, i])
    dondemax = np.argmax(columna)

    if (dondemax != 0):
        temporal = np.copy(AB[i, :])
        AB[i, :] = AB[dondemax + i, :]
        AB[dondemax + i, :] = temporal
AB1 = np.copy(AB)

# eliminación progresiva
for i in range(0, n - 1, 1):
    pivote = AB[i, i]
    adelante = i + 1
    for k in range(adelante, n, 1):
        factor = AB[k, i] / pivote
        AB[k, :] = AB[k, :] - AB[i, :] * factor

# sustitución recursiva
ultfila = n - 1
ultcolumna = m - 1
X = np.zeros(n, dtype=float)

for i in range(ultfila, 0 - 1, -1):
    suma = 0
    for j in range(i + 1, ultcolumna, 1):
        suma = suma + AB[i, j] * X[j]
    b = AB[i, ultcolumna]
    X[i] = (b - suma) / AB[i, i]

X = np.transpose([X])
print('')
print('Matriz solución:')
print('')
print(AB0)
print('')
print('Pivoteo parcial por filas')
print('')
print(AB1)
print('')
print('eliminación progresiva')
print('')
print(AB)
print('')
print('solución: ')
print('')
print(X)
print('')


