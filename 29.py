import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Array A:", a)
print("Array B:", b)

print("\nElement-wise addition:", a + b)
print("Element-wise subtraction:", a - b)
print("Element-wise multiplication:", a * b)
print("Element-wise division:", a / b)

dot_product = np.dot(a, b)
print("\nDot product of A and B:", dot_product)

cross_product = np.cross(a, b)
print("Cross product of A and B:", cross_product)
