# Top Algorithms for Wide Tabular Data With Mixed Features

## A. Gradient Boosting Methods
### 1. XGBoost
**Strengths:** Well-established for tabular data; robust, flexible, and proven in competitions.

**Key Hyperparameters to Tune:**
- `n_estimators` (number of trees)
- `learning_rate`
- `max_depth`
- `min_child_weight` (controls leaf weight / minimum sum of instance weight needed in a child)
- `gamma` (minimum loss reduction required to make a further partition)
- `subsample` (row sampling)
- `colsample_bytree` (feature sampling)
- `reg_alpha`, `reg_lambda` (L1 & L2 regularization)

### 2. LightGBM
**Strengths:** Speed and memory efficiency, especially on large datasets. Excels with categorical data (if using the "categorical_feature" parameter).

**Key Hyperparameters:**
- `num_leaves`
- `max_depth`
- `learning_rate`
- `feature_fraction` (like colsample_bytree)
- `bagging_fraction` and `bagging_freq` (row subsampling)
- `min_data_in_leaf` or `min_child_samples` (analogous to min_child_weight in XGBoost)
- `lambda_l1`, `lambda_l2` (regularization)
- **Categorical handling:** Setting the `categorical_feature` parameter for columns that are truly categorical (if not already label-encoded).

### 3. CatBoost
**Strengths:** Particularly good with categorical data and can automatically handle it via various encodings; can often reduce the amount of explicit label encoding needed.

**Key Hyperparameters:**
- `iterations` (equivalent to n_estimators)
- `learning_rate`
- `depth`
- `l2_leaf_reg` (regularization)
- `random_strength` (similar to randomization in splits)
- `bagging_temperature` (another method of sampling)
- `one_hot_max_size` (threshold for using one-hot vs. target encoding for categorical features)

These gradient boosting methods are generally the strongest candidates for large, wide datasets with mixed numeric & categorical features.

## B. Classical Tree Ensembles
### 1. Random Forest or Extra Trees
**Strengths:**
- Often simpler to tune than GBMs.
- Good baseline if you just want a quick model.

**Drawbacks:**
- Typically outperformed by well-tuned gradient boosting for pure AUC, but still respectable.
- Easier to interpret in terms of feature importance.

**Key Hyperparameters:**
- `n_estimators`
- `max_features` (number of features used per split)
- `max_depth`
- `min_samples_split`, `min_samples_leaf`
- **For Extra Trees:** Choice of “extremely randomized” splitting.

## C. Regularized Linear Models
### 1. Logistic Regression (with Elastic Net / L1 / L2)
**Strengths:**
- Easy to interpret coefficients.
- Good as a secondary / quick baseline.

**Drawbacks:**
- May not capture all complex interactions in wide, highly non-linear data.

**Key Hyperparameters:**
- `penalty` = `l1`, `l2`, or `elasticnet`
- `C` (inverse of regularization strength)
- `l1_ratio` (for elastic net)

If interpretability is important—or if you want a simpler model for regulated applications—this is worth including in the ensemble of models.

## D. Deep Learning for Tabular Data
### 1. TabNet, SAINT, NODE (Neural methods for structured data)
**Strengths:**
- Potential to learn complex interactions automatically.
- Some (like TabNet) incorporate feature selection as part of the architecture.

**Drawbacks:**
- Often overshadowed by GBMs for purely tabular data unless you have a massive dataset and do extensive hyperparameter tuning.
- More complicated to train and tune than tree-based methods.

**Key Hyperparameters (Example: TabNet):**
- `n_d / n_a` (dimensions of the decision/attention steps)
- `n_steps` (how many sequential decision steps)
- `gamma` (relates to feature selection)
- `lambda_sparse` (regularization of sparse feature selection)
- `optimizer params` (learning rate, weight decay, etc.)

If your organization wants to experiment beyond gradient boosting—especially if you start seeing diminishing returns from GBMs—these can be tested.

---

# Strategies for Different Targets & Data Splits

## Immediate Response vs. Future Outcome Prediction

1. **Different Label Definitions:**
   - **Response Classification:** `1 if donor gave to that specific appeal, 0 otherwise.`
   - **Future Outcome Prediction:** `1 if donor gave at least once in the next 6 months, 0 otherwise.`

2. **Potentially Different Input Features:**
   - **Immediate Response:** Last appeal’s recency/frequency, channel, personalization.
   - **Future Outcome:** Aggregated data (past 12-month frequency, average gift, total gifts in last X months, etc.).

3. **Separate or Combined Modeling:**
   - Build separate models for immediate response and 6-month future giving.
   - Alternatively, unify them via multi-label classification (less common unless both tasks are strongly related).

4. **Data Preparation Considerations:**
   - **Time-based splits:** Always train on older appeals, test on newer appeals to avoid data leakage.
   - **Aggregation:** Future prediction models may prefer one row per donor, while immediate response models may keep multiple row-level appeals.
   - **Handling repeated donors:** Group by donor ID in cross-validation to avoid leakage.

---

# Key Tuning "Flags" to Focus On

- **Learning Rate / Step Size:**
  - Lower rates yield better results but need more iterations.
  - Common starting points: `0.05` or `0.01` for large datasets.

- **Depth / Complexity Controls:**
  - **For trees:** `max_depth`, `num_leaves` (LightGBM), or `depth` (CatBoost).
  - **Moderate depth to prevent overfitting in wide datasets.**

- **Regularization:**
  - Use L1, L2, or forms like `gamma`, `min_child_weight` (XGBoost).
  - Helps prevent excessive splits in large, wide datasets.

- **Row and Feature Subsampling:**
  - `subsample`, `colsample_bytree`, `feature_fraction` improve generalization.
  - Range: `[0.6, 1.0]`.

- **Categorical Feature Handling:**
  - CatBoost/LightGBM handle natively; XGBoost requires label encoding or one-hot encoding.
  - Watch for high-cardinality categorical features (>1000 values); consider grouping or target encoding.

---

# Example Hyperparameter Ranges

**LightGBM Example:**
```python
param_grid = {
    'learning_rate':    [0.001, 0.01, 0.05, 0.1],
    'num_leaves':       [31, 63, 127, 255],
    'max_depth':        [-1, 6, 12, 16],
    'min_data_in_leaf': [20, 50, 100],
    'feature_fraction': [0.6, 0.8, 1.0],
    'bagging_fraction': [0.6, 0.8, 1.0],
    'bagging_freq':     [1, 5],
    'lambda_l1':        [0.0, 0.1, 1.0],
    'lambda_l2':        [0.0, 0.1, 1.0]
}
```

By following this framework, you can systematically approach both short-term response classification and long-term donor outcome predictions using largely the same pipeline while adjusting hyperparameters accordingly.




