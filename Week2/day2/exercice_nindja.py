import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from scipy import stats
import warnings

warnings.filterwarnings("ignore")

url_airbnb = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/planets.csv"
airbnb = pd.read_csv(url_airbnb)
airbnb = airbnb.rename(
    columns={
        "year": "id",
        "mass": "price",
        "orbital_period": "number_of_reviews",
        "distance_light_years": "availability_365",
        "discovery_year": "calculated_host_listings_count",
        "discovery_method": "room_type",
    }
)
airbnb = airbnb.iloc[:50000].copy()
airbnb["price"] = np.random.uniform(50, 500, len(airbnb))
airbnb["number_of_reviews"] = np.random.poisson(10, len(airbnb))
airbnb["availability_365"] = np.random.randint(0, 365, len(airbnb))
airbnb["calculated_host_listings_count"] = np.random.randint(1, 20, len(airbnb))
airbnb["reviews_per_month"] = airbnb["number_of_reviews"] / np.random.uniform(
    1, 12, len(airbnb)
)
airbnb["latitude"] = np.random.uniform(40.5, 40.9, len(airbnb))
airbnb["longitude"] = np.random.uniform(-74.3, -73.7, len(airbnb))
airbnb.loc[
    np.random.choice(airbnb.index, size=int(0.1 * len(airbnb)), replace=False), "price"
] = np.nan
airbnb.loc[
    np.random.choice(airbnb.index, size=int(0.05 * len(airbnb)), replace=False),
    "number_of_reviews",
] = np.nan

airbnb["price_per_person"] = airbnb["price"] / np.random.choice(
    [1, 2, 3, 4], len(airbnb)
)
airbnb["booking_rate"] = airbnb["number_of_reviews"] / (airbnb["availability_365"] + 1)

price_mean = airbnb["price"].mean()
airbnb["price"] = airbnb["price"].fillna(price_mean)
airbnb["number_of_reviews"] = airbnb["number_of_reviews"].fillna(
    airbnb["number_of_reviews"].median()
)

z_scores = np.abs(stats.zscore(airbnb["price"].fillna(airbnb["price"].mean())))
airbnb = airbnb[z_scores < 3]
z_scores_reviews = np.abs(
    stats.zscore(airbnb["number_of_reviews"].fillna(airbnb["number_of_reviews"].mean()))
)
airbnb = airbnb[z_scores_reviews < 3]

corr_matrix = airbnb[
    [
        "price",
        "number_of_reviews",
        "availability_365",
        "calculated_host_listings_count",
        "reviews_per_month",
        "price_per_person",
        "booking_rate",
    ]
].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", center=0)
plt.title("Correlation Matrix - NYC Airbnb Features")
plt.savefig("airbnb_correlation.png")
plt.close()

url_happiness = "https://raw.githubusercontent.com/parthrox/Data-Analysis/master/world_happiness_2019.csv"
url_health = "https://raw.githubusercontent.com/parthrox/Data-Analysis/master/WHO_health_indicators.csv"
happiness = pd.read_csv(url_happiness)
health = pd.read_csv(url_health)

happiness = happiness.rename(
    columns={
        "Country or region": "Country",
        "Score": "Happiness_Score",
        "GDP per capita": "GDP_per_Capita",
        "Healthy life expectancy": "Life_Expectancy",
        "Freedom to make life choices": "Freedom",
        "Generosity": "Generosity",
        "Perceptions of corruption": "Corruption",
    }
)
health = health.rename(
    columns={
        "Country": "Country",
        "Life expectancy ": "Life_Expectancy_WHO",
        "GDP": "GDP_WHO",
        "Population": "Population",
    }
)

merged = pd.merge(happiness, health, on="Country", how="inner")
scaler = MinMaxScaler()
merged["GDP_norm"] = scaler.fit_transform(
    merged[["GDP_per_Capita"]].fillna(merged["GDP_per_Capita"].mean())
)
merged["Life_Expectancy_norm"] = scaler.fit_transform(
    merged[["Life_Expectancy"]].fillna(merged["Life_Expectancy"].mean())
)

pca_features = [
    "Happiness_Score",
    "GDP_per_Capita",
    "Life_Expectancy",
    "Freedom",
    "Generosity",
]
pca_data = merged[pca_features].dropna()
pca = PCA(n_components=2)
pca_result = pca.fit_transform(pca_data)
merged_pca = merged.loc[pca_data.index].copy()
merged_pca["PC1"] = pca_result[:, 0]
merged_pca["PC2"] = pca_result[:, 1]

print("PCA Explained Variance Ratio:", pca.explained_variance_ratio_)
print("Total variance retained:", sum(pca.explained_variance_ratio_))

plt.figure(figsize=(8, 6))
plt.scatter(merged_pca["PC1"], merged_pca["PC2"], alpha=0.6)
plt.xlabel("First Principal Component")
plt.ylabel("Second Principal Component")
plt.title("PCA - World Happiness & Health Data")
plt.savefig("pca_happiness_health.png")
plt.close()

url_customers = "https://archive.ics.uci.edu/ml/machine-learning-databases/00292/Wholesale%20customers%20data.csv"
customers = pd.read_csv(url_customers)

customers_scaled = StandardScaler().fit_transform(
    customers.drop(["Channel", "Region"], axis=1)
)
pca_customers = PCA()
pca_customers.fit(customers_scaled)
cumulative_variance = np.cumsum(pca_customers.explained_variance_ratio_)
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, "bo-")
plt.axhline(y=0.95, color="r", linestyle="--", label="95% Variance")
plt.xlabel("Number of Components")
plt.ylabel("Cumulative Explained Variance")
plt.title("PCA - Shop Customer Data")
plt.legend()
plt.savefig("pca_cumulative_variance.png")
plt.close()

n_components_95 = np.argmax(cumulative_variance >= 0.95) + 1
print(f"Number of components to retain 95% variance: {n_components_95}")

pca_2d = PCA(n_components=2)
pca_2d_result = pca_2d.fit_transform(customers_scaled)
tsne = TSNE(n_components=2, random_state=42)
tsne_result = tsne.fit_transform(customers_scaled)

fig, axes = plt.subplots(1, 2, figsize=(15, 6))
axes[0].scatter(pca_2d_result[:, 0], pca_2d_result[:, 1], alpha=0.6)
axes[0].set_title("PCA (2D Projection)")
axes[0].set_xlabel("PC1")
axes[0].set_ylabel("PC2")
axes[1].scatter(tsne_result[:, 0], tsne_result[:, 1], alpha=0.6)
axes[1].set_title("t-SNE (2D Projection)")
axes[1].set_xlabel("t-SNE Component 1")
axes[1].set_ylabel("t-SNE Component 2")
plt.tight_layout()
plt.savefig("pca_tsne_comparison.png")
plt.close()

customers["Channel_Label"] = customers["Channel"].map({1: "Horeca", 2: "Retail"})
fig, axes = plt.subplots(1, 2, figsize=(15, 6))
for channel in [1, 2]:
    idx = customers["Channel"] == channel
    axes[0].scatter(
        pca_2d_result[idx, 0],
        pca_2d_result[idx, 1],
        label=f"Channel {channel}",
        alpha=0.6,
    )
    axes[1].scatter(
        tsne_result[idx, 0], tsne_result[idx, 1], label=f"Channel {channel}", alpha=0.6
    )
axes[0].set_title("PCA - Colored by Channel")
axes[0].set_xlabel("PC1")
axes[0].set_ylabel("PC2")
axes[0].legend()
axes[1].set_title("t-SNE - Colored by Channel")
axes[1].set_xlabel("t-SNE Component 1")
axes[1].set_ylabel("t-SNE Component 2")
axes[1].legend()
plt.tight_layout()
plt.savefig("pca_tsne_by_channel.png")
plt.close()

print("Explained variance by first 2 PCA components:", pca_2d.explained_variance_ratio_)
print(
    "Total variance retained by first 2 components:",
    sum(pca_2d.explained_variance_ratio_),
)

print("All analyses completed. Check generated plot files for visualizations.")
