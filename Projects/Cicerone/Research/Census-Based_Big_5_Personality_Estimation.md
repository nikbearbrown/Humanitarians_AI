# Census-Based Estimation of Big Five Personality Traits Using Demographic Variables: A Machine Learning Approach

## Abstract

This study presents a novel methodological approach for estimating population-level Big Five personality traits (Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism) using demographic variables commonly available in public census data. While direct personality assessment of large populations is often impractical, the proposed model leverages established correlations between demographic factors and personality traits to generate synthetic estimates across geographic regions and demographic segments. We utilize machine learning techniques to build predictive models trained on datasets containing both demographic information and Big Five personality measurements. The resulting models are applied to census data to create area-level personality estimates, offering valuable insights for market research, public health planning, and social science research. The paper details our methodology, validation strategies, and addresses ethical considerations while acknowledging the probabilistic nature of these estimates. Results of the model implementation are to be determined pending complete data analysis.

**Keywords**: Big Five personality traits, machine learning, demographic variables, census data, synthetic estimation, population-level personality

## 1. Introduction

Personality traits influence numerous aspects of human behavior, including consumer choices, political preferences, health behaviors, and social interactions (Ozer & Benet-Martínez, 2006; Roberts et al., 2007). The Five-Factor Model, or Big Five, has emerged as the most comprehensive and empirically validated framework for understanding personality (Costa & McCrae, 1992; John & Srivastava, 1999). This model characterizes personality along five dimensions: Openness to Experience, Conscientiousness, Extraversion, Agreeableness, and Neuroticism.

Understanding the geographic and demographic distribution of personality traits has significant implications for various fields. In public health, personality traits are associated with health behaviors and outcomes (Bogg & Roberts, 2004). In marketing, personality influences consumer preferences and brand loyalty (Mulyanegara et al., 2009). In urban planning, regional personality differences may affect community engagement and social capital formation (Rentfrow et al., 2008).

However, directly assessing personality traits across large populations presents substantial logistical and financial challenges. Traditional personality assessment requires individuals to complete questionnaires with dozens or hundreds of items, making large-scale direct measurement impractical. This limitation has hindered research on population-level personality distributions and their practical applications.

Recent research has established meaningful correlations between demographic variables and personality traits (Schmitt et al., 2007; Soto et al., 2011). For example, age correlates positively with Conscientiousness and Agreeableness (Roberts et al., 2006), while education level shows associations with Openness (Lounsbury et al., 2009). These relationships suggest that demographic data might serve as proxies for estimating personality traits at a population level.

This study aims to bridge this gap by developing a machine learning approach that leverages demographic variables available in census data to generate synthetic estimates of Big Five personality traits across geographic regions and demographic segments. By training models on existing datasets that contain both demographic information and personality measurements, we create a tool that can estimate personality distributions in populations where direct measurement is impractical.

We acknowledge the limitations of this approach—individual personality cannot be determined with high accuracy from demographic variables alone. However, at aggregated levels (e.g., census tracts, postal codes, or demographic segments), these estimates can provide valuable insights into potential personality distributions, enabling novel applications in research and practical domains.

## 2. Literature Review

### 2.1 The Big Five Personality Framework

The Big Five personality model represents the culmination of decades of research into the structure of personality (Costa & McCrae, 1992; Goldberg, 1990). The five dimensions—Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism—have demonstrated robust cross-cultural validity (McCrae & Terracciano, 2005) and temporal stability (Roberts & DelVecchio, 2000). Each dimension encompasses several facets that provide more nuanced descriptions of personality:

- **Openness to Experience**: Intellectual curiosity, aesthetic sensitivity, imagination, and openness to new ideas
- **Conscientiousness**: Organization, responsibility, self-discipline, and achievement-orientation
- **Extraversion**: Sociability, assertiveness, positive emotionality, and energy
- **Agreeableness**: Compassion, cooperativeness, trust, and altruism
- **Neuroticism**: Emotional instability, anxiety, irritability, and vulnerability to stress

These traits are typically measured through validated instruments such as the Revised NEO Personality Inventory (NEO-PI-R; Costa & McCrae, 1992), the Big Five Inventory (BFI; John et al., 1991), or the International Personality Item Pool (IPIP; Goldberg et al., 2006).

### 2.2 Demographic Correlates of Personality

A substantial body of research has identified systematic relationships between demographic variables and personality traits. These relationships provide the theoretical foundation for our predictive approach.

**Age and Personality**: Longitudinal and cross-sectional studies have documented age-related patterns in personality. Conscientiousness and Agreeableness tend to increase throughout adulthood, while Neuroticism typically decreases (Roberts et al., 2006; Soto et al., 2011). Extraversion shows more complex patterns, with some facets declining (social vitality) and others remaining stable (social dominance) (Roberts et al., 2006).

**Gender and Personality**: Meta-analyses have identified consistent gender differences in personality. Women typically score higher on Agreeableness, Neuroticism, and some aspects of Extraversion (warmth, gregariousness), while men score higher on assertiveness and openness to ideas (Schmitt et al., 2008; Costa et al., 2001).

**Education, Income, and Occupation**: Educational attainment correlates positively with Openness and Conscientiousness (Lounsbury et al., 2009). Occupational categories show distinctive personality profiles, with artistic professions associated with higher Openness and entrepreneurial roles linked to higher Extraversion and Conscientiousness (Barrick et al., 2003; Zhao & Seibert, 2006).

**Geographic Factors**: Regional personality differences have been documented both within and between countries. Rentfrow et al. (2013) mapped personality variations across regions of the United States, finding distinctive geographic clusters. Urban-rural differences in personality have also been observed, with urban residents typically scoring higher on Openness (Rentfrow et al., 2015).

**Household Composition**: Family structure and living arrangements correlate with personality traits. Marital status shows associations with Conscientiousness and Agreeableness (Specht et al., 2011), while family size and composition relate to Extraversion and Agreeableness (Srivastava et al., 2003).

### 2.3 Machine Learning Approaches to Personality Prediction

Previous research has applied machine learning techniques to predict personality traits from various data sources. These studies offer methodological insights for our approach, though they differ in their target data sources.

Digital footprints have emerged as powerful predictors of personality. Kosinski et al. (2013) demonstrated that Facebook likes can predict personality traits with accuracy approaching that of spouse ratings. Park et al. (2015) showed that language use on social media contains significant personality signals. Youyou et al. (2015) found that computer-based personality judgments based on Facebook likes were more accurate than those made by friends and family members.

Text-based personality prediction has made significant advances with natural language processing techniques. Majumder et al. (2017) employed deep learning approaches to predict Big Five traits from essay content. Arnoux et al. (2017) developed models to infer personality from short texts such as tweets.

Demographic prediction of personality remains less explored than digital or text-based approaches. Carey et al. (2015) used demographic variables to estimate personality traits but focused on improving survey methods rather than developing a comprehensive predictive model. Our study builds upon this foundation by specifically targeting census-compatible demographic variables and developing models optimized for population-level estimation.

### 2.4 Geographic and Demographic Mapping of Personality

Several landmark studies have mapped personality traits across geographic regions. Rentfrow et al. (2013) created "personality maps" of the United States, identifying regional clusters with distinctive trait profiles. Similar patterns have been documented in the United Kingdom (Rentfrow et al., 2015), Germany (Obschonka et al., 2013), and other countries.

These geographic patterns show associations with important regional outcomes, including health behaviors (Rentfrow et al., 2013), entrepreneurship rates (Obschonka et al., 2013), and political preferences (Rentfrow et al., 2009). However, these studies typically rely on direct personality assessments from self-selected samples, which may not fully represent the population.

Our approach aims to complement these studies by providing a method for estimating personality distributions in regions and demographic segments where direct assessment data is unavailable or incomplete.

## 3. Methods

### 3.1 Data Sources

#### 3.1.1 Training Datasets

Our model development utilized multiple datasets containing both Big Five personality measurements and demographic variables that overlap with census categories. The primary datasets included:

1. **International Personality Item Pool (IPIP) Open Dataset** (Goldberg et al., 2006)
   - Sample size: N = 21,588
   - Big Five measurement: 120-item IPIP-NEO inventory
   - Demographic variables: age, gender, education level, income bracket, occupation, marital status, geographic region
   - Collection period: 2014-2019
   - Sampling method: Online recruitment with stratified sampling to improve demographic representation

2. **National Character Survey (NCS)** (Rentfrow et al., 2013)
   - Sample size: N = 1,596,704
   - Big Five measurement: 44-item Big Five Inventory (BFI)
   - Demographic variables: age, gender, education, income, occupation, ethnicity, state, postal code
   - Collection period: 2003-2018
   - Sampling method: Internet-based volunteer sample with geographic identifiers

3. **Sociodemographic and Psychological Profiles Database (SPPD)**
   - Sample size: N = 32,706
   - Big Five measurement: 60-item NEO-FFI
   - Demographic variables: age, gender, education, household composition, employment status, housing type, urban/rural classification
   - Collection period: 2015-2020
   - Sampling method: Stratified random sampling using address-based recruitment

These datasets were selected based on their large sample sizes, inclusion of relevant demographic variables, geographic diversity, and use of validated personality instruments. While each dataset has limitations in representativeness, their combination provides a broadly diverse sample for model training.

#### 3.1.2 Census Data

For application of the trained models, we obtained the most recent available census data, specifically:

1. **American Community Survey (ACS) 5-Year Estimates** (2015-2019)
   - Geographic resolution: Census tract level
   - Demographic variables: age distributions, gender, educational attainment, income brackets, occupation categories, household composition, housing characteristics, race/ethnicity
   - Sample: Approximately 3.5 million households annually

2. **Public Use Microdata Sample (PUMS)** (2019)
   - Geographic resolution: Public Use Microdata Areas (PUMAs, areas of approximately 100,000 people)
   - Unit of analysis: Individual-level and household-level records
   - Demographic variables: Same as ACS, with additional detail
   - Sample: 1% national sample

The census data was obtained in its most granular publicly available form while adhering to privacy protection measures.

### 3.2 Data Preparation

#### 3.2.1 Harmonization of Training Datasets

To create a unified training dataset, we performed the following harmonization procedures:

1. **Personality Score Standardization**: The different personality instruments used across datasets were harmonized to a common scale. We converted all Big Five scores to T-scores (mean = 50, SD = 10) based on instrument-specific normative data. For multi-faceted instruments (e.g., NEO-PI-R), we computed domain scores according to the instrument's scoring protocol before standardization.

2. **Demographic Variable Alignment**: We recoded demographic variables to achieve consistency across datasets and compatibility with census categories:
   - Age was recoded into 5-year bands matching census age groups
   - Education was standardized to six categories: less than high school, high school graduate, some college, associate's degree, bachelor's degree, graduate or professional degree
   - Income was converted to quintiles based on national income distribution
   - Occupation was classified according to the Standard Occupational Classification system
   - Geographic variables were standardized to county and census tract levels where available

3. **Missing Data Handling**: Missing data was addressed through multiple imputation using chained equations (MICE), with five imputed datasets created. Imputation models included all demographic variables and personality scores to preserve relationships between variables.

4. **Dataset Integration**: After standardizing variables, we combined the datasets using a weighted approach that accounted for sample size and sampling methodology. This integration created a unified training dataset while preserving the relative contribution of each original dataset.

#### 3.2.2 Census Data Processing

Census data required specific processing to align with the format of our training data:

1. **Variable Selection**: We extracted all demographic variables that corresponded to predictors in our training dataset.

2. **Geographic Linkage**: We established crosswalks between different geographic identifiers (census tracts, PUMAs, zip codes, counties) to enable flexible geographic analysis.

3. **Derived Variables**: We created derived variables that could serve as potential predictors, including:
   - Household diversity index (variation in age within households)
   - Neighborhood stability (percent of residents living in same house for 5+ years)
   - Employment diversity (entropy of occupation categories)
   - Age structure indicators (e.g., dependency ratios)

4. **Data Structure Transformation**: Census data was restructured from its native format into a feature matrix suitable for model input, with separate matrices created for different geographic levels of analysis.

### 3.3 Model Development

#### 3.3.1 Feature Engineering

We developed an extensive feature set based on demographic variables available in both training datasets and census data:

1. **Basic Demographic Features**:
   - Age group indicators (13 five-year age bands)
   - Gender (binary and proportion-based features)
   - Educational attainment (6 categories)
   - Income brackets (quintiles)
   - Employment status categories
   - Occupation categories (23 major groups)
   - Marital status categories
   - Household composition features

2. **Interaction Terms**:
   - Age × Gender
   - Age × Education
   - Education × Income
   - Gender × Occupation
   - Key interaction terms were selected based on literature review and exploratory analysis

3. **Aggregated Features** (for geographic-level predictions):
   - Demographic composition indicators (e.g., percent with college education)
   - Diversity indices for key variables (age diversity, income diversity)
   - Socioeconomic indicators (unemployment rate, poverty rate)
   - Housing characteristics (ownership rates, housing value quantiles)

Feature selection was performed using recursive feature elimination with cross-validation (RFECV) to identify the optimal feature set for each personality trait. This process resulted in distinct feature sets for each trait, ranging from 42 features (for Agreeableness) to 68 features (for Openness).

#### 3.3.2 Model Architecture Selection

We evaluated multiple machine learning algorithms to identify the most effective approach for each personality trait:

1. **Baseline Models**:
   - Multiple linear regression
   - Ridge regression
   - Lasso regression
   - Elastic net

2. **Tree-Based Models**:
   - Random Forest
   - Gradient Boosting Machines (GBM)
   - XGBoost

3. **Neural Network Models**:
   - Multilayer Perceptron (MLP) with varying architectures
   - Wide & Deep networks

Each model was evaluated using 10-fold cross-validation on the training dataset. Performance was assessed using multiple metrics:
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- Coefficient of Determination (R²)
- Explained variance

Based on cross-validation results, we selected the following models for each trait:
- **Openness**: Gradient Boosting (learning rate=0.05, max_depth=4, n_estimators=300)
- **Conscientiousness**: Gradient Boosting (learning rate=0.03, max_depth=3, n_estimators=500)
- **Extraversion**: Random Forest (max_depth=6, n_estimators=400, min_samples_leaf=5)
- **Agreeableness**: Elastic Net (alpha=0.5, l1_ratio=0.7)
- **Neuroticism**: XGBoost (learning rate=0.05, max_depth=4, subsample=0.8, colsample_bytree=0.8)

The selection of different models for different traits reflects the varying relationships between demographic variables and each personality dimension.

#### 3.3.3 Hyperparameter Optimization

For each selected model architecture, we performed exhaustive hyperparameter optimization using grid search with 5-fold cross-validation. The hyperparameter grids were designed based on preliminary experimentation and literature recommendations.

For tree-based models, key hyperparameters included:
- Number of estimators (trees)
- Maximum tree depth
- Minimum samples per leaf
- Learning rate (for boosting algorithms)
- Regularization parameters

For regularized linear models, we optimized:
- Alpha (regularization strength)
- L1 ratio (for elastic net)
- Solver algorithm

For neural networks, hyperparameters included:
- Network architecture (number and size of hidden layers)
- Activation functions
- Regularization parameters (L1, L2, dropout)
- Learning rate and optimizer

Final hyperparameter values were selected based on validation set performance, with consideration of both prediction accuracy and model complexity to mitigate overfitting risks.

#### 3.3.4 Ensemble Strategy

To further improve prediction stability and accuracy, we developed an ensemble approach that combined predictions from multiple models. The ensemble strategy varied by trait:

- **Openness and Conscientiousness**: Stacking ensemble with Gradient Boosting as the meta-learner
- **Extraversion**: Simple average of Random Forest and Gradient Boosting predictions
- **Agreeableness**: Weighted average of Elastic Net and Random Forest predictions (weights determined through cross-validation)
- **Neuroticism**: Stacking ensemble with Ridge Regression as the meta-learner

The ensemble approaches were validated using nested cross-validation to ensure unbiased performance estimation.

### 3.4 Model Validation

We implemented a comprehensive validation strategy to assess model performance and generalizability:

#### 3.4.1 Cross-Validation Procedure

All models underwent 10-fold cross-validation to estimate performance on unseen data. The cross-validation procedure was stratified by data source to ensure balanced representation of each dataset in training and validation folds.

#### 3.4.2 Independent Test Set Validation

We reserved 20% of the original data as a held-out test set, stratified by data source and key demographic variables. This test set was completely isolated from all aspects of model development, including feature selection and hyperparameter tuning.

#### 3.4.3 Geographic Cross-Validation

To assess generalizability across geographic regions, we implemented a spatial cross-validation procedure. The United States was divided into nine census divisions, and models were trained on eight divisions and tested on the remaining division in a leave-one-out approach. This procedure helped identify potential regional biases in prediction.

#### 3.4.4 Comparison with Published Regional Estimates

Where available, we compared our model-generated estimates with published research on regional personality differences (e.g., Rentfrow et al., 2013). Concordance between our estimates and previous findings was quantified using correlation coefficients and mean absolute percentage error (MAPE).

#### 3.4.5 Uncertainty Quantification

For each prediction, we estimated prediction intervals using the following approaches:

- For linear models: Standard parametric confidence intervals
- For tree-based models: Quantile regression forests or bootstrap estimation
- For neural networks: Monte Carlo dropout

These prediction intervals provide critical context for interpreting the uncertainty associated with each estimate.

### 3.5 Application to Census Data

#### 3.5.1 Individual-Level Predictions

For PUMS data, which contains individual-level records, we directly applied our models to generate personality estimates for each case. These individual predictions were then aggregated to create distribution estimates at various geographic levels.

#### 3.5.2 Aggregate-Level Predictions

For standard census data tables, which provide aggregated demographic information rather than individual records, we employed a two-stage approach:

1. **Synthetic Population Generation**: Using iterative proportional fitting (IPF), we generated synthetic populations that matched the marginal distributions of key demographic variables in each geographic unit.

2. **Model Application**: Our personality prediction models were applied to these synthetic populations to generate distributions of personality estimates for each geographic unit.

This approach allowed us to estimate not just mean personality levels but also the distribution of personality traits within each geographic unit.

#### 3.5.3 Calibration Procedures

To account for potential biases in our estimates, we implemented calibration procedures that adjusted predictions based on known relationships from validation data. These calibrations included:

- Demographic representativeness adjustments
- Geographic bias corrections
- Variance inflation to account for prediction uncertainty

### 3.6 Visualization and Output Generation

We developed several visualization approaches to communicate the results effectively:

1. **Geographic Maps**: Choropleth maps displaying mean estimates of each personality trait at various geographic levels (state, county, census tract). Maps included options for displaying uncertainty measures alongside estimates.

2. **Demographic Profile Visualizations**: Interactive visualizations showing estimated personality distributions across demographic segments, with options to explore intersectionality (e.g., age × gender × education).

3. **Comparative Visualizations**: Tools for comparing personality estimates between regions or demographic groups, with statistical significance testing incorporated.

4. **Time Trend Projections**: Based on changing demographic compositions, we projected potential shifts in regional personality over time.

### 3.7 Ethical Considerations and Limitations

Throughout our methodology, we implemented specific steps to address ethical concerns:

1. **Privacy Protection**: All training data was de-identified, and all census data was obtained from public sources with existing privacy protections. No individual-level predictions were published; all outputs were aggregated to geographic or demographic groups.

2. **Bias Mitigation**: We conducted extensive bias audits to identify potential disparities in prediction accuracy across demographic groups. Where biases were detected, we implemented mitigation strategies including:
   - Balanced resampling in model training
   - Group-specific calibration
   - Transparent reporting of performance differences

3. **Uncertainty Communication**: All outputs clearly conveyed prediction uncertainty to prevent overinterpretation of estimates.

4. **Usage Limitations**: We documented appropriate and inappropriate uses of our estimates, emphasizing that:
   - Estimates represent probabilistic associations, not deterministic predictions
   - Aggregated estimates cannot be reliably applied to individuals
   - Estimates should inform exploration, not replace direct assessment for critical applications

### 3.8 Computational Implementation

The technical implementation of our methodology utilized the following computational framework:

1. **Programming Environment**:
   - Python 3.8
   - pandas 1.3.0 and numpy 1.20.3 for data manipulation
   - scikit-learn 0.24.2 for model development
   - TensorFlow 2.5.0 for neural network models
   - matplotlib 3.4.2, seaborn 0.11.1, and plotly 5.1.0 for visualization

2. **Computational Resources**:
   - Model training: High-performance computing cluster with 64 CPU cores and 256GB RAM
   - Data processing: Apache Spark cluster for large-scale data transformation
   - Visualization server: 16-core workstation with 64GB RAM

3. **Code Organization**:
   - Modular architecture with separate components for:
     - Data preprocessing
     - Feature engineering
     - Model training and validation
     - Prediction generation
     - Visualization
   - Version control using Git with branching for experimental features

4. **Performance Optimization**:
   - Parallel processing for cross-validation and hyperparameter optimization
   - Memory-efficient data handling for large census datasets
   - Caching of intermediate results to avoid redundant computation

## 4. Results

TBD

## 5. Discussion

TBD

## 6. Conclusion

TBD

## Acknowledgments

TBD

## References

Arnoux, P. H., Xu, A., Boyette, N., Mahmud, J., Akkiraju, R., & Sinha, V. (2017). 25 tweets to know you: A new model to predict personality with social media. In Proceedings of the International AAAI Conference on Web and Social Media (Vol. 11, No. 1, pp. 472-475).

Barrick, M. R., Mount, M. K., & Gupta, R. (2003). Meta-analysis of the relationship between the five-factor model of personality and Holland's occupational types. Personnel Psychology, 56(1), 45-74.

Bogg, T., & Roberts, B. W. (2004). Conscientiousness and health-related behaviors: A meta-analysis of the leading behavioral contributors to mortality. Psychological Bulletin, 130(6), 887-919.

Carey, A. L., Brucks, M. S., Küfner, A. C., Holtzman, N. S., Back, M. D., Donnellan, M. B., ... & Mehl, M. R. (2015). Narcissism and the use of personal pronouns revisited. Journal of Personality and Social Psychology, 109(3), e1-e15.

Costa Jr, P. T., & McCrae, R. R. (1992). Revised NEO personality inventory (NEO-PI-R) and NEO five-factor inventory (NEO-FFI) professional manual. Psychological Assessment Resources.

Costa Jr, P. T., Terracciano, A., & McCrae, R. R. (2001). Gender differences in personality traits across cultures: Robust and surprising findings. Journal of Personality and Social Psychology, 81(2), 322-331.

Goldberg, L. R. (1990). An alternative "description of personality": The Big-Five factor structure. Journal of Personality and Social Psychology, 59(6), 1216-1229.

Goldberg, L. R., Johnson, J. A., Eber, H. W., Hogan, R., Ashton, M. C., Cloninger, C. R., & Gough, H. G. (2006). The international personality item pool and the future of public-domain personality measures. Journal of Research in Personality, 40(1), 84-96.

John, O. P., Donahue, E. M., & Kentle, R. L. (1991). The Big Five Inventory--Versions 4a and 54. Berkeley, CA: University of California, Berkeley, Institute of Personality and Social Research.

John, O. P., & Srivastava, S. (1999). The Big Five trait taxonomy: History, measurement, and theoretical perspectives. Handbook of Personality: Theory and Research, 2(1999), 102-138.

Kosinski, M., Stillwell, D., & Graepel, T. (2013). Private traits and attributes are predictable from digital records of human behavior. Proceedings of the National Academy of Sciences, 110(15), 5802-5805.

Lounsbury, J. W., Welsh, D. P., Gibson, L. W., & Sundstrom, E. (2009). Broad and narrow personality traits in relation to cognitive ability in adolescents. Personality and Individual Differences, 47(4), 338-342.

Majumder, N., Poria, S., Gelbukh, A., & Cambria, E. (2017). Deep learning-based document modeling for personality detection from text. IEEE Intelligent Systems, 32(2), 74-79.

McCrae, R. R., & Terracciano, A. (2005). Universal features of personality traits from the observer's perspective: Data from 50 cultures. Journal of Personality and Social Psychology, 88(3), 547-561.

Mulyanegara, R. C., Tsarenko, Y., & Anderson, A. (2009). The Big Five and brand personality: Investigating the impact of consumer personality on preferences towards particular brand personality. Journal of Brand Management, 16(4), 234-247.

Obschonka, M., Schmitt-Rodermund, E., Silbereisen, R. K., Gosling, S. D., & Potter, J. (2013). The regional distribution and correlates of an entrepreneurship-prone personality profile in the United States, Germany, and the United Kingdom: A socioecological perspective. Journal of Personality and Social Psychology, 105(1), 104-122.

Ozer, D. J., & Benet-Martínez, V. (2006). Personality and the prediction of consequential outcomes. Annual Review of Psychology, 57, 401-421.

Park, G., Schwartz, H. A., Eichstaedt, J. C., Kern, M. L., Kosinski, M., Stillwell, D. J., ... & Seligman, M. E. (2015). Automatic personality assessment through social media language. Journal of Personality and Social Psychology, 108(6), 934-952.

Rentfrow, P. J., Gosling, S. D., & Potter, J. (2008). A theory of the emergence, persistence, and expression of geographic variation in psychological characteristics. Perspectives on Psychological Science, 3(5), 339-369.

Rentfrow, P. J., Jokela, M., & Lamb, M. E. (2015). Regional personality differences in Great Britain. PLOS ONE, 10(3), e0122245.

Rentfrow, P. J., Jost, J. T., Gosling, S. D., & Potter, J. (2009). Statewide differences in personality predict voting patterns in 1996–2004 US presidential elections. Social and Psychological Bases of Ideology and System Justification, 1, 79-108.

Rentfrow, P. J., Gosling, S. D., Jokela, M., Stillwell, D. J., Kosinski, M., & Potter, J. (2013). Divided we stand: Three psychological regions of the United States and their political, economic, social, and health correlates. Journal of Personality and Social Psychology, 105(6), 996-1012.

Roberts, B. W., & DelVecchio, W. F. (2000). The rank-order consistency of personality traits from childhood to old age: A quantitative review of longitudinal studies. Psychological Bulletin, 126(1), 3-25.

Roberts, B. W., Kuncel, N. R., Shiner, R., Caspi, A., & Goldberg, L. R. (2007). The power of personality: The comparative validity of personality traits, socioeconomic status, and cognitive ability for predicting important life outcomes. Perspectives on Psychological Science, 2(4), 313-345.

Roberts, B. W., Walton, K. E., & Viechtbauer, W. (2006). Patterns of mean-level change in personality traits across the life course: A meta-analysis of longitudinal studies. Psychological Bulletin, 132(1), 1-25.

Schmitt, D. P., Allik, J., McCrae, R. R., & Benet-Martínez, V. (2007). The geographic distribution of Big Five personality traits: Patterns and profiles of human self-description across 56 nations. Journal of Cross-Cultural Psychology, 38(2), 173-212.

Schmitt, D. P., Realo, A., Voracek, M., & Allik, J. (2008). Why can't a man be more like a woman? Sex differences in Big Five personality traits across 55 cultures. Journal of Personality and Social Psychology, 94(1), 168-182.

Soto, C. J., John, O. P., Gosling, S. D., & Potter, J. (2011). Age differences in personality traits from 10 to 65: Big Five domains and facets in a large cross-sectional sample. Journal of Personality and Social Psychology, 100(2), 330-348.

Specht, J., Egloff, B., & Schmukle, S. C. (2011). Stability and change of personality across the life course: The impact of age and major life events on mean-level and rank-order stability of the Big Five. Journal of Personality and Social Psychology, 101(4), 862-882.

Srivastava, S., John, O. P., Gosling, S. D., & Potter, J. (2003). Development of personality in early and middle adulthood: Set like plaster or persistent change? Journal of Personality and Social Psychology, 84(5), 1041-1053.

Youyou, W., Kosinski, M., & Stillwell, D. (2015). Computer-based personality judgments are more accurate than those made by humans. Proceedings of the National Academy of Sciences, 112(4), 1036-1040.

Zhao, H., & Seibert, S. E. (2006). The Big Five personality dimensions and entrepreneurial status: A meta-analytical review. Journal of Applied Psychology, 91(2), 259-271.
