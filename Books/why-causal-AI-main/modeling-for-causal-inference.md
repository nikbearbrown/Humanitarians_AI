---
description: Modeling for Causal Inference
---

# Modeling for Causal Inference

## **Modeling for Causal Inference: Theory and Mathematical Detail**

### **1. Introduction to Causal Models**

Causal models are **mathematical frameworks** designed to represent and analyze **causal relationships** between variables in a system. They help **infer causal effects** from statistical data and answer **counterfactual questions** like:

* _What would have happened if a different treatment was applied?_
* _How does a change in one variable influence another?_

> **Goal:**\
> Create a model that simulates a **parallel universe** where we can observe **both treated and untreated** outcomes for the same unit.

***

### **2. Fundamental Problem of Causal Inference**

The **Fundamental Problem of Causal Inference** states that we cannot simultaneously observe both **potential outcomes** Y(1)Y(1) and Y(0)Y(0) for the same individual.

> **Solution:**\
> Use **causal models** and **statistical methods** to estimate the **missing counterfactual outcome**.

***

### **3. Types of Causal Models**

#### **3.1. Structural Causal Models (SCM)**

An **SCM** is defined as a tuple:

M=(V,U,F,P(U))\mathcal{M} = (V, U, F, P(U))

Where:

* V={V1,V2,…,Vn}V = \\{V\_1, V\_2, \ldots, V\_n\\}: **Endogenous variables** (observed variables)
* U={U1,U2,…,Un}U = \\{U\_1, U\_2, \ldots, U\_n\\}: **Exogenous variables** (unobserved, external factors)
* F={f1,f2,…,fn}F = \\{f\_1, f\_2, \ldots, f\_n\\}: **Structural equations** linking variables
* P(U)P(U): Probability distribution over exogenous variables

#### **Structural Equation Example:**

Y=fY(T,X,UY);T=fT(X,UT)Y = f\_Y(T, X, U\_Y) \quad ; \quad T = f\_T(X, U\_T)

Where:

* TT: Treatment
* YY: Outcome
* XX: Covariates (confounders)
* UT,UYU\_T, U\_Y: Unobserved factors affecting TT and YY

***

#### **3.2. Potential Outcomes Framework (Rubin Causal Model)**

For each unit ii:

* Yi(1)Y\_i(1): Potential outcome if treated
* Yi(0)Y\_i(0): Potential outcome if untreated

**Individual Treatment Effect (ITE):**

ITEi=Yi(1)−Yi(0)\text{ITE}\_i = Y\_i(1) - Y\_i(0)

**Average Treatment Effect (ATE):**

ATE=E\[Y(1)−Y(0)]\text{ATE} = \mathbb{E}\[Y(1) - Y(0)]

***

#### **3.3. Graphical Models and Directed Acyclic Graphs (DAGs)**

DAGs represent causal relationships via **nodes** (variables) and **directed edges** (causal links).

**Properties:**

* **Acyclic:** No feedback loops
* **Edges:** Show causal direction (X→YX \rightarrow Y means X causes Y)

**Backdoor Criterion:**

A set of variables ZZ satisfies the **backdoor criterion** if:

1. No node in ZZ is a descendant of TT.
2. ZZ blocks every backdoor path from TT to YY.

**Adjustment formula:**

P(Y∣do(T))=∑zP(Y∣T,Z=z)P(Z=z)P(Y \mid do(T)) = \sum\_{z} P(Y \mid T, Z=z)P(Z=z)

***

### **4. Methods for Causal Inference**

#### **4.1. Experimental Methods**

**Randomized Controlled Trials (RCTs):**

Gold standard for causal inference where treatment is randomly assigned.

* **Effect estimation:**

ATE=E\[Y∣T=1]−E\[Y∣T=0]\text{ATE} = \mathbb{E}\[Y \mid T=1] - \mathbb{E}\[Y \mid T=0]

**Limitations:**

* Expensive, unethical in certain scenarios
* Limited external validity

***

#### **4.2. Observational Methods**

When RCTs are infeasible, use observational data with proper adjustments.

**A. Matching Methods**

Pairs treated and untreated units with similar covariates.

* **Propensity Score:** e(X)=P(T=1∣X)e(X) = P(T=1 \mid X)
* **Weighted ATE Estimation:**

τ^=1n∑i=1nTiYie(Xi)−(1−Ti)Yi1−e(Xi)\hat{\tau} = \frac{1}{n} \sum\_{i=1}^n \frac{T\_i Y\_i}{e(X\_i)} - \frac{(1 - T\_i) Y\_i}{1 - e(X\_i)}

***

**B. Regression Adjustment**

Model outcome as a function of treatment and covariates:

Y=α+βT+γX+ϵY = \alpha + \beta T + \gamma X + \epsilon

Where:

* β\beta: Estimated causal effect of treatment TT.

***

**C. Instrumental Variables (IV)**

Used when **unmeasured confounders** exist.

* **Conditions for Instrument (Z):**
  1. ZZ affects TT (relevance)
  2. ZZ affects YY **only through** TT (exclusion restriction)
* **Two-Stage Least Squares (2SLS):**
  * Stage 1: T=π0+π1Z+ϵTT = \pi\_0 + \pi\_1 Z + \epsilon\_T
  * Stage 2: Y=α+βT^+ϵYY = \alpha + \beta \hat{T} + \epsilon\_Y

**IV Estimator:**

β=Cov(Z,Y)Cov(Z,T)\beta = \frac{\text{Cov}(Z, Y)}{\text{Cov}(Z, T)}

***

**D. Regression Discontinuity Design (RDD)**

Exploits a **cutoff rule** for treatment assignment.

**Estimation near cutoff:**

τ=lim⁡x↓cE\[Y∣X=x]−lim⁡x↑cE\[Y∣X=x]\tau = \lim\_{x \downarrow c} \mathbb{E}\[Y \mid X=x] - \lim\_{x \uparrow c} \mathbb{E}\[Y \mid X=x]

***

**E. Difference-in-Differences (DiD)**

Uses before-and-after comparisons between treated and control groups.

**DiD Estimator:**

DiD=(YT,post−YT,pre)−(YC,post−YC,pre)\text{DiD} = (Y\_{T,post} - Y\_{T,pre}) - (Y\_{C,post} - Y\_{C,pre})

***

### **5. Bias Reduction Techniques**

#### **5.1. Controlling Confounders**

Adjust for confounders to block backdoor paths.

#### **5.2. Avoiding Conditioning on Colliders**

Conditioning on colliders opens non-causal paths, introducing bias.

#### **5.3. Sensitivity Analysis**

Test robustness of causal estimates under different assumptions.

***

### **6. Building a Causal Model**

#### **Steps:**

1. **Define the Research Question:**
   * What causal effect are you estimating?
2. **Identify Variables:**
   * Treatment (T), Outcome (Y), Confounders (Z), Mediators (M), Colliders (C).
3. **Construct a DAG:**
   * Map causal relations and identify backdoor paths.
4. **Select Estimation Method:**
   * Based on data availability and assumptions.
5. **Estimate and Interpret Effects:**
   * Compute ATE, ATT, or ATC using chosen methods.
6. **Validate with Sensitivity Analysis:**
   * Test how assumptions impact results.

***

### **7. Limitations of Causal Models**

* **Unobserved Confounding:** May still bias results.
* **Incorrect DAG Specification:** Leads to invalid conclusions.
* **Overfitting in Complex Models:** Especially with small data sets.
* **Model Dependence:** Estimates sensitive to modeling choices.

***

### **8. Conclusion**

**Causal modeling** is essential for understanding **cause-effect relationships** beyond mere associations. While we can never fully observe counterfactuals, these models help **approximate causal effects** and guide better **decision-making** in fields like medicine, economics, and policy-making.

> **Key Takeaways:**\
> ✅ Models help estimate counterfactuals but can’t eliminate all biases.\
> ✅ Proper adjustments and robust methods are crucial for credible inference.\
> ✅ Domain knowledge is essential for correct model specification.
