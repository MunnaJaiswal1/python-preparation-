import numpy as np
print("0D array:")
arr=np.array(45)
print("\n")
print(arr)

#1D array:
import numpy as np
print("1D array:")
arr=np.array([1,2,3,4,5])
print("\n")
print(arr)


#2D array:
import numpy as np
print("2D array:")
arr=np.array([[1,2,3],[4,5,6]])
print("\n")
print(arr)

#3D array:
import numpy as np
print("3D array:")
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[1,2,3]]])
print("\n")
print(arr)


#to check dimension of Array
import numpy as np
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

