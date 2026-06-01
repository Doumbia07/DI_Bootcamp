import numpy as np

# Exercice 1 :
np.random.seed(42)
mat = np.random.random((5, 5))
max_val = mat.max()
mat[mat == max_val] = 0
print(mat)

# Exercice 2 :
np.random.seed(42)
a = np.random.random(5)
b = np.random.random(5)
common = np.intersect1d(a, b)
print(common)

# Exercice 3 :
np.random.seed(42)
c = np.random.random(10)
asc = np.sort(c)
desc = asc[::-1]
print("Ascending:", asc)
print("Descending:", desc)

# Exercice 4 :
np.random.seed(42)
d = np.random.random((4, 4))
rank = np.linalg.matrix_rank(d)
print("Rank:", rank)

# Exercice 5 :
border = np.zeros((5, 5))
border[0, :] = 1
border[-1, :] = 1
border[:, 0] = 1
border[:, -1] = 1
print(border)
