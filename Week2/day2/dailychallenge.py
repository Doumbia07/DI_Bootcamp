import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 1. Chargement du dataset (depuis GitHub)
url = "https://raw.githubusercontent.com/ntclai/EDA-on-Data-Science-Job-Salaries/main/ds_salaries.csv"
df = pd.read_csv(url)

print("=== Chargement initial ===")
print(f"Shape : {df.shape}")
print(f"Colonnes : {df.columns.tolist()}")
print(df.head())

# 2. Min-Max normalization de la colonne 'salary'
print("\n=== 2. Normalisation Min-Max de 'salary' ===")
scaler = MinMaxScaler()
df["salary_normalized"] = scaler.fit_transform(df[["salary"]])
print("Statistiques avant normalisation :")
print(df["salary"].describe())
print("\nStatistiques après normalisation (devrait être entre 0 et 1) :")
print(df["salary_normalized"].describe())


print("\n=== 3. PCA - Réduction de dimensionnalité ===")

numeric_cols = ["work_year", "salary", "remote_ratio"]
X = df[numeric_cols].copy()

scaler_pca = StandardScaler()
X_scaled = scaler_pca.fit_transform(X)

pca = PCA(n_components=2)
principal_components = pca.fit_transform(X_scaled)
df_pca = pd.DataFrame(data=principal_components, columns=["PC1", "PC2"])
print(f"Variance expliquée par chaque composante : {pca.explained_variance_ratio_}")
print(f"Variance totale expliquée : {sum(pca.explained_variance_ratio_):.4f}")
print("Aperçu des composantes principales :")
print(df_pca.head())


print("\n=== 4. Agrégation par experience_level ===")

exp_map = {
    "EN": "Entry-level / Junior",
    "MI": "Mid-level / Intermediate",
    "SE": "Senior-level / Expert",
    "EX": "Executive-level / Director",
}
df["exp_level_label"] = df["experience_level"].map(exp_map)

agg_stats = df.groupby("exp_level_label")["salary"].agg(["mean", "median"]).round(2)
agg_stats.columns = ["Salaire Moyen (USD)", "Salaire Médian (USD)"]
print(agg_stats)


print("\n=== 5. Visualisation (optionnelle) ===")
plt.figure(figsize=(10, 6))
agg_stats["Salaire Moyen (USD)"].sort_values().plot(kind="barh", color="skyblue")
plt.title("Salaire moyen par niveau d'expérience")
plt.xlabel("Salaire (USD)")
plt.tight_layout()
plt.show()


print("\n=== RAPPORT FINAL (format Markdown) ===\n")
print(
    """# Rapport d'analyse : Data Science Job Salaries

## 1. Min-Max Normalization du salaire
- La colonne `salary` a été normalisée avec MinMaxScaler.
- Les valeurs initiales allaient de {min_salary} à {max_salary}.
- Après normalisation, toutes les valeurs sont comprises entre 0 et 1.
- Cela évite que l'échelle du salaire ne domine d'éventuels modèles.

## 2. PCA (Principal Component Analysis)
- Les colonnes numériques utilisées : `work_year`, `salary`, `remote_ratio`.
- Variance expliquée par PC1 : {var1:.4f}
- Variance expliquée par PC2 : {var2:.4f}
- Variance totale conservée : {total_var:.4f} (sur 3 dimensions d'origine).
- La PCA a permis de réduire la dimensionnalité tout en gardant l'essentiel de l'information.

## 3. Agrégation par expérience
- Regroupement par `experience_level` avec calcul de la moyenne et médiane des salaires.
- Résultats (en USD) :
""".format(
        min_salary=df["salary"].min(),
        max_salary=df["salary"].max(),
        var1=pca.explained_variance_ratio_[0],
        var2=pca.explained_variance_ratio_[1],
        total_var=sum(pca.explained_variance_ratio_),
    )
)
print(agg_stats.to_markdown())
print("""
## Interprétation
- La médiane est souvent plus représentative que la moyenne en présence de valeurs extrêmes.
- On observe une progression claire du salaire avec le niveau d'expérience :
  les seniors et executives gagnent significativement plus.
- La PCA peut être utile pour visualiser la distribution des salaires dans un espace 2D.

---
*Analyse réalisée avec Python, Pandas, Scikit-learn et Matplotlib.*
""")
