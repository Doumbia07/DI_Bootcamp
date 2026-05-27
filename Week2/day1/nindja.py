import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
import re
import warnings

warnings.filterwarnings("ignore")

df_iris = sns.load_dataset("iris")
titanic = sns.load_dataset("titanic")

print("=== EXERCISE 1: EDA on a dataset (using Iris for demonstration) ===")
print(df_iris.head())
print(df_iris.info())
print(df_iris.describe())
print(df_iris.isnull().sum())
for col in df_iris.select_dtypes(include=np.number).columns:
    plt.figure()
    sns.histplot(df_iris[col], kde=True)
    plt.title(f"Distribution of {col}")
    plt.show()
plt.figure()
sns.pairplot(df_iris, hue="species")
plt.show()

print("\n=== EXERCISE 2: TITANIC EDA ===")
print(titanic.head())
print(titanic.info())
print(titanic.describe())
print("Missing values:\n", titanic.isnull().sum())
titanic_clean = titanic.copy()
titanic_clean["age"].fillna(titanic_clean["age"].median(), inplace=True)
titanic_clean["embarked"].fillna(titanic_clean["embarked"].mode()[0], inplace=True)
titanic_clean.drop("deck", axis=1, inplace=True)
titanic_clean["sex"] = titanic_clean["sex"].map({"male": 0, "female": 1})
titanic_clean = pd.get_dummies(titanic_clean, columns=["embarked"], drop_first=True)
plt.figure()
sns.histplot(titanic_clean["age"], bins=30, kde=True)
plt.title("Age Distribution")
plt.show()
plt.figure()
sns.countplot(x="survived", data=titanic_clean)
plt.title("Survival Count")
plt.show()
plt.figure()
sns.barplot(x="pclass", y="survived", data=titanic_clean)
plt.title("Survival by Passenger Class")
plt.show()
plt.figure()
sns.barplot(x="sex", y="survived", data=titanic_clean)
plt.title("Survival by Sex")
plt.show()
plt.figure()
sns.scatterplot(x="age", y="fare", hue="survived", data=titanic_clean)
plt.title("Age vs Fare colored by Survival")
plt.show()
corr = titanic_clean.select_dtypes(include=np.number).corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

print("\n=== EXERCISE 3: IRIS EDA ===")
iris = sns.load_dataset("iris")
print(iris.head())
print(iris.info())
print(iris.describe())
print(iris["species"].value_counts())
for col in iris.columns[:-1]:
    plt.figure()
    sns.histplot(iris[col], kde=True, hue=iris["species"], multiple="stack")
    plt.title(f"Distribution of {col} by Species")
    plt.show()
sns.pairplot(iris, hue="species")
plt.show()
plt.figure()
sns.boxplot(x="species", y="sepal_length", data=iris)
plt.title("Sepal Length by Species")
plt.show()
plt.figure()
sns.boxplot(x="species", y="petal_length", data=iris)
plt.title("Petal Length by Species")
plt.show()
corr_iris = iris.iloc[:, :-1].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_iris, annot=True, cmap="coolwarm")
plt.title("Iris Feature Correlations")
plt.show()

print("\n=== EXERCISE 4: STRUCTURED vs UNSTRUCTURED DATA ===")
sales_data = pd.DataFrame(
    {
        "product_id": np.arange(1, 101),
        "sales": np.random.randint(100, 1000, 100),
        "region": np.random.choice(["North", "South", "East", "West"], 100),
        "date": pd.date_range("2023-01-01", periods=100),
    }
)
print("Structured Sales Data:")
print(sales_data.head())
print(sales_data.describe())
print(sales_data.groupby("region")["sales"].mean())
support_tickets = [
    "I love this product, it's amazing!",
    "The shipping was delayed and customer service was rude.",
    "Product broke after one use, very disappointed.",
    "Great value for money, will buy again.",
    "The packaging was damaged but the product works fine.",
    "I hate the new update, it's so confusing.",
    "Excellent quality, highly recommend.",
    "Worst purchase ever, want a refund.",
    "Average product, nothing special.",
    "Fast delivery and good condition.",
]
tickets_df = pd.DataFrame({"ticket": support_tickets})
tickets_df["sentiment_score"] = tickets_df["ticket"].apply(
    lambda x: TextBlob(x).sentiment.polarity
)
tickets_df["sentiment_label"] = tickets_df["sentiment_score"].apply(
    lambda x: "positive" if x > 0 else ("negative" if x < 0 else "neutral")
)
print("Unstructured Support Tickets Analysis:")
print(tickets_df.head())
print(tickets_df["sentiment_label"].value_counts())
print(
    "\nChallenges with unstructured data: need NLP, text cleaning, context understanding. Tools: TextBlob, NLTK, regex."
)

print("\n=== EXERCISE 5: CONVERTING UNSTRUCTURED TWEETS TO STRUCTURED ===")
tweets_data = pd.DataFrame(
    {
        "tweet": [
            "Loving the new #iPhone14! @Apple thanks #amazing",
            "Terrible service @XYZCo #fail #disappointed",
            "Check out this cool #AI project @OpenAI #machinelearning",
            "Had a great day at the #beach with friends",
            "Why is #twitter down again? @TwitterSupport #angry",
        ],
        "sentiment": ["positive", "negative", "positive", "neutral", "negative"],
    }
)


def extract_hashtags(text):
    return re.findall(r"#\w+", text)


def extract_mentions(text):
    return re.findall(r"@\w+", text)


tweets_data["hashtags"] = tweets_data["tweet"].apply(extract_hashtags)
tweets_data["mentions"] = tweets_data["tweet"].apply(extract_mentions)
tweets_data["hashtags_str"] = tweets_data["hashtags"].apply(lambda x: ",".join(x))
tweets_data["mentions_str"] = tweets_data["mentions"].apply(lambda x: ",".join(x))
structured_tweets = tweets_data[["tweet", "sentiment", "hashtags_str", "mentions_str"]]
print("Structured Tweets DataFrame:")
print(structured_tweets)
print(
    "\nOriginal unstructured: free text. New structured: columns for hashtags and mentions."
)
print("Analysis on structured: count most common hashtags:")
all_hashtags = [h for sublist in tweets_data["hashtags"] for h in sublist]
print(pd.Series(all_hashtags).value_counts())
