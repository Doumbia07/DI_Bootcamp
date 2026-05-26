import pandas as pd
import numpy as np
import os

# EXERCICE 1 : Essai sur l'analyse de données
print("=" * 70)
print("EXERCICE 1 : Introduction à l'analyse de données")
print("=" * 70)
essai = """
Qu'est-ce que l'analyse des données ?
L'analyse des données est le processus d'inspection, de nettoyage, de transformation et de modélisation 
des données afin d'en extraire des informations utiles, de tirer des conclusions et d'éclairer la prise de décision.

Pourquoi est-elle importante dans les contextes modernes ?
Elle permet de passer de décisions intuitives à des décisions fondées sur des preuves, d'identifier des tendances cachées,
d'optimiser les processus (ex: supply chain), de personnaliser l'expérience client et de prédire des comportements futurs.

Trois domaines d'application actuels :
1. Santé : analyse des dossiers patients pour prédire les maladies, améliorer les traitements et gérer les épidémies.
2. Finance : détection de fraudes en temps réel, évaluation du risque de crédit, trading algorithmique.
3. E-commerce / Retail : recommandation de produits (Amazon, Netflix), segmentation client, optimisation des prix et des stocks.
"""
print(essai)

# EXERCICE 2 : Chargement des datasets (Kaggle) – gestion des fichiers absents
print("\n" + "=" * 70)
print("EXERCICE 2 : Chargement des trois jeux de données")
print("=" * 70)

# Liste des noms de fichiers attendus
sleep_file = "How Much Sleep Do Americans Really Get.csv"
mental_file = "Global Trends in Mental Health Disorder.csv"
credit_file = "Credit Card Approvals.csv"


def load_or_dummy(filepath, dummy_data, dummy_desc):
    if os.path.exists(filepath):
        df = pd.read_csv(filepath)
        print(f"✓ Chargé : {filepath}")
    else:
        print(f"⚠ Fichier non trouvé : {filepath}")
        print(f"   → Utilisation de données factices : {dummy_desc}")
        df = pd.DataFrame(dummy_data)
    return df


# Données factices pour que le script continue (colonnes réalistes)
sleep_dummy = {
    "Age": [25, 30, 45, 50, 35],
    "Gender": ["M", "F", "M", "F", "M"],
    "Hours_of_sleep": [7.2, 6.5, 8.1, 5.9, 7.5],
    "Occupation": ["Engineer", "Teacher", "Doctor", "Nurse", "Driver"],
    "Year": [2020, 2021, 2022, 2022, 2023],
}
mental_dummy = {
    "Country": ["USA", "UK", "India", "Brazil", "France"],
    "Year": [2019, 2020, 2021, 2022, 2023],
    "Prevalence": [12.5, 11.2, 15.3, 13.1, 14.0],
    "Disorder": ["Anxiety", "Depression", "Anxiety", "Bipolar", "Depression"],
}
credit_dummy = {
    "Income": [45000, 60000, 35000, 80000, 55000],
    "Debt": [2000, 1500, 5000, 1000, 3000],
    "Credit_Score": [680, 720, 620, 780, 690],
    "Approved": ["Yes", "Yes", "No", "Yes", "No"],
}

sleep_df = load_or_dummy(
    sleep_file, sleep_dummy, "5 personnes (âge, heures de sommeil, etc.)"
)
mental_df = load_or_dummy(
    mental_file, mental_dummy, "pays, année, prévalence des troubles"
)
credit_df = load_or_dummy(
    credit_file, credit_dummy, "revenu, dette, score crédit, approbation"
)

print("\n--- Dataset Sommeil (5 premières lignes) ---")
print(sleep_df.head())
print("\n--- Dataset Santé mentale ---")
print(mental_df.head())
print("\n--- Dataset Cartes de crédit ---")
print(credit_df.head())

print("\nBrève description :")
print(
    "- Sommeil : données sur les heures de sommeil selon âge, sexe, profession, année."
)
print("- Santé mentale : prévalence des troubles par pays et année.")
print("- Cartes de crédit : caractéristiques financières et décision d'approbation.")

# EXERCICE 3 : Classification quantitative / qualitative
print("\n" + "=" * 70)
print("EXERCICE 3 : Classification des colonnes")
print("=" * 70)


def classify(df, name):
    print(f"\n--- {name} ---")
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            print(f"  {col} : quantitative (numérique)")
        else:
            print(f"  {col} : qualitative (catégorielle/texte)")


classify(sleep_df, "Sommeil")
classify(mental_df, "Santé mentale")
classify(credit_df, "Cartes de crédit")

# EXERCICE 4 : Dataset Iris (qualitatif/quantitatif)
print("\n" + "=" * 70)
print("EXERCICE 4 : Dataset Iris (UCI)")
print("=" * 70)

iris_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
iris_cols = [
    "SepalLengthCm",
    "SepalWidthCm",
    "PetalLengthCm",
    "PetalWidthCm",
    "Species",
]
iris = pd.read_csv(iris_url, header=None, names=iris_cols)
print("Premières lignes d'Iris :")
print(iris.head())

print("\nClassification des colonnes :")
for col in iris.columns:
    if col == "Species":
        print(f"  {col} : qualitative (espèce d'iris)")
    else:
        print(f"  {col} : quantitative (longueur/largeur en cm)")

# EXERCICE 5 : Observation (colonnes intéressantes dans dataset sommeil)
print("\n" + "=" * 70)
print("EXERCICE 5 : Colonnes pertinentes pour analyses (dataset sommeil)")
print("=" * 70)

print("Exemples de colonnes intéressantes :")
print(
    "- Analyse de tendance : 'Year' (année) et 'Hours_of_sleep' (heures) → voir évolution dans le temps."
)
print(
    "- Comparaison de groupes : 'Gender' ou 'Occupation' (catégoriel) et 'Hours_of_sleep' → différences entre catégories."
)
print("- Corrélation : 'Age' et 'Hours_of_sleep' → relation âge / temps de sommeil.")
print(
    "Justification : ces choix permettent respectivement de visualiser des tendances, comparer des moyennes et mesurer des liens linéaires."
)

# EXERCICE 6 : Structuré vs non structuré
print("\n" + "=" * 70)
print("EXERCICE 6 : Identification structuré / non structuré")
print("=" * 70)

sources = [
    "Rapports financiers Excel",
    "Photos sur réseau social",
    "Articles de presse",
    "Base de données relationnelle (inventaire)",
    "Enregistrements d'entretiens",
]
reponses = ["Structured", "Unstructured", "Unstructured", "Structured", "Unstructured"]
for s, r in zip(sources, reponses):
    print(f"{s} → {r}")

# EXERCICE 7 : Transformation non structuré → structuré
print("\n" + "=" * 70)
print("EXERCICE 7 : Méthodes de conversion")
print("=" * 70)

transformations = {
    "Blogs de voyage": "NLP (extraction d'entités) → tableau avec destination, date, note, nombre de mots",
    "Appels audio service client": "Reconnaissance vocale + extraction de champs (ID appelant, durée, motif) → base de données relationnelle",
    "Notes manuscrites": "OCR (reconnaissance optique) + étiquetage manuel/auto → fichier CSV avec tags et contenu",
    "Tutoriel vidéo cuisine": "Extraction d'images clés + métadonnées (ingrédients, temps) → table séquentielle des étapes",
}
for k, v in transformations.items():
    print(f"{k} : {v}")

# EXERCICE 8 : Titanic depuis GitHub (comme demandé)
print("\n" + "=" * 70)
print("EXERCICE 8 : Import du Titanic (train.csv depuis GitHub)")
print("=" * 70)

titanic_url = (
    "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
)
titanic = pd.read_csv(titanic_url)
print("Premières lignes du Titanic :")
print(titanic.head())

# EXERCICE 9 : Créer un DataFrame simple et exporter vers Excel et JSON
print("\n" + "=" * 70)
print("EXERCICE 9 : Export Excel et JSON")
print("=" * 70)

df_example = pd.DataFrame(
    {
        "Produit": ["Ordinateur", "Souris", "Clavier"],
        "Prix": [1200, 25, 75],
        "Stock": [10, 100, 50],
    }
)
df_example.to_excel("export_exercice9.xlsx", index=False)
df_example.to_json("export_exercice9.json", orient="records", indent=4)
print("Fichiers générés : 'export_exercice9.xlsx' et 'export_exercice9.json'")

# EXERCICE 10 : Lire des données JSON depuis une URL (exemple public)
print("\n" + "=" * 70)
print("EXERCICE 10 : Lecture JSON depuis URL")
print("=" * 70)

json_url = "https://jsonplaceholder.typicode.com/posts"
json_df = pd.read_json(json_url)
print("5 premières entrées :")
print(json_df.head())

print("\n" + "=" * 70)
print("FIN – Tous les exercices (1 à 10) ont été exécutés avec succès.")
print("=" * 70)
