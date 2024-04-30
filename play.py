import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[1,2],[3,4]])

# print(np.matmul(x,y))
# print(x.shape, y.shape)
xr = x.reshape(2,1,2)
yr = y.T.reshape(1,2,2)
print(xr)
print()
print(yr)
print(xr.shape, yr.shape)
print(xr * yr)
# print(np.sum(xr * yr, axis=2))
print()
print(np.array([[1,2]]) * np.array([[1,3],[2,4]]))

print(np.array([1,2]) * np.array([1,3]))