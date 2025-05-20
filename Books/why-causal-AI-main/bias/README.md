---
description: Bias
---

# Bias

**What is Bias?**

#### **Definition:**

Bias refers to a systematic deviation from the true value or relationship between variables, leading to incorrect conclusions. In social contexts, **unfairness** arises from the unjust treatment of individuals based on group attributes like age, gender, race, or socioeconomic status.

In **artificial intelligence (AI)** and **causal inference**, bias occurs when models fail to capture the true causal relationships, often resulting in unfair or discriminatory outcomes.

#### **Mathematical Definition of Bias:**

For an estimator θ^\hat{\theta} of a parameter θ\theta, **bias** is defined as:

Bias(θ^)=E\[θ^]−θ\text{Bias}(\hat{\theta}) = E\[\hat{\theta}] - \theta

* **Unbiased Estimator:** If Bias(θ^)=0\text{Bias}(\hat{\theta}) = 0
* **Biased Estimator:** If Bias(θ^)≠0\text{Bias}(\hat{\theta}) \neq 0

**Example:**\
If we are estimating the mean μ\mu of a population and the estimator consistently underestimates it, the estimator is biased.

***

### **Bias in Machine Learning and Causal Models**

#### **Independence-Based Bias Definition:**

A model is **biased** if the prediction (y)(y) depends on a protected attribute (p)(p):

P(y∣p)≠P(y)P(y \mid p) \neq P(y)

If the prediction changes with the protected attribute, the model’s outcome is unfair.

#### **Example: Loan Approval Bias**

Let yy represent loan approval and pp represent gender:

* If P(y=1∣p=male)≠P(y=1∣p=female)P(y=1 \mid p=\text{male}) \neq P(y=1 \mid p=\text{female}), the model is gender-biased.

***

### **Sources of Bias**

#### **1. Data Collection Bias**

Occurs when the sample data does not represent the target population.

*   **Selection Bias:**\
    Occurs when data is collected from a non-representative subset.

    **Mathematically:**

    Pr(Y∣X,S=1)≠Pr(Y∣X)Pr(Y \mid X, S=1) \neq Pr(Y \mid X)

    where S=1S=1 indicates sample inclusion.
* **Example:** Using survey data collected online might exclude older populations without internet access.

***

#### **2. Measurement Bias**

Errors in how variables are measured.

**Example:**\
Using incorrect sensors to measure blood pressure leads to biased health data.

Mathematically, if the observed variable X\~\tilde{X} differs systematically from the true variable XX:

X\~=X+ϵwith E\[ϵ]≠0\tilde{X} = X + \epsilon \quad \text{with } E\[\epsilon] \neq 0

***

#### **3. Cognitive Bias in Data Generation**

Human decisions can introduce bias into datasets.

**Example:** Police records used for predictive policing may reflect historical racial biases.

***

#### **4. Bias from Feedback Loops**

A feedback loop occurs when the model’s predictions influence future data collection.

* **Example:** A predictive policing model sending more officers to certain neighborhoods leads to more arrests there, reinforcing biased data.

**Mathematical Representation:**\
Let DtD\_t represent data at time tt:

Dt+1=f(Dt,y^t)D\_{t+1} = f(D\_t, \hat{y}\_t)

If y^t\hat{y}\_t is biased, future data Dt+1D\_{t+1} will carry that bias forward.

***

### **Types of Bias in Causal Inference**

#### **1. Confounding Bias**

Occurs when an unobserved variable affects both the treatment AA and the outcome YY.

**Backdoor Path Example:**\
In a DAG:

A←C→YA \leftarrow C \rightarrow Y

Here, CC is a confounder. Failure to control for CC biases the causal effect of AA on YY.

**Adjustment Formula:**\
To block the backdoor path:

Pr(Y∣do(A))=∑cPr(Y∣A,C=c)Pr(C=c)Pr(Y \mid do(A)) = \sum\_c Pr(Y \mid A, C=c) Pr(C=c)

***

#### **2. Collider Bias**

Occurs when conditioning on a common effect of two variables.

**DAG Example:**

A→B←YA \rightarrow B \leftarrow Y

Conditioning on BB creates a spurious association between AA and YY.

***

#### **3. Selection Bias**

Occurs when data selection depends on both the treatment and the outcome.

**Mathematical Representation:**

Pr(Y∣A,S=1)≠Pr(Y∣A)Pr(Y \mid A, S=1) \neq Pr(Y \mid A)

***

### **Fairness and Bias Mitigation**

#### **Fairness Definitions:**

*   **Demographic Parity:**

    Pr(y^=1∣p=a)=Pr(y^=1∣p=b)Pr(\hat{y}=1 \mid p=a) = Pr(\hat{y}=1 \mid p=b)

    All groups receive positive predictions at equal rates.
*   **Equalized Odds:**

    Pr(y^=1∣y=1,p=a)=Pr(y^=1∣y=1,p=b)Pr(\hat{y}=1 \mid y=1, p=a) = Pr(\hat{y}=1 \mid y=1, p=b)

    True positive rates are equal across groups.

***

### **Bias Mitigation Techniques**

#### **1. Pre-Processing Methods**

*   **Reweighing:** Adjust data weights to balance representation.

    Weight adjustment formula:

    w(x,y,p)=Pr(x,y)Pr(x,y∣p)w(x, y, p) = \frac{Pr(x, y)}{Pr(x, y \mid p)}
* **Disparate Impact Remover:** Modifies features to reduce bias.

***

#### **2. In-Processing Methods**

*   **Fairness Constraints in Models:**\
    Adding regularization terms to penalize bias:

    min⁡θL(θ)+λ⋅BiasPenalty\min\_{\theta} \mathcal{L}(\theta) + \lambda \cdot \text{BiasPenalty}
*   **Adversarial Debiasing:**\
    Train a predictor and an adversary:

    min⁡θmax⁡ϕLpredictor(θ)−λLadversary(ϕ)\min\_{\theta} \max\_{\phi} \mathcal{L}\_{\text{predictor\}}(\theta) - \lambda \mathcal{L}\_{\text{adversary\}}(\phi)

***

#### **3. Post-Processing Methods**

* **Threshold Adjustment:** Different thresholds for different groups to achieve fairness.
* **Equalized Odds Post-Processing:**\
  Adjusts predicted labels to match true positive and false positive rates.

***

### **Causal Approach to Bias Mitigation**

Causal graphs (DAGs) identify **causal** and **non-causal** paths. Removing bias involves blocking non-causal (backdoor) paths.

**Backdoor Criterion:**\
For valid adjustment set ZZ:

Pr(Y∣do(A))=∑zPr(Y∣A,Z=z)Pr(Z=z)Pr(Y \mid do(A)) = \sum\_z Pr(Y \mid A, Z=z) Pr(Z=z)

***

### **Challenges in Bias Mitigation**

* **Multiple Biases:** Over 180 biases exist, making universal solutions difficult.
* **Trade-Offs:** Mitigating bias can reduce predictive accuracy.
* **Ethical Dilemmas:** Balancing fairness and utility can be complex.

***

### **Bias Feedback Loops**

A **bias feedback loop** occurs when biased predictions reinforce biased data collection.

#### **Mathematical Model:**

Let:

* DtD\_t: Data at time tt
* y^t\hat{y}\_t: Model prediction at time tt
* AtA\_t: Action based on prediction

Feedback loop equation:

Dt+1=f(Dt,y^t,At)D\_{t+1} = f(D\_t, \hat{y}\_t, A\_t)

If y^t\hat{y}\_t is biased, subsequent data Dt+1D\_{t+1} will inherit that bias, creating a reinforcing cycle.

***

### **Understanding Human Bias through AI Bias**

AI mirrors human cognitive biases:

| **Human Bias**    | **AI Equivalent**                              |
| ----------------- | ---------------------------------------------- |
| Confirmation Bias | Data selection bias                            |
| Anchoring Bias    | Initial model training bias                    |
| Availability Bias | Over-representation of frequent events in data |

***

### **Conclusion**

Bias in causal inference and AI can severely distort outcomes, leading to unfair decisions. Causal methods, fairness-aware models, and sensitivity analyses are essential tools to identify and mitigate these biases. The goal is to ensure responsible AI systems that are **fair, trustworthy, and aligned with human values**.

Robust AI Models⏟Goal=Data Quality⏟Base+Fair Assumptions⏟Bridge+Causal Understanding⏟Solution\underbrace{\text{Robust AI Models\}}\_{\text{Goal\}} = \underbrace{\text{Data Quality\}}\_{\text{Base\}} + \underbrace{\text{Fair Assumptions\}}\_{\text{Bridge\}} + \underbrace{\text{Causal Understanding\}}\_{\text{Solution\}}
