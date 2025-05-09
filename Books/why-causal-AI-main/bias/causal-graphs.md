---
description: Causal Graphs
---

# Causal Graphs

## **Causal Graphs: Theory, Mathematics, and Applications**

### **Introduction to Causal Graphs**

Causal graphs, often referred to as **Directed Acyclic Graphs (DAGs)**, are essential tools in causal inference. They provide a visual and mathematical representation of causal relationships between variables, capturing both associations and direct causal effects.

***

### **Types of Graphs**

#### **1. Directed Graphs**

A **directed graph** consists of nodes (variables) connected by edges (arrows) that indicate a **direction** of influence.

* **Mathematical Definition:**\
  A directed graph G=(V,E)G = (V, E) is defined by a set of vertices VV and a set of directed edges E⊆V×VE \subseteq V \times V.\
  An edge (X→Y)(X \to Y) implies that XX is a cause of YY.
*   **Example:**\
    If XX represents smoking and YY represents lung cancer:

    X→YX \to Y

    means smoking causes lung cancer.

***

#### **2. Undirected Graphs**

In an **undirected graph**, edges have no direction, representing mere association rather than causation.

* **Mathematical Definition:**\
  An undirected graph G=(V,E)G = (V, E) has edges E⊆\{{x,y}:x,y∈V}E \subseteq \\{ \\{x, y\\} : x, y \in V \\}.
*   **Example:**

    X−YX - Y

    implies XX and YY are associated, but no causal direction is implied.

***

### **Types of Directed Graphs**

#### **1. Cyclic Graphs**

A **cyclic graph** contains at least one cycle — a path that starts and ends at the same node.

*   **Mathematical Condition:**\
    A cycle exists if there is a sequence of edges:

    X1→X2→⋯→Xn→X1X\_1 \to X\_2 \to \cdots \to X\_n \to X\_1
* **Why Not Use Cycles in Causality?**\
  Cycles would imply that a variable can cause itself through a feedback loop, violating the principle that causes precede effects.

***

#### **2. Acyclic Graphs**

An **acyclic graph** contains no cycles. DAGs, by definition, are acyclic.

* **Mathematical Definition:**\
  A DAG G=(V,E)G = (V, E) has no directed cycles.
* **Why Acyclic?**\
  Causal relationships are inherently time-oriented — causes affect future events, not past ones.\
  **No cycles** ensure no variable is its own cause.

***

### **Elements of a Causal DAG**

A **Causal DAG** includes:

1. **Nodes (Vertices)**: Represent variables (e.g., treatment, outcome, confounders).
2. **Edges (Arrows)**: Indicate direct causal relationships. A→B⇒A causes BA \to B \quad \Rightarrow \quad A \text{ causes } B
3. **Missing Arrows**: Imply **sharp assumptions** about absent causal effects.\
   If there’s no edge between XX and YY, we assume no direct causal link.

***

### **Mathematical Representation of Causal Graphs**

Given variables X,Y,ZX, Y, Z:

*   **Joint Distribution Factorization:**\
    DAGs imply a factorization of the joint probability:

    P(X1,X2,…,Xn)=∏i=1nP(Xi∣Parents(Xi))P(X\_1, X\_2, \dots, X\_n) = \prod\_{i=1}^{n} P(X\_i \mid \text{Parents}(X\_i))
*   **Example:**\
    For a DAG: X→Y→ZX \to Y \to Z

    P(X,Y,Z)=P(X)⋅P(Y∣X)⋅P(Z∣Y)P(X, Y, Z) = P(X) \cdot P(Y \mid X) \cdot P(Z \mid Y)
*   **Conditional Independence:**

    X⊥Z∣Y(X and Z are independent given Y)X \perp Z \mid Y \quad \text{(X and Z are independent given Y)}

***

### **Why Use Causal Graphs?**

#### **Key Benefits:**

* Visualize complex causal relationships.
* Explicitly define and communicate assumptions.
* Identify variables that need controlling for unbiased causal estimates.
* Guide interventions and counterfactual reasoning.

***

### **Causal Paths and Biases in DAGs**

#### **1. Confounding Bias**

Occurs when a **common cause** affects both the treatment and outcome.

*   **DAG Structure:**

    A←C→YA \leftarrow C \to Y
*   **Solution:** Control for confounder CC.\
    **Adjustment Formula:**

    P(Y∣do(A))=∑cP(Y∣A,C=c)P(C=c)P(Y \mid do(A)) = \sum\_c P(Y \mid A, C=c)P(C=c)

***

#### **2. Collider Bias**

Occurs when two variables influence a third variable (a **collider**), and we condition on the collider.

*   **DAG Structure:**

    A→B←YA \to B \leftarrow Y
* **Issue:** Conditioning on BB induces spurious association between AA and YY.

***

#### **3. Mediators and Direct vs. Indirect Effects**

*   **Mediator:** A variable on the causal path between treatment and outcome.

    A→M→YA \to M \to Y
* **Direct Effect:** Impact of AA on YY not through MM.
* **Indirect Effect:** Effect of AA on YY through MM.

***

### **Identifying Causal Effects Using Graphs**

#### **Backdoor Criterion:**

A set ZZ satisfies the **backdoor criterion** if it blocks all backdoor paths between treatment AA and outcome YY.

* **Mathematically:** P(Y∣do(A))=∑zP(Y∣A,Z=z)P(Z=z)P(Y \mid do(A)) = \sum\_z P(Y \mid A, Z=z)P(Z=z)

***

#### **Frontdoor Criterion:**

When no backdoor set exists, **frontdoor adjustment** may be used via a mediator MM.

* **Formula:** P(Y∣do(A))=∑mP(M=m∣A)∑aP(Y∣M=m,A=a)P(A=a)P(Y \mid do(A)) = \sum\_m P(M=m \mid A) \sum\_a P(Y \mid M=m, A=a)P(A=a)

***

### **Structural Causal Models (SCMs)**

SCMs extend DAGs with equations:

*   **Definition:**\
    For each variable XiX\_i:

    Xi=fi(Parents(Xi),Ui)X\_i = f\_i(\text{Parents}(X\_i), U\_i)

    where UiU\_i represents unobserved factors.
*   **Example:**

    Y=βA+γC+UYY = \beta A + \gamma C + U\_Y

    Here, YY depends on AA, CC, and noise UYU\_Y.

***

### **Causal Discovery and Structure Learning**

Algorithms (e.g., PC algorithm, GES, LiNGAM) can infer causal structure from data using independence tests and domain knowledge.

***

### **Applications of Causal Graphs**

* **Healthcare:** Estimating treatment effects and reducing confounding.
* **Economics:** Understanding policy impacts.
* **AI Ethics:** Detecting and mitigating bias in predictive models.
* **Marketing:** Evaluating campaign effectiveness.

***

### **Example Case Study: Smoking and Lung Cancer**

DAG:

Smoking→Tar→Lung Cancer,Smoking→Lung Cancer\text{Smoking} \to \text{Tar} \to \text{Lung Cancer}, \quad \text{Smoking} \to \text{Lung Cancer}

#### **Calculating Causal Effect:**

1. Identify backdoor paths.
2. Adjust for confounders (e.g., genetics).
3. Apply do-calculus to estimate causal effect.

***

### **Conclusion**

Causal graphs, especially DAGs, are foundational tools in causal inference. They clarify assumptions, identify confounders, and guide causal effect estimation. Their mathematical rigor enables precise, testable predictions, bridging the gap between correlation and causation.
