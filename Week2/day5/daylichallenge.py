import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from ipywidgets import interact
import plotly.express as px
import warnings

warnings.filterwarnings("ignore")

# 1. Data Preparation
df = pd.read_excel("US Superstore data.xls", sheet_name="Orders")
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Order Year"] = df["Order Date"].dt.year
df["Order Month"] = df["Order Date"].dt.to_period("M")
df.drop_duplicates(inplace=True)
print("Dataset shape:", df.shape)

# 2. Interactive Line Chart (Matplotlib + ipywidgets)
monthly_sales = df.groupby(["Order Month", "Category"])["Sales"].sum().reset_index()
monthly_sales["Date"] = monthly_sales["Order Month"].dt.to_timestamp()


def plot_sales_trend(category="All"):
    plt.figure(figsize=(12, 5))
    if category == "All":
        data = monthly_sales.groupby("Date")["Sales"].sum()
        plt.plot(data.index, data.values, marker="o", linewidth=2, color="steelblue")
        title = "Monthly Sales Trend - All Categories"
    else:
        data = monthly_sales[monthly_sales["Category"] == category].set_index("Date")[
            "Sales"
        ]
        plt.plot(data.index, data.values, marker="o", linewidth=2, color="darkorange")
        title = f"Monthly Sales Trend - {category}"
    plt.title(title, fontsize=14)
    plt.xlabel("Date")
    plt.ylabel("Sales ($)")
    plt.xticks(rotation=45)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()


categories = ["All"] + list(df["Category"].unique())
interact(plot_sales_trend, category=categories)

# 3. Interactive Map (Plotly) - Sales by State
state_sales = df.groupby("State")["Sales"].sum().reset_index()
fig = px.choropleth(
    state_sales,
    locations="State",
    locationmode="USA-states",
    color="Sales",
    scope="usa",
    title="Sales Distribution by State",
    color_continuous_scale="Blues",
    labels={"Sales": "Total Sales ($)"},
)
fig.show()

# 4. Seaborn Bar Chart: Top 10 Products by Sales
top_products = df.groupby("Product Name")["Sales"].sum().nlargest(10).reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(data=top_products, y="Product Name", x="Sales", palette="viridis")
plt.title("Top 10 Products by Total Sales", fontsize=14)
plt.xlabel("Sales ($)")
plt.ylabel("Product Name")
plt.tight_layout()
plt.show()

# 5. Seaborn Scatter Plot: Profit vs Discount
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Discount", y="Profit", alpha=0.5, color="crimson")
sns.regplot(data=df, x="Discount", y="Profit", scatter=False, color="darkblue", ci=None)
plt.axhline(y=0, color="gray", linestyle="--", alpha=0.7)
plt.title("Profit vs Discount (with regression line)", fontsize=14)
plt.xlabel("Discount")
plt.ylabel("Profit ($)")
plt.tight_layout()
plt.show()

""""
Analyse comparative : Matplotlib vs Seaborn

Matplotlib (graphique linéaire interactif)
- Facilité d'utilisation : nécessite plus de code pour obtenir l'interactivité (intégration avec ipywidgets).
- Efficacité : contrôle total sur les éléments du graphique ; le menu déroulant permet un filtrage dynamique, très utile pour l'exploration.

Seaborn (diagramme en barres et nuage de points statiques)
- Facilité d'utilisation : syntaxe très concise ; une seule ligne produit des graphiques esthétiques.
- Efficacité : fonctions statistiques intégrées (regplot) et thèmes par défaut de qualité, mais manque d'interactivité.

Carte interactive : réalisée avec Plotly, car Matplotlib ne gère pas nativement l'interactivité pour ce type de carte.

Principaux enseignements (insights)

- Tendance des ventes : saisonnalité marquée avec des pics en novembre et décembre (effet des fêtes).
- Concentration géographique : la Californie, New York et le Texas sont les États les plus performants.
- Concentration produit : très peu de produits (ex. photocopieurs Canon, téléphones Cisco) génèrent la majeure partie du chiffre d'affaires.
- Impact des remises : les remises supérieures à 20 % sont fortement associées à des profits négatifs (voir le nuage de points).

"""
