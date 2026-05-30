"""
Mini-projet : Analyse marketing - US Superstore Dataset
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")


# 1. Chargement et nettoyage

df = pd.read_excel("US Superstore data.xls", sheet_name="Orders")
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])
df.drop_duplicates(inplace=True)


# 2. Top États par ventes

state_sales = df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=state_sales.values, y=state_sales.index, palette="Blues_r")
plt.title("Top 10 États par ventes totales")
plt.xlabel("Ventes ($)")
plt.ylabel("État")
plt.tight_layout()
plt.show()

print("Top 10 États par ventes :")
print(state_sales.round(0).astype(int))
print()


# 3. Comparaison NY vs Californie

ny_sales = df[df["State"] == "New York"]["Sales"].sum()
ca_sales = df[df["State"] == "California"]["Sales"].sum()
ny_profit = df[df["State"] == "New York"]["Profit"].sum()
ca_profit = df[df["State"] == "California"]["Profit"].sum()

comp = pd.DataFrame(
    {
        "State": ["New York", "California"],
        "Sales": [ny_sales, ca_sales],
        "Profit": [ny_profit, ca_profit],
    }
)
comp[["Sales", "Profit"]] = comp[["Sales", "Profit"]].round(0).astype(int)
print("Comparaison New York vs Californie :")
print(comp)

comp_melt = comp.melt(id_vars="State", var_name="Metric", value_name="Amount")
plt.figure(figsize=(8, 5))
sns.barplot(data=comp_melt, x="State", y="Amount", hue="Metric", palette="Set2")
plt.title("Comparaison NY / CA : Ventes et Profit")
plt.ylabel("Montant ($)")
plt.tight_layout()
plt.show()


# 4. Client exceptionnel à New York

ny_top = (
    df[df["State"] == "New York"]
    .groupby(["Customer ID", "Customer Name"])["Sales"]
    .sum()
    .nlargest(1)
    .reset_index()
)
cust_name = ny_top.iloc[0]["Customer Name"]
cust_sales = int(round(ny_top.iloc[0]["Sales"]))
print(f"Client avec le plus de ventes à New York : {cust_name} : ${cust_sales:,}\n")


# 5. Marge bénéficiaire par État


def margin(x):
    return x["Profit"].sum() / x["Sales"].sum() * 100


state_margin = (
    df.groupby("State")
    .apply(margin)
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)
state_margin.columns = ["State", "Margin (%)"]

plt.figure(figsize=(10, 6))
sns.barplot(data=state_margin, x="Margin (%)", y="State", palette="RdYlGn")
plt.title("Top 10 États par marge bénéficiaire (%)")
plt.tight_layout()
plt.show()

print("Top 10 États par marge bénéficiaire (%) :")
print(state_margin.round(1))
print()


# 6. Pareto : profit par client

cust_profit = df.groupby("Customer ID")["Profit"].sum().sort_values(ascending=False)
total_profit = cust_profit.sum()
cumsum_profit = cust_profit.cumsum()
pct_customers = np.arange(1, len(cust_profit) + 1) / len(cust_profit) * 100
pct_profit = cumsum_profit / total_profit * 100
idx_80 = np.argmax(pct_profit >= 80)
clients_needed = pct_customers[idx_80]

plt.figure(figsize=(8, 6))
plt.plot(pct_customers, pct_profit, "b-", linewidth=2)
plt.axhline(y=80, color="r", linestyle="--", label="80% du profit")
plt.axvline(x=20, color="g", linestyle="--", label="20% des clients")
plt.fill_between(
    pct_customers, pct_profit, 80, where=(pct_profit <= 80), color="yellow", alpha=0.3
)
plt.title("Courbe cumulative du profit par client")
plt.xlabel("Pourcentage de clients")
plt.ylabel("Pourcentage du profit")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print(f"Pour atteindre 80% du profit, il faut {clients_needed:.1f}% des clients.")
print()


# 7. Top 20 villes par ventes et profit

city_sales = df.groupby("City")["Sales"].sum().nlargest(20)
city_profit = df.groupby("City")["Profit"].sum().nlargest(20)

print("Top 20 villes par ventes :")
print(city_sales.round(0).astype(int))
print("\nTop 20 villes par profit :")
print(city_profit.round(0).astype(int))

top_cities = set(city_sales.index).union(set(city_profit.index))
city_margins = (
    df[df["City"].isin(top_cities)]
    .groupby("City")
    .apply(margin)
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)
city_margins.columns = ["City", "Margin (%)"]
print("\nVilles avec les meilleures marges (parmi top 20 ventes/profit) :")
print(city_margins.round(1))

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
city_sales.head(10).sort_values().plot(kind="barh", ax=axes[0], color="steelblue")
axes[0].set_title("Top 10 villes par ventes")
axes[0].set_xlabel("Ventes ($)")
city_profit.head(10).sort_values().plot(kind="barh", ax=axes[1], color="darkgreen")
axes[1].set_title("Top 10 villes par profit")
axes[1].set_xlabel("Profit ($)")
plt.tight_layout()
plt.show()


# 8. Top 20 clients par ventes

top_cust = (
    df.groupby(["Customer ID", "Customer Name"])["Sales"]
    .sum()
    .nlargest(20)
    .reset_index()
)
top10_cust = top_cust.head(10).copy()
top10_cust["Sales"] = top10_cust["Sales"].round(0).astype(int)
print("\nTop 10 clients par ventes :")
print(top10_cust[["Customer Name", "Sales"]])

plt.figure(figsize=(10, 6))
sns.barplot(data=top10_cust, y="Customer Name", x="Sales", palette="viridis")
plt.title("Top 10 clients par ventes")
plt.xlabel("Ventes ($)")
plt.tight_layout()
plt.show()


# 9. Pareto : ventes par client

cust_sales = df.groupby("Customer ID")["Sales"].sum().sort_values(ascending=False)
total_sales = cust_sales.sum()
cumsum_sales = cust_sales.cumsum()
pct_cust = np.arange(1, len(cust_sales) + 1) / len(cust_sales) * 100
pct_sales = cumsum_sales / total_sales * 100
idx_80_sales = np.argmax(pct_sales >= 80)
clients_needed_sales = pct_cust[idx_80_sales]

plt.figure(figsize=(8, 6))
plt.plot(pct_cust, pct_sales, "b-", linewidth=2)
plt.axhline(y=80, color="r", linestyle="--", label="80% des ventes")
plt.axvline(x=20, color="g", linestyle="--", label="20% des clients")
plt.title("Courbe cumulative des ventes par client")
plt.xlabel("Pourcentage de clients")
plt.ylabel("Pourcentage des ventes")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
print(f"\nPour 80% des ventes, il faut {clients_needed_sales:.1f}% des clients.")


# 10. Recommandations

top_states = state_sales.head(3).index.tolist()
top_margin_states = state_margin.head(3)["State"].tolist()
top_sales_cities = city_sales.head(5).index.tolist()
top_profit_cities = city_profit.head(5).index.tolist()

print("\n" + "=" * 60)
print("RECOMMANDATIONS MARKETING")
print("=" * 60)
print(f"""
 PRIORITÉS GÉOGRAPHIQUES :
- États à fort volume de ventes : {', '.join(top_states)}
- États avec les meilleures marges : {', '.join(top_margin_states)}
- Villes clés pour les ventes : {', '.join(top_sales_cities)}
- Villes clés pour le profit : {', '.join(top_profit_cities)}

 CLIENTS :
- {clients_needed:.0f}% des clients génèrent 80% du profit → concentrer les efforts sur ces clients.
- Mettre en place un programme de fidélisation pour les top 10 clients identifiés.

 ACTIONS RECOMMANDÉES :
1. Allouer davantage de budget marketing aux États de {', '.join(top_states)}.
2. Étudier les pratiques des villes à forte marge (ex: {top_profit_cities[0] if top_profit_cities else 'non listée'}) pour les reproduire ailleurs.
3. Réduire les remises excessives dans les zones à faible profit.
4. Appliquer la règle de Pareto pour prioriser les actions commerciales.
""")
print("Analyse terminée.")
