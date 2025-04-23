import numpy as np

arr = np.array([10, 20, 30, 40, 50])
arr2 = np.array([5, 10, 15, 20, 25])

print("Data array:", arr)

print("\nMean of the array:", np.mean(arr))
print("Median of the array:", np.median(arr))
print("Standard deviation:", np.std(arr))
print("Variance:", np.var(arr))

print("\nNow comparing with another array:", arr2)
correlation = np.corrcoef(arr, arr2)
print("Correlation coefficient matrix:\n", correlation)
