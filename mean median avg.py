import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("array:\n",a)
print("\nmedian of array along axis 0:", np.median(a, 0))
print(" mean of array along axis 0", np.mean(a,0))
print("average of array along axis 1", np.median(a,1))      
