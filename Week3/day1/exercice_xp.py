import numpy as np

# Exercice 1
arr1 = np.arange(10)
print(arr1)

# Exercice 2
arr2 = np.array([3.14, 2.17, 0, 1, 2]).astype(int)
print(arr2)

# Exercice 3
arr3 = np.arange(1, 10).reshape(3, 3)
print(arr3)

# Exercice 4
arr4 = np.random.random((4, 5))
print(arr4)

# Exercice 5
arr5 = np.array([[21,22,23,22,22],[20,21,22,23,24],[21,22,23,22,22]])
row2 = arr5[1, :]
print(row2)

# Exercice 6
arr6 = np.arange(10)[::-1]
print(arr6)

# Exercice 7
arr7 = np.eye(4)
print(arr7)

# Exercice 8
arr8 = np.arange(10) 
print("Sum:", np.sum(arr8), "Average:", np.mean(arr8))

# Exercice 9
arr9 = np.arange(1, 21).reshape(4, 5)
print(arr9)

# Exercice 10
arr10 = np.arange(1, 11)
odd = arr10[arr10 % 2 == 1]
print(odd)