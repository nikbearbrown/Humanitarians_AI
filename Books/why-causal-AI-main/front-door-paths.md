---
description: Front Door Paths
---

# Front Door Paths

## **Front-Door Paths in Causal Inference: Theory, Mathematics, and Applications**

***

### **1. Introduction to Front-Door Paths**

In causal inference, **front-door paths** represent **causal pathways** from a treatment (or exposure) variable XX to an outcome variable YY. These paths **start with an arrow moving away from the treatment** and **capture the direct or indirect causal effect** of the treatment on the outcome.

#### **Why the term "Front-Door"?**

* **Front-door paths:** Show how the **treatment causes the outcome**.
* **Backdoor paths:** Represent **non-causal associations** that need to be blocked.

Unlike backdoor paths (which introduce confounding bias), **front-door paths should not be blocked** when estimating the causal effect since they represent the **causal effect we want to measure**.

***

### **2. Front-Door Criterion: Formal Definition**

The **front-door criterion** provides conditions under which the **causal effect of XX on YY** can be identified **through a mediator MM**, even in the presence of unmeasured confounders.

#### **Front-Door Criterion Conditions:**

A set of variables M\mathbf{M} satisfies the front-door criterion relative to an ordered pair (X,Y)(X, Y) if:

1. **All directed paths from XX to YY pass through MM** (i.e., MM mediates the effect of XX on YY).
2. **No backdoor path exists from XX to MM** (or it can be blocked by conditioning on observed variables).
3. **All backdoor paths from MM to YY are blocked by conditioning on XX**.

***

### **3. Mathematical Derivation of the Front-Door Adjustment Formula**

If the front-door criterion is satisfied, the **causal effect** of XX on YY can be identified using the **front-door adjustment formula**:

P(Y∣do(X))=∑mP(M=m∣X)∑x′P(Y∣M=m,X=x′)P(X=x′)P(Y \mid \text{do}(X)) = \sum\_m P(M = m \mid X) \sum\_{x'} P(Y \mid M = m, X = x') P(X = x')

#### **Explanation of the formula:**

1. **P(M=m∣X)P(M = m \mid X):** Probability of the mediator MM given treatment XX.
2. **P(Y∣M=m,X=x′)P(Y \mid M = m, X = x'):** Probability of the outcome YY given mediator MM and treatment X=x′X = x'.
3. **P(X=x′)P(X = x'):** Marginal distribution of XX.

This formula **decouples** the estimation into two components:

* **Step 1:** Effect of XX on the mediator MM.
* **Step 2:** Effect of the mediator MM on the outcome YY.

***

### **4. Understanding Through Graphical Models (DAGs)**

#### **Example DAG with Front-Door Path:**

X→M→YX \rightarrow M \rightarrow Y

* XX: Treatment
* MM: Mediator
* YY: Outcome

The path X→M→YX \rightarrow M \rightarrow Y is a **front-door path**.

***

### **5. Why Use Front-Door Adjustment?**

#### **Benefits:**

✅ Identifies causal effects **even with unobserved confounders** between XX and YY.\
✅ Useful when **backdoor adjustment is impossible** (e.g., unobserved confounders).

#### **Limitations:**

❌ Requires that all backdoor paths from MM to YY are blocked by conditioning on XX.\
❌ Requires that MM fully mediates the effect of XX on YY.

***

### **6. Practical Example of Front-Door Adjustment**

#### **Scenario:**

You want to estimate the causal effect of a **job training program (XX)** on **increased income (YY)**.

* XX: Job training participation
* MM: Skill acquisition (mediator)
* YY: Income level

#### **DAG Representation:**

X→M→YX \rightarrow M \rightarrow Y

✅ No direct backdoor path between XX and YY is needed since MM fully mediates the causal effect.

***

### **7. Step-by-Step Computation**

#### **Step 1: Effect of XX on MM**

P(M∣do(X))=P(M∣X)P(M \mid \text{do}(X)) = P(M \mid X)

* Learn how participating in training affects skill acquisition.

***

#### **Step 2: Effect of MM on YY**

P(Y∣do(M))=∑x′P(Y∣M,X=x′)P(X=x′)P(Y \mid \text{do}(M)) = \sum\_{x'} P(Y \mid M, X=x') P(X=x')

* Evaluate how skill acquisition affects income.

***

#### **Step 3: Combine Using Front-Door Adjustment**

P(Y∣do(X))=∑mP(M∣X)∑x′P(Y∣M,X=x′)P(X=x′)P(Y \mid \text{do}(X)) = \sum\_m P(M \mid X) \sum\_{x'} P(Y \mid M, X=x') P(X=x')

* Obtain the **total causal effect** of XX on YY via the mediator MM.

***

### **8. Example with Hypothetical Data**

| XX (Training) | MM (Skills) | YY (Income) |
| ------------- | ----------- | ----------- |
| 1 (Yes)       | High        | High        |
| 1 (Yes)       | Low         | Medium      |
| 0 (No)        | Low         | Low         |

#### **Computation:**

1. **Step 1: Estimate P(M∣X=1)P(M \mid X=1)**

P(M=High∣X=1)=0.7,P(M=Low∣X=1)=0.3P(M=\text{High} \mid X=1) = 0.7, \quad P(M=\text{Low} \mid X=1) = 0.3

2. **Step 2: Estimate P(Y∣M)P(Y \mid M)**

P(Y=High∣M=High)=0.8,P(Y=Medium∣M=Low)=0.6P(Y=\text{High} \mid M=\text{High}) = 0.8, \quad P(Y=\text{Medium} \mid M=\text{Low}) = 0.6

3. **Step 3: Apply Front-Door Formula**

P(Y∣do(X=1))=∑mP(M=m∣X=1)P(Y∣M=m)P(Y \mid \text{do}(X=1)) = \sum\_m P(M=m \mid X=1) P(Y \mid M=m)

Substitute values:

\=(0.7×0.8)+(0.3×0.6)=0.56+0.18=0.74= (0.7 \times 0.8) + (0.3 \times 0.6) = 0.56 + 0.18 = 0.74

✅ Estimated probability of high income after training: **74%**.

***

### **9. Front-Door vs. Backdoor Adjustment**

| **Aspect**                          | **Front-Door Adjustment**                  | **Backdoor Adjustment**                         |
| ----------------------------------- | ------------------------------------------ | ----------------------------------------------- |
| **Requirement**                     | Requires a **mediator** between XX and YY. | Requires **observed confounders** of XX and YY. |
| **Handles Unobserved Confounders?** | ✅ Yes (if front-door criterion holds)      | ❌ No (if confounders are unobserved)            |
| **Method**                          | Adjust through the mediator MM.            | Adjust directly through confounders.            |
| **Use Case**                        | When backdoor adjustment is infeasible.    | When confounders are fully observed.            |

***

### **10. Common Mistakes and Pitfalls**

❌ **Blocking the front-door path** by conditioning on the mediator MM when estimating total effect.\
✅ Use the **front-door formula** instead of direct conditioning.

❌ **Violating the front-door criterion conditions:**

* Unblocked backdoor paths from MM to YY invalidate the adjustment.\
  ✅ Verify DAG structure before proceeding.

***

### **11. Real-World Applications**

* **Healthcare:**
  * XX: Medication; MM: Biomarker response; YY: Health outcome.
  * Use front-door adjustment when patient behavior confounds direct estimation.
* **Marketing:**
  * XX: Ad exposure; MM: Website visits; YY: Purchases.
  * Measure indirect effect of ads through website engagement.
* **Economics:**
  * XX: Tax incentives; MM: Investment; YY: Job creation.

***

### **12. R Code Example**

```r
library(dagitty)

# Define the DAG
dag <- dagitty("dag {
  X [exposure]
  M [mediator]
  Y [outcome]
  X -> M -> Y
}")

# Check if front-door criterion holds
adjustmentSets(dag, exposure = "X", outcome = "Y", type = "frontdoor")
```

✅ Output will suggest adjusting through the mediator MM.

***

### **13. Conclusion**

✅ **Front-door adjustment** allows identification of causal effects **even with unobserved confounders**.\
✅ Requires that a **mediator fully transmits the causal effect** of XX on YY.\
✅ Use the **front-door formula** to decompose the effect into measurable components.

***

### **14. Key Takeaways**

🔑 **Front-door criterion:** A powerful tool when backdoor adjustment is infeasible.\
🔑 Focuses on **mediators** that capture causal effects.\
🔑 **Do not condition directly on mediators** when estimating the **total causal effect**.\
🔑 Widely used in fields like **healthcare, economics, and policy evaluation**.

***

### **Further Resources**

* **Judea Pearl’s "The Book of Why"** – Comprehensive guide to causality and front-door criterion.
* **Elwert’s DAG Primer:** [Download PDF](https://www.ssc.wisc.edu/~felwert/causality/wp-content/uploads/2013/06/2-elwert_dags.pdf)
* **Nick Huntington-Klein’s Videos on Causality:** [YouTube Channel](https://www.youtube.com/channel/UCD9MdeZS5UebIov2U2Bu1GA)

By understanding and applying the **front-door criterion**, researchers can make **valid causal claims** even in complex settings with **unobserved confounding**.
