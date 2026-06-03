import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Exercise 1: Diagonal matrix operations
matrix = np.random.randint(1, 20, size=(4, 4))
diag_elements = np.diag(matrix)
diag_matrix = np.diag(diag_elements)
print("Original matrix:\n", matrix)
print("Diagonal elements:", diag_elements)
print("Diagonal matrix from elements:\n", diag_matrix)

# Exercise 2: Conditional array operations
arr = np.random.random(20)
arr[arr > 0.5] = -1
print("\nConditional array (replace >0.5 by -1):\n", arr)

# Exercise 3: Data normalization (manual and with StandardScaler)
data = np.random.randn(10) * 5 + 20  # random data
manual_norm = (data - np.mean(data)) / np.std(data)
scaler = StandardScaler()
sklearn_norm = scaler.fit_transform(data.reshape(-1, 1)).flatten()
print("\nOriginal data:\n", data)
print("Normalized (manual):\n", manual_norm)
print("Normalized (sklearn):\n", sklearn_norm)

# Exercise 4: Pearson correlation coefficient
x = np.random.randn(50)
y = 2 * x + np.random.randn(50) * 0.5
corr = np.corrcoef(x, y)[0, 1]
print("\nPearson correlation coefficient:", corr)

# Exercise 5: Time series trend line
days = np.arange(1, 16)
values = np.random.randint(10, 100, size=15)
coeffs = np.polyfit(days, values, 1)
trend = np.polyval(coeffs, days)
plt.figure(figsize=(10, 5))
plt.plot(days, values, "o-", label="Time series")
plt.plot(days, trend, "r--", label=f"Trend line (slope={coeffs[0]:.2f})")
plt.xlabel("Day")
plt.ylabel("Value")
plt.title("Time series with linear trend")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
