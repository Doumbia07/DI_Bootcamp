# BUSINESS INTELLIGENCE REPORT: US SUPERSTORE ANALYSIS
# Complete analysis with interactive visualizations and strategic insights

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from ipywidgets import interact, Dropdown, IntSlider
from IPython.display import display
import warnings

warnings.filterwarnings("ignore")

print("=" * 70)
print("US SUPERSTORE DATA ANALYSIS - BUSINESS INTELLIGENCE REPORT")
print("=" * 70)

# 1. DATA SCOPING AND PREPARATION

print("\n[1] LOADING AND PREPARING THE DATASET...")

# Load dataset (update path if needed)
try:
    df = pd.read_csv("superstore_dataset.csv")
    print("✓ Dataset loaded successfully.")
except FileNotFoundError:
    print(
        "✗ File 'superstore_dataset.csv' not found. Creating sample dataset for demonstration."
    )
    # Create minimal sample for demonstration
    np.random.seed(42)
    dates = pd.date_range("2019-01-01", "2022-12-31", freq="D")
    n = 5000
    df = pd.DataFrame(
        {
            "Order Date": np.random.choice(dates, n),
            "Ship Date": np.random.choice(dates, n),
            "Sales": np.random.uniform(10, 1000, n),
            "Profit": np.random.uniform(-100, 300, n),
            "Discount": np.random.uniform(0, 0.5, n),
            "Category": np.random.choice(
                ["Furniture", "Office Supplies", "Technology"], n
            ),
            "Sub-Category": np.random.choice(
                ["Chairs", "Tables", "Phones", "Binders", "Storage"], n
            ),
            "Product Name": ["Product " + str(i) for i in range(n)],
            "State": np.random.choice(
                [
                    "California",
                    "New York",
                    "Texas",
                    "Florida",
                    "Illinois",
                    "Pennsylvania",
                ],
                n,
            ),
            "Postal Code": np.random.choice([10001, 20001, 30001, 40001, None], n),
        }
    )
    print("Sample dataset created for demonstration purposes.")

# Basic exploration
print(f"\nDataset Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(f"Missing values:\n{df.isnull().sum()}")

# Data cleaning
print("\n--- DATA CLEANING ---")
print(f"Duplicate rows before: {df.duplicated().sum()}")
df = df.drop_duplicates()
print(f"Duplicate rows after removal: {df.duplicated().sum()}")

# Handle missing Postal Code
if "Postal Code" in df.columns:
    df["Postal Code"] = df["Postal Code"].fillna(0)
    print("Missing postal codes filled with 0.")

# Convert dates to datetime
date_columns = ["Order Date", "Ship Date"]
for col in date_columns:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col])
print("Date columns converted to datetime.")

# Feature engineering
print("\n--- FEATURE ENGINEERING ---")
df["Profit Margin"] = (df["Profit"] / df["Sales"]) * 100
df["Order Year"] = df["Order Date"].dt.year
df["Order Month"] = df["Order Date"].dt.month
df["Order Month-Year"] = df["Order Date"].dt.to_period("M")
print("Created: Profit Margin, Order Year, Order Month, Order Month-Year")

print(f"\nFinal dataset shape: {df.shape}")
print(df[["Sales", "Profit", "Profit Margin", "Order Year", "Order Month"]].head())

# 2. DEEP-DIVE EXPLORATORY ANALYSIS (MATPLOTLIB)

print("\n" + "=" * 70)
print("[2] TIME-SERIES TREND ANALYSIS WITH INTERACTIVITY")
print("=" * 70)

# Prepare monthly sales data
monthly_sales = (
    df.groupby(["Order Month-Year", "Category"])["Sales"].sum().reset_index()
)
monthly_sales["Date"] = monthly_sales["Order Month-Year"].dt.to_timestamp()


def plot_monthly_sales(category="All"):
    plt.figure(figsize=(12, 6))
    if category == "All":
        total_monthly = df.groupby("Order Month-Year")["Sales"].sum()
        plt.plot(
            total_monthly.index.to_timestamp(),
            total_monthly.values,
            marker="o",
            linewidth=2,
            markersize=4,
            color="steelblue",
        )
        title = "Monthly Sales Trend - All Categories"
    else:
        cat_data = monthly_sales[monthly_sales["Category"] == category]
        plt.plot(
            cat_data["Date"],
            cat_data["Sales"],
            marker="o",
            linewidth=2,
            markersize=4,
            color="darkorange",
        )
        title = f"Monthly Sales Trend - {category}"
    plt.title(title, fontsize=16, fontweight="bold")
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Sales ($)", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


categories = ["All"] + list(df["Category"].unique())
category_dropdown = Dropdown(options=categories, value="All", description="Category:")
interact(plot_monthly_sales, category=category_dropdown)

# Geographic sales performance
print("\n" + "=" * 70)
print("[3] GEOGRAPHIC SALES PERFORMANCE (INTERACTIVE)")
print("=" * 70)

state_sales = df.groupby("State")["Sales"].sum().sort_values(ascending=True)


def plot_top_states(top_n=10):
    plt.figure(figsize=(12, max(6, top_n * 0.4)))
    top_states = state_sales.tail(top_n)
    bars = plt.barh(range(len(top_states)), top_states.values, color="steelblue")
    plt.yticks(range(len(top_states)), top_states.index)
    plt.xlabel("Total Sales ($)", fontsize=12)
    plt.ylabel("State", fontsize=12)
    plt.title(
        f"Top {top_n} States by Sales Performance", fontsize=16, fontweight="bold"
    )
    for i, (state, value) in enumerate(top_states.items()):
        plt.text(
            value + max(top_states.values()) * 0.01,
            i,
            f"${value:,.0f}",
            va="center",
            fontsize=10,
        )
    plt.grid(axis="x", alpha=0.3)
    plt.tight_layout()
    plt.show()
    print(f"Total states analyzed: {len(state_sales)}")
    print(
        f"Top {top_n} states represent: ${top_states.sum():,.0f} in sales ({top_states.sum()/state_sales.sum()*100:.1f}% of total)"
    )


top_n_slider = IntSlider(min=5, max=25, value=10, description="Top N States:")
interact(plot_top_states, top_n=top_n_slider)

# 3. COMMUNICATING INSIGHTS (SEABORN)

print("\n" + "=" * 70)
print("[4] TOP PROFITABLE PRODUCTS (SEABORN BARPLOT)")
print("=" * 70)

product_profit = (
    df.groupby("Product Name")["Profit"].sum().sort_values(ascending=False).head(10)
)

plt.figure(figsize=(12, 8))
ax = sns.barplot(
    x=product_profit.values, y=product_profit.index, palette="viridis", orient="h"
)
plt.title(
    "Top 10 Most Profitable Products\nExecutive Summary - Product Performance Analysis",
    fontsize=16,
    fontweight="bold",
    pad=20,
)
plt.xlabel("Total Profit ($)", fontsize=12, fontweight="bold")
plt.ylabel("Product Name", fontsize=12, fontweight="bold")
for i, (product, profit) in enumerate(product_profit.items()):
    ax.text(
        profit + max(product_profit.values()) * 0.01,
        i,
        f"${profit:,.0f}",
        va="center",
        fontweight="bold",
        fontsize=10,
    )
plt.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.show()

print("Key Insights:")
print(f"• Most profitable product generates: ${product_profit.iloc[0]:,.0f}")
print(f"• Top 10 products contribute: ${product_profit.sum():,.0f} total profit")
print(f"• Average profit per top product: ${product_profit.mean():,.0f}")

# Discount vs Profit scatter plot
print("\n" + "=" * 70)
print("[5] DISCOUNT STRATEGY ANALYSIS (SCATTER + REGRESSION)")
print("=" * 70)

plt.figure(figsize=(14, 8))
sns.scatterplot(data=df, x="Discount", y="Profit", hue="Category", alpha=0.6, s=50)
sns.regplot(
    data=df,
    x="Discount",
    y="Profit",
    scatter=False,
    color="red",
    line_kws={"linewidth": 2, "linestyle": "--"},
)
plt.title(
    "Discount Strategy Analysis: Impact on Profitability by Category",
    fontsize=16,
    fontweight="bold",
    pad=20,
)
plt.xlabel("Discount Rate", fontsize=12, fontweight="bold")
plt.ylabel("Profit ($)", fontsize=12, fontweight="bold")
plt.axhline(y=0, color="black", linestyle="-", alpha=0.3, linewidth=1)
plt.text(0.5, 50, "Break-even line", fontsize=10, alpha=0.7)
plt.grid(True, alpha=0.3)
plt.legend(title="Product Category", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.show()

high_discount = df[df["Discount"] > 0.2]
print("Discount Analysis Insights:")
print(f"• Transactions with >20% discount: {len(high_discount):,}")
print(f"• Average profit for high discounts: ${high_discount['Profit'].mean():.2f}")
print(
    f"• Percentage of high-discount sales with losses: {(high_discount['Profit'] < 0).mean()*100:.1f}%"
)
print("\nCategory-specific discount impact:")
for category in df["Category"].unique():
    cat_data = df[df["Category"] == category]
    high_disc_cat = cat_data[cat_data["Discount"] > 0.2]
    if len(high_disc_cat) > 0:
        avg_loss = high_disc_cat["Profit"].mean()
        print(f"• {category}: Average profit at >20% discount = ${avg_loss:.2f}")

# 4. METHODOLOGY AND TOOLING REVIEW

print("\n" + "=" * 70)
print("[6] MATPLOTLIB vs SEABORN COMPARISON")
print("=" * 70)

# Speed comparison
import time

start = time.time()
plt.figure(figsize=(8, 6))
plt.plot(df.groupby("Order Year")["Sales"].sum())
plt.close()
matplotlib_time = time.time() - start

start = time.time()
plt.figure(figsize=(8, 6))
sns.lineplot(
    data=df.groupby("Order Year")["Sales"].sum().reset_index(),
    x="Order Year",
    y="Sales",
)
plt.close()
seaborn_time = time.time() - start

print("MATPLOTLIB STRENGTHS:")
print("• Fine-grained control over interactive widgets")
print("• Custom annotations and text positioning")
print("• Precise subplot layouts and figure sizing")
print("• Integration with ipywidgets for dynamic updates")
print("\nSEABORN STRENGTHS:")
print("• Built-in statistical visualizations (regplot)")
print("• Automatic color palettes and legends")
print("• Clean, publication-ready default styling")
print("• Easy categorical data visualization")
print(
    f"\nSpeed comparison: Matplotlib: {matplotlib_time:.4f}s, Seaborn: {seaborn_time:.4f}s"
)

print("\nRECOMMENDATION:")
print("For rapid exploration, I will use Matplotlib because it offers faster rendering")
print(
    "for basic plots and seamless integration with interactive widgets for dynamic analysis."
)
print("For stakeholder-facing presentations, I will prefer Seaborn because it provides")
print(
    "publication-ready aesthetics, built-in statistical functionality, and professional"
)
print("color schemes that enhance executive communication.")

# 5. FINAL EXECUTIVE SUMMARY

print("\n" + "=" * 70)
print("EXECUTIVE SUMMARY - KEY FINDINGS")
print("=" * 70)

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
profit_margin = (total_profit / total_sales) * 100

print(f"📊 BUSINESS PERFORMANCE:")
print(f"• Total Revenue: ${total_sales:,.0f}")
print(f"• Total Profit: ${total_profit:,.0f}")
print(f"• Overall Profit Margin: {profit_margin:.1f}%")

top_state = state_sales.index[-1]
top_state_sales = state_sales.iloc[-1]
print(f"\n🗺️ GEOGRAPHIC PERFORMANCE:")
print(f"• Top performing state: {top_state} (${top_state_sales:,.0f})")
print(
    f"• Geographic concentration: Top 5 states = {(state_sales.tail(5).sum()/total_sales)*100:.1f}% of sales"
)

top_category = (
    df.groupby("Category")["Sales"].sum().sort_values(ascending=False).index[0]
)
print(f"\n🏆 PRODUCT PERFORMANCE:")
print(f"• Leading category: {top_category}")
if len(product_profit) > 0:
    print(f"• Most profitable product: {product_profit.index[0]}")

high_discount_loss_rate = (df[df["Discount"] > 0.2]["Profit"] < 0).mean() * 100
print(f"\n💰 DISCOUNT STRATEGY INSIGHTS:")
print(
    f"• High discount risk: {high_discount_loss_rate:.1f}% of >20% discounts result in losses"
)
print(f"• Recommended max discount threshold: 20% to maintain profitability")

# Example finding and recommendation
print("\n📌 EXAMPLE FINDING:")
print("Furniture discounts above 20% lead to average profit losses of 15%.")

print("\n📌 EXAMPLE RECOMMENDATION:")
print(
    "Limit standard Furniture discounts to a maximum of 20%. Introduce approval steps for exceptions."
)

# OPTIONAL ADVANCED CHALLENGES

print("\n" + "=" * 70)
print("[OPTIONAL] ADVANCED DASHBOARD & OUTLIER ANALYSIS")
print("=" * 70)


# 5.1 Multi-chart dashboard
def create_dashboard():
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    monthly_total = df.groupby("Order Month-Year")["Sales"].sum()
    ax1.plot(
        monthly_total.index.to_timestamp(),
        monthly_total.values,
        marker="o",
        color="steelblue",
    )
    ax1.set_title("Monthly Sales Trend")
    ax1.tick_params(axis="x", rotation=45)
    category_sales = df.groupby("Category")["Sales"].sum()
    ax2.bar(category_sales.index, category_sales.values, color="darkgreen")
    ax2.set_title("Sales by Category")
    top_10_states = state_sales.tail(10)
    ax3.barh(range(len(top_10_states)), top_10_states.values, color="royalblue")
    ax3.set_yticks(range(len(top_10_states)))
    ax3.set_yticklabels(top_10_states.index)
    ax3.set_title("Top 10 States by Sales")
    for category in df["Category"].unique():
        cat_data = df[df["Category"] == category]
        ax4.scatter(cat_data["Discount"], cat_data["Profit"], label=category, alpha=0.6)
    ax4.set_xlabel("Discount")
    ax4.set_ylabel("Profit")
    ax4.set_title("Discount vs Profit by Category")
    ax4.legend()
    ax4.axhline(y=0, color="black", linestyle="--", alpha=0.5)
    plt.suptitle(
        "Interactive Dashboard - US Superstore Performance",
        fontsize=18,
        fontweight="bold",
    )
    plt.tight_layout()
    plt.show()


create_dashboard()

# 5.2 Outlier annotation
plt.figure(figsize=(12, 8))
sns.scatterplot(data=df, x="Discount", y="Profit", hue="Category", alpha=0.6)
top_3_profitable = df.nlargest(3, "Profit")
bottom_3_profitable = df.nsmallest(3, "Profit")
for idx, row in top_3_profitable.iterrows():
    plt.annotate(
        f'Best: ${row["Profit"]:.0f}',
        xy=(row["Discount"], row["Profit"]),
        xytext=(10, 10),
        textcoords="offset points",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="green", alpha=0.7),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"),
    )
for idx, row in bottom_3_profitable.iterrows():
    plt.annotate(
        f'Worst: ${row["Profit"]:.0f}',
        xy=(row["Discount"], row["Profit"]),
        xytext=(10, -20),
        textcoords="offset points",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="red", alpha=0.7),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"),
    )
plt.title(
    "Discount vs Profit Analysis with Outlier Identification",
    fontsize=16,
    fontweight="bold",
)
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.axhline(y=0, color="black", linestyle="--", alpha=0.3)
plt.tight_layout()
plt.show()

# 5.3 Plotly comparison (if plotly installed)
try:
    import plotly.express as px

    fig = px.scatter(
        df,
        x="Discount",
        y="Profit",
        color="Category",
        hover_data=["Product Name", "Sales"],
        title="Interactive Discount vs Profit Analysis (Plotly)",
    )
    fig.add_traces(px.scatter(df, x="Discount", y="Profit", trendline="ols").data[1])
    fig.show()
    print("\nPLOTLY vs MATPLOTLIB COMPARISON:")
    print(
        "Plotly Advantages: Built-in interactivity, easy online sharing, professional tooltips, responsive design."
    )
    print(
        "Matplotlib + ipywidgets Advantages: More customization, better Jupyter integration, smaller files, familiar to Python data scientists."
    )
except ImportError:
    print(
        "\nPlotly not installed. Install with 'pip install plotly' to see interactive version."
    )

print("\n" + "=" * 70)
print("ANALYSIS COMPLETE. ALL VISUALIZATIONS AND INSIGHTS GENERATED.")
print("=" * 70)
