from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Daily Challenge: Comprehensive Mobile Price Analysis
# 1. CHARGEMENT ET EXPLORATION INITIALE DES DONNÉES

# Charger le fichier CSV depuis le dossier du script
script_dir = Path(__file__).resolve().parent
data_path = script_dir / "train.csv"
data = pd.read_csv(data_path)

# Afficher les 5 premières lignes pour voir la structure
print(data.head())

# 1.3. Informations générales
print(data.info())

# 1.4. Vérifier les valeurs manquantes (null values)
print(data.isnull().sum())

# 1.5. Statistiques descriptives de base (moyenne, écart-type, min, max, quartiles)
print("Statistiques descriptives")
print(data.describe())


# 2. NETTOYAGE ET PRÉTRAITEMENT

# Convertir les colonnes catégorielles (type 'object') en codes numériques
#     car les modèles statistiques nécessitent des nombres.
for col in data.select_dtypes(include=["object"]).columns:
    data[col] = pd.Categorical(data[col]).codes

# Afficher de nouveau les statistiques après transformation (optionnel)
print("Statistiques après encodage des catégories ")
print(data.describe())


# 3 ANALYSE STATISTIQUE AVANCÉE AVEC NUMPY ET SCIPY


stats_summary = {}

# Pour chaque colonne
for col in data.columns:
    if col != "price_range":
        col_data = data[col]
        stats_summary[col] = {
            "mean": np.mean(col_data),
            "median": np.median(col_data),
            "mode": stats.mode(col_data, keepdims=True).mode[0],
            "variance": np.var(col_data),
            "std": np.std(col_data),
            "range": np.ptp(col_data),
            "skewness": stats.skew(col_data),
            "kurtosis": stats.kurtosis(col_data),
        }

# Transformer le dictionnaire en DataFrame pour une lecture facile
stats_data = pd.DataFrame(stats_summary).T
print("Statistiques détaillées par caractéristique ")
print(stats_data)

# Test d'hypothèse : comparer la RAM entre les téléphones les moins chers (price_range=0)
# et les plus chers (price_range=3) avec un test t de Student.
low_price = data[data["price_range"] == 0]["ram"]
high_price = data[data["price_range"] == 3]["ram"]
t_stat, p_val = stats.ttest_ind(low_price, high_price)

print("Test t : RAM entre les prix bas (0) et très haut (3) ")
print(f"  - t-statistique = {t_stat:.3f}")
print(f"  - p-value = {p_val:.3e}")
if p_val < 0.05:
    print("Conclusion : différence significative (rejet de H0).")
else:
    print("Conclusion : pas de différence significative.")

# Corrélation de Pearson entre chaque caractéristique et le prix (price_range)
correlations = {}
for col in data.columns:
    if col != "price_range":
        corr, _ = stats.pearsonr(data[col], data["price_range"])
        correlations[col] = corr

# Trier les corrélations par force décroissante
corr_data = pd.DataFrame(list(correlations.items()), columns=["feature", "correlation"])
corr_data = corr_data.sort_values("correlation", ascending=False)

print("Corrélation de chaque caractéristique avec price_range ")
print(corr_data)


# 4. VISUALISATION AVEC MATPLOTLIB ET SEABORN

# Histogrammes de toutes les caractéristiques (sauf la cible)
#     pour observer la distribution de chaque variable.
plt.figure(figsize=(15, 10))
n_cols = len(data.columns) - 1
for i, col in enumerate(data.columns[:-1], 1):
    plt.subplot(3, 7, i)
    plt.hist(data[col], bins=30, edgecolor="black", alpha=0.7)
    plt.title(col, fontsize=8)
    plt.tight_layout()
plt.suptitle("Histogrammes des caractéristiques", y=1.02)
plt.show()

# Boxplot de la RAM par gamme de prix
plt.figure(figsize=(12, 6))
sns.boxplot(x="price_range", y="ram", data=data)
plt.title("Distribution de la RAM selon la gamme de prix")
plt.xlabel("Gamme de prix (0=bas, 3=très haut)")
plt.ylabel("RAM")
plt.show()

# Boxplot de la capacité de la batterie par gamme de prix
plt.figure(figsize=(12, 6))
sns.boxplot(x="price_range", y="battery_power", data=data)
plt.title("Capacité de la batterie selon la gamme de prix")
plt.xlabel("Gamme de prix")
plt.ylabel("Battery power (mAh)")
plt.show()

# Heatmap de la matrice de corrélation (seulement colonnes numériques)
plt.figure(figsize=(10, 8))
numeric_cols = data.select_dtypes(include=[np.number]).columns
corr_matrix = data[numeric_cols].corr()
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", square=True)
plt.title("Matrice de corrélation des caractéristiques")
plt.show()

# 5. SYNTHÈSE DES RÉSULTATS ET CONCLUSIONS

# Identifier les caractéristiques ayant une corrélation forte
important_features = corr_data[corr_data["correlation"].abs() > 0.2]["feature"].tolist()
print("Caractéristiques déterminantes pour le prix ")
print(important_features)

#  Résumé des principales découvertes
print("CONNAISSANCES FINAUX ")
print(
    f"1. La caractéristique la plus corrélée positivement au prix : {corr_data.iloc[0]['feature']} (r={corr_data.iloc[0]['correlation']:.3f})"
)
print(
    f"2. La caractéristique la plus corrélée négativement : {corr_data.iloc[-1]['feature']} (r={corr_data.iloc[-1]['correlation']:.3f})"
)
print(
    f"3. La RAM diffère significativement entre les téléphones bas de gamme et haut de gamme (p={p_val:.2e})."
)
print(
    "4. Les histogrammes montrent que certaines distributions sont asymétriques (skewness non nul)."
)
print(
    "5. La matrice de corrélation révèle des liaisons intéressantes (ex: RAM ↔ prix)."
)
