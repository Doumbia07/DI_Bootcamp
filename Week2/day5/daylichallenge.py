# %% [markdown]
# # Daily Challenge: Interactive Data Visualization with Matplotlib and Seaborn
# ## US Superstore Data Analysis
#
# Ce notebook utilise **Matplotlib** pour les graphiques interactifs (line chart et carte) et **Seaborn** pour les graphiques statiques.

# %% [code]
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from ipywidgets import interact
import mplleaflet  # pour convertir un plot Matplotlib en carte interactive Leaflet
import warnings

warnings.filterwarnings("ignore")


# 1. Data Preparation

df = pd.read_excel("US Superstore data.xls", sheet_name="Orders")
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Order Year"] = df["Order Date"].dt.year
df["Order Month"] = df["Order Date"].dt.to_period("M")
df.drop_duplicates(inplace=True)
print("Dataset shape:", df.shape)

# %% [markdown]
# ## 2. Interactive Line Chart with Matplotlib + ipywidgets

# %% [code]
monthly = df.groupby(["Order Month", "Category"])["Sales"].sum().reset_index()
monthly["Date"] = monthly["Order Month"].dt.to_timestamp()


def plot_sales_trend(category="All"):
    """
    Affiche un graphique linéaire des ventes mensuelles pour une catégorie donnée.

    Paramètres:
    category (str): Nom de la catégorie ('All', 'Furniture', 'Office Supplies', 'Technology')

    Retour:
    None (affiche le graphique)
    """
    plt.figure(figsize=(12, 5))
    if category == "All":
        data = monthly.groupby("Date")["Sales"].sum()
        plt.plot(data.index, data.values, marker="o", linewidth=2, color="steelblue")
        title = "Monthly Sales - All Categories"
    else:
        data = monthly[monthly["Category"] == category].set_index("Date")["Sales"]
        plt.plot(data.index, data.values, marker="o", linewidth=2, color="darkorange")
        title = f"Monthly Sales - {category}"
    plt.title(title, fontsize=14)
    plt.xlabel("Date")
    plt.ylabel("Sales ($)")
    plt.xticks(rotation=45)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()


categories = ["All"] + list(df["Category"].unique())
interact(plot_sales_trend, category=categories)

# %% [markdown]
# ## 3. Interactive Map using Matplotlib + mplleaflet
#
# La librairie `mplleaflet` convertit un tracé Matplotlib (avec des coordonnées géographiques) en une carte interactive Leaflet.

# %% [code]
# Création d'un scatter plot des ventes par état (avec coordonnées approximatives)
# Pour simplifier, on utilise des coordonnées centrales de chaque état (latitude, longitude)
# Ces données sont disponibles via une base intégrée ou on peut les générer à partir de librairies.
# Nous utilisons un dictionnaire simplifié pour les principaux états.

# Coordonnées approximatives (lat, lon) des capitales ou centres des états
state_coords = {
    "California": (36.7783, -119.4179),
    "New York": (40.7128, -74.0060),
    "Texas": (31.9686, -99.9018),
    "Florida": (27.6648, -81.5158),
    "Illinois": (40.6331, -89.3985),
    "Pennsylvania": (41.2033, -77.1945),
    "Ohio": (40.4173, -82.9071),
    "Georgia": (32.1656, -82.9001),
    "North Carolina": (35.7596, -79.0193),
    "Michigan": (44.3148, -85.6024),
    "Virginia": (37.4316, -78.6569),
    "Washington": (47.7511, -120.7401),
    "Massachusetts": (42.4072, -71.3824),
    "Arizona": (34.0489, -111.0937),
    "Tennessee": (35.5175, -86.5804),
    "Indiana": (40.2672, -86.1349),
    "Missouri": (37.9643, -91.8318),
    "Maryland": (39.0458, -76.6413),
    "Wisconsin": (43.7844, -88.7879),
    "Minnesota": (46.7296, -94.6859),
    "Colorado": (39.5501, -105.7821),
    "Alabama": (32.3182, -86.9023),
    "South Carolina": (33.8361, -81.1637),
    "Louisiana": (30.9843, -91.9623),
    "Kentucky": (37.8393, -84.2700),
    "Oregon": (44.0582, -120.9156),
    "Oklahoma": (35.4676, -97.5164),
    "Connecticut": (41.6032, -73.0877),
    "Iowa": (41.8780, -93.0977),
    "Mississippi": (32.3547, -89.3985),
    "Arkansas": (34.9697, -92.3731),
    "Kansas": (39.0119, -98.4842),
    "Utah": (39.3210, -111.0937),
    "Nevada": (38.8026, -116.4194),
    "New Mexico": (34.5199, -105.8701),
    "Nebraska": (41.4925, -99.9018),
    "West Virginia": (38.5976, -80.4549),
    "Idaho": (44.0682, -114.7420),
    "Maine": (45.2538, -69.4455),
    "New Hampshire": (43.1939, -71.5724),
    "Hawaii": (19.8968, -155.5828),
    "Alaska": (64.2008, -149.4937),
}

# Agréger les ventes par état
state_sales = df.groupby("State")["Sales"].sum().reset_index()
# Filtrer les états présents dans le dictionnaire
state_sales = state_sales[state_sales["State"].isin(state_coords.keys())]
state_sales["lat"] = state_sales["State"].apply(lambda x: state_coords[x][0])
state_sales["lon"] = state_sales["State"].apply(lambda x: state_coords[x][1])

# Créer un scatter plot avec Matplotlib
plt.figure(figsize=(10, 8))
sc = plt.scatter(
    state_sales["lon"],
    state_sales["lat"],
    s=state_sales["Sales"] / 1000,  # taille des points proportionnelle aux ventes
    c=state_sales["Sales"],
    cmap="Blues",
    alpha=0.6,
    edgecolors="black",
)
plt.colorbar(sc, label="Total Sales ($)")
plt.title("Sales Distribution by State (size = sales volume)", fontsize=14)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(alpha=0.3)

# Convertir en carte interactive Leaflet
mplleaflet.show()

# %% [markdown]
# ## 4. Seaborn Visualizations (Static)

# %% [code]
# Bar chart: Top 10 products by sales
top_products = df.groupby("Product Name")["Sales"].sum().nlargest(10).reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(data=top_products, y="Product Name", x="Sales", palette="viridis")
plt.title("Top 10 Products by Total Sales", fontsize=14)
plt.xlabel("Sales ($)")
plt.ylabel("Product Name")
plt.tight_layout()
plt.show()

# Scatter plot: Profit vs Discount with regression line
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Discount", y="Profit", alpha=0.5, color="crimson")
sns.regplot(data=df, x="Discount", y="Profit", scatter=False, color="darkblue", ci=None)
plt.axhline(y=0, color="gray", linestyle="--", alpha=0.7)
plt.title("Profit vs Discount (with regression line)", fontsize=14)
plt.xlabel("Discount")
plt.ylabel("Profit ($)")
plt.tight_layout()
plt.show()

# %% [markdown]
# ## 5. Comparative Analysis

# %% [markdown]
# **Analyse comparative : Matplotlib vs Seaborn**
#
# **Matplotlib (graphique linéaire interactif + carte interactive)**
# - *Facilité d'utilisation* : Nécessite plus de code pour obtenir l'interactivité (intégration avec ipywidgets pour la ligne, mplleaflet pour la carte).
# - *Efficacité* : Contrôle total sur les éléments du graphique ; permet un filtrage dynamique avec le dropdown. La carte interactive via mplleaflet reste simple à implémenter.
#
# **Seaborn (diagramme en barres et nuage de points statiques)**
# - *Facilité d'utilisation* : Syntaxe très concise ; une seule ligne produit des graphiques esthétiques.
# - *Efficacité* : Fonctions statistiques intégrées (regplot) et thèmes par défaut de qualité, mais manque d'interactivité.
#
# **Carte interactive** : Réalisée avec Matplotlib + mplleaflet, ce qui respecte la consigne initiale tout en apportant l'interactivité.
#
# **Principaux enseignements**
# - **Tendance des ventes** : Saisonnalité marquée avec des pics en novembre et décembre (effet des fêtes).
# - **Concentration géographique** : La Californie, New York et le Texas sont les États les plus performants.
# - **Concentration produit** : Très peu de produits (ex. photocopieurs Canon, téléphones Cisco) génèrent la majeure partie du chiffre d'affaires.
# - **Impact des remises** : Les remises supérieures à 20 % sont fortement associées à des profits négatifs (voir le nuage de points).
