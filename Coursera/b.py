import numpy as np
import matplotlib.pyplot as plt

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


x_train = np.array([1.0, 2.0,3,4])
y_train = np.array([300.0, 500.0,600,900])
plt.scatter(x_train, y_train, marker='x', c='r')
plt.title("Housing Prices")
plt.ylabel('Price (in 1000s of dollars)')
plt.xlabel('Size (1000 sqft)')
plt.show()
