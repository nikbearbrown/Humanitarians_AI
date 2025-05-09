---
description: Assumptions
---

# Assumptions

## **Assumptions in Causal Inference: The Role of Human Intervention and Mathematical Foundations**

***

**Why Do We Need Assumptions in Causal Inference?**

Causal inference requires assumptions to bridge the gap between **what we know** (observed data) and **what we want to know** (causal effects and counterfactuals). Unlike statistical inference, which focuses on associations, causal inference seeks to answer questions like:

* _What would have happened if a different action had been taken?_
* _Would an intervention have improved the outcome?_

Without assumptions, causal conclusions cannot be derived from data alone—especially from **observational data**, which lacks the randomization provided by experiments.

***

### **The Data Generating Process (DGP)**

Every dataset is the result of an unknown **Data Generating Process (DGP)**. Our goal is to infer causal relationships from this process. Formally, the DGP can be described using **Structural Causal Models (SCMs)**:

Y=f(A,X,UY)A=g(X,UA)Y = f(A, X, U\_Y) \quad \quad A = g(X, U\_A)

* YY: Outcome
* AA: Treatment or intervention variable
* XX: Observed covariates
* UY,UAU\_Y, U\_A: Unobserved factors (confounders)

Since UYU\_Y and UAU\_A are unobserved, assumptions are necessary to estimate causal effects.

***

### **Key Types of Assumptions in Causal Inference**

#### **1. Consistency Assumption**

If an individual receives treatment A=aA=a, the observed outcome YY equals the potential outcome under that treatment:

Y=Y(a)if A=aY = Y^{(a)} \quad \text{if } A=a

**Interpretation:**\
If a patient receives a drug, the observed outcome (e.g., blood pressure) should match the hypothetical outcome had we assigned the drug in a controlled experiment.

***

#### **2. Exchangeability (No Unmeasured Confounding)**

In the absence of confounding, potential outcomes are independent of treatment assignment:

Y(a)⊥A∣XY^{(a)} \perp A \mid X

**Implication:**\
Within strata of XX, treated and untreated groups are comparable.

> **Without exchangeability, causal inference is biased.**

***

#### **3. Positivity (Overlap Condition)**

For all covariates XX, there must be a non-zero probability of receiving each treatment level:

0\<Pr(A=a∣X)<10 < Pr(A=a \mid X) < 1

**Why is this important?**\
If certain groups never receive a treatment, it’s impossible to estimate the causal effect for those groups.

***

#### **4. Stable Unit Treatment Value Assumption (SUTVA)**

Two key parts:

1. **No Interference:** One individual’s treatment does not affect another’s outcome.
2. **Consistency in Treatment Versions:** The treatment is well-defined and consistent.

Mathematically:

Yi(a) is unaffected by Aj∀i≠jY\_i^{(a)} \text{ is unaffected by } A\_j \quad \forall i \neq j

***

### **Assumptions vs. Data: The Need for Human Judgment**

> **"If we had all the data we needed, we wouldn’t need assumptions."**

#### **Reality Check:**

* **Population:** All elements of interest (e.g., all men in the U.S.).
* **Sample:** A subset from the population.

If we aim to calculate the **average height of men in the U.S.**:

* **Ideal case:** Measure everyone (no assumptions needed).
* **Real case:** Use a sample and assume it’s representative (selection bias risk).

***

### **Mathematical Framework: Inference from Data + Assumptions**

INFERENCE (Prediction)⏟Goal=DATA⏟Evidence+ASSUMPTIONS⏟Bridge\underbrace{\text{INFERENCE (Prediction)\}}\_{\text{Goal\}} = \underbrace{\text{DATA\}}\_{\text{Evidence\}} + \underbrace{\text{ASSUMPTIONS\}}\_{\text{Bridge\}}

> **Assumptions connect what we know with what we wish to know.**

***

### **Examples of Everyday Assumptions**

| **Scenario**     | **Assumption**                                           |
| ---------------- | -------------------------------------------------------- |
| Calculator use   | Embedded math formulas are correct.                      |
| Driving a Tesla  | Trust in safety ratings and manufacturer claims.         |
| Online banking   | Systems are secure and function as intended.             |
| Weather forecast | Atmospheric models accurately represent weather systems. |

***

### **When Assumptions Differ: Divergent Conclusions**

Different people → Different assumptions → Different conclusions

**Example: COVID-19 Impact Analysis**

* **Researcher A:** Assumes comorbidities fully measured → Strong causal effect estimated.
* **Researcher B:** Believes unmeasured socioeconomic confounders exist → Effect size adjusted downward.

***

### **The Role of Domain Experts**

Domain knowledge helps refine assumptions:

| **Field**  | **Expertise Needed**                   |
| ---------- | -------------------------------------- |
| Healthcare | Pathophysiology, treatment guidelines  |
| Economics  | Market dynamics, policy knowledge      |
| Education  | Pedagogical methods, learning theories |

> **Better assumptions → More accurate causal diagrams (DAGs)**

***

### **Testing and Specifying Assumptions**

#### **1. Sensitivity Analysis**

How robust are conclusions to assumption violations?

**Mathematical Formulation:**\
If Γ\Gamma represents unmeasured confounding strength:

Pr(Y∣do(A))=Pr(Y∣A)−ΓPr(Y \mid do(A)) = Pr(Y \mid A) - \Gamma

#### **2. Placebo Tests**

Use variables where no causal effect is expected. If detected → Violation of assumptions.

#### **3. Negative Controls**

Incorporate variables that should not affect the outcome to test for bias.

***

### **Assumptions in Practice: Graphical Approach**

Causal assumptions are visualized via **Directed Acyclic Graphs (DAGs)**:

Example of backdoor adjustment:

Pr(Y∣do(A))=∑zPr(Y∣A,Z=z)Pr(Z=z)Pr(Y \mid do(A)) = \sum\_z Pr(Y \mid A, Z=z) Pr(Z=z)

Here, ZZ blocks the backdoor path between AA and YY.

***

### **Sensitivity to Positivity Violations**

Consider estimating:

E\[Y(a)]=∫E\[Y∣A=a,X=x]f(x)dxE\[Y^{(a)}] = \int E\[Y \mid A=a, X=x] f(x) dx

If f(x)f(x) places weight on regions where Pr(A=a∣X=x)Pr(A=a \mid X=x) is near 0 → **Positivity violation** occurs.

***

### **Formalizing Assumptions: Structural Causal Models (SCMs)**

SCMs consist of:

* **Causal Graph GG:** Structure of relationships
* **Structural Equations:** A=fA(UA),Y=fY(A,X,UY)A = f\_A(U\_A), \quad Y = f\_Y(A, X, U\_Y)
* **Exogenous Variables UU:** Capture external factors

**Goal:**\
Estimate Pr(Y∣do(A=a))Pr(Y \mid do(A=a)) from observed Pr(Y,A,X)Pr(Y, A, X) and assumptions.

***

### **Conclusion: Assumptions are Inevitable, Essential, and Actionable**

* **Data alone is insufficient** for causal conclusions.
* **Assumptions formalize our beliefs** about how data is generated.
* **Domain expertise enhances the quality** of assumptions.
* **Testing assumptions** via sensitivity analyses strengthens inference validity.

Ultimately:

Decision Making⏟Goal=Data+Assumptions+Domain Knowledge\underbrace{\text{Decision Making\}}\_{\text{Goal\}} = \text{Data} + \text{Assumptions} + \text{Domain Knowledge}

> **The clearer our assumptions, the more actionable our decisions become.**
