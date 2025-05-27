---
description: Bayesian Networks
---

# Bayesian Networks

## **Testable Implications and Bayesian Networks: Mathematical Foundations and Theory**

***

### **1. Introduction to Testable Implications**

Testable implications in causal inference refer to the probabilistic statements and dependencies implied by a Directed Acyclic Graph (DAG). These implications can be verified using data, allowing us to check whether a DAG is consistent with observed distributions.

#### **Why Are Testable Implications Important?**

✅ Validate causal assumptions from the DAG.\
✅ Detect model misspecifications.\
✅ Identify conditional independencies.

***

### **2. Bayesian Networks and DAGs**

#### **What is a Bayesian Network?**

A **Bayesian network** is a probabilistic graphical model that represents the conditional dependencies between variables using a DAG.

#### **Components:**

* **Nodes:** Random variables.
* **Edges:** Direct dependencies between variables.
* **Conditional Probability Distributions (CPDs):** Specify how each node depends on its parents.

***

### **3. Joint Probability Factorization from a DAG**

The key property of Bayesian networks is that the **joint probability distribution** of all variables can be factorized into the product of conditional probabilities based on the DAG structure.

#### **General Factorization Formula:**

For variables V={V1,V2,…,Vn}V = \\{V\_1, V\_2, \dots, V\_n\\}:

P(V1,V2,…,Vn)=∏i=1nP(Vi∣Parents(Vi))P(V\_1, V\_2, \dots, V\_n) = \prod\_{i=1}^n P(V\_i \mid \text{Parents}(V\_i))

***

### **4. Example: Factorizing a Joint Distribution**

#### **Consider a DAG with variables:**

A→B→C,B→D,C→E,D→E,E→F,G→DA \rightarrow B \rightarrow C, \quad B \rightarrow D, \quad C \rightarrow E, \quad D \rightarrow E, \quad E \rightarrow F, \quad G \rightarrow D

#### **Joint Distribution Factorization:**

P(A,B,C,D,E,F,G)=P(A)⋅P(G)⋅P(B∣A)⋅P(D∣B,G)⋅P(C∣B)⋅P(E∣B,C,D)⋅P(F∣E)P(A, B, C, D, E, F, G) = P(A) \cdot P(G) \cdot P(B \mid A) \cdot P(D \mid B, G) \cdot P(C \mid B) \cdot P(E \mid B, C, D) \cdot P(F \mid E)

#### **Explanation:**

* **Root nodes** AA and GG: No parents → Marginal distributions P(A)P(A) and P(G)P(G).
* **Node BB**: Depends on AA → P(B∣A)P(B \mid A).
* **Node DD**: Depends on BB and GG → P(D∣B,G)P(D \mid B, G).
* **Node CC**: Depends on BB → P(C∣B)P(C \mid B).
* **Node EE**: Depends on B,C,DB, C, D → P(E∣B,C,D)P(E \mid B, C, D).
* **Node FF**: Depends on EE → P(F∣E)P(F \mid E).

***

### **5. Conditional Independence and D-Separation**

#### **D-Separation Criterion:**

Two variables XX and YY are **conditionally independent** given a set of variables ZZ if all paths between XX and YY are **blocked** when conditioning on ZZ.

#### **Mathematically:**

X⊥Y∣Zif and only if all paths from X to Y are blocked given Z.X \perp Y \mid Z \quad \text{if and only if all paths from } X \text{ to } Y \text{ are blocked given } Z.

***

#### **Example with Variables F and E:**

* **Direct dependence:**

P(F∣E)P(F \mid E)

✅ FF depends directly on EE.

* **Conditional independence given E:**

P(F∣A,B,C,D,E,G)=P(F∣E)P(F \mid A, B, C, D, E, G) = P(F \mid E)

✅ Conditioning on EE removes the influence of all other variables on FF.

* **Marginal dependence between F and C:**

P(F∣C)≠P(F)P(F \mid C) \neq P(F)

⚠️ Without conditioning on EE, FF and CC are dependent.

***

### **6. Probability Distributions from DAGs**

DAGs help visualize **which variables are dependent or independent**:

#### **Key Relationships:**

✅ **Direct dependence:** P(F∣E)P(F \mid E)\
✅ **Conditional independence:** F⊥A,B,C,D,G∣EF \perp A, B, C, D, G \mid E\
✅ **Marginal dependence:** FF and CC are dependent without conditioning on EE.

***

### **7. Testable Implications Derived from DAGs**

#### **Testable Independence Relations:**

Derived by checking which variables should be independent or dependent according to the DAG.

#### **Example Implications:**

1. **Without conditioning:**

P(F∣A,B,C,D,G)≠P(F)P(F \mid A, B, C, D, G) \neq P(F)

2. **With conditioning on E:**

P(F∣A,B,C,D,E,G)=P(F∣E)P(F \mid A, B, C, D, E, G) = P(F \mid E)

✅ Test by comparing these probabilities using data.

***

### **8. Python Code: Simulating and Testing a Bayesian Network**

```python
import networkx as nx
import matplotlib.pyplot as plt

# Create DAG
dag = nx.DiGraph()
dag.add_edges_from([("A", "B"), ("B", "C"), ("B", "D"), ("C", "E"), ("D", "E"), ("E", "F"), ("G", "D")])

# Plot DAG
pos = nx.spring_layout(dag)
nx.draw(dag, pos, with_labels=True, node_size=2000, node_color='skyblue', arrows=True)
plt.title("Bayesian Network DAG")
plt.show()
```

✅ Visualizes the DAG to understand dependencies.

***

### **9. Markov Property in Bayesian Networks**

#### **Local Markov Property:**

A variable is independent of its non-descendants given its parents.

#### **Mathematically:**

For variable XX:

P(X∣Parents(X),NonDescendants(X))=P(X∣Parents(X))P(X \mid \text{Parents}(X), \text{NonDescendants}(X)) = P(X \mid \text{Parents}(X))

***

### **10. Practical Applications of Testable Implications**

✅ **Healthcare:** Predicting disease progression with DAGs.\
✅ **Marketing:** Understanding customer behavior dependencies.\
✅ **Economics:** Modeling causal effects of policy interventions.

***

### **11. Conclusion**

✅ **Testable implications** help validate DAG assumptions with data.\
✅ **Bayesian networks** provide a framework for probabilistic inference.\
✅ Understanding **dependencies** improves causal inference accuracy.

***

### **12. Further Resources**

📘 _Causality_ by Judea Pearl\
🔗 [DAGitty - Online DAG Tool](http://www.dagitty.net/)\
🎥 Nick Huntington-Klein’s Causality Series

***

With DAGs and Bayesian networks, you can **move beyond correlation** and **uncover causal truths** hidden in your data!
