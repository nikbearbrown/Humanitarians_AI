---
description: Limitations of Causal Graphs
---

# Limitations of Causal Graphs

## **Limitations of Causal Graphs: In-Depth Theory and Mathematical Insights**

Causal graphs, particularly **Directed Acyclic Graphs (DAGs)**, have revolutionized causal inference by offering a structured way to represent causal assumptions. However, like any modeling tool, DAGs have inherent **limitations** that researchers must be aware of. Below is an expanded exploration of these limitations, accompanied by mathematical details and theoretical insights.

***

### **1. Causal Graphs Do Not Quantify the Strength of Relationships**

#### **Limitation:**

Causal graphs show the existence of causal relationships but do **not indicate the magnitude** or **strength** of these relationships.

#### **Mathematical Explanation:**

In a DAG:

X→YX \rightarrow Y

This arrow indicates a causal effect but provides **no information** about:

* The size of the effect (e.g., is it a 1% or 50% increase?).
* The functional form (linear, nonlinear, etc.).

#### **How to Quantify Strength:**

Quantification requires **structural equations** or **regression models**:

Y=α+βX+ϵY = \alpha + \beta X + \epsilon

* **β (beta)**: Quantifies the strength of the effect.
* The DAG **alone** only shows the direction of causality, not β’s value.

***

### **2. Uncontrolled Confounding Cannot Always Be Detected or Estimated**

#### **Limitation:**

DAGs rely on correctly identifying all confounders. **Unmeasured or unknown confounders** can still bias causal estimates.

#### **Example of Uncontrolled Confounding:**

X←U→YX \leftarrow U \rightarrow Y

Where:

* UU: **Unmeasured confounder** affecting both XX and YY.
* If UU is unknown or unobserved, we **cannot block** the backdoor path X←U→YX \leftarrow U \rightarrow Y.

#### **Mathematical Impact:**

Without adjusting for UU:

P(Y∣do(X))≠P(Y∣X)P(Y \mid \text{do}(X)) \neq P(Y \mid X)

⚠️ This results in **biased causal estimates**.

***

### **3. DAGs Depend on the Quality and Completeness of Information**

#### **Limitation:**

A DAG’s accuracy depends entirely on the information and assumptions provided. **Missing variables or incorrect causal directions** can lead to misleading conclusions.

#### **Example of Information Dependence:**

Incorrectly specifying:

A→B(true)vs.B→A(incorrect)A \rightarrow B \quad \text{(true)} \quad \text{vs.} \quad B \rightarrow A \quad \text{(incorrect)}

* Misrepresenting the direction of causality reverses the causal interpretation.

#### **Mathematical Consequence:**

Using an incorrect DAG structure alters **d-separation properties** and leads to **invalid conditional independence assumptions**.

***

### **4. Multiple DAGs Can Explain the Same Data**

#### **Limitation:**

**Markov equivalence classes** imply that **different DAGs** can encode the **same set of conditional independence relations** in the data.

#### **Example: Markov Equivalent DAGs:**

X→Z→YandX←Z→YX \rightarrow Z \rightarrow Y \quad \text{and} \quad X \leftarrow Z \rightarrow Y

Both imply:

X⊥Y∣ZX \perp Y \mid Z

⚠️ Without additional assumptions or experiments, **we cannot distinguish** between these structures.

***

### **5. Variables Can Simultaneously Be Mediators, Colliders, and Confounders**

#### **Limitation:**

A **single variable** may act as:

* **Mediator** on one path.
* **Confounder** on another path.
* **Collider** on yet another path.

This complexity can lead to **contradictory decisions** on whether to condition on the variable.

#### **Example Scenario:**

X→M→Y(M as mediator)X \rightarrow M \rightarrow Y \quad \text{(M as mediator)}  W→MandW→Y(M as confounder)W \rightarrow M \quad \text{and} \quad W \rightarrow Y \quad \text{(M as confounder)}  X→C←Y(C as collider)X \rightarrow C \leftarrow Y \quad \text{(C as collider)}

#### **Implication:**

* **Conditioning on a mediator (M)**: Removes indirect effects.
* **Conditioning on a collider (C)**: Introduces **collider bias**.
* **Conditioning on a confounder (W)**: Helps **control bias**.

#### **Mathematical Complexity:**

Deciding whether to condition on a variable ZZ:

P(Y∣X,Z)vs.P(Y∣X)P(Y \mid X, Z) \quad \text{vs.} \quad P(Y \mid X)

⚠️ Conditioning can either **reduce bias** or **introduce new biases** depending on ZZ's role.

***

### **6. Conditioning on Colliders Can Induce Spurious Associations**

#### **Limitation:**

**Conditioning on a collider opens a path** that otherwise would have been blocked, introducing **spurious correlations**.

#### **Example of Collider Bias:**

X→C←YX \rightarrow C \leftarrow Y

* Without conditioning on CC: X⊥YX \perp Y (independent).
* Conditioning on CC: XX and YY become **dependent**:

P(X,Y∣C)≠P(X∣C)P(Y∣C)P(X, Y \mid C) \neq P(X \mid C)P(Y \mid C)

#### **Mathematical Derivation:**

P(X,Y∣C)=P(C∣X,Y)P(X,Y)P(C)P(X, Y \mid C) = \frac{P(C \mid X, Y)P(X, Y)}{P(C)}

⚠️ Collider conditioning **creates associations** where none existed.

***

### **7. DAGs Cannot Model Feedback Loops or Cycles**

#### **Limitation:**

DAGs are **acyclic** and thus **cannot represent feedback loops**, which are common in dynamic systems.

#### **Example of a Feedback System (Not representable in a DAG):**

X→YandY→XX \rightarrow Y \quad \text{and} \quad Y \rightarrow X

#### **Alternative Models:**

* **Dynamic Bayesian Networks**
* **Structural Equation Models (SEMs)** with cycles

***

### **8. Measurement Error and Unobserved Confounders Can Distort DAG-Based Inferences**

#### **Limitation:**

**Measurement error** in variables or **unobserved confounders** can invalidate causal conclusions from a DAG.

#### **Mathematical Example:**

Observed variable X∗=X+ϵX^\* = X + \epsilon, where ϵ∼N(0,σ2)\epsilon \sim \mathcal{N}(0, \sigma^2).

P(Y∣do(X∗))≠P(Y∣do(X))P(Y \mid \text{do}(X^\*)) \neq P(Y \mid \text{do}(X))

⚠️ **Measurement error biases causal effect estimates.**

***

### **9. Limited Ability to Represent Effect Modifications and Interaction Terms**

#### **Limitation:**

DAGs **do not easily depict interactions** (effect modification), where the effect of XX on YY depends on another variable ZZ.

#### **Mathematical Representation:**

Y=β0+β1X+β2Z+β3(X⋅Z)+ϵY = \beta\_0 + \beta\_1 X + \beta\_2 Z + \beta\_3 (X \cdot Z) + \epsilon

* **β3≠0\beta\_3 \neq 0** indicates an interaction.
* DAGs **lack visual indicators** for such interactions.

***

### **10. Practical Challenges in Large-Scale DAGs**

#### **Limitation:**

As the number of variables grows, DAGs:\
✅ Become **visually cluttered**.\
✅ Make **identification of backdoor paths** difficult.\
✅ Require **advanced algorithms** for causal effect identification.

***

### **Mitigating the Limitations**

#### ✅ **Combining DAGs with Statistical Models:**

Use DAGs to identify adjustment sets, then quantify effects with regression or Bayesian methods.

#### ✅ **Sensitivity Analysis:**

Evaluate how unmeasured confounding could affect causal conclusions.

#### ✅ **Expert Knowledge Integration:**

DAGs benefit from domain expertise to include relevant variables and plausible relationships.

#### ✅ **Use of Structural Equation Models (SEMs):**

SEMs can incorporate latent variables and measure strength of causal effects.

***

### **Conclusion**

While **causal graphs (DAGs)** are powerful tools for **visualizing and reasoning about causal relationships**, they:\
⚠️ Do **not quantify effect sizes**.\
⚠️ Cannot represent **cycles or feedback loops**.\
⚠️ Depend heavily on **complete and accurate information**.\
⚠️ Are **vulnerable to collider bias** and **unmeasured confounding**.

#### **Best Practice:**

**Use DAGs as a starting point** for causal reasoning but **validate with data, statistical models, and domain knowledge**.

***

### **Further Reading and Tools**

* 📘 _Causality_ by Judea Pearl
* 📚 _The Book of Why_ by Pearl & Mackenzie
* 🔗 [DAGitty - Online DAG Tool](http://www.dagitty.net/)
* 🎥 Nick Huntington-Klein’s Causality Series on YouTube

***

### **Bottom Line:**

DAGs **clarify causal assumptions**, but careful analysis is needed to **avoid common pitfalls** and **ensure robust causal conclusions**!
