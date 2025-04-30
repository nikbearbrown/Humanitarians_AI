# AutoML Agents

**Requirements Document: Enhanced Binary Classifier Framework**

**Objective:**
The goal of this project is to enhance the existing binary classification pipeline by allowing easy addition of new classifiers, leveraging agentic AI for evaluation, and integrating automated leaderboard management for model selection. The final system should allow seamless integration of various classifiers while ensuring optimal model performance in a constrained feature space.

---

## **System Requirements**

### **1. Framework Architecture**
- Support easy integration of new binary classification algorithms.
- Implement a modular structure where classifiers can be plugged in and compared.
- Develop tools for agentic AI agents to evaluate models and provide recommendations.
- Export models in various formats compatible with different tools.
- Allow leaderboard-based selection of the best-performing classifier.
- Automate feature engineering, hyperparameter tuning, and ensembling in later phases.

---

### **2. Model Integration & Management**
- Support the following algorithms across different categories:
  
  **Classic Machine Learning Algorithms:**
  - Logistic Regression, SVM, Decision Trees, k-NN, Naive Bayes, LDA, QDA
  
  **Ensemble Methods:**
  - Random Forest, Extra Trees, AdaBoost, GBM, LightGBM, XGBoost, CatBoost
  
  **Deep Learning Models:**
  - MLP, CNNs, RNNs (LSTM, GRU), Transformer-based models
  
  **Specialized & Hybrid Approaches:**
  - Gaussian Processes Classifier, SGD Classifier, Elastic Net, Kernel Ridge, RuleFit, Factorization Machines
  
  **Advanced & Emerging Algorithms:**
  - NODE, TabNet, DeepFM, NAS-optimized architectures, gcForest, SAINT

- Each classifier should:
  - Be tunable using hyperparameter optimization techniques.
  - Output consistent evaluation metrics (AUC, accuracy, precision, recall, F1-score, etc.).
  - Be comparable via a unified benchmarking system.
  - Allow auto-selection of the best classifier for deployment.

---

### **3. Model Evaluation and Leaderboard**
- Implement a leaderboard system to rank classifiers based on:
  - Accuracy and generalizability across datasets.
  - Performance on unseen data.
  - Interpretability vs. complexity trade-offs.
- Use agentic AI to:
  - Analyze leaderboard results.
  - Suggest algorithmic improvements.
  - Automate model selection based on use case.

---

### **4. AutoML and Manual Optimization**
- Compare newly added classifiers against AutoML frameworks:
  - H2O AutoML
  - AutoGluon
- Develop a methodology to:
  - Outperform AutoML models on a constrained feature space.
  - Identify optimal hyperparameters for selected classifiers.
  - Implement stacked ensembles in later iterations.

| Algorithm     | Most Accurate on Non-Profit Data with Many Categorical Features | Re-Encodes Categorical Data         | Encoding Method                                  | Mathematical Basis                                        | Bias-Variance Tradeoff               | Computational Speed | Overfitting Tendency |
|--------------|----------------------------------------------------------------|------------------------------------|------------------------------------------------|----------------------------------------------------------|---------------------------------------|-------------------|----------------------|
| Random Forest | Moderate                                                      | Requires manual encoding           | One-hot, ordinal                                 | Bagging with decision trees, Gini impurity/entropy       | Low bias, moderate variance          | Moderate          | Low (due to bagging) |
| Extra Trees  | Moderate                                                      | Requires manual encoding           | One-hot, ordinal                                 | Randomized splits, no bootstrap sampling                 | Lower bias, higher variance          | Fast              | Moderate (random splits) |
| AdaBoost     | Low                                                           | Requires manual encoding           | One-hot, ordinal                                 | Exponential loss minimization, weighted re-sampling      | Low bias, high variance              | Slow              | High (reweighting mechanism) |
| GBM          | Moderate                                                      | Requires manual encoding           | One-hot, ordinal                                 | Gradient descent on loss function, residual fitting      | Moderate bias, moderate variance    | Moderate          | Moderate (depends on tuning) |
| LightGBM     | High                                                          | Requires manual encoding           | One-hot, ordinal                                 | Histogram-based gradient boosting, GOSS, EFB            | Moderate bias, lower variance       | Very Fast         | Moderate (leaf-wise growth) |
| XGBoost      | High                                                          | Requires manual encoding           | One-hot, ordinal                                 | Second-order optimization (Newton-Raphson), regularization | Low bias, low variance              | Fast              | Low (regularization in place) |
| CatBoost     | Very High                                                     | Automatically with Target Statistics | Target Statistics, Ordered Boosting             | Ordered boosting, symmetric trees, categorical handling  | Low bias, low variance              | Moderate          | Low (ordered boosting, L2 regularization) |

### Why CatBoost?

CatBoost should be the next algorithm to try because it is specifically designed to handle categorical data efficiently, making it an excellent choice for non-profit datasets that often contain many categorical features. Unlike other boosting algorithms that require manual encoding (such as one-hot or ordinal encoding), CatBoost automatically processes categorical variables using Target Statistics and Ordered Boosting, reducing the risk of target leakage and improving model performance. Its symmetric tree structure ensures balanced splits, which enhances stability and generalization. With low bias and variance, moderate computational speed, and strong regularization (L2 leaf penalization), CatBoost is well-suited for achieving high accuracy while minimizing overfitting, making it an ideal candidate for non-profit data classification tasks.


---

### **5. Integration with Squark's Platform**
- Ensure models can be exported in a format usable by Squark’s infrastructure.
- Maintain compatibility with existing orchestration scripts.
- Provide seamless integration with existing data pipelines.

---

### **6. Implementation Steps**
#### **Phase 1: Research & Selection**
- Conduct comparative research on different classifiers.
- Select a shortlist of algorithms based on dataset constraints.
- Develop an initial benchmark using AutoGluon and H2O AutoML.

#### **Phase 2: Model Development & Benchmarking**
- Implement the selected classifiers.
- Perform hyperparameter tuning.
- Compare models against AutoGluon and H2O AutoML.

#### **Phase 3: Agentic AI Integration**
- Develop an AI-driven evaluation module.
- Implement auto-selection of classifiers.
- Integrate leaderboard ranking system.

#### **Phase 4: Deployment & Optimization**
- Finalize the best-performing classifiers.
- Ensure seamless integration with Squark’s infrastructure.
- Automate feature engineering and ensembling in future iterations.

---

## **Action Items & Deliverables**
- **Research & Documentation:**
  - Detailed comparison of classifiers (mathematical basis, strengths, weaknesses).
  - Recommended algorithms for initial testing.
- **Development:**
  - Implementation of classifiers with benchmark results.
  - Python module for integration into Squark’s system.
- **Testing & Optimization:**
  - Performance analysis vs. AutoML frameworks.
  - Fine-tuning of hyperparameters for optimal accuracy.
- **Final Integration:**
  - Deployment-ready models.
  - Automated leaderboard and AI-driven model selection.

---

## **Next Steps & Timeline**
- **Week 1:** Research, shortlist algorithms, benchmark AutoGluon & H2O.
- **Week 2:** Develop initial classifiers, perform tuning & testing.
- **Week 3:** Integrate AI-driven evaluation and leaderboard system.
- **Week 4:** Deploy top-performing models and optimize for production.

**Why CatBoost?**

CatBoost should be the next algorithm to try because it is specifically designed to handle categorical data efficiently, making it an excellent choice for non-profit datasets that often contain many categorical features. Unlike other boosting algorithms that require manual encoding (such as one-hot or ordinal encoding), CatBoost automatically processes categorical variables using Target Statistics and Ordered Boosting, reducing the risk of target leakage and improving model performance. Its symmetric tree structure ensures balanced splits, which enhances stability and generalization. With low bias and variance, moderate computational speed, and strong regularization (L2 leaf penalization), CatBoost is well-suited for achieving high accuracy while minimizing overfitting, making it an ideal candidate for non-profit data classification tasks.

---

### **CatBoost Libraries and Hyperparameters**

To implement CatBoost, you will need to install the CatBoost library:
```bash
pip install catboost
```

In Python, you can import and use it as follows:
```python
from catboost import CatBoostClassifier
model = CatBoostClassifier()
```

#### **Key Hyperparameters in CatBoost**

| Hyperparameter      | Description | Default Value |
|---------------------|-------------|--------------|
| `iterations`       | Number of boosting iterations. | `1000` |
| `learning_rate`    | Step size shrinkage used to prevent overfitting. | `0.03` |
| `depth`            | Depth of the tree. | `6` |
| `l2_leaf_reg`      | L2 regularization term to prevent overfitting. | `3.0` |
| `loss_function`    | Defines the objective function (e.g., `Logloss` for classification). | `Logloss` |
| `eval_metric`      | Performance metric for evaluation. | `AUC` |
| `cat_features`     | Specifies categorical feature indices. | `[]` |
| `border_count`     | Number of splits for numerical features. | `254` |
| `verbose`          | Controls logging output. | `200` |

---

### **Hyperparameter Search for CatBoost Using AutoML Agents**
To find the best-performing hyperparameters for CatBoost, we can use grid search, random search, or Bayesian optimization. The AutoML approach leverages AI-driven tuning to automate this process.

#### **Using Grid Search for Hyperparameter Tuning**
```python
from sklearn.model_selection import GridSearchCV
from catboost import CatBoostClassifier

# Define parameter grid
param_grid = {
    'depth': [4, 6, 8, 10],
    'learning_rate': [0.01, 0.03, 0.1],
    'iterations': [500, 1000],
    'l2_leaf_reg': [1, 3, 5]
}

model = CatBoostClassifier(cat_features=[0, 1, 2])
grid_search = GridSearchCV(model, param_grid, scoring='roc_auc', cv=3)
grid_search.fit(X_train, y_train)
print(grid_search.best_params_)
```

#### **Using Bayesian Optimization for AutoML-Driven Search**
```python
from skopt import BayesSearchCV

opt = BayesSearchCV(
    CatBoostClassifier(cat_features=[0, 1, 2], verbose=0),
    {
        'depth': (4, 10),
        'learning_rate': (0.01, 0.1, 'log-uniform'),
        'iterations': (500, 2000),
        'l2_leaf_reg': (1, 10)
    },
    n_iter=30, cv=3, scoring='roc_auc'
)

opt.fit(X_train, y_train)
print(opt.best_params_)
```

#### **Using Optuna for Advanced Hyperparameter Optimization**
```python
import optuna
from catboost import CatBoostClassifier
from sklearn.model_selection import cross_val_score

def objective(trial):
    params = {
        'iterations': trial.suggest_int('iterations', 500, 2000),
        'depth': trial.suggest_int('depth', 4, 10),
        'learning_rate': trial.suggest_loguniform('learning_rate', 0.01, 0.1),
        'l2_leaf_reg': trial.suggest_int('l2_leaf_reg', 1, 10),
        'eval_metric': 'AUC',
        'cat_features': [0, 1, 2],
        'verbose': 0
    }
    
    model = CatBoostClassifier(**params)
    score = cross_val_score(model, X_train, y_train, cv=3, scoring='roc_auc').mean()
    return score

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=30)
print(study.best_params)
```

---

### **Integration with AutoML Agents**
To further automate the process of model selection, AutoML Agents can be leveraged to run experiments, track model performance, and identify the best-performing classifier dynamically. Some tools that can be used include:
- **H2O AutoML**
- **AutoGluon**
- **TPOT**
- **MLFlow for tracking experiments**

This ensures that CatBoost's hyperparameters are optimized efficiently, leading to the best possible performance in constrained feature spaces. As a next step, CatBoost can be benchmarked against AutoML frameworks such as H2O AutoML to validate its performance in the enhanced binary classification pipeline.

---

By leveraging CatBoost’s ability to handle categorical features efficiently, optimizing hyperparameters using AutoML-based searches, and integrating it with an AI-driven leaderboard system, we can build a highly effective binary classification pipeline for non-profit data applications.

## What is Target Leakage?

Imagine you’re building a machine learning model to predict whether a student will pass or fail an exam based on things like **study hours, homework scores, and attendance**. Target leakage happens when your model accidentally uses information that wouldn’t be available **before** the exam is taken—basically, it’s like cheating.

For example, if you include **the student’s final test score** as an input, your model will look very accurate because it already knows the answer! But in real-world use, this model would fail because you wouldn’t have the final test score in advance.

### **How Algorithms Can Create Features That Cause Problems**
Some machine learning algorithms, like **gradient boosting models** (CatBoost, LightGBM, XGBoost), try to automatically create new features from the data to improve predictions. This can be really powerful, but it can also introduce **unexpected problems**, especially when dealing with **rare categories** in categorical data.

#### **Example: Automatically Created Features in Categorical Data**
Let’s say you're analyzing student behavior at a school, and one of your features is **which classroom they usually study in**. Some classrooms might have many students, but what if **one student is the only one who ever studied in Classroom X?** 

- During **training**, the model might learn that "Classroom X" is a very strong signal for whether a student passes or fails because it was seen in historical data.
- But during **testing**, if no students from Classroom X appear, the model **doesn't know how to handle it** and might crash or give incorrect predictions.

This issue happens because the algorithm **created a new feature** (i.e., it learned a specific rule for Classroom X) that was only present in the training data but missing in the test data.

### **How CatBoost Handles This Problem**
Some algorithms handle this problem better than others. **CatBoost**, for example, uses a technique called **Ordered Boosting** and **Target Statistics** to process categorical data more safely. Instead of creating strict rules that depend on rare categories, it replaces them with a generalized number based on all the available data—helping to **avoid errors when rare features appear only in training** but not in testing.

### **Key Takeaways**
1. **Target leakage** happens when the model learns from information it shouldn’t have at prediction time—like knowing the test score before predicting if someone passes.
2. **Automatically created features** (especially from categorical variables) can cause problems when rare features exist in training but not in testing.
3. **Some algorithms, like CatBoost, have built-in ways to handle this issue** by encoding categorical features in a way that reduces reliance on rare categories.

Would you trust a model that predicts who will pass a test by **already knowing their grade?** No way! That’s why we have to be careful with feature engineering and how machine learning models create new features. 🚀
# Handling Missing Features in Testing

A common issue in machine learning pipelines is when a feature appears in the training data but does not exist in the test set. This can cause models to fail during inference. CatBoost provides built-in mechanisms to handle such cases effectively:

### CatBoost's Built-in Handling Mechanisms

- **Default Missing Value Handling** - CatBoost can automatically treat missing categorical and numerical values without explicit imputation.
- **Categorical Feature Handling** - Since CatBoost uses Target Statistics, rare categories that appear only in training but not in testing will not cause errors, as they will be mapped to default category encodings.
- **`allow_const_label` Parameter** - This allows CatBoost to handle datasets where some categories or features may be missing.
- **`cat_features` Argument** - By explicitly defining categorical features, CatBoost can manage unseen categories by applying previously learned encodings.

To ensure robust handling of feature mismatches between training and testing sets, preprocessing techniques such as dynamic feature engineering and automated feature consistency checks should be integrated into the pipeline.

### Example Code to Handle Unseen Categorical Features

```python
from catboost import CatBoostClassifier

# Define the model and specify categorical features
model = CatBoostClassifier(cat_features=[0, 1, 2], use_best_model=True)

# Train the model
model.fit(X_train, y_train)

# Handling unseen categorical values
X_test = X_test.apply(lambda x: x if x in model.classes_ else 'Unknown')

# Make predictions
predictions = model.predict(X_test)






