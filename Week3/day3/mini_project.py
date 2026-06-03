import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import mplfinance as mpf

# 1: Load and Explore Data
df = pd.read_csv("Week3/day3/Apple Stock Prices_(1981 to 2023).csv")
print(df.head())
print(df.info())
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
print(df.isnull().sum())
df.set_index("Date", inplace=True)
print(df.describe())
# 2: Line Plot of Closing Price
plt.figure(figsize=(12, 5))
plt.plot(df.index, df["Close"], label="Close Price", color="blue")
plt.title("AAPL Closing Price Over Time")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
# 2: Candlestick Chart
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)
ax1.plot(df.index, df["Close"], color="blue", linewidth=1)
ax1.set_title("AAPL Closing Price")
ax1.set_ylabel("Price (USD)")
ax1.grid(True, alpha=0.3)
ax2.bar(df.index, df["Volume"], color="gray", alpha=0.6, width=1)
ax2.set_title("Trading Volume")
ax2.set_xlabel("Date")
ax2.set_ylabel("Volume")
ax2.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
# 3: Candlestick Chart with mplfinance
mpf.plot(
    df[["Open", "High", "Low", "Close", "Volume"]],
    type="candle",
    style="charles",
    title="AAPL Candlestick Chart",
    volume=True,
)
# 4: Statistical Analysis
print(df[["Open", "High", "Low", "Close", "Volume"]].describe())
# 5: Moving Average and Visualization
window = 20
df["MA20"] = df["Close"].rolling(window=window).mean()
plt.figure(figsize=(12, 5))
plt.plot(df.index, df["Close"], label="Close Price", alpha=0.5)
plt.plot(df.index, df["MA20"], label=f"{window}-day MA", color="red")
plt.title(f"AAPL Closing Price with {window}-day Moving Average")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
# 6: Correlation Analysis
year1 = 2010
year2 = 2020
close_year1 = df[df.index.year == year1]["Close"]
close_year2 = df[df.index.year == year2]["Close"]
t_stat, p_value = stats.ttest_ind(close_year1, close_year2)
print(f"Mean {year1}: ${close_year1.mean():.2f}")
print(f"Mean {year2}: ${close_year2.mean():.2f}")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4e}")
if p_value < 0.05:
    print("Significant difference in average closing prices.")
else:
    print("No significant difference.")

df["Return"] = df["Close"].pct_change().dropna()
returns = df["Return"].dropna()
norm_stat, norm_p = stats.normaltest(returns)
print(f"Normality test p-value: {norm_p:.4e}")
if norm_p < 0.05:
    print("Returns are NOT normally distributed.")
else:
    print("Returns are normally distributed.")

plt.figure(figsize=(10, 5))
plt.hist(
    returns, bins=50, density=True, alpha=0.6, color="skyblue", label="Observed returns"
)
mu, std = stats.norm.fit(returns)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, mu, std)
plt.plot(x, p, "r-", label=f"Normal fit (μ={mu:.4f}, σ={std:.4f})")
plt.title("Distribution of Daily Returns with Normal Fit")
plt.xlabel("Daily Return")
plt.ylabel("Density")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()


# 7: Advanced Analysis - Moving Average with Convolution
def moving_average_convolve(data, window):
    return np.convolve(data, np.ones(window) / window, mode="valid")


close_prices = df["Close"].values
ma_convolve = moving_average_convolve(close_prices, window)
dates_aligned = df.index[window - 1 :]
plt.figure(figsize=(12, 5))
plt.plot(df.index, df["Close"], label="Close Price", alpha=0.5)
plt.plot(dates_aligned, ma_convolve, label=f"{window}-day MA (convolve)", color="green")
plt.title("Moving Average using np.convolve")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

df["MA20"] = df["Close"].rolling(window=20).mean()
corr_ma_volume = df[["MA20", "Volume"]].corr().iloc[0, 1]
print(f"Correlation MA20 and Volume: {corr_ma_volume:.4f}")

df["Return"] = df["Close"].pct_change()
corr_return_volume = df[["Return", "Volume"]].corr().iloc[0, 1]
print(f"Correlation Return and Volume: {corr_return_volume:.4f}")

from scipy import signal

b, a = signal.butter(3, 0.05, btype="low")
trend = signal.filtfilt(b, a, close_prices)
detrended = close_prices - trend
plt.figure(figsize=(12, 5))
plt.plot(df.index, close_prices, label="Original", alpha=0.5)
plt.plot(df.index, trend, label="Trend (low-pass)", linewidth=2)
plt.plot(df.index, detrended, label="Detrended (residual)", alpha=0.7)
plt.title("Detrending Closing Price with Butterworth Filter")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
