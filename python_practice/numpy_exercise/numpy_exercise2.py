import numpy as np

Matrix_A = np.array( [[1,1],[0,1]] )
Matrix_B = np.array( [[2,0],[3,4]] )

print Matrix_A*Matrix_B

print Matrix_A.dot(Matrix_B) 

print np.dot(Matrix_A, Matrix_B)    

Matrix_C = np.ones((2,3), dtype=int)
Matrix_C *= 3

print Matrix_C

Matrix_D = np.ones((2,3), dtype=int)

print Matrix_C+Matrix_D

Matrix_E = np.arange(12).reshape(3,4)

print Matrix_E

print Matrix_E[2,3]

print Matrix_E[ : , 1]

print Matrix_E[1 , : ]
