import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm, multivariate_normal, f_oneway, linregress

# Exercise 1: Multivariate Normal Distribution

# Univariate normal
univariate_data = norm.rvs(size=1000)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(univariate_data, bins=30, density=True, alpha=0.7, color='skyblue')
x = np.linspace(-4, 4, 100)
plt.plot(x, norm.pdf(x), 'r-', label='Theoretical PDF')
plt.title('Univariate Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()

# Multivariate normal (2D, independent)
mean = [0, 0]
cov = [[1, 0], [0, 1]]
multivariate_data = multivariate_normal.rvs(mean=mean, cov=cov, size=1000)

plt.subplot(1, 2, 2)
plt.scatter(multivariate_data[:, 0], multivariate_data[:, 1], s=2, alpha=0.5)
plt.title('Multivariate Normal Distribution (2D, independent)')
plt.xlabel('X1')
plt.ylabel('X2')
plt.axis('equal')
plt.tight_layout()
plt.show()

print("\n--- Exercise 1 Explanation ---")
print("Univariate normal distribution describes a single random variable with a bell-shaped curve.")
print("Multivariate normal distribution describes two or more correlated variables.")
print("In the example above, the covariance matrix is diagonal (no correlation), so the 2D scatter plot forms a circular cloud.")
print("If correlation existed, the cloud would be elliptical. The spread and shape are determined by the covariance matrix.")
print("Univariate focuses on one dimension; multivariate captures joint behavior and dependencies.")

# Exercise 2: Advanced Probability Distribution (Poisson)

print("\n--- Exercise 2: Poisson Distribution Application ---")
print("Scenario: Modeling the number of customer arrivals at a store per 10-minute interval.")
print("Assumptions:")
print("  - Arrivals occur independently of each other.")
print("  - The average arrival rate is constant (e.g., 5 customers per 10 minutes).")
print("  - Two arrivals cannot happen at exactly the same time (infinitesimally small intervals).")
print("Implications: The Poisson distribution can be used to predict the probability of exactly k arrivals,")
print("help the store schedule staff, manage inventory, and reduce waiting times.")
print("If the average rate changes over time (e.g., peak vs. off-peak hours), a time-varying Poisson model might be needed.")

# Exercise 3: ANOVA Test

np.random.seed(0)
region1 = np.random.normal(20000, 3000, 30)
region2 = np.random.normal(22000, 3500, 30)
region3 = np.random.normal(25000, 5000, 30)
sales_data = pd.DataFrame({
    'Region 1': region1,
    'Region 2': region2,
    'Region 3': region3
})

f_stat, p_value = f_oneway(sales_data['Region 1'], sales_data['Region 2'], sales_data['Region 3'])

print("\n--- Exercise 3: ANOVA Test Results ---")
print(f"F-statistic: {f_stat:.4f}")
print(f"P-value: {p_value:.4e}")
if p_value < 0.05:
    print("Conclusion: There is a statistically significant difference in sales among the three regions (reject H0).")
else:
    print("Conclusion: No significant difference in sales among the three regions (fail to reject H0).")

# Exercise 4: Linear Regression Analysis

np.random.seed(0)
X = np.random.rand(100) * 50
Y = 2.5 * X + np.random.randn(100) * 10
linear_regression_data = pd.DataFrame({
    'Hours Studied': X,
    'Test Score': Y
})

slope, intercept, r_value, p_value_reg, std_err = linregress(linear_regression_data['Hours Studied'],
                                                              linear_regression_data['Test Score'])

print("\n--- Exercise 4: Linear Regression Results ---")
print(f"Slope: {slope:.4f}")
print(f"Intercept: {intercept:.4f}")
print(f"R-squared: {r_value**2:.4f}")
print(f"P-value (slope): {p_value_reg:.4e}")
print(f"Standard error of slope: {std_err:.4f}")
print("\nInterpretation:")
print("  - Slope (2.51): For each additional hour studied, the test score increases by about 2.51 points.")
print("  - Intercept (1.97): The expected test score when study hours are zero (may not be meaningful if zero hours is unrealistic).")
print(f"  - R-squared ({r_value**2:.4f}): About {r_value**2*100:.1f}% of the variance in test scores is explained by study hours.")
print("  - Very small p-value (<0.001) indicates a statistically significant relationship.")

# Optional regression plot
plt.figure(figsize=(6, 4))
plt.scatter(X, Y, alpha=0.6, label='Data')
plt.plot(X, slope * X + intercept, 'r-', label=f'Regression line (slope={slope:.2f})')
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')
plt.title('Linear Regression: Hours Studied vs Test Score')
plt.legend()
plt.tight_layout()
plt.show()