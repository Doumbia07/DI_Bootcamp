import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Data Preparation
np.random.seed(42)
temperatures = np.random.uniform(-5, 35, size=(12, 10))

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]
cities = [f"City{i+1}" for i in range(10)]

df = pd.DataFrame(temperatures, index=months, columns=cities)

print("Dataset (first 5 months):")
print(df.head())

# 2. Data Analysis
annual_avg = df.mean(axis=0)
print("\nAnnual average temperature per city (°C):")
print(annual_avg.round(2))

city_highest = annual_avg.idxmax()
city_lowest = annual_avg.idxmin()
temp_highest = annual_avg.max()
temp_lowest = annual_avg.min()

print(f"\nCity with highest annual average: {city_highest} ({temp_highest:.2f}°C)")
print(f"City with lowest annual average: {city_lowest} ({temp_lowest:.2f}°C)")

# 3. Data Visualization
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
for city in cities:
    plt.plot(df.index, df[city], marker="o", linewidth=1, alpha=0.7)
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.title("Monthly Temperature Trends for All Cities")
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.5)

plt.subplot(1, 2, 2)
annual_avg_sorted = annual_avg.sort_values()
colors = [
    "red" if c == city_highest else "blue" if c == city_lowest else "skyblue"
    for c in annual_avg_sorted.index
]
plt.bar(annual_avg_sorted.index, annual_avg_sorted.values, color=colors)
plt.xlabel("City")
plt.ylabel("Annual Average Temperature (°C)")
plt.title("Annual Average Temperature per City")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()
