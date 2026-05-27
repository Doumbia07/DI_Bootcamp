import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Chargement du dataset Titanic (train.csv)
# Source : fichier brut de Kaggle (via GitHub)
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print("=== Chargement initial ===")
print(f"Shape : {df.shape}")
print(f"Colonnes : {df.columns.tolist()}")
print(df.head())

# EXERCICE 1 : Détection et suppression des doublons
print("\n=== EXERCICE 1 : Doublons ===")
initial_rows = df.shape[0]
duplicates = df.duplicated().sum()
print(f"Nombre de lignes dupliquées (toutes colonnes) : {duplicates}")

# Suppression des doublons
df = df.drop_duplicates()
print(
    f"Lignes après suppression : {df.shape[0]} (supprimées : {initial_rows - df.shape[0]})"
)

# EXERCICE 2 : Gestion des valeurs manquantes
print("\n=== EXERCICE 2 : Valeurs manquantes ===")
missing_before = df.isnull().sum()
print("Avant traitement :\n", missing_before[missing_before > 0])


df.drop("Cabin", axis=1, inplace=True)

# Imputation Age par médiane
median_age = df["Age"].median()
df["Age"].fillna(median_age, inplace=True)

# Imputation Embarked par le mode
mode_embarked = df["Embarked"].mode()[0]
df["Embarked"].fillna(mode_embarked, inplace=True)

missing_after = df.isnull().sum()
print("\nAprès traitement :\n", missing_after[missing_after > 0])
print("Aucune valeur manquante restante (sauf si d'autres colonnes)")

# EXERCICE 3 : Feature Engineering (nouveaux attributs, encodage)
print("\n=== EXERCICE 3 : Feature Engineering ===")

# 3.1 Taille de la famille (FamilySize = SibSp + Parch + 1)
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1


# 3.2 Extraction du titre (Mr, Mrs, Miss, Master, ...) depuis le nom
def extract_title(name):
    # Ex: "Braund, Mr. Owen Harris" -> "Mr"
    title = name.split(",")[1].split(".")[0].strip()
    return title


df["Title"] = df["Name"].apply(extract_title)

# Regroupement des titres rares
title_counts = df["Title"].value_counts()
rare_titles = title_counts[title_counts < 10].index
df["Title"] = df["Title"].replace(rare_titles, "Rare")


title_dummies = pd.get_dummies(df["Title"], prefix="Title")
df = pd.concat([df, title_dummies], axis=1)
df.drop("Title", axis=1, inplace=True)

print("Nouveaux attributs créés : FamilySize, Title (encodé en one-hot)")
print(f"Shape après feature engineering : {df.shape}")

# EXERCICE 4 : Détection et traitement des outliers (Fare, Age)
print("\n=== EXERCICE 4 : Outliers sur Fare et Age ===")

# 4.1 Visualisation avant traitement
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
sns.boxplot(x=df["Fare"], ax=axes[0])
axes[0].set_title("Fare - avant traitement")
sns.boxplot(x=df["Age"], ax=axes[1])
axes[1].set_title("Age - avant traitement")
plt.tight_layout()
plt.show()

# On explore avec df.quantile()
fare_98 = df["Fare"].quantile(0.98)
age_98 = df["Age"].quantile(0.98)
print(f"Quantile 0.98 de Fare : {fare_98:.2f}")
print(f"Quantile 0.98 de Age : {age_98:.2f}")

# 4.3 Capping (plafonnement) des outliers
df["Fare_capped"] = df["Fare"].clip(upper=fare_98)
df["Age_capped"] = df["Age"].clip(upper=age_98)

# Comparaison avant/après
print("\nStatistiques Fare (avant capping) :")
print(df["Fare"].describe())
print("\nStatistiques Fare (après capping 0.98) :")
print(df["Fare_capped"].describe())

print("\nStatistiques Age (avant capping) :")
print(df["Age"].describe())
print("\nStatistiques Age (après capping 0.98) :")
print(df["Age_capped"].describe())

# On remplace les colonnes originales par les versions capées
df["Fare"] = df["Fare_capped"]
df["Age"] = df["Age_capped"]
df.drop(["Fare_capped", "Age_capped"], axis=1, inplace=True)

# Visualisation après traitement
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
sns.boxplot(x=df["Fare"], ax=axes[0])
axes[0].set_title("Fare - après capping")
sns.boxplot(x=df["Age"], ax=axes[1])
axes[1].set_title("Age - après capping")
plt.tight_layout()
plt.show()

# EXERCICE 5 : Standardisation et Normalisation des features numériques
print("\n=== EXERCICE 5 : Standardisation / Normalisation ===")

# Copie pour éviter les avertissements
df_scaled = df.copy()

# StandardScaler sur Age
scaler_std = StandardScaler()
df_scaled["Age_scaled"] = scaler_std.fit_transform(df[["Age"]])

# MinMaxScaler sur Fare
scaler_mm = MinMaxScaler()
df_scaled["Fare_scaled"] = scaler_mm.fit_transform(df[["Fare"]])

# On remplace les colonnes originales ou on conserve les deux
# On garde les versions originales ET les versions scalées
df["Age_scaled"] = df_scaled["Age_scaled"]
df["Fare_scaled"] = df_scaled["Fare_scaled"]

print(
    "Nouvelles colonnes créées : Age_scaled (StandardScaler), Fare_scaled (MinMaxScaler)"
)
print("Exemple des premières valeurs scalées :")
print(df[["Age", "Age_scaled", "Fare", "Fare_scaled"]].head())

# EXERCICE 6 : Encodage final des variables catégorielles restantes
print("\n=== EXERCICE 6 : Encodage catégoriel final ===")

# One-hot encoding pour Sex et Embarked
categorical_cols = ["Sex", "Embarked"]
df_encoded = pd.get_dummies(df, columns=categorical_cols, prefix=categorical_cols)

# Vérification : les colonnes originales ont été remplacées par des dummies
print("Colonnes après one-hot encoding :")
print([col for col in df_encoded.columns if "Sex_" in col or "Embarked_" in col])

# On remplace df par la version encodée
df = df_encoded.copy()
print(f"Shape finale après encodage : {df.shape}")

# EXERCICE 7 : Transformation de l'âge en tranches (Age groups)
print("\n=== EXERCICE 7 : Tranches d'âge (age groups) ===")

# Définition des bins et des libellés
bins = [0, 12, 18, 60, 100]
labels = ["child", "teen", "adult", "senior"]

# Création de la colonne catégorielle
df["AgeGroup"] = pd.cut(df["Age"], bins=bins, labels=labels, right=False)

# One-hot encoding des tranches d'âge
agegroup_dummies = pd.get_dummies(df["AgeGroup"], prefix="AgeGroup")
df = pd.concat([df, agegroup_dummies], axis=1)
df.drop("AgeGroup", axis=1, inplace=True)

print("Tranches d'âge créées : child, teen, adult, senior (one-hot encodées)")
print("Colonnes ajoutées :", [col for col in df.columns if "AgeGroup_" in col])

# Affichage final : aperçu du dataset prétraité
print("\n=== RÉSUMÉ FINAL ===")
print(f"Dimensions finales : {df.shape}")
print("\n5 premières lignes :")
print(df.head())

# Sauvegarde optionnelle
df.to_csv("titanic_preprocessed.csv", index=False)
