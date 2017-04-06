import numpy as np

Matrix_A = np.array( [[1,1],[0,1]] )
Matrix_B = np.array( [[2,0],[3,4]] )

print Matrix_A*Matrix_B

print Matrix_A.dot(Matrix_B) 

print np.dot(Matrix_A, Matrix_B)    
