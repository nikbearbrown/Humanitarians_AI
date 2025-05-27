---
description: Key Causal Terms
---

# Key Causal Terms

## **Causal Inference Glossary and FAQ**

This glossary provides key terms, mathematical definitions, and frequently asked questions related to causal inference, helping to clarify fundamental concepts in understanding cause-and-effect relationships in data analysis.

***

### **Key Causal Terms**

#### **1. What is the Causal Effect?**

The **causal effect** measures the difference in potential outcomes when an intervention is applied versus when it is not. Mathematically:

Causal Effect=Y(Treatment)−Y(No Treatment)\text{Causal Effect} = Y(\text{Treatment}) - Y(\text{No Treatment})

For population-level measures, we use the **Average Treatment Effect (ATE)**:

ATE=E\[Y(a=1)]−E\[Y(a=0)]\text{ATE} = E\[Y^{(a=1)}] - E\[Y^{(a=0)}]

***

#### **2. What Does Cause Mean?**

A **cause** refers to a variable that, when changed, leads to a change in another variable, holding all else constant:

X causes Y  ⟺  Pr(Y∣do(X=x))≠Pr(Y∣do(X=x′))X \text{ causes } Y \iff Pr(Y \mid do(X=x)) \neq Pr(Y \mid do(X=x'))

***

#### **3. Purpose of Causality**

Causality seeks to uncover true cause-and-effect relationships.

* **Example Question:** Does smoking cause cancer?\
  Mathematically, we seek to determine if:

Pr(Cancer=1∣do(Smoking=1))>Pr(Cancer=1∣do(Smoking=0))Pr(\text{Cancer}=1 \mid do(\text{Smoking}=1)) > Pr(\text{Cancer}=1 \mid do(\text{Smoking}=0))

***

#### **4. What is Causal Reasoning?**

**Causal reasoning** involves understanding how interventions influence outcomes. If AA causes BB, then without AA, BB should not occur:

A→B⇒Pr(B∣do(A=0))\<Pr(B∣do(A=1))A \to B \quad \Rightarrow \quad Pr(B \mid do(A=0)) < Pr(B \mid do(A=1))

***

#### **5. What is an Estimand?**

An **estimand** defines the quantity of interest in causal analysis. For example, the ATE is an estimand:

Estimand=E\[Y(1)]−E\[Y(0)]\text{Estimand} = E\[Y^{(1)}] - E\[Y^{(0)}]

***

#### **6. What is the Data Generating Process (DGP)?**

The **DGP** is the underlying process that produces the data. In a **Structural Causal Model (SCM)**:

Y=f(A,UY),A=g(Z,UA)Y = f(A, U\_Y), \quad A = g(Z, U\_A)

Where UY,UAU\_Y, U\_A are unobserved noise variables. The goal is to infer properties of the DGP from observed data.

***

#### **7. What is Causal Inference?**

**Causal inference** draws conclusions about causal relationships using data and assumptions.

**Inputs:**

* **Question:** What do we wish to know?
* **Knowledge:** What do we already know?
* **Data:** Observational or experimental data.

**Outputs:**

* Effects of interventions: Pr(Y∣do(A=a))Pr(Y \mid do(A=a))
* Counterfactual predictions: Pr(Ya′∣A=a,Y=y)Pr(Y\_{a'} \mid A=a, Y=y)

***

#### **8. What are Treatment and Outcome?**

* **Treatment (AA):** The cause/intervention. Example: Giving a vaccine.
* **Outcome (YY):** The effect. Example: Getting sick or not.

***

#### **9. What is the Gold Standard for Causal Analysis?**

**Randomized Controlled Trials (RCTs)** are the gold standard:

Pr(Y=1∣do(A=1))−Pr(Y=1∣do(A=0))Pr(Y=1 \mid do(A=1)) - Pr(Y=1 \mid do(A=0))

However, RCTs are not always feasible. Observational studies with methods like **Inverse Probability Weighting (IPW)** offer alternatives:

E^\[Y(a)]=1N∑i=1NI(Ai=a)YiPr(Ai=a∣Xi)\hat{E}\[Y^{(a)}] = \frac{1}{N} \sum\_{i=1}^N \frac{\mathbb{I}(A\_i=a)Y\_i}{Pr(A\_i=a \mid X\_i)}

***

#### **10. Predictive Modeling vs. Causal Modeling**

* **Predictive:** Estimates Pr(Y∣X)Pr(Y \mid X). Focus: _What will happen?_
* **Causal:** Estimates Pr(Y∣do(X))Pr(Y \mid do(X)). Focus: _What if we intervene?_

***

#### **11. Examples of Causal Questions**

* Does drinking wine prevent heart disease?
* How effective is a vaccine in preventing illness?
* Was it the marketing campaign or tax break that increased sales?

***

#### **12. Where Does Causality Fit in Machine Learning?**

* **Causal Inference:** Like unsupervised regression. Estimating causal effects from unknown parameters.
* **Causal Structure Learning:** Similar to unsupervised classification—inferring causal graphs without labeled data.

***

#### **13. Challenges in Causal Analysis**

* **Association ≠ Causation:** Pr(Y∣X)≠Pr(Y∣do(X))Pr(Y \mid X) \neq Pr(Y \mid do(X))
* **Confounding:** Unobserved variables influencing both XX and YY.
* **Directionality Uncertainty:** Is X→YX \to Y or Y→XY \to X?

***

#### **14. What is the Causal Hierarchy?** _(Pearl’s Ladder of Causation)_

| Level           | Type      | Example                                              |
| --------------- | --------- | ---------------------------------------------------- |
| Association     | Seeing    | Pr(Y∣X)Pr(Y \mid X) - Prediction                     |
| Intervention    | Doing     | Pr(Y∣do(X))Pr(Y \mid do(X)) - Policy changes         |
| Counterfactuals | Imagining | Pr(Yx′)∣X=x,Y=y)Pr(Y\_{x'}) \mid X=x, Y=y) - What-if |

***

#### **15. What is an Intervention?**

An **intervention** sets a variable to a value externally:

Pr(Y∣do(A=a))≠Pr(Y∣A=a)Pr(Y \mid do(A=a)) \neq Pr(Y \mid A=a)

For example, administering a new drug to observe health outcomes.

***

#### **16. Structural Causal Model (SCM) vs. Structural Equation Model (SEM)**

* **SCM:** Incorporates causal graphs and interventions.
* **SEM:** Focuses on linear equations without direct intervention modeling.

***

#### **17. Evidence-Based Pyramid**

| Level                        | Evidence Quality |
| ---------------------------- | ---------------- |
| Systematic Reviews           | Highest          |
| Randomized Controlled Trials | High             |
| Observational Studies        | Moderate         |
| Expert Opinions              | Lowest           |

RCTs remain the standard but have limitations in feasibility.

***

### **FAQ**

#### **Why Do We Need Causality?**

Causality helps us:

* Avoid spurious correlations.
* Understand the data generating process.
* Make better decisions beyond prediction.

***

#### **Can Machines Achieve Human-Level Intelligence Without Causality?**

No. Humans naturally reason about cause and effect. For AI to emulate this:

Pr(Y∣do(X))andPr(Yx′∣X=x,Y=y)Pr(Y \mid do(X)) \quad \text{and} \quad Pr(Y\_{x'} \mid X=x, Y=y)

must be incorporated into learning systems.

***

#### **How Does Causal Inference Improve Decision-Making?**

Without causality, decisions rely on associations that may be misleading. For example:

* **Predictive:** Who buys after an ad?
* **Causal:** Will increasing ad spend cause more purchases?

***

#### **What Is Counterfactual Analysis?**

Counterfactuals answer "What if...?" questions:

Pr(Ya′∣A=a,Y=y)Pr(Y\_{a'} \mid A=a, Y=y)

Example: Would a patient recover if they hadn’t received the treatment?

***

#### **How Do We Deal with Confounders?**

Methods include:

* **Backdoor Adjustment:**

Pr(Y∣do(A))=∑zPr(Y∣A,Z=z)Pr(Z=z)Pr(Y \mid do(A)) = \sum\_z Pr(Y \mid A,Z=z)Pr(Z=z)

* **IPW and Standardization:** Reweight data to simulate randomization.

***

#### **What is Simpson’s Paradox?**

An observed trend in aggregated data reverses when data is disaggregated by a confounder:

Pr(Y∣X)≠Pr(Y∣X,Z)Pr(Y \mid X) \neq Pr(Y \mid X,Z)

***

### **Conclusion**

Causality provides the foundation for understanding interventions, decision-making, and the mechanisms underlying data. Mastering causal inference ensures that our conclusions are actionable, fair, and grounded in reality rather than mere correlations.
