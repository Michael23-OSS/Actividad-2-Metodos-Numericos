import numpy as np

#Algoritmo para la matriz

def cholesky(a):
     a = np.array(a, float)
     L = np.zeros_like(a)
     n,_ = np.shape(a)
     for j in range(n):
          for i in range(j,n):
               if i == j:
                    L[i,j] = np.sqrt(a[i,j]-np.sum(L[i,:j]**2))
               else:
                    L[i,j] = (a[i,j] - np.sum(L[i,:j]*L[j,:j])) / L[j,j]
     return L

def solveLU(L,U,b):
     L = np.array(L,float)
     U = np.array(U,float)
     b = np.array(b,float)
     n,_=np.shape(L)
     y = np.zeros(n)
     x = np.zeros(n)

     #Sustitución Progresiva
     for i in range(n):
          sumj = 0
          for j in range(i):
               sumj += L[i,j] * y[j]
          y[i] = (b[i]-sumj)/L[i,i]

     #Sustitución Regresiva
     for i in range(n-1,-1,-1):
          sumj = 0
          for j in range(i+1,n):
               sumj += U[i,j] * x[j]
          x[i] = (y[i]-sumj)/U[i,i]
     return x

#implementación de la matriz

a = [[8, 3, 8],
     [3, 7, 2],
     [0, 2, 5]]

b = [9, 1, 7]

l = cholesky(a)
x = solveLU(l,np.transpose(l),b)

print('')
print('Matriz')
print('')
print(a)
print('---------------------------------')
print(b)
print('')
print('Sustitución Regresiva:')
print('')
print(x)
print('')
print('Sustitución Progresiva:')
print('')
print(np.linalg.solve(a,b))

