# TBD
# Comparing Factor Analysis with Principal Component Analysis (PCA)

While we've utilized factor analysis to identify underlying dimensions in our NanoVan data, it's instructive to compare these results with Principal Component Analysis (PCA) to understand the differences between these two dimension reduction techniques.

## Key Theoretical Differences

Factor Analysis and PCA differ in several important ways:

1. **Conceptual Difference**:
   - Factor Analysis attempts to identify latent constructs that explain correlations among variables
   - PCA is a mathematical transformation that maximizes variance explanation without assuming underlying factors

2. **Variance Approach**:
   - Factor Analysis focuses on shared variance (communalities)
   - PCA considers all variance including unique and error variance

3. **Usage in Marketing Research**:
   - Factor Analysis is preferred when the goal is to identify underlying consumer dimensions
   - PCA is preferred for pure dimensionality reduction or when creating uncorrelated composite variables

Let's apply PCA to our data and compare the results with our factor analysis.

```python
# Run PCA on the same attribute variables
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# First standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[attribute_vars])

# Determine number of components based on Kaiser criterion (eigenvalue > 1)
# This ensures we can compare with the same number of factors from our factor analysis
pca = PCA()
pca.fit(scaled_data)
n_components = sum(pca.explained_variance_ > 1)
print(f"Number of principal components with eigenvalue > 1: {n_components}")
```

```python
# Run PCA with the determined number of components
pca = PCA(n_components=n_components)
principal_components = pca.fit_transform(scaled_data)

# Create a DataFrame with the principal components
pc_df = pd.DataFrame(
    data=principal_components,
    columns=[f'PC{i+1}' for i in range(n_components)]
)

# Display variance explained by each component
explained_variance = pca.explained_variance_ratio_ * 100
cumulative_variance = np.cumsum(explained_variance)

variance_df = pd.DataFrame({
    'Component': [f'PC{i+1}' for i in range(n_components)],
    'Eigenvalue': pca.explained_variance_,
    'Variance Explained (%)': explained_variance,
    'Cumulative Variance (%)': cumulative_variance
})

print("\nVariance Explained by Principal Components:")
print(variance_df)
```

```python
# Create a scree plot for PCA
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(pca.explained_variance_) + 1), pca.explained_variance_, 'bo-')
plt.axhline(y=1, color='r', linestyle='--')
plt.xlabel('Principal Component Number')
plt.ylabel('Eigenvalue')
plt.title('Scree Plot of PCA Eigenvalues')
plt.grid(True)
plt.show()
```

```python
# Compare variance explained: PCA vs Factor Analysis
# Create a comparison DataFrame
comparison_df = pd.DataFrame({
    'Component/Factor': range(1, n_components + 1),
    'PCA Variance (%)': explained_variance,
    'Factor Analysis Variance (%)': explained_var[:n_components]  # Using the previously calculated values
})

plt.figure(figsize=(12, 6))
comparison_df.plot(x='Component/Factor', y=['PCA Variance (%)', 'Factor Analysis Variance (%)'], 
                  kind='bar', figsize=(12, 6))
plt.title('Variance Explained: PCA vs Factor Analysis')
plt.grid(axis='y')
plt.show()
```

```python
# Get component loadings (similar to factor loadings)
loadings = pca.components_.T
loadings_df = pd.DataFrame(
    data=loadings,
    columns=[f'PC{i+1}' for i in range(n_components)],
    index=attribute_vars
)

# Highlight significant loadings (> 0.4 in absolute value)
loadings_filtered = loadings_df.copy()
loadings_filtered[loadings_filtered.abs() < 0.4] = ''

print("\nPCA Component Loadings (values < 0.4 suppressed for clarity):")
print(loadings_filtered)
```

```python
# Create a heatmap of PCA loadings
plt.figure(figsize=(12, 10))
mask = loadings_df.abs() < 0.4  # Mask insignificant loadings
sns.heatmap(loadings_df, annot=True, cmap='coolwarm', mask=mask, fmt='.2f', linewidths=.5)
plt.title('PCA Component Loadings Heatmap (loadings < 0.4 hidden)', fontsize=16)
plt.tight_layout()
plt.show()
```

```python
# Use PCA components to predict NanoVan liking
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Prepare data
X_pca = pc_df
y = df['nvliking']

# Run regression with PCA components
model_pca = LinearRegression()
model_pca.fit(X_pca, y)

# Calculate R-squared
y_pred_pca = model_pca.predict(X_pca)
r2_pca = r2_score(y, y_pred_pca)
rmse_pca = np.sqrt(mean_squared_error(y, y_pred_pca))

print(f"\nRegression Results with PCA Components:")
print(f"R-squared: {r2_pca:.4f}")
print(f"RMSE: {rmse_pca:.4f}")
```

```python
# Compare with original regression and factor analysis regression
print(f"\nComparison of R-squared values:")
print(f"Original R-squared (30 variables): {r2:.4f}")
print(f"Factor Analysis R-squared ({n_factors} factors): {r2_factors:.4f}")
print(f"PCA R-squared ({n_components} components): {r2_pca:.4f}")
```

```python
# Create component importance dataframe
component_importance = pd.DataFrame({
    'Component': [f'PC{i+1}' for i in range(n_components)],
    'Coefficient': model_pca.coef_,
    'Abs_Coefficient': abs(model_pca.coef_)
})
component_importance = component_importance.sort_values('Abs_Coefficient', ascending=False)

print("\nPCA Component Importance in Predicting NanoVan Liking:")
print(component_importance)
```

```python
# Compare factor and component importance
comparison_data = pd.DataFrame({
    'Predictor': list(factor_importance['Factor'][:n_components]) + list(component_importance['Component']),
    'Coefficient': list(factor_importance['Coefficient'][:n_components]) + list(component_importance['Coefficient']),
    'Type': ['Factor Analysis'] * n_components + ['PCA'] * n_components
})

plt.figure(figsize=(12, 6))
sns.barplot(x='Predictor', y='Coefficient', hue='Type', data=comparison_data)
plt.title('Comparison of Regression Coefficients: Factor Analysis vs PCA', fontsize=16)
plt.axhline(y=0, color='r', linestyle='--')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
```

## Interpretation of PCA Results and Comparison with Factor Analysis

### Variance Explained
PCA typically explains slightly more variance with the same number of components compared to factor analysis. This is because PCA includes all variance (common, unique, and error variance), while factor analysis focuses on shared variance.

### Component Structure vs. Factor Structure
PCA components are mathematical constructs that maximize variance explanation but may not represent meaningful underlying constructs. Factor analysis often produces more interpretable results that better align with theoretical marketing constructs.

### Prediction Power
The regression results show that both approaches have similar predictive power for NanoVan liking, but the factor analysis produces more interpretable dimensions that can directly inform marketing strategy.

### Key Differences in Results

1. **Component Loading Patterns**:
   - PCA loadings tend to be more dispersed across variables
   - Factor analysis (with rotation) produces cleaner, more interpretable patterns

2. **Marketing Interpretability**:
   - PCA components are optimal for variance explanation but may combine conceptually distinct dimensions
   - Factor analysis better separates conceptually distinct marketing constructs

3. **Strategic Utility**:
   - PCA is excellent for dimensionality reduction but may be less useful for developing targeted marketing strategies
   - Factor analysis produces dimensions that more directly inform messaging and positioning strategies

### When to Use Each Method in Marketing Research

**Use Factor Analysis when:**
- You want to identify underlying consumer dimensions for targeting and positioning
- Interpretability of dimensions is critical
- You have a theoretical framework about consumer attitudes you want to test

**Use PCA when:**
- Pure dimensionality reduction is the goal
- You need orthogonal predictor variables for further analysis
- You're more concerned with prediction than interpretation

For the NanoVan case, factor analysis provides more actionable results for Lake View Associates by clearly identifying consumer dimensions that can guide marketing strategy development.
