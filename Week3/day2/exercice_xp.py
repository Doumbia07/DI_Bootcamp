import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#  Exercice 1 : Déterminant et inverse d’une matrice 3x3
A = np.array([[4, 7, 2], [3, 6, 1], [2, 5, 3]])
det = np.linalg.det(A)
inv = np.linalg.inv(A)
print("Determinant:", det)
print("Inverse:\n", inv)

#  Exercice 2 : Moyenne, médiane, écart-type de 50 nombres aléatoires
data = np.random.randn(50)
mean = np.mean(data)
median = np.median(data)
std = np.std(data)
print(f"Mean: {mean:.3f}, Median: {median:.3f}, Std: {std:.3f}")

#  Exercice 3 : Dates de janvier 2023 au format YYYY/MM/DD
dates = np.arange("2023-01-01", "2023-02-01", dtype="datetime64[D]")
formatted = np.datetime_as_string(dates, unit="D")
formatted_slash = np.array([d.replace("-", "/") for d in formatted])
print(formatted_slash)

#  Exercice 4 : DataFrame avec random + condition + agrégation
df = pd.DataFrame(np.random.randn(10, 3), columns=["A", "B", "C"])
cond = df[df["A"] > 0]
sum_cols = df.sum()
mean_cols = df.mean()
print("Condition (A>0):\n", cond.head())
print("Sum:\n", sum_cols)
print("Mean:\n", mean_cols)

#  Exercice 5 : Image en niveaux de gris 5x5
img = np.array(
    [
        [0, 50, 100, 150, 200],
        [50, 100, 150, 200, 250],
        [100, 150, 200, 250, 255],
        [150, 200, 250, 255, 200],
        [200, 250, 255, 200, 150],
    ]
)
print("Image array (5x5 grayscale):\n", img)

#  Exercice 6 : Test d’hypothèse sur programme de formation
np.random.seed(42)
before = np.random.normal(loc=50, scale=10, size=30)
after = before + np.random.normal(loc=5, scale=3, size=30)
# H0 : pas de différence ; H1 : amélioration (after > before)
diff = after - before
mean_diff = np.mean(diff)
std_diff = np.std(diff, ddof=1)  # écart-type échantillon
t_stat = mean_diff / (std_diff / np.sqrt(30))
print(f"Mean difference: {mean_diff:.2f}, t-statistic: {t_stat:.2f}")
# Interprétation approximative : si t_stat > 2, on rejette H0
if t_stat > 2:
    print("Reject H0: training seems effective.")
else:
    print("Cannot reject H0: insufficient evidence.")

#  Exercice 7 : Comparaison élément par élément
arr1 = np.array([1, 5, 3, 8, 2])
arr2 = np.array([2, 4, 6, 7, 3])
greater = arr1 > arr2
print("arr1 > arr2 :", greater)

#  Exercice 8 : Time series 2023 et slicing par trimestres
time_series = np.arange("2023-01-01", "2024-01-01", dtype="datetime64[D]")

q1 = time_series[
    (time_series >= np.datetime64("2023-01-01"))
    & (time_series < np.datetime64("2023-04-01"))
]
q2 = time_series[
    (time_series >= np.datetime64("2023-04-01"))
    & (time_series < np.datetime64("2023-07-01"))
]
q3 = time_series[
    (time_series >= np.datetime64("2023-07-01"))
    & (time_series < np.datetime64("2023-10-01"))
]
q4 = time_series[
    (time_series >= np.datetime64("2023-10-01"))
    & (time_series < np.datetime64("2024-01-01"))
]

print("Q1 (Jan-Mar):", q1[0], "to", q1[-1])
print("Q2 (Apr-Jun):", q2[0], "to", q2[-1])
print("Q3 (Jul-Sep):", q3[0], "to", q3[-1])
print("Q4 (Oct-Dec):", q4[0], "to", q4[-1])

#  Exercice 9 : Conversion NumPy array <-> Pandas DataFrame
numpy_arr = np.random.randn(4, 3)
df_from_arr = pd.DataFrame(numpy_arr, columns=["X", "Y", "Z"])
arr_from_df = df_from_arr.to_numpy()
print("Original NumPy array shape:", numpy_arr.shape)
print("DataFrame:\n", df_from_arr.head())
print("Back to NumPy array shape:", arr_from_df.shape)

#  Exercice 10 : Visualisation d’une ligne de nombres aléatoires
x = np.linspace(0, 10, 50)
y = np.random.randn(50).cumsum()  # marche aléatoire
plt.figure(figsize=(10, 4))
plt.plot(x, y, marker="o", linestyle="-", markersize=3)
plt.title("Random Walk Line Graph")
plt.xlabel("X")
plt.ylabel("Cumulative Sum")
plt.grid(True, alpha=0.3)
plt.show()
