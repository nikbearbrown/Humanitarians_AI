---
description: Mediators
---

# Mediators

## **Mediators in Causal Inference: Theory, Mathematics, and Applications**

### **What is a Mediator?**

A **mediator** is a variable that **lies on the causal pathway** between the treatment/exposure (XX) and the outcome (YY). Mediators help **explain how or why** a treatment affects an outcome.

* **Causal Pathway:** X→M→YX \rightarrow M \rightarrow Y
* Here, MM is the **mediator**, which transmits the effect of XX on YY.

***

### **Why Are Mediators Important?**

* **Understanding Mechanisms:** They reveal the process through which a cause leads to an effect.
* **Intervention Planning:** Helps identify **intervention points** that can change the outcome.
* **Distinguishing Direct vs. Indirect Effects:**
  * **Direct effect:** Effect of XX on YY not through MM.
  * **Indirect effect:** Effect of XX on YY through MM.

***

### **Mathematical Formulation of Mediation**

#### **Total Effect (TE)**

The total effect of XX on YY is the combination of:

1. **Direct effect:** X→YX \rightarrow Y (not via MM)
2. **Indirect effect:** X→M→YX \rightarrow M \rightarrow Y

Total Effect (TE)⏟Total influence of X on Y=Direct Effect (DE)⏟X → Y+Indirect Effect (IE)⏟X → M → Y\underbrace{\text{Total Effect (TE)\}}\_{\text{Total influence of } X \text{ on } Y} = \underbrace{\text{Direct Effect (DE)\}}\_{\text{X → Y\}} + \underbrace{\text{Indirect Effect (IE)\}}\_{\text{X → M → Y\}}

***

#### **Potential Outcomes Framework**

Let:

* Y(x)Y^{(x)}: Potential outcome if XX is set to xx.
* M(x)M^{(x)}: Potential mediator if XX is set to xx.
* Y(x,m)Y^{(x,m)}: Potential outcome if XX is set to xx and MM is set to mm.

**Natural Direct Effect (NDE)**

Effect of changing XX while holding the mediator fixed at the level it would have taken without treatment:

NDE=E\[Y(1,M(0))]−E\[Y(0,M(0))]\text{NDE} = E\[Y^{(1, M^{(0)})}] - E\[Y^{(0, M^{(0)})}]

**Natural Indirect Effect (NIE)**

Effect of changing the mediator from M(0)M^{(0)} to M(1)M^{(1)} while holding XX constant:

NIE=E\[Y(0,M(1))]−E\[Y(0,M(0))]\text{NIE} = E\[Y^{(0, M^{(1)})}] - E\[Y^{(0, M^{(0)})}]

**Total Effect Decomposition**

E\[Y(1)]−E\[Y(0)]⏟Total Effect (TE)=NDE⏟Direct+NIE⏟Indirect\underbrace{E\[Y^{(1)}] - E\[Y^{(0)}]}\_{\text{Total Effect (TE)\}} = \underbrace{\text{NDE\}}\_{\text{Direct\}} + \underbrace{\text{NIE\}}\_{\text{Indirect\}}

***

### **Regression Approach to Mediation**

#### **Step 1: Regress Mediator on Treatment**

M=α0+α1X+ϵMM = \alpha\_0 + \alpha\_1 X + \epsilon\_M

* α1\alpha\_1: Effect of XX on MM.

***

#### **Step 2: Regress Outcome on Treatment and Mediator**

Y=β0+β1X+β2M+ϵYY = \beta\_0 + \beta\_1 X + \beta\_2 M + \epsilon\_Y

* β1\beta\_1: Direct effect of XX on YY.
* β2\beta\_2: Effect of MM on YY controlling for XX.

***

#### **Indirect and Direct Effects:**

* **Indirect Effect:** α1×β2\alpha\_1 \times \beta\_2
* **Direct Effect:** β1\beta\_1
* **Total Effect:** β1+α1β2\beta\_1 + \alpha\_1 \beta\_2

***

### **Example: Medication, Blood Pressure, and Weight Loss**

* XX: Taking medication
* MM: Weight loss (mediator)
* YY: Blood pressure reduction

#### **Scenario:**

Medication reduces blood pressure partly by causing weight loss.

#### **DAG Representation:**

X→M→Ywith possible X→Y direct pathX \rightarrow M \rightarrow Y \quad \text{with possible } X \rightarrow Y \text{ direct path}

#### **Analysis:**

* **Indirect effect (via weight loss):** α1β2\alpha\_1 \beta\_2
* **Direct effect (not through weight loss):** β1\beta\_1

***

### **Front-Door Criterion and Mediation**

#### **Front-Door Adjustment Formula**

If MM satisfies the **front-door criterion**:

P(Y∣do(X))=∑mP(M=m∣X)∑yP(Y=y∣M=m)P(M=m)P(Y \mid \text{do}(X)) = \sum\_m P(M=m \mid X) \sum\_y P(Y=y \mid M=m)P(M=m)

Conditions for front-door adjustment:

1. All causal paths from XX to YY go through MM.
2. No unblocked backdoor paths from XX to MM.
3. All backdoor paths from MM to YY are blocked by XX.

***

### **Graphical Interpretation of Mediation**

#### **Causal DAG with Mediator**

X→M→YX \rightarrow M \rightarrow Y

* **Indirect path:** X→M→YX \rightarrow M \rightarrow Y
* **Direct path (if exists):** X→YX \rightarrow Y

***

### **Why Avoid Conditioning on Mediators for Causal Estimation?**

#### **Collider Bias Introduction**

Conditioning on a mediator can **open a collider path** if there are unobserved confounders between the mediator and the outcome:

X→M←U→YX \rightarrow M \leftarrow U \rightarrow Y

Conditioning on MM opens the path X↔U→YX \leftrightarrow U \rightarrow Y, introducing **bias**.

***

### **Common Applications of Mediation Analysis**

| **Field**    | **Application Example**                                                |
| ------------ | ---------------------------------------------------------------------- |
| Epidemiology | Understanding how smoking affects lung cancer through tar accumulation |
| Psychology   | Examining how therapy affects anxiety through self-efficacy            |
| Economics    | How job training improves wages via skill acquisition                  |
| Marketing    | How advertising increases sales through brand awareness                |

***

### **Challenges in Mediation Analysis**

* **Confounding of the Mediator-Outcome Path:**
  * Requires control for variables affecting both MM and YY.
* **Measurement Error in Mediators:**
  * Can bias estimates of indirect effects.
* **Unmeasured Mediators:**
  * Ignoring important mediators may underestimate indirect effects.
* **Overadjustment:**
  * Controlling for mediators while estimating total effects reduces accuracy.

***

### **Identifying Mediators in DAGs**

#### **Rules:**

1. A mediator **lies on a directed path** from XX to YY.
2. Removing the mediator from the path **breaks the causal chain**.
3. Mediators **transmit** rather than **confound** effects.

***

### **Difference Between Confounders, Mediators, and Colliders**

| **Feature**        | **Confounder**                    | **Mediator**                          | **Collider**                      |
| ------------------ | --------------------------------- | ------------------------------------- | --------------------------------- |
| Causal Role        | Common cause of both XX and YY    | Transmits effect from XX to YY        | Common effect of two variables    |
| Adjustment Effect  | Removes bias                      | Estimates direct and indirect effects | Opens bias path if conditioned on |
| DAG Representation | X←Z→YX \leftarrow Z \rightarrow Y | X→M→YX \rightarrow M \rightarrow Y    | X→C←YX \rightarrow C \leftarrow Y |

***

### **Example Problem**

#### **Scenario:**

Researchers want to understand how education (XX) affects income (YY) through job skills (MM).

1. **Total Effect:** Difference in income with vs. without higher education.
2. **Direct Effect:** Impact of education on income **not through job skills**.
3. **Indirect Effect:** Portion of the effect explained by **improved job skills**.

**Solution Approach:**

* Step 1: Model job skills as a function of education.
* Step 2: Model income as a function of education and job skills.
* Step 3: Decompose effects into direct and indirect components.

***

### **Conclusion**

✅ **Mediators explain the "how" and "why"** of causal relationships.\
✅ Use **mediation analysis** to separate direct and indirect effects.\
✅ Avoid conditioning on mediators when estimating total effects to prevent bias.\
✅ **Front-door criterion** provides a robust approach to handle unmeasured confounders.

***

### **Key Takeaways**

🔍 **Mediation analysis = Understanding mechanisms of causality.**\
📊 **Total Effect = Direct Effect + Indirect Effect (via Mediator).**\
⚠️ **Caution:** Conditioning on mediators can introduce bias if confounding exists.

***

By understanding mediators, researchers and practitioners can **design better interventions**, **predict outcomes more accurately**, and **make informed decisions** that target the **true mechanisms** underlying causal relationships.
