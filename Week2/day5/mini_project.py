"""
Mini-projet : Analyse marketing - US Superstore
Version simplifiée, lisible, tout en français, avec fonctions.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Chargement des données (chemin relatif)
def charger_donnees():
    df = pd.read_excel("US Superstore data.xls", sheet_name="Orders")
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])
    df.drop_duplicates(inplace=True)
    return df


# 2. Top États par ventes
def top_etats_ventes(df, n=10):
    top = df.groupby("State")["Sales"].sum().nlargest(n)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top.values, y=top.index, palette="Blues_r")
    plt.title(f"Top {n} États par ventes")
    plt.xlabel("Ventes ($)")
    plt.ylabel("État")
    plt.tight_layout()
    plt.show()
    print("Top États (ventes) :\n", top.round(0).astype(int), "\n")
    return top


# 3. Comparaison New York / Californie
def comparer_ny_ca(df):
    ny = df[df["State"] == "New York"]
    ca = df[df["State"] == "California"]
    ventes = [ny["Sales"].sum(), ca["Sales"].sum()]
    profits = [ny["Profit"].sum(), ca["Profit"].sum()]
    comp = pd.DataFrame(
        {"État": ["New York", "Californie"], "Ventes": ventes, "Profit": profits}
    )
    comp[["Ventes", "Profit"]] = comp[["Ventes", "Profit"]].round(0).astype(int)
    print("Comparaison NY / Californie :\n", comp, "\n")

    # Graphique
    fond = comp.melt(id_vars="État", var_name="Métrique", value_name="Montant")
    plt.figure(figsize=(8, 5))
    sns.barplot(data=fond, x="État", y="Montant", hue="Métrique", palette="Set2")
    plt.title("Ventes et profit : NY vs Californie")
    plt.ylabel("Montant ($)")
    plt.tight_layout()
    plt.show()


# 4. Client le plus vendeur à New York
def client_top_ny(df):
    top = (
        df[df["State"] == "New York"]
        .groupby(["Customer ID", "Customer Name"])["Sales"]
        .sum()
        .nlargest(1)
        .reset_index()
    )
    nom = top.iloc[0]["Customer Name"]
    ventes = int(round(top.iloc[0]["Sales"]))
    print(f"Client NY le plus vendeur : {nom} - ${ventes:,}\n")


# 5. Marge bénéficiaire par État (Top 10)
def marge_par_etat(df, n=10):
    def marge(g):
        return g["Profit"].sum() / g["Sales"].sum() * 100

    top = df.groupby("State").apply(marge).nlargest(n).reset_index()
    top.columns = ["État", "Marge (%)"]
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top, x="Marge (%)", y="État", palette="RdYlGn")
    plt.title(f"Top {n} États par marge bénéficiaire (%)")
    plt.tight_layout()
    plt.show()
    print("Top marges par État :\n", top.round(1), "\n")
    return top


# 6. Pareto (80/20) sur le profit client
def pareto_profit(df):
    profit_client = (
        df.groupby("Customer ID")["Profit"].sum().sort_values(ascending=False)
    )
    cumul = profit_client.cumsum() / profit_client.sum() * 100
    pct_clients = np.arange(1, len(profit_client) + 1) / len(profit_client) * 100
    seuil = np.argmax(cumul >= 80)
    pct_necessaire = pct_clients[seuil]

    plt.figure(figsize=(8, 6))
    plt.plot(pct_clients, cumul, "b-", linewidth=2)
    plt.axhline(80, color="r", linestyle="--", label="80% du profit")
    plt.axvline(20, color="g", linestyle="--", label="20% des clients")
    plt.fill_between(
        pct_clients, cumul, 80, where=(cumul <= 80), color="yellow", alpha=0.3
    )
    plt.title("Courbe de Pareto : profit par client")
    plt.xlabel("Pourcentage de clients")
    plt.ylabel("Pourcentage du profit")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()
    print(f"Pour 80% du profit, il faut {pct_necessaire:.1f}% des clients.\n")
    return pct_necessaire


# 7. Top 20 villes (ventes, profit, marges)
def top_villes(df):
    ventes = df.groupby("City")["Sales"].sum().nlargest(20)
    profits = df.groupby("City")["Profit"].sum().nlargest(20)
    print("Top 20 villes par ventes :\n", ventes.round(0).astype(int), "\n")
    print("Top 20 villes par profit :\n", profits.round(0).astype(int), "\n")

    # Marges sur l'ensemble des villes des deux tops
    villes_union = set(ventes.index) | set(profits.index)

    def marge(g):
        return g["Profit"].sum() / g["Sales"].sum() * 100

    marges = (
        df[df["City"].isin(villes_union)]
        .groupby("City")
        .apply(marge)
        .nlargest(10)
        .reset_index()
    )
    marges.columns = ["Ville", "Marge (%)"]
    print("Top 10 marges parmi ces villes :\n", marges.round(1), "\n")

    # Graphique comparatif top 10
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    ventes.head(10).sort_values().plot(kind="barh", ax=ax1, color="steelblue")
    ax1.set_title("Top 10 villes par ventes")
    ax1.set_xlabel("Ventes ($)")
    profits.head(10).sort_values().plot(kind="barh", ax=ax2, color="darkgreen")
    ax2.set_title("Top 10 villes par profit")
    ax2.set_xlabel("Profit ($)")
    plt.tight_layout()
    plt.show()
    return ventes, profits, marges


# 8. Top 10 clients par ventes
def top_clients_ventes(df, n=10):
    top = (
        df.groupby(["Customer ID", "Customer Name"])["Sales"]
        .sum()
        .nlargest(n)
        .reset_index()
    )
    top["Sales"] = top["Sales"].round(0).astype(int)
    print(f"Top {n} clients par ventes :\n", top[["Customer Name", "Sales"]], "\n")
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top, y="Customer Name", x="Sales", palette="viridis")
    plt.title(f"Top {n} clients par ventes")
    plt.xlabel("Ventes ($)")
    plt.tight_layout()
    plt.show()


# 9. Pareto (80/20) sur les ventes client
def pareto_ventes(df):
    ventes_client = (
        df.groupby("Customer ID")["Sales"].sum().sort_values(ascending=False)
    )
    cumul = ventes_client.cumsum() / ventes_client.sum() * 100
    pct_clients = np.arange(1, len(ventes_client) + 1) / len(ventes_client) * 100
    seuil = np.argmax(cumul >= 80)
    pct_necessaire = pct_clients[seuil]
    plt.figure(figsize=(8, 6))
    plt.plot(pct_clients, cumul, "b-", linewidth=2)
    plt.axhline(80, color="r", linestyle="--", label="80% des ventes")
    plt.axvline(20, color="g", linestyle="--", label="20% des clients")
    plt.title("Courbe de Pareto : ventes par client")
    plt.xlabel("Pourcentage de clients")
    plt.ylabel("Pourcentage des ventes")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()
    print(f"Pour 80% des ventes, il faut {pct_necessaire:.1f}% des clients.\n")
    return pct_necessaire


# 10. Recommandations finales
def recommandations(
    state_sales, state_margin, city_sales, city_profit, pct_clients_profit
):
    top_states = state_sales.head(3).index.tolist()
    top_margin_states = state_margin.head(3)["État"].tolist()
    top_sales_cities = city_sales.head(5).index.tolist()
    top_profit_cities = city_profit.head(5).index.tolist()
    print("\n" + "=" * 60)
    print("RECOMMANDATIONS MARKETING")
    print("=" * 60)
    print(f"""
 PRIORITÉS GÉOGRAPHIQUES :
- États à fort volume : {', '.join(top_states)}
- États à meilleure marge : {', '.join(top_margin_states)}
- Villes clés ventes : {', '.join(top_sales_cities)}
- Villes clés profit : {', '.join(top_profit_cities)}

 CLIENTS :
- {pct_clients_profit:.0f}% des clients génèrent 80% du profit → concentrer les efforts.
- Programme de fidélisation pour les top 10 clients identifiés.

 ACTIONS :
1. Augmenter le budget marketing dans {', '.join(top_states)}.
2. Étudier et dupliquer les bonnes pratiques des villes à forte marge.
3. Réduire les remises trop élevées dans les zones peu rentables.
4. Utiliser la règle de Pareto pour prioriser les actions commerciales.
    """)


# Programme principal
if __name__ == "__main__":
    df = charger_donnees()
    print("Données chargées :", df.shape, "\n")

    state_sales = top_etats_ventes(df)
    comparer_ny_ca(df)
    client_top_ny(df)
    state_margin = marge_par_etat(df)
    pct_clients_profit = pareto_profit(df)
    city_sales, city_profit, _ = top_villes(df)
    top_clients_ventes(df)
    pareto_ventes(df)
    recommandations(
        state_sales, state_margin, city_sales, city_profit, pct_clients_profit
    )
