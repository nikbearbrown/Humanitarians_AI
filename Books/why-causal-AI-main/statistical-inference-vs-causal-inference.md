---
description: Statistical Inference Vs Causal Inference
---

# Statistical Inference Vs Causal Inference

## **Causation and Causal Effects: A Mathematical Exploration**

Understanding the difference between correlation and causation is central to scientific inquiry, decision-making, and policy evaluation. Statistical methods like machine learning models excel at identifying associations, but **causal inference** helps us answer _why_ these associations exist and what would happen under interventions.

***

### **1. Causation vs. Association: Mathematical Foundations**

#### **1.1. Defining Causation Through Probability Differences**

Causation is often assessed by examining the **difference in conditional probabilities**:

Pr(Y=1∣A=1)≠Pr(Y=1∣A=0)Pr(Y=1 \mid A=1) \neq Pr(Y=1 \mid A=0)

* YY: Outcome variable (e.g., purchasing a product, recovering from illness)
* AA: Treatment or intervention (e.g., receiving an ad or vaccine)

If the probability of the outcome changes when AA is introduced, there is an association—possibly causal.

***

### **1.2. Causal Effect: The Difference in Expected Outcomes**

The **causal effect** measures how much an intervention changes the expected outcome:

Causal Effect=E\[Y(a=1)]−E\[Y(a=0)]\text{Causal Effect} = E\[Y^{(a=1)}] - E\[Y^{(a=0)}]

* E\[Y(a=1)]E\[Y^{(a=1)}]: Expected outcome if everyone receives the treatment.
* E\[Y(a=0)]E\[Y^{(a=0)}]: Expected outcome if no one receives the treatment.

If this difference is nonzero, the treatment affects the outcome.

#### **Sharp Causal Null Hypothesis**

Y(a=1)=Y(a=0)∀ individualsY^{(a=1)} = Y^{(a=0)} \quad \forall \text{ individuals}

This hypothesis asserts no individual is affected by the treatment.

***

### **2. Association vs. Causation: Detailed Mathematical Metrics**

Two variables are **associated** if knowing one provides information about the other. However, association does not imply causation. Let’s explore the key measures:

#### **2.1. Difference in Probabilities**

Association exists if:

Pr(Y=1∣A=1)−Pr(Y=1∣A=0)≠0Pr(Y=1 \mid A=1) - Pr(Y=1 \mid A=0) \neq 0

✅ **No association** if the difference is 0.\
✅ **Association exists** if the difference is nonzero.

**Example (COVID-19 Vaccine):**

* Pr(Y=1∣A=1)=0.1Pr(Y=1 \mid A=1) = 0.1 (probability of getting sick with vaccine)
* Pr(Y=1∣A=0)=0.3Pr(Y=1 \mid A=0) = 0.3 (probability of getting sick without vaccine)

0.1−0.3=−0.2≠0(Association exists)0.1 - 0.3 = -0.2 \quad \neq 0 \quad (\text{Association exists})

The vaccine reduces sickness risk.

***

#### **2.2. Risk Ratio (Relative Risk)**

Risk Ratio (RR)=Pr(Y=1∣A=1)Pr(Y=1∣A=0)\text{Risk Ratio (RR)} = \frac{Pr(Y=1 \mid A=1)}{Pr(Y=1 \mid A=0)}

✅ **No association** if RR=1RR = 1.\
✅ **Association** if RR≠1RR \neq 1.

**Example (Marketing Campaign):**

* With ad: Pr(Y=1∣A=1)=0.4Pr(Y=1 \mid A=1) = 0.4
* Without ad: Pr(Y=1∣A=0)=0.2Pr(Y=1 \mid A=0) = 0.2

RR=0.40.2=2(Association exists)RR = \frac{0.4}{0.2} = 2 \quad (\text{Association exists})

Seeing the ad doubles the chance of purchasing.

***

#### **2.3. Odds and Odds Ratio**

Odds of an event:

Odds(Y=1∣A=a)=Pr(Y=1∣A=a)Pr(Y=0∣A=a)\text{Odds}(Y=1 \mid A=a) = \frac{Pr(Y=1 \mid A=a)}{Pr(Y=0 \mid A=a)}

The **Odds Ratio (OR)** compares odds under treatment vs. control:

OR=Odds(Y=1∣A=1)Odds(Y=1∣A=0)OR = \frac{\text{Odds}(Y=1 \mid A=1)}{\text{Odds}(Y=1 \mid A=0)}

✅ **No association** if OR=1OR = 1.\
✅ **Association** if OR≠1OR \neq 1.

**Example (Vaccine Effectiveness):**

* With vaccine: Pr(Y=1∣A=1)=0.1Pr(Y=1 \mid A=1)=0.1, Pr(Y=0∣A=1)=0.9Pr(Y=0 \mid A=1)=0.9

Odds(A=1)=0.10.9=0.11\text{Odds}(A=1) = \frac{0.1}{0.9}=0.11

* Without vaccine: Pr(Y=1∣A=0)=0.3Pr(Y=1 \mid A=0)=0.3, Pr(Y=0∣A=0)=0.7Pr(Y=0 \mid A=0)=0.7

Odds(A=0)=0.30.7=0.43\text{Odds}(A=0) = \frac{0.3}{0.7}=0.43 OR=0.110.43=0.26(Association exists)OR = \frac{0.11}{0.43}=0.26 \quad (\text{Association exists})

The vaccine reduces odds of illness.

***

### **3. Counterfactual Causality: The "What If" Analysis**

#### **3.1. Counterfactual Notation**

The potential outcomes framework uses counterfactuals:

Pr(Y(a=1)=1)≠Pr(Y(a=0)=1)Pr(Y^{(a=1)} = 1) \neq Pr(Y^{(a=0)} = 1)

* Y(a=1)Y^{(a=1)}: Outcome if treated.
* Y(a=0)Y^{(a=0)}: Outcome if not treated.

A causal effect exists if these probabilities differ.

***

#### **3.2. Average Treatment Effect (ATE)**

ATE=E\[Y(a=1)−Y(a=0)]\text{ATE} = E\[Y^{(a=1)} - Y^{(a=0)}]

If ATE≠0\text{ATE} \neq 0, treatment has a causal effect.

***

#### **3.3. Average Treatment Effect on the Treated (ATT)**

ATT=E\[Y(a=1)−Y(a=0)∣A=1]\text{ATT} = E\[Y^{(a=1)} - Y^{(a=0)} \mid A=1]

Focuses on those who received the treatment.

***

### **4. Observational Studies vs. Randomized Experiments**

#### **4.1. Randomized Controlled Trials (RCTs)**

* Treatment assignment is random.
* **Exchangeability** holds:

Pr(Y(a)=1∣A=1)=Pr(Y(a)=1∣A=0)Pr(Y^{(a)}=1 \mid A=1)=Pr(Y^{(a)}=1 \mid A=0)

Randomization ensures comparability.

***

#### **4.2. Observational Studies**

* Treatment not assigned randomly.
* Confounding variables may bias results.

**Inverse Probability Weighting (IPW)** adjusts for confounders:

E^\[Y(a)]=1N∑i=1NI(Ai=a)YiPr(Ai=a∣Xi)\hat{E}\[Y^{(a)}] = \frac{1}{N}\sum\_{i=1}^{N} \frac{\mathbb{I}(A\_i=a) Y\_i}{Pr(A\_i=a \mid X\_i)}

***

### **5. Identifiability Conditions in Causal Inference**

For valid causal conclusions, these must hold:

1. **Consistency:**

Y=Y(a)if A=aY = Y^{(a)} \quad \text{if } A=a

2. **Exchangeability:**

Pr(Y(a)=1∣A=1)=Pr(Y(a)=1∣A=0)Pr(Y^{(a)}=1 \mid A=1)=Pr(Y^{(a)}=1 \mid A=0)

3. **Positivity:**

0\<Pr(A=a∣X=x)<10 < Pr(A=a \mid X=x) < 1

***

### **6. Frontdoor and Backdoor Criteria**

#### **6.1. Backdoor Criterion (Controlling Confounders)**

To block backdoor paths:

Pr(Y∣do(A))=∑zPr(Y∣A,Z=z)Pr(Z=z)Pr(Y \mid do(A)) = \sum\_{z} Pr(Y \mid A, Z=z)Pr(Z=z)

***

#### **6.2. Frontdoor Criterion (Mediated Causality)**

Used when confounding can’t be controlled directly:

Pr(Y∣do(A))=∑mPr(M=m∣A)∑yPr(Y=y∣M=m)Pr(Y \mid do(A)) = \sum\_{m} Pr(M=m \mid A) \sum\_{y} Pr(Y=y \mid M=m)

***

### **7. Granger Causality and Time-Series Analysis**

**Granger causality** states XX Granger-causes YY if:

Var(Yt∣Yt−1,…,Xt−1)\<Var(Yt∣Yt−1,… )Var(Y\_t \mid Y\_{t-1}, \dots, X\_{t-1}) < Var(Y\_t \mid Y\_{t-1}, \dots)

Past values of XX improve YY's prediction.

***

### **8. Conclusion**

#### **Statistical inference** answers: _What is the association?_

#### **Causal inference** answers: _What causes the change?_

Both approaches are vital, but causality allows us to predict **what will happen if we intervene**, enabling better decisions in healthcare, policy, and business.

***

### **9. Key Takeaways**

✅ **Statistical Inference:** Finds correlations but not causality.\
✅ **Causal Inference:** Establishes cause-and-effect relationships.\
✅ **Mathematical Metrics:** Risk ratios, odds ratios, and counterfactuals quantify effects.\
✅ **Methods:** Use RCTs, IPW, DAGs, and Granger causality for robust conclusions.

***

### **10. Resources**

* **The Book of Why** – Judea Pearl
* **Causal Inference in Statistics** – Miguel Hernán & James Robins
* **AI: Beyond Curve Fitting to Genuine Intelligence** ([Diginomica](https://diginomica.com/ai-curve-fitting-not-intelligence))
* **Why Causality Matters in Data Science** ([Towards Data Science](https://towardsdatascience.com/why-do-we-need-causality-in-data-science-aec710da021e))

***

With causal inference, we **move beyond predicting outcomes** to **understanding the impact of decisions**—crucial for progress in science, technology, and human welfare.
