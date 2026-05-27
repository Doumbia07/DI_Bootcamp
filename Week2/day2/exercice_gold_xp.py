import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
import seaborn as sns

url_titanic = (
    "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
)
titanic = pd.read_csv(url_titanic)

url_superstore = "https://raw.githubusercontent.com/parthrox/Data-Analysis/master/Global%20Superstore%20Orders.csv"
superstore = pd.read_csv(url_superstore, encoding="latin1")

url_air = "https://raw.githubusercontent.com/aashita-k/Air-Quality-Data-India/master/city_day.csv"
air = pd.read_csv(url_air)

scaler_std = StandardScaler()
scaler_minmax = MinMaxScaler()

titanic["Age_standardized"] = scaler_std.fit_transform(
    titanic[["Age"]].fillna(titanic["Age"].mean())
)
titanic["Age_minmax"] = scaler_minmax.fit_transform(
    titanic[["Age"]].fillna(titanic["Age"].mean())
)
titanic["Fare_standardized"] = scaler_std.fit_transform(
    titanic[["Fare"]].fillna(titanic["Fare"].mean())
)
titanic["Fare_minmax"] = scaler_minmax.fit_transform(
    titanic[["Fare"]].fillna(titanic["Fare"].mean())
)

titanic["FamilySize"] = titanic["SibSp"] + titanic["Parch"] + 1
titanic["IsAlone"] = (titanic["FamilySize"] == 1).astype(int)

titanic["Age_zscore"] = (titanic["Age"] - titanic["Age"].mean()) / titanic["Age"].std()
titanic["Age_minmax2"] = (titanic["Age"] - titanic["Age"].min()) / (
    titanic["Age"].max() - titanic["Age"].min()
)
titanic["Fare_zscore"] = (titanic["Fare"] - titanic["Fare"].mean()) / titanic[
    "Fare"
].std()
titanic["Fare_minmax2"] = (titanic["Fare"] - titanic["Fare"].min()) / (
    titanic["Fare"].max() - titanic["Fare"].min()
)

plt.figure()
titanic["Age"].dropna().hist(alpha=0.5, label="Original")
titanic["Age_minmax"].dropna().hist(alpha=0.5, label="MinMax")
titanic["Age_standardized"].dropna().hist(alpha=0.5, label="Standardized")
plt.legend()
plt.title("Age Distributions")
plt.savefig("age_norm_comparison.png")
plt.close()

features = titanic[["Age", "Fare", "FamilySize", "SibSp", "Parch"]].dropna()
pca = PCA(n_components=2)
pca_result = pca.fit_transform(features)
titanic_pca = titanic.loc[features.index].copy()
titanic_pca["PC1"] = pca_result[:, 0]
titanic_pca["PC2"] = pca_result[:, 1]

air["Date"] = pd.to_datetime(air["Date"])
air["Month"] = air["Date"].dt.month
air["Year"] = air["Date"].dt.year
air_agg = (
    air.groupby(["City", "Year", "Month"])
    .agg(
        {
            "PM2.5": "mean",
            "PM10": "mean",
            "NO2": "mean",
            "CO": "mean",
            "SO2": "mean",
            "O3": "mean",
        }
    )
    .reset_index()
)

superstore["Sales_normalized"] = scaler_minmax.fit_transform(
    superstore[["Sales"]].fillna(0)
)
superstore["Profit_normalized"] = scaler_minmax.fit_transform(
    superstore[["Profit"]].fillna(0)
)

print("Titanic normalized columns added.")
print("FamilySize and IsAlone created.")
print("PCA applied and air quality aggregated.")
print("Superstore Sales and Profit normalized.")
