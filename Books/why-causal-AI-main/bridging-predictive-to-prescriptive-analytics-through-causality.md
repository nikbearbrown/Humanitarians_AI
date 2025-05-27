---
description: Bridging Predictive to Prescriptive Analytics Through Causality
---

# Bridging Predictive to Prescriptive Analytics Through Causality

## **Types of Data Analysis: Bridging Predictive to Prescriptive Analytics Through Causality**

Data analysis plays a critical role in understanding patterns, forecasting future events, and making informed decisions. Traditionally, analytics have been categorized into three main types:

1. **Descriptive Analytics:** _What happened?_
2. **Predictive Analytics:** _What will happen?_
3. **Prescriptive Analytics:** _What should we do?_

While predictive analytics can forecast future outcomes based on patterns in historical data, **prescriptive analytics** seeks to provide actionable recommendations. Transitioning from predictive to prescriptive analytics requires understanding _causality_—the relationships that explain why changes in one variable lead to changes in another.

***

### **1. Descriptive Analytics: Understanding the Past**

Descriptive analytics focuses on summarizing historical data to answer _"What happened?"_ using methods like:

* **Statistical summaries:** Mean, median, variance
* **Data visualizations:** Histograms, boxplots, time-series plots
* **Probability distributions:** To understand data spread

#### **Mathematical Framework:**

Given a dataset {x1,x2,…,xn}\\{x\_1, x\_2, \dots, x\_n\\}:

* **Mean:** xˉ=1n∑i=1nxi\bar{x} = \frac{1}{n}\sum\_{i=1}^{n} x\_i
* **Variance:** σ2=1n−1∑i=1n(xi−xˉ)2\sigma^2 = \frac{1}{n-1}\sum\_{i=1}^{n}(x\_i - \bar{x})^2
* **Probability distribution function (PDF):** For continuous data, fX(x)f\_X(x) describes the probability of observing a value near xx.

Descriptive analytics is crucial for understanding the data landscape but lacks the ability to predict or prescribe actions.

***

### **2. Predictive Analytics: Forecasting the Future**

Predictive analytics uses statistical models and machine learning to predict future events based on historical data. It answers _"What will happen?"_

#### **Common Techniques:**

* **Regression models:** Linear regression, logistic regression
* **Time series forecasting:** ARIMA, exponential smoothing
* **Machine learning models:** Random forests, neural networks

#### **Mathematical Details:**

**2.1. Linear Regression Model:**

For a response variable YY and predictors XX:

Y=β0+β1X+ϵY = \beta\_0 + \beta\_1X + \epsilon

Where:

* β0\beta\_0: Intercept
* β1\beta\_1: Slope (change in YY per unit change in XX)
* ϵ\epsilon: Error term (ϵ∼N(0,σ2)\epsilon \sim N(0, \sigma^2))

Prediction for a new observation x∗x^\*:

Y^=β0+β1x∗\hat{Y} = \beta\_0 + \beta\_1 x^\*

***

**2.2. Classification Example (Logistic Regression):**

To predict binary outcomes:

Pr(Y=1∣X)=11+e−(β0+β1X)Pr(Y=1 \mid X) = \frac{1}{1 + e^{-(\beta\_0 + \beta\_1 X)\}}

The model outputs a probability between 0 and 1.

***

**2.3. Limitations of Predictive Analytics:**

Predictive models are built on correlations:

Pr(Y=1∣A=1)≠Pr(Y=1∣A=0)Pr(Y=1 \mid A=1) \neq Pr(Y=1 \mid A=0)

While useful, this doesn’t imply that changing AA causes a change in YY. Predictive models may be misleading if confounding variables exist.

***

### **3. Prescriptive Analytics: Making Decisions with Causality**

Prescriptive analytics focuses on recommending actions by answering: _"What should we do?"_ Achieving this requires understanding **causal relationships**, not just associations.

#### **3.1. Moving from Prediction to Prescription:**

To prescribe an action (like launching a marketing campaign), we must understand:

Pr(Y=1∣do(A=1))vs.Pr(Y=1∣A=1)Pr(Y=1 \mid do(A=1)) \quad \text{vs.} \quad Pr(Y=1 \mid A=1)

* **Without causality:** Pr(Y=1∣A=1)Pr(Y=1 \mid A=1) shows association.
* **With causality:** Pr(Y=1∣do(A=1))Pr(Y=1 \mid do(A=1)) measures the effect of actively intervening on AA.

***

#### **3.2. Causal Inference Methods:**

**Potential Outcomes Framework (Rubin Causal Model):**

Defines potential outcomes under treatment and control:

Y(a=1):Outcome if treated,Y(a=0):Outcome if not treatedY^{(a=1)}: \text{Outcome if treated}, \quad Y^{(a=0)}: \text{Outcome if not treated}

**Average Treatment Effect (ATE):**

ATE=E\[Y(a=1)]−E\[Y(a=0)]\text{ATE} = E\[Y^{(a=1)}] - E\[Y^{(a=0)}]

If ATE ≠0\neq 0, the treatment causally affects the outcome.

***

**3.3. Counterfactual Prediction:**

Counterfactuals answer _"What would have happened if...?"_

For an individual:

Individual Treatment Effect (ITE)=Y(a=1)−Y(a=0)\text{Individual Treatment Effect (ITE)} = Y^{(a=1)} - Y^{(a=0)}

Example:

* Y(a=1)=1Y^{(a=1)}=1 (purchased after ad)
* Y(a=0)=0Y^{(a=0)}=0 (wouldn’t purchase without ad)

ITE = 1 - 0 = 1 (Positive causal effect)

***

### **4. The Role of Intervention in Decision Making**

Predictive models provide probabilities, but decision-making involves _intervention_. To move from _"What might happen?"_ to _"What should we do?"_, we must ask:

* **What if we offer discounts?**
* **How would customer retention change if we improved service?**
* **Would reducing ad frequency improve user engagement?**

#### **Mathematical Formulation:**

Interventions are represented using the **do-operator**:

Pr(Y∣do(A=a))=∑zPr(Y∣A=a,Z=z)Pr(Z=z)Pr(Y \mid do(A=a)) = \sum\_{z} Pr(Y \mid A=a, Z=z)Pr(Z=z)

* ZZ: Confounders that affect both AA and YY.
* **Frontdoor and Backdoor Criteria:** Methods to control confounding and identify causal effects.

***

### **5. Why Causality Matters for Decision Intelligence**

#### **5.1. Example: Recommendation Systems**

Predictive model:

Pr(Activity=1∣Friends=x)=f(x)Pr(\text{Activity}=1 \mid \text{Friends}=x) = f(x)

Finds correlation between online activity and number of friends.

**Key question for prescriptive analytics:**

* _"Will adding friends increase user activity?"_

Causal analysis investigates:

Pr(Activity=1∣do(Friends=x+1))≠Pr(Activity=1∣Friends=x+1)Pr(\text{Activity}=1 \mid do(\text{Friends}=x+1)) \neq Pr(\text{Activity}=1 \mid \text{Friends}=x+1)

Without causal analysis, decisions may be based on spurious correlations.

***

#### **5.2. Simpsons Paradox**

**Paradox:** Trends appear in different groups but reverse when data is combined.

**Example (Medical Study):**

* In separate age groups, Treatment A seems better.
* Combined data suggests Treatment B is superior.

This discrepancy occurs without accounting for confounders.

**Mathematical Illustration:**

Pr(Y=1∣A=1,Z=young)>Pr(Y=1∣A=0,Z=young)Pr(Y=1 \mid A=1, Z=young) > Pr(Y=1 \mid A=0, Z=young) Pr(Y=1∣A=1,Z=old)>Pr(Y=1∣A=0,Z=old)Pr(Y=1 \mid A=1, Z=old) > Pr(Y=1 \mid A=0, Z=old)

But:

Pr(Y=1∣A=1)\<Pr(Y=1∣A=0)(Simpsons Paradox)Pr(Y=1 \mid A=1) < Pr(Y=1 \mid A=0) \quad \text{(Simpsons Paradox)}

***

### **6. Decision Intelligence: The Future of Data-Driven Decisions**

**Decision Intelligence** integrates data science, social science, and managerial science to improve decision-making.

#### **Key Mathematical Tools:**

* **Structural Causal Models (SCMs):**

Y=f(A,U),U⊥AY = f(A, U), \quad U \perp A

* **Inverse Probability Weighting (IPW):**

E^\[Y(a)]=1N∑i=1NI(Ai=a)YiPr(Ai=a∣Xi)\hat{E}\[Y^{(a)}] = \frac{1}{N} \sum\_{i=1}^{N} \frac{\mathbb{I}(A\_i=a) Y\_i}{Pr(A\_i=a \mid X\_i)}

* **Do-calculus:** Allows manipulation of causal expressions for identification.

***

### **7. Real-World Applications and Causal Questions**

| **Domain**    | **Predictive Analysis**   | **Prescriptive (Causal) Analysis**               |
| ------------- | ------------------------- | ------------------------------------------------ |
| **Marketing** | Will a user click the ad? | What happens if we show fewer ads?               |
| **Medicine**  | Risk of disease?          | Does the vaccine cause fewer hospitalizations?   |
| **Economics** | Future unemployment rate? | How will raising minimum wage affect employment? |

***

### **8. Conclusion: Causality as the Foundation of Decision-Making**

* **Descriptive Analytics:** Helps understand the past.
* **Predictive Analytics:** Forecasts future outcomes.
* **Prescriptive Analytics (Causal):** Guides _what actions to take_.

Causality transforms predictions into actionable insights. By understanding **cause-and-effect relationships**, organizations can make more informed, ethical, and effective decisions.

***

### **9. Key Takeaways**

✅ Predictive models forecast but do not explain _why_.\
✅ Prescriptive models use causality for actionable decisions.\
✅ Ignoring confounders leads to misguided strategies.\
✅ Causal inference methods provide robust frameworks for decision-making.

***

### **10. Resources**

* **Pearl, J. (2018).** _The Book of Why_
* **Hernán, M., & Robins, J. (2020).** _Causal Inference: What If_
* **Wikipedia:** [Decision Intelligence](https://en.wikipedia.org/wiki/Decision_intelligence)

***

Understanding causality isn’t just an academic exercise—it’s the difference between **guessing** and **knowing** how decisions will shape the future.
