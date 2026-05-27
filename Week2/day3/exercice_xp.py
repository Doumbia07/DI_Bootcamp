import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import (
    norm,
    ttest_ind,
    linregress,
    f_oneway,
    binom,
    pearsonr,
    spearmanr,
)
import pandas as pd

# Exercice 1 : Utilisation de base de SciPy
print("=" * 50)
print("Exercice 1 : Version de SciPy")
print("=" * 50)
import scipy

print("Version de SciPy :", scipy.__version__)
print()

# Exercice 2 : Statistiques descriptives
print("=" * 50)
print("Exercice 2 : Statistiques descriptives")
print("=" * 50)
data = [12, 15, 13, 12, 18, 20, 22, 21]
mean = np.mean(data)
median = np.median(data)
variance = np.var(data, ddof=1)  # variance d'échantillon (ddof=1)
std_dev = np.std(data, ddof=1)  # écart-type d'échantillon

print(f"Données : {data}")
print(f"Moyenne : {mean:.2f}")
print(f"Médiane : {median}")
print(f"Variance (échantillon) : {variance:.2f}")
print(f"Écart-type (échantillon) : {std_dev:.2f}\n")

# Exercice 3 : Génération et tracé d'une distribution normale
print("=" * 50)
print("Exercice 3 : Distribution normale (μ=50, σ=10)")
print("=" * 50)
mu, sigma = 50, 10
x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 200)
y = norm.pdf(x, loc=mu, scale=sigma)

plt.figure(figsize=(8, 4))
plt.plot(x, y, "b-", linewidth=2, label=f"N({mu}, {sigma}²)")
plt.title("Distribution normale")
plt.xlabel("Valeur")
plt.ylabel("Densité de probabilité")
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()
print("Graphique affiché.\n")

# Exercice 4 : Test t de Student (t-test)
print("=" * 50)
print("Exercice 4 : Test t sur deux échantillons aléatoires")
print("=" * 50)
np.random.seed(42)  # pour reproductibilité
data1 = np.random.normal(50, 10, 100)
data2 = np.random.normal(60, 10, 100)

t_stat, p_value = ttest_ind(data1, data2)
print(f"Statistique t : {t_stat:.4f}")
print(f"Valeur p : {p_value:.4e}")
if p_value < 0.05:
    print("Conclusion : Différence significative (p < 0.05)")
else:
    print("Conclusion : Pas de différence significative (p >= 0.05)")
print()

# Exercice 5 : Régression linéaire
print("=" * 50)
print("Exercice 5 : Régression linéaire - Prix des maisons")
print("=" * 50)
house_sizes = [50, 70, 80, 100, 120]  # m²
house_prices = [150000, 200000, 210000, 250000, 280000]  # monnaie

slope, intercept, r_value, p_value_reg, std_err = linregress(house_sizes, house_prices)

print(f"Pente (slope) : {slope:.2f} unités monétaires/m²")
print(f"Ordonnée à l'origine (intercept) : {intercept:.2f} unités monétaires")
print(f"Coefficient de corrélation (R) : {r_value:.4f}")

# Prédiction pour 90 m²
size_pred = 90
price_pred = slope * size_pred + intercept
print(
    f"\nPrédiction pour une maison de {size_pred} m² : {price_pred:.2f} unités monétaires"
)

print("\nInterprétation de la pente :")
print(
    "La pente représente le coût additionnel par mètre carré. Ici, chaque m² supplémentaire"
)
print(f"augmente le prix d'environ {slope:.2f} unités monétaires.\n")

# Exercice 6 : ANOVA
print("=" * 50)
print("Exercice 6 : ANOVA - Effet de trois engrais")
print("=" * 50)
fertilizer_1 = [5, 6, 7, 6, 5]
fertilizer_2 = [7, 8, 7, 9, 8]
fertilizer_3 = [4, 5, 4, 3, 4]

f_stat, p_value_anova = f_oneway(fertilizer_1, fertilizer_2, fertilizer_3)

print(f"Valeur F : {f_stat:.4f}")
print(f"Valeur p : {p_value_anova:.6f}")

alpha = 0.05
if p_value_anova < alpha:
    print(
        "Conclusion : Les engrais ont des effets significativement différents (p < 0.05)."
    )
else:
    print("Conclusion : Aucune différence significative entre les engrais (p >= 0.05).")

print("\nSi la valeur p était supérieure à 0,05 :")
print("On accepterait l'hypothèse nulle (pas de différence d'effet entre les engrais).")
print(
    "Les différences observées seraient attribuables au hasard plutôt qu'à un vrai effet.\n"
)

# Exercice 7 (Optionnel) : Distribution binomiale
print("=" * 50)
print("Exercice 7 (Optionnel) : Probabilité binomiale")
print("=" * 50)
n_flips = 10
p_head = 0.5
k = 5

prob_exact_5 = binom.pmf(k, n_flips, p_head)
print(
    f"Probabilité d'obtenir exactement {k} faces (piles) en {n_flips} lancers : {prob_exact_5:.4f} ({prob_exact_5*100:.2f}%)"
)

# Exemple supplémentaire : probabilité d'au plus 3 succès
prob_at_most_3 = binom.cdf(3, n_flips, p_head)
print(f"Probabilité d'au plus 3 succès : {prob_at_most_3:.4f}\n")

# Exercice 8 (Optionnel) : Corrélation de Pearson et Spearman
print("=" * 50)
print("Exercice 8 (Optionnel) : Coefficients de corrélation")
print("=" * 50)
df = pd.DataFrame(
    {"age": [23, 25, 30, 35, 40], "income": [35000, 40000, 50000, 60000, 70000]}
)

pearson_corr, p_pearson = pearsonr(df["age"], df["income"])
spearman_corr, p_spearman = spearmanr(df["age"], df["income"])

print("Jeu de données :")
print(df)
print(f"\nCorrélation de Pearson : r = {pearson_corr:.4f}, p-value = {p_pearson:.4e}")
print(f"Corrélation de Spearman : ρ = {spearman_corr:.4f}, p-value = {p_spearman:.4e}")

print(
    "\nInterprétation : Une forte corrélation positive indique que plus l'âge augmente,"
)
print(
    "plus le revenu a tendance à augmenter (linéairement pour Pearson, monotoniquement pour Spearman).\n"
)

print("Fin des exercices.")
