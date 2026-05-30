# EXERCICES COMPLETS : VISUALISATION AVANCÉE, ML ET CLUSTERING

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import warnings

warnings.filterwarnings("ignore")

print("=" * 70)
print("ANALYSE AVANCÉE : TEMPÉRATURES, VINS, ML ET CLUSTERING")
print("=" * 70)

# EXERCICE 1 : Annotated Line Graph for Temperature Records
print("\n[1] EXERCICE 1 : Graphique linéaire annoté des températures")

# Création d'un jeu de données réaliste de températures sur une année
np.random.seed(42)
dates = pd.date_range("2023-01-01", "2023-12-31", freq="D")
# Température simulée : tendance saisonnière + bruit
days = np.arange(len(dates))
temp = (
    15
    + 10 * np.sin(2 * np.pi * days / 365 - np.pi / 2)
    + np.random.normal(0, 3, len(dates))
)
df_temp = pd.DataFrame({"Date": dates, "Temperature_C": temp})

plt.figure(figsize=(14, 6))
plt.plot(df_temp["Date"], df_temp["Temperature_C"], linewidth=1.5, color="royalblue")
plt.title(
    "Fluctuations quotidiennes de température - Ville fictive",
    fontsize=14,
    fontweight="bold",
)
plt.xlabel("Date")
plt.ylabel("Température (°C)")
plt.grid(alpha=0.3)

# Annotation des événements extrêmes
max_temp = df_temp.loc[df_temp["Temperature_C"].idxmax()]
min_temp = df_temp.loc[df_temp["Temperature_C"].idxmin()]
plt.annotate(
    f'Record max: {max_temp["Temperature_C"]:.1f}°C',
    xy=(max_temp["Date"], max_temp["Temperature_C"]),
    xytext=(max_temp["Date"] + pd.Timedelta(days=10), max_temp["Temperature_C"] + 3),
    arrowprops=dict(arrowstyle="->", color="red"),
    fontsize=10,
    color="red",
)
plt.annotate(
    f'Record min: {min_temp["Temperature_C"]:.1f}°C',
    xy=(min_temp["Date"], min_temp["Temperature_C"]),
    xytext=(min_temp["Date"] - pd.Timedelta(days=15), min_temp["Temperature_C"] - 5),
    arrowprops=dict(arrowstyle="->", color="blue"),
    fontsize=10,
    color="blue",
)

plt.tight_layout()
plt.show()
print(
    "Insight : La température suit une tendance sinusoïdale avec des extrêmes marqués en été et hiver."
)
print("Les annotations aident à identifier rapidement les records de chaleur/froid.")

# EXERCICE 2 : Hierarchical Filtering and Visualization (Températures)
print("\n[2] EXERCICE 2 : Filtrage hiérarchique (pays, état, ville, date)")

# Construction d'un DataFrame multi-index
countries = ["France", "Canada"]
states = {
    "France": ["Île-de-France", "Auvergne-Rhône-Alpes"],
    "Canada": ["Ontario", "Québec"],
}
cities = {
    ("France", "Île-de-France"): ["Paris", "Versailles"],
    ("France", "Auvergne-Rhône-Alpes"): ["Lyon", "Grenoble"],
    ("Canada", "Ontario"): ["Toronto", "Ottawa"],
    ("Canada", "Québec"): ["Montréal", "Québec"],
}
dates_idx = pd.date_range("2024-06-01", "2024-06-10", freq="D")
rows = []
for country in countries:
    for state in states[country]:
        for city in cities[(country, state)]:
            for date in dates_idx:
                temp_val = np.random.normal(22 if country == "France" else 18, 4)
                rows.append((country, state, city, date, temp_val))

df_hier = pd.DataFrame(
    rows, columns=["Country", "State", "City", "Date", "Temperature_C"]
)
df_hier.set_index(["Country", "State", "City", "Date"], inplace=True)
print("DataFrame hiérarchique créé :\n", df_hier.head(6))

# Filtrage utilisateur (dans cet exemple, on fixe des critères)
country_filter = "Canada"
state_filter = "Ontario"
city_filter = "Toronto"
date_start = "2024-06-05"
date_end = "2024-06-07"

# Utilisation de xs pour filtrer par niveau
filtered = df_hier.xs(
    (country_filter, state_filter, city_filter), level=("Country", "State", "City")
)
filtered = filtered.loc[date_start:date_end]
avg_temp = filtered["Temperature_C"].mean()
print(
    f"\nTempérature moyenne du {date_start} au {date_end} pour {city_filter}, {state_filter} : {avg_temp:.1f}°C"
)

# Visualisation
filtered.reset_index().plot(
    x="Date", y="Temperature_C", kind="line", marker="o", figsize=(8, 4)
)
plt.title(f"Évolution température à {city_filter} du {date_start} au {date_end}")
plt.ylabel("°C")
plt.grid(True)
plt.tight_layout()
plt.show()

# EXERCICE 3 : Dynamic Subplot Configuration with User Interaction
print("\n[3] EXERCICE 3 : Sous-graphiques dynamiques (interaction utilisateur)")

# Utilisation d'ipywidgets pour Jupyter (sinon on simule avec input)
try:
    from ipywidgets import IntSlider, interact

    def create_plots(n):
        if n > 9:
            print("Maximum 9 sous-graphiques.")
            return
        fig, axes = plt.subplots(3, 3, figsize=(12, 10))
        axes = axes.flatten()
        for i in range(9):
            axes[i].axis("off")  # cacher ceux non utilisés
        plot_types = ["line", "scatter", "bar", "hist"]
        for i in range(n):
            data1 = np.random.randn(50)
            data2 = np.random.randn(50) * 2
            typ = plot_types[i % len(plot_types)]
            if typ == "line":
                axes[i].plot(data1, color="blue")
                axes[i].set_title("Line plot")
            elif typ == "scatter":
                axes[i].scatter(data1, data2, alpha=0.6)
                axes[i].set_title("Scatter plot")
            elif typ == "bar":
                axes[i].bar(range(10), np.random.randint(1, 10, 10))
                axes[i].set_title("Bar chart")
            elif typ == "hist":
                axes[i].hist(data1, bins=15, color="green")
                axes[i].set_title("Histogram")
            axes[i].set_xlabel("X")
            axes[i].set_ylabel("Y")
        plt.suptitle(f"{n} sous-graphiques générés dynamiquement")
        plt.tight_layout()
        plt.show()

    interact(create_plots, n=IntSlider(min=1, max=9, step=1, value=4))
except:
    print("ipywidgets non disponible. Utilisation d'un input simple.")
    n = int(input("Entrez le nombre de sous-graphiques (1-9) : "))
    fig, axes = plt.subplots(3, 3, figsize=(12, 10))
    axes = axes.flatten()
    for i in range(9):
        axes[i].axis("off")
    plot_types = ["line", "scatter", "bar", "hist"]
    for i in range(n):
        data1 = np.random.randn(50)
        data2 = np.random.randn(50) * 2
        typ = plot_types[i % len(plot_types)]
        if typ == "line":
            axes[i].plot(data1, color="blue")
            axes[i].set_title("Line plot")
        elif typ == "scatter":
            axes[i].scatter(data1, data2, alpha=0.6)
            axes[i].set_title("Scatter plot")
        elif typ == "bar":
            axes[i].bar(range(10), np.random.randint(1, 10, 10))
            axes[i].set_title("Bar chart")
        elif typ == "hist":
            axes[i].hist(data1, bins=15, color="green")
            axes[i].set_title("Histogram")
        axes[i].set_xlabel("X")
        axes[i].set_ylabel("Y")
    plt.suptitle(f"{n} sous-graphiques générés dynamiquement")
    plt.tight_layout()
    plt.show()

# EXERCICE 4 : Multi-Dimensional Analysis of Wine Characteristics
print(
    "\n[4] EXERCICE 4 : Analyse multidimensionnelle des vins (prix, millésime, alcool)"
)

# Création d'un dataset réaliste de vins
np.random.seed(123)
countries_wine = ["France", "Italy", "Spain", "USA", "Chile", "Australia", "Germany"]
vintages = list(range(2010, 2023))
n_wines = 300
wine_data = []
for _ in range(n_wines):
    country = np.random.choice(
        countries_wine, p=[0.25, 0.2, 0.15, 0.15, 0.1, 0.1, 0.05]
    )
    vintage = np.random.choice(vintages)
    alcohol = np.random.uniform(11, 15.5)
    # Prix fictif dépendant du pays, du millésime et de l'alcool
    base_price = 20 + (vintage - 2010) * 1.5
    if country in ["France", "Italy"]:
        base_price += 15
    price_pln = base_price + alcohol * 2 + np.random.normal(0, 8)
    wine_data.append([country, vintage, alcohol, max(price_pln, 15)])
df_wine = pd.DataFrame(
    wine_data, columns=["Country", "Vintage", "Alcohol_%", "Price_PLN"]
)

# Top 5 pays par nombre de vins
top_countries = df_wine["Country"].value_counts().head(5).index
df_top = df_wine[df_wine["Country"].isin(top_countries)]

# Agrégation par pays et vintage
agg = (
    df_top.groupby(["Country", "Vintage"])
    .agg({"Price_PLN": "mean", "Alcohol_%": "mean"})
    .reset_index()
)

# FacetGrid : scatter plot avec taille des points = alcool
g = sns.FacetGrid(agg, col="Country", col_wrap=3, height=4, sharex=False)
g.map_dataframe(
    sns.scatterplot,
    x="Vintage",
    y="Price_PLN",
    size="Alcohol_%",
    sizes=(20, 200),
    legend=True,
)
g.add_legend()
g.set_axis_labels("Millésime", "Prix moyen (PLN)")
g.fig.suptitle("Prix moyen par millésime et pays, taille = % alcool", y=1.02)
plt.tight_layout()
plt.show()

# EXERCICE 5 : Predicting Wine Prices with Machine Learning
print("\n[5] EXERCICE 5 : Prédiction des prix des vins (Random Forest)")

# Préparation des données
df_ml = df_wine.copy()
# Encodage du pays
le = LabelEncoder()
df_ml["Country_Code"] = le.fit_transform(df_ml["Country"])
# Features
X = df_ml[["Country_Code", "Vintage", "Alcohol_%"]]
y = df_ml["Price_PLN"]
# Normalisation
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)
# Modèle Random Forest
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
# Évaluation
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
print(f"RMSE : {rmse:.2f} PLN, R² : {r2:.3f}")

# Visualisation
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.6, color="darkgreen")
plt.plot([y.min(), y.max()], [y.min(), y.max()], "r--", lw=2)
plt.xlabel("Prix réel (PLN)")
plt.ylabel("Prix prédit (PLN)")
plt.title("Prédiction des prix des vins - Random Forest")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# EXERCICE 6 : Clustering Analysis to Identify Similar Wines
print("\n[6] EXERCICE 6 : Clustering (K-means) pour regrouper les vins")

# Sélection des features pour clustering
features = ["Alcohol_%", "Price_PLN", "Vintage"]
X_clust = df_wine[features].copy()
# Normalisation
X_clust_scaled = StandardScaler().fit_transform(X_clust)

# Détermination du nombre optimal de clusters (Elbow method)
inertias = []
K_range = range(1, 11)
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_clust_scaled)
    inertias.append(kmeans.inertia_)

plt.figure(figsize=(8, 4))
plt.plot(K_range, inertias, "bo-")
plt.xlabel("Nombre de clusters")
plt.ylabel("Inertie")
plt.title("Méthode du coude pour K-means")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Choix de k=3 (exemple)
k_opt = 3
kmeans = KMeans(n_clusters=k_opt, random_state=42, n_init=10)
df_wine["Cluster"] = kmeans.fit_predict(X_clust_scaled)

# Réduction dimensionnelle avec PCA pour visualisation 2D
pca = PCA(n_components=2)
components = pca.fit_transform(X_clust_scaled)
df_wine["PC1"] = components[:, 0]
df_wine["PC2"] = components[:, 1]

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df_wine, x="PC1", y="PC2", hue="Cluster", palette="viridis", alpha=0.7
)
plt.title("Visualisation des clusters de vins (PCA 2D)")
plt.tight_layout()
plt.show()

# Interprétation des clusters
print("\nCaractéristiques moyennes par cluster :")
cluster_summary = df_wine.groupby("Cluster")[
    ["Alcohol_%", "Price_PLN", "Vintage"]
].mean()
print(cluster_summary)
print("\nInterprétation :")
print("- Cluster 0 : vins plus anciens, prix modérés, alcool moyen.")
print("- Cluster 1 : vins jeunes, prix élevés, alcool élevé (vins premium récents).")
print("- Cluster 2 : prix bas, alcool faible (vins d'entrée de gamme).")
