---
description: Potential Outcomes Framework
---

# Potential Outcomes Framework

## **Potential Outcomes Framework: Expanded Theory and Mathematical Detail**

### **1. Introduction**

The **Potential Outcomes Framework (POF)**, also known as the **Rubin Causal Model (RCM)**, provides a mathematical and conceptual structure for defining and estimating **causal effects**. It formalizes the idea that each individual or unit has **potential outcomes** corresponding to different treatment conditions.

* **Treatment variable (T)**: T∈{0,1}T \in \\{0,1\\}, where:
  * T=1T = 1: Unit receives treatment.
  * T=0T = 0: Unit does not receive treatment (control/placebo).
* **Outcome variable (Y)**: The result of interest under each treatment condition.

***

### **2. Potential Outcomes**

#### **Definition:**

For each individual ii:

* Yi(1)Y\_i(1): Potential outcome if individual ii receives the treatment (T=1T=1).
* Yi(0)Y\_i(0): Potential outcome if individual ii does not receive the treatment (T=0T=0).

> **Key Point:**\
> We **cannot observe both outcomes simultaneously** for the same individual. This is known as the **Fundamental Problem of Causal Inference**.

***

#### **Example:**

Investigating the effect of pursuing a Master’s degree on obtaining a high-paying job:

* **Treatment:** Doing a Master’s (T=1T=1)
* **Control:** Not doing a Master’s (T=0T=0)

For an individual ii:

* Yi(1)Y\_i(1): Income if the person completes a Master’s.
* Yi(0)Y\_i(0): Income if the person does not complete a Master’s.

***

### **3. Causal Effects**

#### **3.1. Individual Causal Effect (ICE)**

The **Individual Causal Effect** for an individual ii is defined as:

ICEi=Yi(1)−Yi(0)\text{ICE}\_i = Y\_i(1) - Y\_i(0)

**Problem:**

Only one of these outcomes is observable; the other is a **counterfactual**.

***

#### **3.2. Average Treatment Effect (ATE)**

The **Average Treatment Effect** is the **population-level average** of the individual causal effects:

ATE=E\[Y(1)−Y(0)]=E\[Y(1)]−E\[Y(0)]\text{ATE} = \mathbb{E}\[Y(1) - Y(0)] = \mathbb{E}\[Y(1)] - \mathbb{E}\[Y(0)]

**Interpretation:**

The ATE measures the expected difference in outcomes if **everyone** in the population received treatment versus if **no one** did.

> **Note:**\
> Even if the **individual causal effects** are non-zero, the **ATE can be zero** if positive and negative effects cancel out.

***

#### **3.3. Average Treatment Effect on the Treated (ATT)**

The **ATT** focuses on the **subgroup that received treatment**:

ATT=E\[Y(1)−Y(0)∣T=1]\text{ATT} = \mathbb{E}\[Y(1) - Y(0) \mid T=1]

**Interpretation:**

“How did the treatment benefit those who actually received it?”

***

#### **3.4. Average Treatment Effect on the Control (ATC)**

The **ATC** focuses on those who **did not receive treatment**:

ATC=E\[Y(1)−Y(0)∣T=0]\text{ATC} = \mathbb{E}\[Y(1) - Y(0) \mid T=0]

***

### **4. Mathematical Derivations**

#### **4.1. Observed and Unobserved Components**

Let’s define the **observed outcome**:

Yi=TiYi(1)+(1−Ti)Yi(0)Y\_i = T\_i Y\_i(1) + (1 - T\_i) Y\_i(0)

Where:

* If Ti=1T\_i = 1, Yi=Yi(1)Y\_i = Y\_i(1).
* If Ti=0T\_i = 0, Yi=Yi(0)Y\_i = Y\_i(0).

> **Challenge:**\
> To estimate the ATE, we need both E\[Y(1)]\mathbb{E}\[Y(1)] and E\[Y(0)]\mathbb{E}\[Y(0)], but each individual contributes only to one of these expectations.

***

#### **4.2. Estimating ATE with Conditional Independence Assumption (CIA)**

**CIA Assumption:**\
If (Y(0),Y(1))⊥ ⁣ ⁣ ⁣⊥T∣X(Y(0), Y(1)) \perp\\!\\!\\!\perp T \mid X, where XX is a set of covariates, then:

ATE=EX\[E\[Y∣T=1,X]−E\[Y∣T=0,X]]\text{ATE} = \mathbb{E}\_{X} \left\[ \mathbb{E}\[Y \mid T=1, X] - \mathbb{E}\[Y \mid T=0, X] \right]

***

#### **4.3. Propensity Score Weighting**

**Propensity score:** e(X)=P(T=1∣X)e(X) = P(T=1 \mid X).

Using inverse probability weighting:

ATE=E\[TYe(X)−(1−T)Y1−e(X)]\text{ATE} = \mathbb{E}\left\[ \frac{T Y}{e(X)} - \frac{(1 - T) Y}{1 - e(X)} \right]

***

### **5. Decomposition of Causal Effects**

#### **5.1. Direct and Indirect Effects**

For a mediator MM:

* **Total Effect (TE):** E\[Y(1)−Y(0)]\mathbb{E}\[Y(1) - Y(0)]
* **Natural Direct Effect (NDE):** Effect of treatment holding MM constant.
* **Natural Indirect Effect (NIE):** Effect of treatment via MM.

TE=NDE+NIE\text{TE} = \text{NDE} + \text{NIE}

***

### **6. Visual Representation**

A **causal DAG** can represent the potential outcomes framework:

T→YZ→T,Z→YT \rightarrow Y \quad \quad Z \rightarrow T, Z \rightarrow Y

Where:

* ZZ: Confounder.
* Adjusting for ZZ allows for unbiased estimation of causal effects.

***

### **7. Example Calculation**

Suppose in a study:

* E\[Y∣T=1]=0.8\mathbb{E}\[Y \mid T=1] = 0.8
* E\[Y∣T=0]=0.6\mathbb{E}\[Y \mid T=0] = 0.6

#### **Calculate ATE:**

ATE=0.8−0.6=0.2\text{ATE} = 0.8 - 0.6 = 0.2

This suggests that treatment increases the outcome probability by 20 percentage points.

***

### **8. Challenges in the Potential Outcomes Framework**

* **Fundamental Problem of Causal Inference:** We never observe both potential outcomes simultaneously.
* **Selection Bias:** Non-random assignment of treatment leads to confounding.
* **Violation of Positivity:** Lack of overlap in treatment and control groups for certain covariates.

***

### **9. Solutions to Address Challenges**

1. **Randomized Controlled Trials (RCTs):** Eliminate confounding by design.
2. **Matching Methods:** Pair treated and control units with similar covariates.
3. **Propensity Score Methods:** Balance covariates across groups.
4. **Instrumental Variables:** Address unobserved confounding.

***

### **10. Conclusion**

The **Potential Outcomes Framework** is foundational for understanding **causal effects** in data analysis. By conceptualizing **counterfactual outcomes** and formalizing causal quantities like **ATE**, **ATT**, and **ICE**, it provides a rigorous structure for causal inference.

#### ✅ **Key Takeaways:**

* Each individual has two potential outcomes but only one is observable.
* Causal effects quantify the difference between these potential outcomes.
* Proper adjustments for confounding are critical for valid causal conclusions.
