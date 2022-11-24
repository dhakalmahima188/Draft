import numpy as np

a=np.array([0,1])
b=np.array([1,0])
print(np.dot(a,b))


X=np.array([[1,0],[0,1]])
Y=np.array([[0,1],[1,0]])
Z=X+Y
print(Z)

X=np.array([[1,0,1],[2,2,2]]) 
out=X[0,1:3]
print(out)

X=np.array([[1,0],[0,1]])
Y=np.array([[2,1],[1,2]]) 
Z=np.dot(X,Y)
print(Z)
