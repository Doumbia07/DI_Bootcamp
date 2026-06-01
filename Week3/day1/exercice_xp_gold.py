import numpy as np

#  Exercice 1 :
arr1 = np.random.random((5, 5))
min_val = arr1.min()
max_val = arr1.max()
print(f"Min: {min_val:.2f}, Max: {max_val:.2f}")

#  Exercice 2 :
arr2 = np.random.random((3, 3))
mean = np.mean(arr2)
std = np.std(arr2)
normalized = (arr2 - mean) / std
print(normalized)

#  Exercice 3 :
arr3 = np.linspace(0, 10, 50, endpoint=False)
print(arr3)

#  Exercice 4 :
A = np.random.random((5, 3))
B = np.random.random((3, 2))
C = A @ B
print(C)

#  Exercice 5 :

D = np.random.random((4, 2))
E = np.random.random((2, 3))
F = D @ E
print(F)
