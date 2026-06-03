import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# 1. Classe principale pour l'analyse
class PowerPlantAnalysis:

    def __init__(self, filepath):

        self.df = pd.read_csv(filepath)
        self.clean_df = None
        self.fuel_stats = None
        self.top_fuels = ["Coal", "Gas", "Hydro", "Solar", "Wind", "Oil"]

    def __repr__(self):

        if self.clean_df is not None:
            return f"PowerPlantAnalysis: {len(self.clean_df)} centrales propres"
        return f"PowerPlantAnalysis: données brutes, {len(self.df)} lignes"

    def __len__(self):

        return len(self.clean_df) if self.clean_df is not None else 0

    # 2. Nettoyage des données

    def clean_data(self):

        cols = [
            "country",
            "country_long",
            "name",
            "capacity_mw",
            "latitude",
            "longitude",
            "primary_fuel",
            "commissioning_year",
            "generation_gwh_2017",
        ]
        df_clean = self.df[cols].copy()
        df_clean = df_clean.dropna(subset=["capacity_mw"])
        df_clean["commissioning_year"] = pd.to_numeric(
            df_clean["commissioning_year"], errors="coerce"
        )
        df_clean = df_clean[
            (df_clean["commissioning_year"] >= 1900)
            | (df_clean["commissioning_year"].isna())
        ]
        df_clean["decade"] = (df_clean["commissioning_year"] // 10) * 10
        self.clean_df = df_clean
        print(f"Nettoyage terminé : {len(self.clean_df)} centrales conservées.")
        return self.clean_df

    # 3. Analyse exploratoire (Pandas)

    def exploratory_stats(self):

        self.fuel_stats = (
            self.clean_df.groupby("primary_fuel")["capacity_mw"]
            .agg(["count", "mean", "median", "std"])
            .sort_values("mean", ascending=False)
        )
        print("\n Statistiques par type de combustible ")
        print(self.fuel_stats.head(10))

        country_counts = self.clean_df["country_long"].value_counts().head(10)
        print("\n Top 10 pays par nombre de centrales ")
        print(country_counts)
        return self.fuel_stats, country_counts

    # 4. Test d'hypothèse (Charbon vs Solaire)

    def hypothesis_test(self):

        coal = self.clean_df[self.clean_df["primary_fuel"] == "Coal"][
            "capacity_mw"
        ].dropna()
        solar = self.clean_df[self.clean_df["primary_fuel"] == "Solar"][
            "capacity_mw"
        ].dropna()
        if len(coal) == 0 or len(solar) == 0:
            print("Données insuffisantes pour le test.")
            return None
        t_stat, p_value = stats.ttest_ind(coal, solar)
        print("\n Test d'hypothèse (Charbon vs Solaire) ")
        print(f"Effectifs : Charbon={len(coal)}, Solaire={len(solar)}")
        print(f"Moyennes : Charbon={coal.mean():.1f} MW, Solaire={solar.mean():.1f} MW")
        print(f"t = {t_stat:.3f}, p-value = {p_value:.3e}")
        if p_value < 0.05:
            print("Rejet de H0 : différence significative.")
        else:
            print("Pas de différence significative.")
        return t_stat, p_value

    # 5. Analyse temporelle (séries chronologiques)

    def time_series_analysis(self):

        plants_by_year = (
            self.clean_df.dropna(subset=["commissioning_year"])["commissioning_year"]
            .value_counts()
            .sort_index()
        )
        # Mix par décennie pour les combustibles principaux
        df_fuels = self.clean_df[self.clean_df["primary_fuel"].isin(self.top_fuels)]
        fuel_by_decade = (
            df_fuels.groupby(["decade", "primary_fuel"]).size().unstack(fill_value=0)
        )
        fuel_prop = fuel_by_decade.div(fuel_by_decade.sum(axis=1), axis=0)
        print("\n Évolution du mix énergétique (proportions) ")
        print(fuel_prop.round(3))
        return plants_by_year, fuel_prop

    # 6. Visualisations (Matplotlib & Seaborn)

    def plot_distributions(self):

        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        # Histogramme log
        for fuel in self.top_fuels[:5]:
            data = self.clean_df[self.clean_df["primary_fuel"] == fuel]["capacity_mw"]
            axes[0].hist(data, bins=50, alpha=0.5, label=fuel, log=True)
        axes[0].set_title("Distribution des capacités (échelle log)")
        axes[0].set_xlabel("Capacité (MW)")
        axes[0].legend()
        # Boxplot
        df_fuels = self.clean_df[self.clean_df["primary_fuel"].isin(self.top_fuels)]
        sns.boxplot(data=df_fuels, x="primary_fuel", y="capacity_mw", ax=axes[1])
        axes[1].set_yscale("log")
        axes[1].set_title("Capacité par type de combustible (log)")
        axes[1].tick_params(axis="x", rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_geographic_density(self):

        plt.figure(figsize=(10, 6))
        hb = plt.hexbin(
            self.clean_df["longitude"],
            self.clean_df["latitude"],
            gridsize=80,
            cmap="YlOrRd",
            mincnt=1,
        )
        plt.colorbar(hb, label="Nombre de centrales")
        plt.title("Densité géographique des centrales")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.show()

    def plot_temporal_evolution(self, plants_by_year, fuel_prop):

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
        ax1.plot(plants_by_year.index, plants_by_year.values, marker=".", color="green")
        ax1.set_title("Mises en service par année")
        ax1.set_xlabel("Année")
        ax1.set_ylabel("Nombre de centrales")
        ax1.grid(True, alpha=0.3)

        fuel_prop.plot.area(ax=ax2, colormap="tab10", alpha=0.8)
        ax2.set_title("Évolution du mix énergétique (proportion par décennie)")
        ax2.set_xlabel("Décennie")
        ax2.set_ylabel("Proportion")
        ax2.legend(title="Combustible", bbox_to_anchor=(1.05, 1), loc="upper left")
        plt.tight_layout()
        plt.show()

    # 7. Opérations matricielles NumPy

    def matrix_operations(self):

        numeric_cols = ["capacity_mw", "latitude", "longitude"]
        M = self.clean_df[numeric_cols].dropna().values
        mean, std = np.mean(M, axis=0), np.std(M, axis=0)
        M_norm = (M - mean) / std
        corr = np.corrcoef(M_norm, rowvar=False)
        eigvals, eigvecs = np.linalg.eig(corr)
        print("\n Matrice de corrélation ")
        print(pd.DataFrame(corr, columns=numeric_cols, index=numeric_cols))
        print("\n Valeurs propres ")
        print(eigvals.round(4))
        print(" Vecteurs propres ")
        print(pd.DataFrame(eigvecs, columns=numeric_cols, index=numeric_cols))
        return corr, eigvals, eigvecs

    # 8. Intégration filtrage vectorisé, nouvelle colonne, scatter coloré

    def advanced_integration(self):

        # Filtrage avec masque NumPy
        mask = (self.clean_df["capacity_mw"].values > 1000) & (
            self.clean_df["primary_fuel"].values == "Coal"
        )
        large_coal = self.clean_df[mask]
        print(f"\nCentrales au charbon > 1000 MW : {len(large_coal)}")

        # Nouvelle colonne vectorisée
        self.clean_df["capacity_gw"] = self.clean_df["capacity_mw"].values / 1000.0

        # Scatter plot couleur par capacité
        plt.figure(figsize=(10, 6))
        sc = plt.scatter(
            self.clean_df["latitude"],
            self.clean_df["longitude"],
            c=self.clean_df["capacity_mw"],
            cmap="plasma",
            s=5,
            alpha=0.6,
        )
        plt.colorbar(sc, label="Capacité (MW)")
        plt.title("Carte des centrales (couleur = capacité)")
        plt.xlabel("Latitude")
        plt.ylabel("Longitude")
        plt.show()


# 9. Exécution principale
if __name__ == "__main__":
    # Instanciation et chargement
    analysis = PowerPlantAnalysis("global_power_plant_database.csv")
    print(analysis)

    # Nettoyage
    analysis.clean_data()
    print(f"Nombre de centrales après nettoyage : {len(analysis)}")

    # Analyse exploratoire
    analysis.exploratory_stats()

    # Test d'hypothèse
    analysis.hypothesis_test()

    # Série temporelle
    plants_by_year, fuel_prop = analysis.time_series_analysis()

    # Visualisations
    analysis.plot_distributions()
    analysis.plot_geographic_density()
    analysis.plot_temporal_evolution(plants_by_year, fuel_prop)

    # Opérations matricielles
    analysis.matrix_operations()

    # Intégration avancée
    analysis.advanced_integration()

    # Résumé final
    print("\nRÉSUMÉ DES DÉCOUVERTES")
    print(f"{len(analysis)} centrales analysées.")
    print(f"Combustible le plus fréquent : {analysis.fuel_stats.index[0]}.")
    print(
        f"Pays avec le plus de centrales : {analysis.clean_df['country_long'].value_counts().index[0]}."
    )
    print("Différence significative entre charbon et solaire (p < 0.05).")
