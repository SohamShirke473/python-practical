import numpy as np

array_1d = np.array([1, 2, 3, 4, 5])
print("Here's a 1D array:", array_1d)

array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\nNow a 2D array (2 rows, 3 columns):")
print(array_2d)

array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\nAnd a 3D array (2 blocks, each 2x2):")
print(array_3d)

reshaped = array_1d.reshape(5, 1)
print("\nReshaped the 1D array into a column vector:")
print(reshaped)

slice_1d = array_1d[1:4]
print("\nTaking a slice from index 1 to 3 of the 1D array:", slice_1d)

print("\nAccessing specific elements:")
print("Element from 2D array at row 1, column 2:", array_2d[1][2])
print("Element from 3D array [block 1][row 0][column 1]:", array_3d[1][0][1])
