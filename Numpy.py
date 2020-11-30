import numpy as np

A = np.array([[6, 5], [8, -6]]) #tao ma tran
B = np.array([[9, -3], [2, 6]])
C = A + B
print(C) #tong ma tran a va b
D = A.dot(B)
print(D) # tich ma tran a va b
print(A.transpose()) #chuyen vi ma tran a