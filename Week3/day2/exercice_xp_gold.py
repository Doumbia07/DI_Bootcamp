import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import skew, kurtosis

# EXERCICE 1 : Matrice aléatoire 5x5 - valeurs propres,

print("\n" + "=" * 60)
print("EXERCICE 1 : Matrice 5x5 aléatoire")
print("=" * 60)

# 1. Créer une matrice 5x5 avec des nombres aléatoires (valeurs entre 0 et 1)
M = np.random.rand(5, 5)
print("Matrice aléatoire :\n", M)

# 2. Calculer les valeurs propres et vecteurs propres
eigenvalues, eigenvectors = np.linalg.eig(M)
print("\nValeurs propres :", eigenvalues)
print(
    "Vecteurs propres (chaque colonne correspond à une valeur propre) :\n", eigenvectors
)

# 3. Normalisation de la matrice (centrée-réduite : moyenne=0, écart-type=1)
#    On normalise colonne par colonne.
M_mean = np.mean(M, axis=0)  # moyenne de chaque colonne
M_std = np.std(M, axis=0)  # écart-type de chaque colonne
M_normalized = (M - M_mean) / M_std
print("\nMatrice normalisée (moyenne=0, écart-type=1 par colonne) :\n", M_normalized)

# EXERCICE 2 : Génération d'une distribution normale,
#              histogramme, skewness, kurtosis
print("\n" + "=" * 60)
print("EXERCICE 2 : Distribution normale")
print("=" * 60)

# Générer 1000 valeurs suivant une loi normale (moyenne=0, écart-type=1)
data = np.random.normal(loc=0, scale=1, size=1000)

# Tracer l'histogramme
plt.figure(figsize=(8, 5))
plt.hist(data, bins=30, edgecolor="black", alpha=0.7, color="skyblue")
plt.title("Histogramme d'une distribution normale")
plt.xlabel("Valeur")
plt.ylabel("Fréquence")
plt.grid(True, alpha=0.3)
plt.show()

# Calculer et afficher l'asymétrie (skewness) et l'aplatissement (kurtosis)
skewness = skew(data)
kurt = kurtosis(data)  # kurtosis par défaut = kurtosis de Fisher (0 = normale)
print(f"Asymétrie (skewness) : {skewness:.4f}")
print(f"Aplatissement (kurtosis) : {kurt:.4f}")
print("Interprétation :")
print("- Skewness proche de 0 → distribution symétrique.")
print("- Kurtosis proche de 0 → forme similaire à une distribution normale.")

# EXERCICE 3 : Prévision de séries temporelles (régression linéaire)
print("\n" + "=" * 60)
print("EXERCICE 3 : Prévision de ventes mensuelles par régression linéaire")
print("=" * 60)

# Données aléatoires de ventes sur 12 mois
np.random.seed(42)  # pour reproductibilité
monthly_sales = np.random.randint(100, 500, size=12)
print("Ventes mensuelles :", monthly_sales)

# Créer les indices des mois (0 à 11)
months = np.arange(12)

# Régression linéaire : on cherche pente a et intercept b tels que sales = a*month + b
a, b = np.polyfit(months, monthly_sales, 1)
print(f"\nTendance linéaire : ventes = {a:.2f} * mois + {b:.2f}")

# Prévoir les ventes pour les 3 prochains mois (mois 12, 13, 14)
future_months = np.arange(12, 15)
forecast = a * future_months + b
for m, f in zip(future_months, forecast):
    print(f"Prévision pour le mois {m+1} : {f:.0f}")

# Tracer les données réelles et la droite de régression
plt.figure(figsize=(10, 5))
plt.plot(months, monthly_sales, "o-", label="Ventes réelles")
plt.plot(months, a * months + b, "r--", label="Régression linéaire")
plt.plot(future_months, forecast, "s", color="green", label="Prévisions")
plt.xlabel("Mois (0 = janvier)")
plt.ylabel("Ventes")
plt.title("Prévision des ventes par régression linéaire")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# EXERCICE 4 : Agrégation de données avec Pandas
print("\n" + "=" * 60)
print("EXERCICE 4 : Agrégation et groupby avec Pandas")
print("=" * 60)

# Créer le DataFrame exemple
data = {
    "Product": ["Product A", "Product B", "Product C", "Product A", "Product B"],
    "Sales": [200, 150, 300, 250, 180],
    "Month": ["January", "February", "March", "April", "May"],
}
df = pd.DataFrame(data)
print("DataFrame original :\n", df)

# 1. Grouper par produit et calculer la somme des ventes
sales_by_product = df.groupby("Product")["Sales"].sum()
print("\nSomme des ventes par produit :\n", sales_by_product)

# 2. Grouper par produit et calculer la moyenne des ventes
mean_by_product = df.groupby("Product")["Sales"].mean()
print("\nMoyenne des ventes par produit :\n", mean_by_product)

# 3. Agrégation multiple : compter, somme, moyenne, min, max
aggregation = df.groupby("Product")["Sales"].agg(["count", "sum", "mean", "min", "max"])
print("\nAgrégation complète par produit :\n", aggregation)

# 4. Grouper par mois et par produit (si plus de données)
#    Ici, on peut aussi faire un groupby simple sur le mois
if "Month" in df.columns:
    sales_by_month = df.groupby("Month")["Sales"].sum()
    print("\nVentes totales par mois :\n", sales_by_month)

# EXERCICE 5 : Multi-plot layout avec différents types de graphiques
print("\n" + "=" * 60)
print("EXERCICE 5 : Multi-plot (line, scatter, bar) avec Matplotlib")
print("=" * 60)

# Générer des données NumPy pour les graphiques
np.random.seed(0)
x = np.linspace(0, 10, 50)
y1 = np.sin(x) + np.random.normal(0, 0.1, size=50)  # sin + bruit
y2 = 2 * x + np.random.normal(0, 2, size=50)  # droite avec bruit
categories = ["A", "B", "C", "D", "E"]
values = np.random.randint(10, 100, size=5)

# Créer une figure avec 3 sous-graphiques (1 ligne, 3 colonnes)
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 1. Graphique en lignes (line plot)
axes[0].plot(x, y1, "o-", color="blue", markersize=4, label="Signal bruité")
axes[0].plot(x, np.sin(x), "r--", label="Sin pur")
axes[0].set_title("Graphique en lignes")
axes[0].set_xlabel("X")
axes[0].set_ylabel("Y")
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# 2. Nuage de points (scatter plot)
axes[1].scatter(x, y2, color="green", alpha=0.6, label="Données linéaires bruitées")
axes[1].set_title("Nuage de points")
axes[1].set_xlabel("X")
axes[1].set_ylabel("Y")
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# 3. Diagramme à barres (bar chart)
axes[2].bar(categories, values, color="orange", edgecolor="black")
axes[2].set_title("Diagramme à barres")
axes[2].set_xlabel("Catégorie")
axes[2].set_ylabel("Valeur")

plt.tight_layout()
plt.show()

print("\nTous les exercices sont terminés.")
