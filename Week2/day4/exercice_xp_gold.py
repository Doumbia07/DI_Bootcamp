# EXERCICES COMPLETS : VISUALISATION AVANCÉE ET INDEXATION HIÉRARCHIQUE

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# EXERCICE 1 : BAR GRAPH (Ventes par catégorie de produit)
print("\n" + "=" * 60)
print("EXERCICE 1 : BAR GRAPH - Ventes par catégorie")
print("=" * 60)

categories = ["Électronique", "Vêtements", "Maison", "Sports", "Jouets"]
ventes = [12500, 9800, 10500, 7200, 4300]

plt.figure(figsize=(8, 5))
plt.bar(categories, ventes, color="teal", edgecolor="black")
plt.xlabel("Catégories de produits", fontsize=12)
plt.ylabel("Ventes totales ($)", fontsize=12)
plt.title("Ventes par catégorie - Données fictives", fontsize=14, fontweight="bold")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# EXERCICE 2 : INDEXATION HIÉRARCHIQUE (Températures >30°C au Canada)
print("\n" + "=" * 60)
print("EXERCICE 2 : Filtrage avec index hiérarchique (températures)")
print("=" * 60)

# Création d'un DataFrame avec index multi-niveaux
np.random.seed(42)
dates = pd.date_range("2023-07-01", "2023-07-10", freq="D")
countries = ["Canada", "USA"]
cities_canada = ["Toronto", "Montreal", "Vancouver"]
cities_usa = ["New York", "Los Angeles"]

index = []
for country in countries:
    if country == "Canada":
        cities = cities_canada
    else:
        cities = cities_usa
    for city in cities:
        for date in dates:
            index.append((country, city, date))

df_temp = pd.DataFrame(
    index=pd.MultiIndex.from_tuples(index, names=["Country", "City", "Date"]),
    data={"Temperature_C": np.random.uniform(20, 35, len(index))},
)

# Filtrage : Canada, température > 30°C
filtered = df_temp.xs("Canada", level="Country").query("Temperature_C > 30")

print("Jours avec température > 30°C au Canada :")
print(filtered)
print(
    "\nExplication : L'indexation hiérarchique permet de filtrer rapidement à différents niveaux"
)
print(
    "(pays, ville, date) sans avoir à créer des colonnes supplémentaires ou à utiliser des jointures complexes."
)

# EXERCICE 3 : FILTRAGE AVANCÉ AVEC INDEX HIÉRARCHIQUE (Salary > 50k par département)
print("\n" + "=" * 60)
print("EXERCICE 3 : Filtrage 'Salary > 50 000' par département")
print("=" * 60)

# Création d'un DataFrame hiérarchique pour les employés
departments = ["IT", "HR", "Sales", "Marketing"]
employees = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
np.random.seed(0)

rows = []
for dept in departments:
    for emp in employees:
        rows.append((dept, emp))

df_salary = pd.DataFrame(
    index=pd.MultiIndex.from_tuples(rows, names=["Department", "Employee"]),
    data={"Salary": np.random.randint(30000, 90000, len(rows))},
)

print("DataFrame original :")
print(df_salary.head(10))

# Filtrage : Salary > 50000 pour chaque département
filtered_salary = df_salary[df_salary["Salary"] > 50000]
print("\nEmployés avec salaire > 50 000 :")
print(filtered_salary)

print(
    "\nDémonstration : L'index hiérarchique permet de filtrer directement sur la valeur sans"
)
print(
    "manipuler les colonnes de groupe séparément. On peut aussi utiliser .xs() ou .query() par niveau."
)

# EXERCICE 4 : DISTRIBUTION DES DURÉES DES FILMS MCU (avec KDE)
print("\n" + "=" * 60)
print("EXERCICE 4 : Distribution des durées des films MCU")
print("=" * 60)

# Création d'un jeu de données fictif des films MCU
mcu_movies = pd.DataFrame(
    {
        "Movie": [
            "Iron Man",
            "The Incredible Hulk",
            "Iron Man 2",
            "Thor",
            "Captain America",
            "The Avengers",
            "Iron Man 3",
            "Thor 2",
            "Captain America 2",
            "Guardians of the Galaxy",
        ],
        "Duration_min": [126, 112, 124, 115, 124, 143, 130, 112, 136, 121],
        "Tomato_Meter": [94, 67, 72, 77, 80, 91, 79, 66, 89, 92],
        "Audience_Score": [91, 71, 74, 76, 74, 86, 78, 69, 88, 92],
        "Production_Budget_M": [140, 150, 170, 150, 140, 220, 200, 170, 170, 170],
        "Opening_Weekend_M": [98, 55, 128, 65, 65, 207, 174, 85, 95, 94],
        "Domestic_Box_Office_M": [318, 134, 312, 181, 176, 623, 409, 206, 259, 333],
        "Worldwide_Box_Office_M": [585, 263, 623, 449, 370, 1518, 1214, 644, 714, 773],
        "Phase": [1, 1, 1, 1, 1, 1, 2, 2, 2, 2],
    }
)

plt.figure(figsize=(10, 6))
sns.histplot(
    mcu_movies["Duration_min"], kde=True, bins=8, color="purple", edgecolor="black"
)
plt.title(
    "Distribution des durées des films MCU (avec KDE)", fontsize=14, fontweight="bold"
)
plt.xlabel("Durée (minutes)")
plt.ylabel("Fréquence")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# EXERCICE 5 : BOX PLOT - Tomatometer vs Audience Score
print("\n" + "=" * 60)
print("EXERCICE 5 : Box plot comparatif (Tomato Meter vs Audience Score)")
print("=" * 60)

# Melt des deux colonnes pour le boxplot
scores_melted = mcu_movies.melt(
    id_vars=["Movie"],
    value_vars=["Tomato_Meter", "Audience_Score"],
    var_name="Score_Type",
    value_name="Score",
)

plt.figure(figsize=(8, 6))
sns.boxplot(data=scores_melted, x="Score_Type", y="Score", palette="Set2")
plt.title(
    "Comparaison des scores Tomato Meter et Audience", fontsize=14, fontweight="bold"
)
plt.xlabel("Type de score")
plt.ylabel("Score (%)")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# EXERCICE 6 : PAIR PLOT DES DONNÉES FINANCIÈRES (par phase MCU)
print("\n" + "=" * 60)
print("EXERCICE 6 : Pair plot des métriques financières (hue = Phase)")
print("=" * 60)

# Sélection des colonnes pertinentes
financial_cols = [
    "Production_Budget_M",
    "Opening_Weekend_M",
    "Domestic_Box_Office_M",
    "Worldwide_Box_Office_M",
]

# Création du pair plot
sns.set_style("whitegrid")
pair_plot = sns.pairplot(
    mcu_movies[financial_cols + ["Phase"]],
    hue="Phase",
    diag_kind="hist",
    palette="husl",
    plot_kws={"alpha": 0.6, "s": 50},
)
pair_plot.fig.suptitle(
    "Relations entre métriques financières (colorées par Phase MCU)",
    y=1.02,
    fontsize=14,
    fontweight="bold",
)
plt.tight_layout()
plt.show()

print("\nObservations sur le pair plot :")
print(
    "- Les budgets de production sont fortement corrélés avec les box office mondiaux."
)
print(
    "- Les phases plus récentes (Phase 2) montrent des budgets et revenus plus élevés."
)
print("- La phase 1 a une plus grande variabilité dans les recettes d'ouverture.")

print("\n" + "=" * 60)
print("FIN DES EXERCICES - TOUS LES GRAPHIQUES ONT ÉTÉ GÉNÉRÉS")
print("=" * 60)
