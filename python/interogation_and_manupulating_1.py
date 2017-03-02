import numpy as np
array = np.array([range(4),range(10,14)])
print array.shape
print array.size
print array.max()
print array.min()
print np.reshape(array,(2,2,2))
print np.transpose(array)
print np.ravel(array)
print array.astype(np.float64)
