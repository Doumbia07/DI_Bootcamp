import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from faker import Faker
import warnings

warnings.filterwarnings("ignore")

boston = load_boston()
boston_df = pd.DataFrame(boston.data, columns=boston.feature_names)
boston_df["PRICE"] = boston.target
print("Boston Housing - MEDV mean:", boston_df["PRICE"].mean())
print("Boston Housing - MEDV median:", boston_df["PRICE"].median())
print("Boston Housing - MEDV std:", boston_df["PRICE"].std())

retail_url = (
    "https://raw.githubusercontent.com/parthrox/Data-Analysis/master/Online_Retail.csv"
)
reviews_url = "https://raw.githubusercontent.com/parthrox/Data-Analysis/master/Womens%20Clothing%20E-Commerce%20Reviews.csv"
retail = pd.read_csv(retail_url, encoding="latin1")
reviews = pd.read_csv(reviews_url)

retail_sales = (
    retail.groupby("Country")["Quantity"].sum().sort_values(ascending=False).head(5)
)
print("Top 5 countries by sales quantity:\n", retail_sales)

review_sentiment = reviews["Rating"].value_counts(normalize=True)
print("Review rating distribution:\n", review_sentiment)

ecommerce_url = "https://raw.githubusercontent.com/parthrox/Data-Analysis/master/E-Commerce%20Data.csv"
ecommerce = pd.read_csv(ecommerce_url)
print("E-Commerce first 5 rows:\n", ecommerce.head())
print("Rows:", ecommerce.shape[0], "Columns:", ecommerce.shape[1])
print("Column names:", list(ecommerce.columns))

traffic_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00492/Metro_Interstate_Traffic_Volume.csv"
traffic = pd.read_csv(traffic_url)
print("Traffic dataset first rows:\n", traffic.head())
structured_cols = [
    "holiday",
    "temp",
    "rain_1h",
    "snow_1h",
    "clouds_all",
    "weather_main",
    "weather_description",
    "date_time",
    "traffic_volume",
]
print("Structured elements:", structured_cols)

movielens_ratings = pd.read_csv(
    "https://files.grouplens.org/datasets/movielens/ml-latest-small/ratings.csv"
)
print("MovieLens ratings head:\n", movielens_ratings.head())
print("Structured columns:", list(movielens_ratings.columns))

fake = Faker()
products = []
for i in range(500):
    products.append(
        {
            "product_id": i + 1,
            "name": fake.word().capitalize() + " " + fake.word(),
            "description": fake.sentence(nb_words=15),
            "price": round(np.random.uniform(5, 500), 2),
        }
    )
product_df = pd.DataFrame(products)
print(product_df.head())
