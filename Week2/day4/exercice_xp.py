# EXERCICES COMPLETS : VISUALISATION DE DONNÉES AVEC PYTHON

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# EXERCICE 1 : Comprendre la visualisation des données
print("\n" + "=" * 60)
print("EXERCICE 1 : IMPORTANCE DE LA VISUALISATION")
print("=" * 60)

print("""
Pourquoi la visualisation des données est-elle importante ?
- Elle permet de détecter rapidement des tendances, des anomalies ou des corrélations.
- Elle facilite la communication de résultats complexes à un public non technique.
- Elle aide à la prise de décision basée sur les données.
- Elle permet d'explorer et de comprendre la structure d'un jeu de données.

Quel est le but d'un graphique linéaire (line graph) ?
- Un graphique linéaire sert principalement à montrer l'évolution d'une variable 
  quantitative en fonction d'une autre variable continue, souvent le temps.
- Il permet de visualiser des tendances, des cycles, des augmentations ou 
  des diminutions sur une période donnée.
""")

# EXERCICE 2 : Tracé linéaire des températures de la semaine
print("\n" + "=" * 60)
print("EXERCICE 2 : LINE PLOT - TEMPÉRATURES DE LA SEMAINE")
print("=" * 60)

jours = ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"]
temperatures = [72, 74, 76, 80, 82, 78, 75]

plt.figure(figsize=(8, 5))
plt.plot(jours, temperatures, marker="o", linestyle="-", color="orange", linewidth=2)
plt.xlabel("Jour")
plt.ylabel("Température (°F)")
plt.title("Variation des températures sur une semaine")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

# EXERCICE 3 : Diagramme en barres des ventes mensuelles
print("\n" + "=" * 60)
print("EXERCICE 3 : BAR CHART - VENTES MENSUELLES")
print("=" * 60)

mois = ["Jan", "Fév", "Mar", "Avr", "Mai"]
ventes = [5000, 5500, 6200, 7000, 7500]

plt.figure(figsize=(8, 5))
plt.bar(mois, ventes, color="skyblue", edgecolor="black")
plt.xlabel("Mois")
plt.ylabel("Montant des ventes ($)")
plt.title("Ventes mensuelles d’un magasin")
plt.tight_layout()
plt.show()

# EXERCICES 4, 5, 6 : Dataset "Student Mental Health"
print("\n" + "=" * 60)
print("EXERCICES 4,5,6 : ANALYSE DU DATASET SUR LA SANTÉ MENTALE DES ÉTUDIANTS")
print("=" * 60)

# Chargement du dataset (à adapter selon le chemin de votre fichier)
# Remplacez 'student_mental_health.csv' par le vrai nom du fichier
try:
    df = pd.read_csv("student_mental_health.csv")
    print("Fichier chargé avec succès.")
except FileNotFoundError:
    print("""ERREUR : Le fichier 'student_mental_health.csv' n'a pas été trouvé.
Assurez-vous d'avoir téléchargé le dataset et de l'avoir placé dans le même répertoire.
Vous pouvez aussi modifier le chemin dans le code.""")

    # Création d'un petit jeu de données factice pour démonstration (optionnel)
    print("\nCréation d'un dataset factice pour la démonstration des graphiques.")
    import numpy as np

    np.random.seed(42)
    n = 200
    df = pd.DataFrame(
        {
            "CGPA": np.random.uniform(2.0, 9.5, n),
            "Do you have Anxiety?": np.random.choice(["Yes", "No"], n, p=[0.35, 0.65]),
            "Choose your gender": np.random.choice(
                ["Male", "Female", "Other"], n, p=[0.45, 0.50, 0.05]
            ),
            "Age": np.random.randint(18, 30, n),
            "Do you have Panic Attacks?": np.random.choice(
                ["Yes", "No"], n, p=[0.25, 0.75]
            ),
        }
    )
    print("Dataset factice prêt (200 étudiants).\n")

# EXERCICE 4 : Histogramme de la distribution du CGPA
print("\n--- EXERCICE 4 : Histogramme du CGPA ---")

plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="CGPA", bins=15, color="green", edgecolor="black", alpha=0.7)
plt.title("Distribution des CGPA des étudiants")
plt.xlabel("CGPA")
plt.ylabel("Fréquence")
plt.tight_layout()
plt.show()

# EXERCICE 5 : Comparaison de l’anxiété selon le genre
print("\n--- EXERCICE 5 : Anxiété selon le genre ---")

plt.figure(figsize=(8, 5))
sns.countplot(
    data=df,
    x="Choose your gender",
    hue="Do you have Anxiety?",
    palette="Set2",
    edgecolor="black",
)
plt.title("Présence d’anxiété selon le genre")
plt.xlabel("Genre")
plt.ylabel("Nombre d'étudiants")
plt.legend(title="Anxiété", labels=["Non", "Oui"])
plt.tight_layout()
plt.show()

# EXERCICE 6 : Relation entre l’âge et les crises de panique
print("\n--- EXERCICE 6 : Âge vs Crises de panique ---")

# Convertir la colonne 'Do you have Panic Attacks?' en numérique
df["Panic_Numeric"] = df["Do you have Panic Attacks?"].map({"Yes": 1, "No": 0})

plt.figure(figsize=(8, 5))
sns.stripplot(
    data=df,
    x="Age",
    y="Panic_Numeric",
    jitter=True,
    alpha=0.6,
    color="crimson",
    edgecolor="black",
)
plt.title("Relation entre l’âge et les crises de panique")
plt.xlabel("Âge")
plt.ylabel("Crises de panique (1 = Oui, 0 = Non)")
plt.yticks([0, 1], ["Non", "Oui"])
plt.tight_layout()
plt.show()

print("\n" + "=" * 60)
print("FIN DES EXERCICES - TOUS LES GRAPHIQUES ONT ÉTÉ AFFICHÉS")
print("=" * 60)
