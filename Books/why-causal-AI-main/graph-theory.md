---
description: Graph Theory
---

# Graph Theory

## **Graph Theory in Causal Inference: A Comprehensive Overview**

***

### **1. Introduction to Graph Theory**

**Graph theory** is the study of graphs, which are mathematical structures used to model relationships between objects.

* **Leonhard Euler (1736)**: Introduced graph theory to solve the Königsberg bridge problem.
* **Judea Pearl (1995)**: Extended graph theory to **causal inference** with **Directed Acyclic Graphs (DAGs)**.

#### **Why Graph Theory in Causality?**

Graphs help:\
✅ Visualize causal structures.\
✅ Identify confounders and mediators.\
✅ Determine which variables to control for.

***

### **2. Components of Graphs**

#### **2.1 Nodes (Vertices)**

* Represent **variables** (e.g., treatment, outcome, confounder).
* Denoted by circles: V={X,Y,Z}V = \\{X, Y, Z\\}.

#### **2.2 Edges (Links)**

* Represent **relationships** between variables.
* Types of edges:
  * **Directed edge**: X→YX \rightarrow Y (X causes Y)
  * **Undirected edge**: X−YX - Y (association without direction)

***

### **3. Paths in Graphs**

#### **3.1 Path Definition**

A **path** is a sequence of connected nodes:

X→Z→YX \rightarrow Z \rightarrow Y

* **Direct Path**: X→YX \rightarrow Y
* **Indirect Path**: X→Z→YX \rightarrow Z \rightarrow Y

***

#### **3.2 Blocked and Unblocked Paths**

* **Blocked Path**: Information flow is stopped (e.g., by conditioning on a collider).
* **Unblocked Path**: Information can flow between variables.

#### **How to Block a Path:**

1. **Conditioning on a confounder**: Blocks backdoor paths.
2. **Conditioning on a collider**: **Unblocks** an otherwise blocked path (counterintuitive).

***

### **4. Types of Nodes and Relationships**

| **Term**           | **Definition**                                     |
| ------------------ | -------------------------------------------------- |
| **Parent Node**    | Node with an outgoing edge (cause)                 |
| **Child Node**     | Node with an incoming edge (effect)                |
| **Ancestor**       | Parent’s parent, and so on                         |
| **Descendant**     | Child’s child, and so on                           |
| **Adjacent Nodes** | Nodes connected directly by an edge                |
| **Degree of Node** | Number of connected edges (in-degree + out-degree) |

***

### **5. Causal Relationships**

#### **5.1 Direct Causal Relationship**

X→YX \rightarrow Y

X directly causes Y.

***

#### **5.2 Indirect Causal Relationships**

1.  **Indirect Cause:**

    X→Z→YX \rightarrow Z \rightarrow Y

    X causes Y through Z.
2.  **Indirect Effect:**

    X←Z←YX \leftarrow Z \leftarrow Y

    Z affects both X and Y.
3.  **Common Cause (Confounder):**

    X←Z→YX \leftarrow Z \rightarrow Y

    Z confounds the X–Y relationship.
4.  **Common Effect (Collider):**

    X→Z←YX \rightarrow Z \leftarrow Y

    Z is a collider for X and Y.

***

### **6. Conditional Independence and D-Separation**

#### **6.1 Conditional Independence**

Two variables XX and YY are **conditionally independent given ZZ** if:

P(X,Y∣Z)=P(X∣Z)P(Y∣Z)P(X, Y \mid Z) = P(X \mid Z) P(Y \mid Z)

Notation: X⊥Y∣ZX \perp Y \mid Z

***

#### **6.2 D-Connection vs. D-Separation**

| **Term**        | **Definition**                                 |
| --------------- | ---------------------------------------------- |
| **D-Connected** | X and Y have an unblocked path.                |
| **D-Separated** | All paths between X and Y are blocked given Z. |

**Rules of D-Separation:**

1. **Non-collider conditioning blocks the path.**
2. **Conditioning on a collider opens the path.**
3. **Conditioning on a collider’s descendant also opens the path.**

#### **Mathematical Criterion:**

For variables X,Y,ZX, Y, Z:

D-Separation: X⊥Y∣Z  ⟺  all paths between X and Y are blocked by Z\text{D-Separation: } X \perp Y \mid Z \iff \text{all paths between } X \text{ and } Y \text{ are blocked by } Z

***

### **7. Types of Paths in Causal Graphs**

#### **7.1 Frontdoor Paths:**

* Paths with arrows **moving away** from the treatment.
* Represent **causal effects** we want to measure.
* **Do not block** these paths during analysis.

**Example:**

X→M→YX \rightarrow M \rightarrow Y

***

#### **7.2 Backdoor Paths:**

* Paths that **enter the treatment node** from behind.
* Represent **non-causal associations** (confounding).
* **Must be blocked** to identify causal effects.

**Example:**

X←Z→YX \leftarrow Z \rightarrow Y

**Backdoor Criterion:**

A set ZZ satisfies the criterion if:

1. No node in ZZ is a descendant of XX.
2. ZZ blocks every backdoor path from XX to YY.

P(Y∣do(X))=∑zP(Y∣X,Z=z)P(Z=z)P(Y \mid \textbf{do}(X)) = \sum\_z P(Y \mid X, Z=z) P(Z=z)

***

#### **7.3 Colliders and Their Effects:**

* **Collider:** X→Z←YX \rightarrow Z \leftarrow Y blocks the path.
* **Conditioning on a collider** opens the path, allowing spurious associations.

***

### **8. Causal Markov Condition**

The **Causal Markov Condition** states:\
Given a variable’s **parents** in the DAG, it is independent of all **non-descendants**.

Mathematically:

P(Vi∣Pa(Vi))=P(Vi∣Pa(Vi),non-descendants)P(V\_i \mid Pa(V\_i)) = P(V\_i \mid Pa(V\_i), \text{non-descendants})

✅ Ensures that causal influences flow through directed paths.

***

### **9. Practical Examples**

#### **9.1 Health Example:**

* XX: Smoking
* YY: Lung Cancer
* ZZ: Genetic Predisposition

**Without Adjustment:**

P(Y∣X)may be biased.P(Y \mid X) \quad \text{may be biased.}

**With Backdoor Adjustment:**

P(Y∣do(X))=∑zP(Y∣X,Z=z)P(Z=z)P(Y \mid \textbf{do}(X)) = \sum\_z P(Y \mid X, Z=z) P(Z=z)

✅ Removes confounding from ZZ.

***

#### **9.2 Marketing Example:**

* XX: Advertisement
* YY: Product Sales
* ZZ: Seasonality

✅ Adjusting for ZZ ensures sales increase is truly due to the ad.

***

### **10. Python Code for D-Separation Using DoWhy**

```python
import dowhy
import pandas as pd
import numpy as np

# Create synthetic data
np.random.seed(42)
data = pd.DataFrame({
    "X": np.random.binomial(1, 0.5, 1000),  # Treatment
    "Z": np.random.normal(0, 1, 1000),       # Confounder
})
data["Y"] = 0.4 * data["X"] + 0.6 * data["Z"] + np.random.normal(0, 1, 1000)  # Outcome

# Causal Model
model = dowhy.CausalModel(
    data=data,
    treatment="X",
    outcome="Y",
    graph="digraph { Z -> X; Z -> Y; X -> Y; }"
)

# Identify effect
identified_estimand = model.identify_effect()
estimate = model.estimate_effect(identified_estimand, method_name="backdoor.linear_regression")

print("Estimated Causal Effect:", estimate.value)
```

✅ **Output:** Estimated causal effect ≈ 0.4 (matches true coefficient).

***

### **11. Key Takeaways**

✅ **Graphs** provide a visual and mathematical foundation for causal reasoning.\
✅ **Backdoor paths** must be blocked to remove confounding.\
✅ **Frontdoor paths** capture the direct causal effect.\
✅ **D-Separation** links graphical separation to statistical independence.\
✅ **Causal Markov Condition** ensures efficient factorization of probabilities.

***

### **12. Further Reading and Resources**

📘 **Books:**

* _Causality_ by Judea Pearl
* _The Book of Why_ by Judea Pearl & Dana Mackenzie

🔗 **Tools:**

* [DAGitty for online DAG construction](http://www.dagitty.net/)
* [DoWhy Python Library](https://github.com/py-why/dowhy)

🎥 **Videos:**

* Judea Pearl’s lectures on causal graphs.
* Nick Huntington-Klein’s YouTube series on D-Separation.

***

Graph theory is the **mathematical backbone** of modern causal inference. By understanding its principles, researchers can **distinguish causation from mere association**, leading to **more accurate predictions** and **better decision-making**.
