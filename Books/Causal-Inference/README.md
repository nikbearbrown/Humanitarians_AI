# Causal Inference

## What is Causal Inference

The following explores the evolution of causal inference, from David Hume’s philosophical principles to modern statistical methods, emphasizing randomized experiments, observational studies, and counterfactual reasoning. It distinguishes between different conceptions of causation and highlights the progression of causal inference methodologies in statistics. Throughout, we will focus on practical examples in **marketing** and **medicine**, with a special emphasis on **COVID-19** case studies to illustrate real-world applications of these methods.


### **1. Hume’s Conception of Causation**
David Hume (1740) proposed three criteria for causation:
1. **Temporal Priority** – The cause must occur before the effect.
2. **Contiguity** – The cause and effect must be spatially or temporally connected.
3. **Constant Conjunction** – The effect must always follow the cause under the same conditions.

Hume’s framework suggests that causation is deterministic, meaning a specific cause always produces a given effect, provided external conditions remain unchanged. However, modern discussions acknowledge that causation may not always be deterministic and can be subject to variation.

---

### **2. Necessity and Sufficiency in Causation**
- A **sufficient cause** always leads to the effect.
- A **necessary cause** must be present for the effect to occur but does not guarantee it.
- A **necessary and sufficient cause** means that the effect occurs **if and only if** the cause is present.

Example:  
- Speeding might not always cause an accident, but if an accident occurs, speeding might have been a necessary contributing factor.
- However, other factors like poor road conditions and weather might also contribute.

---

### **3. Deterministic vs. Probabilistic Causation**
In scientific studies, causation is often **probabilistic** rather than deterministic. That is, a cause increases the probability of an effect occurring rather than guaranteeing it.
Here’s the updated version with **GitHub-flavored markdown (GFM)** for math formatting:

---

## **3. Causation and Causal Effects**

- **Causation is established through probability differences:**  
  `Pr[Y=1 | A=1] ≠ Pr[Y=1 | A=0]`  
  This means that the probability of an outcome \( Y \) given treatment \( A \) differs from the probability of \( Y \) occurring without the treatment.

- **Causal Effect:**  
  `E[Y^(a=1)] - E[Y^(a=0)]`  
  This represents the difference in expected outcomes under treatment versus no treatment.

- **Sharp causal null hypothesis:**  
  `Y^(a=1) = Y^(a=0)`  
  This states that the treatment has no causal effect on any individual.

---
## **4. Association**


This is about understanding the **relationship between two things**:  
👉 Does changing **A** affect the chances of **Y** happening?

In simpler words, imagine you're asking:  
> *"If I change something (like sending an ad or giving a medicine), does it change the result (like buying a product or getting healthy)?"*

---

## **What do A and Y mean?**

- **A:** Something you can change (a condition or choice)  
  - Example: Sending an ad (marketing) or giving a vaccine (medicine)  
  - \( A = 1 \) means *yes* (ad was sent / vaccine was given)  
  - \( A = 0 \) means *no* (no ad / no vaccine given)  

- **Y:** The outcome (what happens after)  
  - Example: Whether someone buys a product (marketing) or gets sick (medicine)  
  - \( Y = 1 \) means *yes* (they bought the product / got sick)  
  - \( Y = 0 \) means *no* (they didn’t buy / didn’t get sick)  

---

## **What is association?**

Two things are **associated** if knowing one gives you information about the other.

- **Marketing Example:**  
  👉 If people who see an ad (A) are more likely to buy a product (Y), then seeing the ad and buying are associated.

- **Medicine Example (COVID-19):**  
  👉 If people who get the COVID-19 vaccine (A) are less likely to get sick (Y), then getting vaccinated and getting sick are associated.

---

## **What does the math say?**

### **1. Association exists if:**  

\[
Pr(Y=1 \mid A=1) \neq Pr(Y=1 \mid A=0)
\]

🔍 This means:  
- The chance of **Y** happening when **A** happens is *not* the same as when **A** doesn’t happen.  

➡️ **If they are different:** A affects Y (there is an association)  
➡️ **If they are the same:** No association  

---

## **How do we show no association?**

There are **three ways** to check if **A** and **Y** are unrelated (no association):

---

### **1. Using subtraction (difference of probabilities):**  

\[
Pr(Y=1 \mid A=1) - Pr(Y=1 \mid A=0) = 0
\]

✅ No association if the difference is **0**.  

**Marketing Example:**  
- Chance of buying after seeing an ad: 0.4  
- Chance of buying without seeing an ad: 0.4  

\[
0.4 - 0.4 = 0 \quad \checkmark \quad (\text{No association})
\]

---

**COVID-19 Example (Medicine):**  
- Chance of getting sick with the vaccine: 0.1  
- Chance of getting sick without the vaccine: 0.3  

\[
0.1 - 0.3 = -0.2 \quad \neq 0 \quad (\text{Association exists})
\]

➡️ Vaccination reduces the chance of getting sick.

---

### **2. Using division (risk ratio):**  

\[
\frac{Pr(Y=1 \mid A=1)}{Pr(Y=1 \mid A=0)} = 1
\]

✅ No association if the ratio is **1**.  

**Marketing Example:**  
- With ad: 0.4  
- Without ad: 0.4  

\[
\frac{0.4}{0.4} = 1 \quad \checkmark \quad (\text{No association})
\]

---

**COVID-19 Example (Medicine):**  
- With vaccine: 0.1  
- Without vaccine: 0.3  

\[
\frac{0.1}{0.3} = 0.33 \quad \neq 1 \quad (\text{Association exists})
\]

➡️ The vaccine reduces the risk of getting sick.

---

### **3. Using odds (odds ratio):**  

First, what are **odds**?  
\[
\text{Odds} = \frac{\text{Chance of success}}{\text{Chance of failure}}
\]

No association if:  

\[
\frac{Pr(Y=1 \mid A=1)/Pr(Y=0 \mid A=1)}{Pr(Y=1 \mid A=0)/Pr(Y=0 \mid A=0)} = 1
\]

---

**Marketing Example:**  
- With ad: 40% buy, 60% don’t → Odds = \( \frac{0.4}{0.6} = 0.67 \)  
- Without ad: 40% buy, 60% don’t → Odds = \( \frac{0.4}{0.6} = 0.67 \)  

\[
\frac{0.67}{0.67} = 1 \quad \checkmark \quad (\text{No association})
\]

---

**COVID-19 Example (Medicine):**  
- With vaccine: 10% sick, 90% healthy → Odds = \( \frac{0.1}{0.9} = 0.11 \)  
- Without vaccine: 30% sick, 70% healthy → Odds = \( \frac{0.3}{0.7} = 0.43 \)  

\[
\frac{0.11}{0.43} = 0.26 \quad \neq 1 \quad (\text{Association exists})
\]

➡️ The vaccine lowers the odds of getting sick.

---

## **Bottom line:**

👉 If changing **A** (like showing an ad or giving a vaccine) **changes the chances** of **Y** (buying or getting sick), **there is an association**.  

👉 If the chances **stay the same**, there’s **no association** — that’s what the math checks!  

---

## **Why does this matter?**

- In **marketing**, understanding association helps companies know if ads actually increase sales.  
- In **medicine** (like during **COVID-19**), it helps figure out if vaccines or treatments work.  

Knowing these associations helps people make smarter decisions!

## **4. Counterfactual Causality**

A modern approach to causation involves **counterfactual reasoning**, where we ask:  
*"What would have happened if the treatment had not been applied?"*

- If John skids off the road while speeding, we consider:  
  *Would he have skidded if he had not been speeding?*  

From **NOTES**:  
- **Counterfactual outcome notation:**  
  `Pr[Y^(a=1) = 1] ≠ Pr[Y^(a=0) = 1]`  
  If these probabilities differ, then treatment \( A \) affects outcome \( Y \), indicating causation.

---

## **5. Observational Studies vs. Randomized Experiments**

- **Randomized Experiments:** The treatment is assigned randomly, eliminating confounders and allowing causal conclusions.
- **Observational Studies:** Treatment is not randomly assigned, so confounders may bias the results.

From **NOTES**:  
- **Exchangeability condition** (for valid causal inference in observational studies):  
  `Pr[Y^a = 1 | A=1] = Pr[Y^a = 1 | A=0]`  
  This means the treated and untreated groups must be comparable in terms of potential outcomes.

- **Standardization and Inverse Probability Weighting (IPW)** can adjust for confounding by reweighting observations to approximate a randomized study.

---

## **6. Granger Causality and Correlation**

- **Karl Pearson (1894):** Initially equated correlation with causation.  
- **George Yule (1895):** Introduced partial correlation to distinguish between spurious and causal relationships.  
- **Granger Causality:** A time-series method where \( X \) is said to “Granger-cause” \( Y \) if past values of \( X \) improve the prediction of \( Y \) beyond what past values of \( Y \) alone can do.

From **NOTES**:  
- **Confounding and Spurious Correlation:**  
  If \( X \) and \( Y \) are correlated, a third variable \( Z \) might be causing both.  
  `Pr[Y | X, Z] = Pr[Y | Z]`  
  This suggests that controlling for \( Z \) removes the association between \( X \) and \( Y \), implying no direct causation.

- **Example of Spurious Causality:**  
  Greek economist X. Shin found a correlation between economic activity and sunspots using Granger causality, demonstrating the risks of relying solely on correlation.

---

## **7. Potential Outcomes and Rubin’s Framework**

Donald Rubin (1970s) reintroduced the **potential outcomes framework**, which formalizes causal inference as:  
`E[Y^(a=1)] - E[Y^(a=0)]`  
This measures the **average treatment effect (ATE)**.

From **NOTES**:  
- **Causal Risk Ratio:**  
  `Pr[Y^(a=1) = 1] / Pr[Y^(a=0) = 1]`  
  This compares the probability of the outcome under treatment versus no treatment.

- **Identifiability Conditions for Causal Inference:**  
  1. **Consistency:** The observed outcome matches the counterfactual.  
  2. **Exchangeability:** The treatment groups must be comparable.  
  3. **Positivity:** Each individual has a nonzero probability of receiving either treatment.



### **8. Differences Between Observational and Experimental Approaches**
- **Observational studies ask:** *What are the causes of an effect?*  
  - Example: What factors influence a person's earnings?
- **Experiments ask:** *What is the effect of a cause?*  
  - Example: What is the effect of job training on earnings?

From **NOTES**:
- **Frontdoor and Backdoor Criteria:**  
  - The **backdoor criterion** adjusts for confounders blocking non-causal paths.  
  - The **frontdoor criterion** estimates causal effects through mediators when confounding cannot be controlled directly.

---

### **9. Conclusion**
Modern causal inference builds on Hume’s ideas but extends them with:
- **Counterfactual reasoning**
- **Probabilistic causation**
- **Randomized experiments and observational adjustments**

The **Rubin Causal Model (RCM)** now dominates observational studies, emphasizing that causal inference is not about defining causation itself, but about establishing conditions under which causal relationships can be inferred.

From **NOTES**:
- **Causal Diagrams (DAGs)** help visualize causal relationships.
- **Effect Modification and Interaction** help identify when causal effects vary across subpopulations.

This framework has transformed research across social sciences, medicine, economics, and machine learning, improving the accuracy and reliability of causal claims.

---

## Module 2

**Title:**  
**Understanding Causal Inference: Singular Causation, Counterfactuals, and Treatment Effects**

---

## **Detailed Summary of Concepts and Equations**

This section explores the foundational principles of **causal inference** through the lens of **singular causation**, **counterfactual reasoning**, and **treatment effects**. It builds on the philosophical underpinnings of causation, focusing on how to quantify and estimate causal effects when only one outcome is observed per individual. The discussion introduces critical concepts like **potential outcomes**, **average treatment effects (ATE)**, and key assumptions like the **Stable Unit Treatment Value Assumption (SUTVA)**.

---

### **1. Singular Causation and Counterfactual Conditionals**  
Causal inference begins with two key criteria:  
1. **Singular Causation**:  
   - Causation can be considered at an individual level.  
   - Example: *John takes medicine and gets better* vs. *John doesn’t take medicine and gets worse*.  
   - This approach allows for scenarios where causes vary across populations (e.g., speeding causing accidents in Mexico but not in Canada).  

2. **Counterfactual Conditionals**:  
   - Causal claims involve imagining “what would have happened” if a different choice were made.  
   - Example: *If John hadn’t taken the medicine, he wouldn’t have recovered.*  
   - **Counterfactuals** underpin modern causal inference by comparing actual outcomes with hypothetical alternatives.  

From **NOTES**:  
- **Causal Effect Formula**:  
  \[
  Pr[Y=1|A=1] \neq Pr[Y=1|A=0]
  \]
  A treatment \( A \) is causal if the probability of outcome \( Y \) differs when the treatment is present versus absent.  

---

### **2. Potential Outcomes Framework**  
Developed by Donald Rubin, the **Potential Outcomes** framework formalizes causation as follows:

- **Notation**:  
  - \( Y_i(1) \): Outcome for individual \( i \) if treated (e.g., John takes medicine).  
  - \( Y_i(0) \): Outcome for individual \( i \) if untreated (e.g., John doesn’t take medicine).  
- **Fundamental Problem of Causal Inference**:  
  We **only observe one** of these two outcomes per person.  

**Individual Treatment Effect (ITE)**:  
\[
\text{ITE}_i = Y_i(1) - Y_i(0)
\]
- If ITE > 0: Treatment benefits the individual.  
- If ITE = 0: No effect.  
- If ITE < 0: Treatment harms the individual.  

From **NOTES**:  
- **Counterfactual Representation**:  
  \[
  Pr[Y^{(a=1)}=1] - Pr[Y^{(a=0)}=1]
  \]
  Measures the causal effect across potential outcomes.  

---

### **3. Treatment Assignment and Observed Outcomes**  
Let \( Z_i \) be the **treatment assignment indicator**:  
- \( Z_i = 1 \): Individual \( i \) receives treatment.  
- \( Z_i = 0 \): Individual \( i \) does not receive treatment.  

**Observed Outcome**:  
\[
Y_i = Z_iY_i(1) + (1 - Z_i)Y_i(0)
\]
- We see only the outcome corresponding to the assigned treatment.  

From **NOTES**:  
- **Sharp causal null hypothesis**:  
  \[
  Y_i(1) = Y_i(0) \quad \forall i
  \]
  No individual causal effects exist if this holds true.  

---

### **4. Average Treatment Effects (ATE)**  
Since we cannot observe individual causal effects directly, we estimate **population-level effects**:

#### **4.1. Sample Average Treatment Effect (SATE)**  
\[
\text{SATE} = \frac{1}{n}\sum_{i=1}^n [Y_i(1) - Y_i(0)]
\]
- Average effect across a finite sample.  

#### **4.2. Population Average Treatment Effect (PATE)**  
\[
\text{PATE} = \frac{1}{N}\sum_{i=1}^N [Y_i(1) - Y_i(0)]
\]
- Average effect across the entire population.  

#### **4.3. Average Treatment Effect (ATE)**  
\[
\text{ATE} = E[Y(1) - Y(0)]
\]
- Expected treatment effect in a theoretical infinite population.  

From **NOTES**:  
- **Causal Risk Difference**:  
  \[
  Pr[Y=1|A=1] - Pr[Y=1|A=0]
  \]
  Equivalent to the ATE when dealing with binary outcomes.  

---

### **5. Treatment Effect Variations**  

#### **5.1. Average Treatment Effect on the Treated (ATT)**  
Focuses on the effect for individuals who **actually received the treatment**:  
\[
\text{ATT} = E[Y(1) - Y(0)|Z=1]
\]
- Important for policies targeting voluntary interventions.  

#### **5.2. Average Treatment Effect on the Untreated (ATU)**  
\[
\text{ATU} = E[Y(1) - Y(0)|Z=0]
\]
- Assesses potential benefits for those not receiving treatment.  

From **NOTES**:  
- **Effect Modification**: If treatment effects differ by subgroup (e.g., age, gender), the ATT and ATU may vary significantly.  

---

### **6. Challenges in Estimating Treatment Effects**  
- **Missing Data**:  
  We only observe \( Y_i(1) \) or \( Y_i(0) \), **never both**.  
- **Ignorability (Unconfoundedness)**:  
  \[
  Y(1), Y(0) \perp Z \mid X
  \]
  Treatment assignment is independent of potential outcomes given covariates \( X \).  

- **Positivity** (from **NOTES**):  
  \[
  Pr[Z=z|X=x] > 0 \quad \forall x
  \]
  Every individual has a chance of receiving both treatment and control conditions.  

---

### **7. Stable Unit Treatment Value Assumption (SUTVA)**  
SUTVA ensures well-defined potential outcomes:  

1. **No hidden variations of the treatment**:  
   - If pill and capsule forms differ, they must be treated as distinct treatments.  

2. **No interference between units**:  
   - One individual’s treatment doesn’t affect another’s outcome (e.g., flu vaccination must account for herd immunity).  

From **NOTES**:  
- **Interference** violates SUTVA, complicating causal estimation.  

---

### **8. Identifiability and Estimation Methods**  
Under **ignorability** and **SUTVA**:  
- We can estimate **ATE** using observed outcomes and treatment assignments.  
- **Randomized Experiments**: Satisfy ignorability by design.  
- **Observational Studies**: Require methods like:  
  - **Inverse Probability Weighting (IPW)** (from **NOTES**): Reweights samples to mimic randomization.  
  - **Matching**: Pairs treated and untreated units with similar covariates.  
  - **Regression Adjustment**: Controls for confounders statistically.  

---

### **9. Beyond Simple Averages**  
Sometimes, we want more nuanced estimands:  
- **Median Treatment Effect**: Focuses on median changes rather than means.  
- **Probability of Improvement**:  
  \[
  Pr[Y(1) > Y(0)]
  \]
  - Requires knowledge of the **joint distribution** of potential outcomes.  
  - More complex to estimate but crucial in decision-making contexts.  

---

### **10. Practical Implications**  
- **Doctors** need to know how treatments work **on average** when individual effects are unknown.  
- **Policymakers** rely on ATE and ATT to implement beneficial interventions.  
- **Researchers** must navigate assumptions and select appropriate estimation methods.  

From **NOTES**:  
- **Frontdoor and Backdoor Criteria** help identify valid adjustment sets for causal inference.  

---

## **Key Equations Summary:**  

| **Concept** | **Equation** | **Explanation** |
|-------------|--------------|-----------------|
| Individual Treatment Effect (ITE) | \( Y_i(1) - Y_i(0) \) | Effect of treatment on an individual. |
| Average Treatment Effect (ATE) | \( E[Y(1)-Y(0)] \) | Population-level causal effect. |
| Sample Average Treatment Effect (SATE) | \( \frac{1}{n}\sum (Y_i(1)-Y_i(0)) \) | Average effect in a sample. |
| Average Treatment Effect on Treated (ATT) | \( E[Y(1)-Y(0)|Z=1] \) | Effect for treated individuals. |
| Observed Outcome | \( Y_i = Z_iY_i(1)+(1-Z_i)Y_i(0) \) | Outcome under observed treatment. |
| Ignorability Condition | \( Y(1), Y(0) \perp Z \mid X \) | No unmeasured confounding given covariates. |
| Positivity | \( Pr[Z=z|X=x] > 0 \) | Everyone can receive any treatment level. |

---

## **Conclusion**  
This chapter establishes a robust foundation for causal inference through:  
- Singular-level causation  
- Counterfactual reasoning  
- Population-level treatment effects (ATE, ATT, ATU)  
- Essential assumptions (SUTVA, ignorability, positivity)  

Future sections will explore how to **identify** and **estimate** these causal effects, especially in complex observational settings.  

---

## Module 3

**Title:**  
**Unconfoundedness, Ignorability, and Estimating Causal Effects in Randomized and Observational Studies**

---

## **Detailed Summary of Concepts and Equations**

This section builds on the previous discussions of **potential outcomes** and **treatment effects** by focusing on the conditions necessary to **unbiasedly and consistently estimate causal effects**. It introduces key concepts like **unconfoundedness** (also known as **ignorability**), **randomization**, and the **bridge between randomized experiments and observational studies**. The section explains why randomization ensures unconfoundedness, how observational studies can mimic randomization under certain conditions, and highlights the challenges involved when these conditions do not hold.

---

## **1. Recap of Potential Outcomes and Treatment Effects**  
In the previous lesson, we defined:  

- **Individual Treatment Effect (ITE)**:  
  \[
  \text{ITE}_i = Y_i(1) - Y_i(0)
  \]
  Measures the causal effect of the treatment on an individual.  

- **Sample Average Treatment Effect (SATE)**:  
  \[
  \text{SATE} = \frac{1}{n} \sum_{i=1}^n [Y_i(1) - Y_i(0)]
  \]
  Average treatment effect across the sample.  

- **Finite Population Average Treatment Effect (FPATE)**:  
  \[
  \text{FPATE} = \frac{1}{N} \sum_{i=1}^N [Y_i(1) - Y_i(0)]
  \]
  Average treatment effect across a known population of size \( N \).  

- **Average Treatment Effect (ATE)**:  
  \[
  \text{ATE} = E[Y(1) - Y(0)]
  \]
  Expected treatment effect in a (possibly infinite) population.  

While these estimands are conceptually straightforward, the **fundamental problem of causal inference** remains: **we cannot observe both potential outcomes for the same individual**.

---

## **2. Unconfoundedness and Ignorability Conditions**  
### **Definition:**  
**Unconfoundedness (Ignorability)** holds if the assignment of treatment \( Z \) is independent of the potential outcomes \( Y(1) \) and \( Y(0) \), given a set of covariates \( X \).  

Formally:  
\[
(Y(1), Y(0)) \perp Z \mid X
\]

This means that once we condition on \( X \), treatment assignment is "as good as random."

### **Why is this important?**  
- If unconfoundedness holds, the difference in average observed outcomes between treated and untreated groups **reflects the causal effect** of the treatment.  
- Without unconfoundedness, comparing groups can be misleading due to **confounding variables** that affect both treatment assignment and outcomes.

---

## **3. Randomized Experiments: Natural Satisfaction of Unconfoundedness**  
In **randomized controlled trials (RCTs)**:
- **Treatment assignment \( Z \)** is independent of potential outcomes by design.
- **Unconfoundedness automatically holds**:  
  \[
  (Y(1), Y(0)) \perp Z
  \]
- Sample means estimate the expectations:  
  \[
  \bar{Y}_1 = \frac{1}{n_1}\sum_{i:Z_i=1} Y_i(1) \approx E[Y(1)]
  \]
  \[
  \bar{Y}_0 = \frac{1}{n_0}\sum_{i:Z_i=0} Y_i(0) \approx E[Y(0)]
  \]
- **ATE estimate**:  
  \[
  \widehat{\text{ATE}} = \bar{Y}_1 - \bar{Y}_0
  \]

From **NOTES**:  
- Randomization ensures **exchangeability**:  
  \[
  Pr[Y^a=1|Z=1] = Pr[Y^a=1|Z=0]
  \]
  This equality implies the treated and untreated groups are comparable.

---

## **4. Observational Studies: Challenges and Solutions**  
### **Challenge:**  
In observational studies, treatment assignment is **not random**.  
- Patients, doctors, or other agents decide on treatment based on factors like age, health status, or preferences.  
- These decisions may correlate with outcomes, causing **confounding**.

### **Example of Confounding:**  
- **Age** affects both:
  - Likelihood of receiving treatment (\( Z \))  
  - Potential outcomes (\( Y(1), Y(0) \))  
- Failing to adjust for age can **bias the ATE estimate**.

---

### **Solution: Conditional Unconfoundedness**  
By conditioning on covariates \( X \) (e.g., age):  
\[
(Y(1), Y(0)) \perp Z \mid X
\]

This assumption allows the observational study to be treated like a **stratified randomized experiment**.

#### **Steps to Achieve Conditional Unconfoundedness:**  
1. **Stratify by confounders (e.g., age groups)**.  
2. Estimate ATE within each stratum:  
   \[
   \text{ATE}(x) = E[Y(1)-Y(0)|X=x]
   \]
3. Compute overall ATE as a weighted average:  
   \[
   \text{ATE} = \sum_x \text{ATE}(x) \cdot Pr[X=x]
   \]

From **NOTES**:  
- **Positivity Condition**:  
  \[
  Pr[Z=1|X=x] > 0 \quad \text{and} \quad Pr[Z=0|X=x] > 0
  \]
  Both treatment and control must be possible within each stratum.  

---

## **5. Understanding the Role of Independence and Correlation**  
### **Common Student Confusion:**  
- **Ignorability suggests independence between treatment and potential outcomes**, but if treatment causes the outcome, wouldn't they be correlated?  

### **Clarification:**  
- **Before treatment assignment:**  
  Potential outcomes are independent of the decision to treat.  
- **After assignment:**  
  The observed outcome \( Y \) is a function of both \( Z \) and the potential outcomes:  
  \[
  Y = Z \cdot Y(1) + (1-Z) \cdot Y(0)
  \]

From **NOTES**:  
- **Covariance formula under ignorability:**  
  \[
  \text{Cov}(Z, Y) = Pr(Z=1)Pr(Z=0)[E[Y(1)] - E[Y(0)]]
  \]
- **Implication:**  
  - If ATE ≠ 0, there will be a correlation between \( Z \) and \( Y \) in the data.  
  - Ignorability pertains to potential outcomes, **not the observed outcome**.

---

## **6. Bridging Randomized and Observational Studies**  
### **Randomized Experiments:**  
- **Known assignment mechanism** ensures confidence in causal estimates.  

### **Observational Studies:**  
- Require **stronger assumptions** (e.g., no unmeasured confounders).  
- **Cannot be empirically tested** without additional assumptions.  

#### **Key Bridge:**  
If **within levels of covariates** treatment assignment is effectively random:  
\[
(Y(1), Y(0)) \perp Z \mid X
\]
Then the observational study can **mimic a stratified randomized experiment**.

From **NOTES**:  
- **Inverse Probability Weighting (IPW)**:  
  Reweights individuals to balance covariates across treatment groups.  
- **Matching**:  
  Pairs treated units with similar untreated units based on covariates.  

---

## **7. Practical Implications and Limitations**  
### **Advantages of Randomized Experiments:**  
✅ Transparent assignment mechanism.  
✅ Reliable causal estimates with minimal assumptions.  

### **Challenges in Observational Studies:**  
⚠️ Identifying all relevant confounders can be difficult.  
⚠️ Positivity violations (e.g., no older patients receive treatment) limit generalizability.  
⚠️ **Residual confounding** may bias results even after adjustments.  

---

## **8. Summary of Key Conditions for Causal Inference**  

| **Condition** | **Description** | **Formula/Notation** |
|---------------|-----------------|----------------------|
| **Consistency** | Potential outcomes match observed outcomes under treatment assignment. | \( Y = Y(Z) \) |
| **Unconfoundedness (Ignorability)** | Treatment assignment independent of potential outcomes given covariates. | \( (Y(1), Y(0)) \perp Z \mid X \) |
| **Positivity** | Every individual has a nonzero probability of receiving treatment/control. | \( Pr[Z=z|X=x] > 0 \) |
| **Exchangeability** | Treated and untreated groups are comparable. | \( Pr[Y^a=1|Z=1] = Pr[Y^a=1|Z=0] \) |

---

## **9. Next Steps**  
Upcoming lessons will explore:  
- **Identification and estimation of treatment effects** in more detail.  
- **Addressing violations of unconfoundedness** through instrumental variables and sensitivity analyses.  
- **Handling multiple confounders** and complex treatment structures.  

---

## **Conclusion**  
To make valid causal inferences:  
- **Randomized experiments** naturally satisfy key assumptions.  
- **Observational studies** require careful adjustments and stronger assumptions.  
- **Conditional unconfoundedness** serves as a bridge between these study designs, enabling causal inference under the right conditions.  

From **NOTES**:  
- Conditioning on covariates, using DAGs to identify confounders, and applying techniques like IPW and matching are critical to credible causal claims in observational research.

---

## Module 4

**Title:**  
**Randomized Experiments and Randomization-Based Inference for Estimating Causal Effects**

---

## **Detailed Summary of Concepts and Equations**

This module focuses on **randomized experiments** as the foundation for causal inference and explores **randomization-based inference** for testing and estimating treatment effects. The key components include understanding different randomization designs, calculating unbiased estimates of treatment effects, testing null hypotheses using randomization distributions, and discussing practical considerations for large samples.

---

## **1. Introduction to Randomized Experiments**  
Randomized experiments provide a **gold standard** for causal inference. By randomly assigning units to treatment and control groups, **confounding is eliminated** on average, ensuring that treatment assignment is **unconfounded** (or **strongly ignorable**) given the covariates.

### **Key Notation:**  
- \( i = 1, 2, \ldots, n \): Units in the study  
- \( Z_i \in \{0, 1\} \): Treatment assignment (1 = treated, 0 = control)  
- \( X_i \): Covariates for unit \( i \)  
- \( Y_i(0), Y_i(1) \): Potential outcomes under control and treatment  
- \( Y_i = Z_i Y_i(1) + (1 - Z_i)Y_i(0) \): Observed outcome  
- **Propensity score**: \( e(X_i) = P(Z_i=1 | X_i) \)

---

## **2. Types of Randomized Experiments**

### **2.1 Bernoulli Randomized Experiment:**  
- Each subject is independently assigned to treatment with probability \(\lambda\).  
- **Propensity score**: \( e(X_i) = \lambda \), same for all units, independent of covariates.  
- **Assignment probability**:  
  \[
  P(Z) = \lambda^{\sum Z_i} (1-\lambda)^{n - \sum Z_i}
  \]

---

### **2.2 Completely Randomized Experiment (CRE):**  
- Exactly \( n_1 \) units receive treatment, \( n_0 = n - n_1 \) receive control.  
- **Assignment probability**:  
  \[
  P(Z) = \frac{1}{{n \choose n_1}}
  \]
- **Propensity score**: \( e(X_i) = \frac{n_1}{n} \), constant for all units.  

---

### **2.3 Randomized Block Experiment:**  
- Subjects are grouped into **strata** based on covariates.  
- Within each stratum \( s \):  
  - \( n_s \): number of units  
  - \( n_{s1} \): treated units  
  - **Assignment probability** within stratum:  
    \[
    P(Z_s) = \frac{1}{{n_s \choose n_{s1}}}
    \]
  - **Propensity score**: \( e(X_i) = \frac{n_{s1}}{n_s} \), now dependent on covariates.  

---

### **2.4 Paired Randomized Experiment:**  
- Special case of block randomization with \( n_s=2 \).  
- Each pair has one treated and one control unit.  
- **Connection to matched-pairs t-test:** Equivalent to classical matched-pair analysis.  

---

## **3. Randomization-Based Inference**

### **3.1 Key Ideas:**  
- **Potential outcomes** are **fixed constants**.  
- **Randomness** stems solely from the treatment assignment mechanism.  
- Inference focuses on the **randomization distribution** under the null hypothesis.  

### **3.2 Null Hypotheses:**  
- **Sharp null of no effect**: \( Y_i(1) = Y_i(0) \ \forall i \).  
- **Constant treatment effect**: \( Y_i(1) = Y_i(0) + \tau \ \forall i \).  

### **3.3 Testing Procedure:**  
1. **Choose a test statistic** \( T(Z, Y) \) (e.g., difference in means).  
2. **Calculate observed test statistic** from actual assignment.  
3. **Enumerate/simulate all possible assignments** \( Z' \in \Omega \).  
4. **Compute p-value**:  
   \[
   p = P(T(Z') \geq T_{\text{obs}}) = \frac{\#\{Z': T(Z') \geq T_{\text{obs}}\}}{|\Omega|}
   \]

---

### **3.4 Examples of Test Statistics:**  
- **Difference in Means:**  
  \[
  T(Z, Y) = \bar{Y}_1 - \bar{Y}_0
  \]
- **Rank-Based Tests:**  
  - **Wilcoxon Rank-Sum Test**: Uses ranks of outcomes to reduce sensitivity to outliers.  
  - **Median Test**: Counts how many treated units exceed the overall median.  

- **Binary Outcomes:**  
  - **McNemar’s Test**: For paired binary data.  
- **Continuous Outcomes with Pairs:**  
  - **Wilcoxon Signed-Rank Test**: For paired continuous outcomes.  

---

## **4. Estimating the Sample Average Treatment Effect (SATE)**

### **4.1 SATE Definition:**  
\[
\text{SATE} = \frac{1}{n} \sum_{i=1}^n [Y_i(1) - Y_i(0)]
\]

### **4.2 Estimator:**  
\[
\widehat{\text{SATE}} = \bar{Y}_1 - \bar{Y}_0 = \frac{1}{n_1}\sum_{i:Z_i=1}Y_i - \frac{1}{n_0}\sum_{i:Z_i=0}Y_i
\]

- **Unbiasedness**:  
  Under a completely randomized experiment:  
  \[
  E[\widehat{\text{SATE}}] = \text{SATE}
  \]
- **Randomization ensures that the assignment mechanism yields an unbiased estimator.**

---

### **4.3 Variance of the Estimator:**  
\[
\text{Var}(\bar{Y}_1 - \bar{Y}_0) = \frac{\sigma_1^2}{n_1} + \frac{\sigma_0^2}{n_0} - \frac{\sigma_{\Delta}^2}{n}
\]

- \(\sigma_1^2\): Variance of treated potential outcomes.  
- \(\sigma_0^2\): Variance of control potential outcomes.  
- \(\sigma_{\Delta}^2\): Variance of unit treatment effects.  

**Challenge:** The third term is unobservable because we only see one potential outcome per unit.  

---

### **4.4 Conservative Variance Estimator:**  
Use sample variances:  
\[
\widehat{\text{Var}}(\bar{Y}_1 - \bar{Y}_0) = \frac{s_1^2}{n_1} + \frac{s_0^2}{n_0}
\]

- **Conservative** but **unbiased** when treatment effects are constant.  
- **Confidence Interval:**  
  \[
  \widehat{\text{SATE}} \pm z_{\alpha/2} \sqrt{\widehat{\text{Var}}(\bar{Y}_1 - \bar{Y}_0)}
  \]

---

## **5. Randomization-Based Confidence Intervals**

### **5.1 Constant Treatment Effect Hypothesis:**  
- Null: \( Y_i(1) - Y_i(0) = \tau \) for all \( i \).  
- Vary \(\tau\) and identify values not rejected at level \(\alpha\) to form a CI.  

---

## **6. Practical Considerations**

### **6.1 Computational Issues:**  
- Enumerating all assignments is **infeasible** for large \( n \).  
  - \( n = 500 \) with \( n_1 = 250 \) leads to \( {500 \choose 250} > 10^{149} \) possibilities.  

### **6.2 Solutions:**  
- **Monte Carlo Sampling:**  
  Randomly sample assignments to approximate p-values.  
- **Normal Approximation:**  
  Use asymptotic distributions for large samples.  

---

## **7. Advantages and Limitations of Randomization-Based Inference**

### ✅ **Advantages:**  
- Minimal assumptions (no distributional assumptions on outcomes).  
- Strong internal validity.  
- Intuitive and grounded in the experimental design.  

### ⚠️ **Limitations:**  
- **Heterogeneity of treatment effects**: Hard to capture under sharp null assumptions.  
- **Generalizability**: Focused on internal validity; external validity requires more assumptions.  
- **Computationally demanding** for large experiments.  

---

## **8. Extensions and Notes**

### **From NOTES:**  
- **Propensity Score (Rosenbaum & Rubin, 1983):**  
  Balances covariates across treatment groups.  
  \[
  e(X) = P(Z=1 | X)
  \]
  Essential for observational studies but less critical in well-randomized experiments.  

- **Stable Unit Treatment Value Assumption (SUTVA):**  
  Assumes no interference between units and well-defined treatments.  

- **Covariate Adjustment:**  
  Improves precision by accounting for pre-treatment covariates.  

- **Blocking and Pairing:**  
  Reduces variance of estimates, especially with strong covariate-outcome relationships.  

- **Heterogeneous Effects:**  
  Estimation beyond average effects (e.g., quantiles or variance of treatment effects) requires advanced methods.  

---

## **9. Conclusion and Next Steps**

Randomized experiments serve as the **benchmark** for causal inference, providing **unbiased** and **consistent** estimates of treatment effects when properly designed. **Randomization-based inference** leverages the known assignment mechanism to make valid inferences without strong distributional assumptions.  

Upcoming modules will explore:  
- **Extending methods to observational studies** using propensity scores.  
- **Addressing treatment effect heterogeneity**.  
- **Advanced estimation techniques** for finite and infinite populations.  

Understanding these foundations ensures that causal claims are both credible and scientifically rigorous.

## Module 5
**Title:**  
**Estimating the Finite Population Average Treatment Effect (FATE) and Average Treatment Effect (ATE): Randomization and Regression Approaches**

---

## **Detailed Summary of Concepts and Equations**

This lesson explores how to **estimate causal effects**—particularly the **Finite Population Average Treatment Effect (FATE)** and the **Average Treatment Effect (ATE)**—using randomization-based inference and regression approaches. It highlights differences between randomized experiments and observational studies, emphasizing the importance of the assignment mechanism and how covariates impact estimation.

---

## **1. Key Concepts and Notation**  

### **1.1 Potential Outcomes Framework**  
- **Units:** \( i = 1, 2, \dots, n \) drawn from a population of size \( N \).  
- **Treatment Assignment:**  
  - \( Z_i = 1 \): unit \( i \) receives treatment.  
  - \( Z_i = 0 \): unit \( i \) is in control.  
- **Potential Outcomes:**  
  - \( Y_i(1) \): outcome if treated.  
  - \( Y_i(0) \): outcome if untreated.  
  - **Observed outcome:** \( Y_i = Z_i Y_i(1) + (1 - Z_i) Y_i(0) \).  

---

### **1.2 Treatment Effects**  
- **Unit-level Treatment Effect:**  
  \[
  \tau_i = Y_i(1) - Y_i(0)
  \]
- **Sample Average Treatment Effect (SATE):**  
  \[
  \text{SATE} = \frac{1}{n}\sum_{i=1}^n \tau_i
  \]
- **Finite Population Average Treatment Effect (FATE):**  
  \[
  \text{FATE} = \frac{1}{N}\sum_{i=1}^N \tau_i
  \]
- **Population Average Treatment Effect (ATE):**  
  \[
  \text{ATE} = \mathbb{E}[Y(1) - Y(0)]
  \]

---

## **2. Estimating FATE with Randomization-Based Inference**  

### **2.1 Randomness Sources:**  
- **Random assignment** of treatments to \( n \) units.  
- **Random sampling** of \( n \) units from population of size \( N \).  

### **2.2 Estimator for FATE:**  
Use the **difference in sample means**:  
\[
\widehat{\text{FATE}} = \bar{Y}_1 - \bar{Y}_0 = \frac{1}{n_1}\sum_{i:Z_i=1}Y_i - \frac{1}{n_0}\sum_{i:Z_i=0}Y_i
\]
- **Unbiasedness:**  
  \[
  \mathbb{E}[\widehat{\text{FATE}}] = \text{FATE}
  \]

---

### **2.3 Variance of the Estimator:**  
\[
\text{Var}(\widehat{\text{FATE}}) = \frac{\sigma_1^2}{n_1} + \frac{\sigma_0^2}{n_0} - \frac{\sigma_{\tau}^2}{n}
\]
- \(\sigma_1^2\), \(\sigma_0^2\): variances of potential outcomes under treatment and control.  
- \(\sigma_{\tau}^2\): variance of unit-level treatment effects.  
- If treatment effects are constant, \(\sigma_{\tau}^2 = 0\).

---

### **2.4 Hypothesis Testing and Confidence Intervals:**  
- **Null Hypothesis (no treatment effect):** \(\text{FATE} = 0\)  
- **Test Statistic:**  
  \[
  Z = \frac{\widehat{\text{FATE}}}{\sqrt{\widehat{\text{Var}}(\widehat{\text{FATE}})}}
  \]
- **Confidence Interval:**  
  \[
  \widehat{\text{FATE}} \pm z_{\alpha/2} \sqrt{\widehat{\text{Var}}(\widehat{\text{FATE}})}
  \]

---

## **3. Model-Based Inference for ATE**  

### **3.1 Transition to Infinite Population ATE**  
Instead of treating potential outcomes as fixed constants, **model-based inference** assumes:  
\[
Y_i(z) \sim \text{i.i.d. with } \mathbb{E}[Y_i(z)] = \mu_z \quad \text{for } z \in \{0,1\}.
\]
- **ATE definition:**  
  \[
  \text{ATE} = \mu_1 - \mu_0
  \]

---

### **3.2 Independence and Unconfoundedness**  
- **Unconfoundedness assumption:**  
  \[
  (Y_i(0), Y_i(1)) \perp Z_i \mid X_i
  \]
- In a **randomized experiment**, this holds by design.  
- In an **observational study**, must be justified by measured covariates.  

---

## **4. Regression Approach to Estimating ATE**  

### **4.1 Basic Regression Model:**  
\[
Y_i = \alpha + \tau Z_i + \varepsilon_i
\]
- \(\alpha\): average outcome under control.  
- \(\tau\): treatment effect.  
- OLS estimator:  
  \[
  \widehat{\tau} = \bar{Y}_1 - \bar{Y}_0
  \]

---

### **4.2 Regression with Covariates:**  
Incorporate covariates \( X_i \):  
\[
Y_i = \alpha + \tau Z_i + \beta'X_i + \varepsilon_i
\]
- Reduces variance of \(\widehat{\tau}\).  
- **Unbiasedness condition:** Covariates must be independent of treatment assignment.  

---

### **4.3 Variance and Efficiency Gains:**  
- **Without covariates:** \(\widehat{\tau}\) is unbiased but less efficient.  
- **With covariates:** Variance reduction:  
  \[
  \text{Var}(\widehat{\tau}_{\text{with } X}) \leq \text{Var}(\widehat{\tau}_{\text{without } X})
  \]

---

## **5. Comparing Randomized Experiments and Observational Studies**  

| **Feature** | **Randomized Experiments** | **Observational Studies** |
|-------------|----------------------------|---------------------------|
| Assignment | Random | Self-selected |
| Unconfoundedness | By design | Must be assumed/tested |
| Bias Risk | Low | High (without proper adjustment) |
| Estimation | Straightforward | Requires covariate control |

---

## **6. Stratified and Block Randomization**  

### **6.1 Stratified Estimation:**  
Within each stratum \( s \):  
\[
\widehat{\tau}_s = \bar{Y}_{1,s} - \bar{Y}_{0,s}
\]
- Overall estimate:  
  \[
  \widehat{\text{ATE}} = \sum_{s=1}^S w_s \widehat{\tau}_s \quad \text{with } w_s = \frac{n_s}{n}.
  \]

---

### **6.2 Equivalence in Observational Studies:**  
If **treatment assignment is unconfounded within strata**, stratification in observational studies can mimic block randomization.  

---

## **7. Practical Considerations**  

### **7.1 Variance Estimation Challenges:**  
- Unknown unit-level effects make variance estimation challenging.  
- Conservative estimators are used for inference.  

### **7.2 Model Misspecification:**  
- In **observational studies**, incorrect covariate modeling can bias results.  
- Important to include relevant covariates and consider flexible models.  

---

## **8. Insights from the NOTES**  

- **Propensity Scores (Rosenbaum & Rubin, 1983):**  
  \[
  e(X_i) = P(Z_i = 1 \mid X_i)
  \]
  Balances covariates between groups, crucial in observational studies.  

- **SUTVA (Stable Unit Treatment Value Assumption):**  
  Ensures that each unit’s outcome depends only on its own treatment.  

- **Regression Adjustments:**  
  - Improve efficiency in randomized trials.  
  - Crucial for bias reduction in observational studies.  

- **Bias Sources:**  
  - Covariate imbalance leads to biased \(\widehat{\tau}\) in observational data.  
  - Unmeasured confounders can invalidate causal claims.  

---

## **9. Conclusion and Next Steps**  

Estimating the **FATE** and **ATE** involves careful consideration of the assignment mechanism, sampling design, and covariate balance. While randomized experiments provide clean identification of causal effects, **observational studies require assumptions** like **unconfoundedness** and **covariate adjustment** to ensure unbiased estimates.  

Future lessons will explore:  
- **Advanced propensity score methods** (matching, weighting).  
- **Sensitivity analysis** for unmeasured confounding.  
- **Machine learning approaches** to treatment effect estimation.

## Module 6
# **Title:**  
**The Propensity Score: Estimation and Application in Causal Inference**

---

## **Detailed Summary of Concepts and Equations**

This lesson focuses on the **propensity score**, a fundamental concept in causal inference, especially for **observational studies** where randomization is not possible. The **propensity score**, introduced by Rosenbaum and Rubin (1983), serves as a tool to **balance covariates** between treated and control groups, reducing bias in estimating the **Average Treatment Effect (ATE)** and the **Average Treatment Effect on the Treated (ATT)**.

---

## **1. Background and Motivation**

### **1.1 Challenges in Observational Studies**  
- Unlike randomized experiments, observational studies often have **imbalanced covariates** between treatment and control groups, causing **confounding bias**.
- The **difference in means** between groups does **not provide an unbiased estimate** of the treatment effect unless covariates are balanced.

### **1.2 Approaches to Address Confounding**  
1. **Model the Outcome (Regression Adjustment):**  
   - Regression on covariates and treatment assignment.  
   - **Limitation:** Misspecification leads to biased estimates.  
2. **Balance Covariates (Matching or Stratification):**  
   - Direct matching on covariates is challenging due to **curse of dimensionality**.  
3. **Use the Propensity Score (Preferred):**  
   - Reduces a **multi-dimensional problem to a single scalar** value.  
   - Facilitates **matching, weighting, and stratification**.  

---

## **2. Definition and Properties of the Propensity Score**

### **2.1 Definition**  
The **propensity score** \( e(X) \) is the probability of receiving treatment given covariates \( X \):
\[
e(X) = P(Z=1 \mid X)
\]
Where:
- \( Z \in \{0,1\} \): treatment assignment indicator.  
- \( X \): vector of observed covariates.  

### **2.2 Key Properties**  
**1. Balancing Property:**  
Given the propensity score, the distribution of covariates is **independent of treatment assignment**:
\[
Z \perp X \mid e(X)
\]
> Units with the **same propensity score** have **balanced covariates** regardless of treatment assignment.  

**2. Unconfoundedness with the Propensity Score:**  
If treatment assignment is **unconfounded** given \( X \), it is also unconfounded given \( e(X) \):
\[
(Y(0), Y(1)) \perp Z \mid e(X)
\]
> Allows us to **control for confounding** by adjusting for the propensity score rather than the full covariate vector.  

**3. Overlap (Positivity):**  
\[
0 < e(X) < 1 \quad \forall X
\]
> Ensures that **each unit has a chance** of being both treated and untreated.  

---

## **3. Methods of Using the Propensity Score**

### **3.1 Regression Adjustment on the Propensity Score**  
- **Model:**  
  \[
  Y_i = \alpha + \tau Z_i + \beta e(X_i) + \varepsilon_i
  \]
- **Advantage:** Reduces dimensionality; improves efficiency.  
- **Limitation:** Requires correct specification of both the propensity score and outcome models.

---

### **3.2 Subclassification (Stratification) on the Propensity Score**  

#### **Steps:**  
1. Estimate the propensity score \( \hat{e}(X) \) for each unit.  
2. Divide the sample into \( S \) **strata** (often 5-10) based on quantiles of \( \hat{e}(X) \).  
3. Within each stratum \( s \), compute:  
   \[
   \hat{\tau}_s = \bar{Y}_{1,s} - \bar{Y}_{0,s}
   \]
4. Estimate the ATE by weighting each stratum’s estimate by the proportion of units:  
   \[
   \widehat{\text{ATE}} = \sum_{s=1}^S \frac{n_s}{n} \hat{\tau}_s
   \]

#### **Bias-Variance Trade-Off:**  
- **More strata:** Reduces bias but increases variance.  
- **Fewer strata:** Reduces variance but increases bias.  

> **Common practice:** Use **5 strata**, which often removes **>90% of the bias**.

---

### **3.3 Inverse Probability of Treatment Weighting (IPTW)**  

#### **Idea:**  
Reweight units to **create a pseudo-population** in which treatment assignment is independent of covariates.

#### **Weights:**  
- For treated units:  
  \[
  w_i = \frac{1}{\hat{e}(X_i)}
  \]
- For control units:  
  \[
  w_i = \frac{1}{1 - \hat{e}(X_i)}
  \]

#### **ATE Estimator:**  
\[
\widehat{\text{ATE}} = \frac{1}{n}\sum_{i=1}^n \left( \frac{Z_i Y_i}{\hat{e}(X_i)} - \frac{(1 - Z_i)Y_i}{1 - \hat{e}(X_i)} \right)
\]

#### **Properties:**  
- **Unbiased** if the propensity score model is correct.  
- **Issue:** Extreme weights when \( \hat{e}(X_i) \) is close to 0 or 1.  

> **Solution:**  
- **Trim sample** to exclude units with extreme propensity scores.  
- **Stabilize weights:**  
  \[
  w_i^{\text{stabilized}} = \frac{Z_i P(Z=1)}{\hat{e}(X_i)} + \frac{(1 - Z_i) P(Z=0)}{1 - \hat{e}(X_i)}
  \]

---

### **3.4 Matching on the Propensity Score**  

#### **Procedure:**  
- Pair each treated unit with control units having **similar propensity scores**.  
- Estimate treatment effect as the **average difference in matched pairs**.  

#### **Matching Methods:**  
- **Nearest neighbor matching**  
- **Caliper matching** (limits distance between matched pairs)  
- **Kernel matching** (weights multiple controls for each treated unit)  

#### **Advantages:**  
- Improves covariate balance.  
- Reduces model dependence.  

---

## **4. Addressing Practical Issues**

### **4.1 Insufficient Overlap and Common Support**  
- **Problem:** Lack of treated units at certain covariate values.  
- **Solution:**  
  - **Trim samples** outside overlapping regions.  
  - **Focus on the region of common support**.

---

### **4.2 Model Misspecification of the Propensity Score**  
- **Impact:** Bias in the estimated treatment effect.  
- **Solutions:**  
  - Include **interaction terms** and **higher-order terms** in the propensity score model.  
  - Use **machine learning methods** (e.g., random forests, gradient boosting) for flexible modeling.  

---

### **4.3 Double Robustness**  
- **Property:** If **either** the propensity score model **or** the outcome model is correctly specified, the estimator is **consistent**.  
- **Double Robust Estimator:**  
  Combines regression adjustment with weighting.  

#### **Equation:**  
\[
\widehat{\text{ATE}}_{\text{DR}} = \frac{1}{n}\sum_{i=1}^n \left( \frac{Z_i (Y_i - \hat{m}_1(X_i))}{\hat{e}(X_i)} + \hat{m}_1(X_i) - \frac{(1 - Z_i)(Y_i - \hat{m}_0(X_i))}{1 - \hat{e}(X_i)} - \hat{m}_0(X_i) \right)
\]
Where:
- \( \hat{m}_1(X) \), \( \hat{m}_0(X) \): predicted outcomes under treatment/control.  

---

## **5. Applications of the Propensity Score**

### **5.1 Estimating the Effect of Treatment on the Treated (ATT)**  
\[
\widehat{\text{ATT}} = \frac{1}{n_1}\sum_{i:Z_i=1} \left( Y_i - \frac{\hat{e}(X_i)}{1 - \hat{e}(X_i)} \sum_{j:Z_j=0} w_j Y_j \right)
\]
- **Focuses on treated population**; used in policy evaluation.

---

### **5.2 Longitudinal Causal Inference**  
- **Extension:** Estimate effects over time (e.g., repeated treatments).  
- **Inverse Probability of Treatment Weighting (IPTW)** is central to longitudinal models.  

---

## **6. Insights from NOTES**  

- **Strong Ignorability:**  
  Treatment assignment is unconfounded given covariates and the propensity score ensures overlap.  

- **Balancing Score Hierarchy:**  
  - **Propensity score:** Coarsest balancing score.  
  - **Exact covariate matching:** Finer but suffers from dimensionality.  

- **Trade-offs:**  
  - **Subclassification:** Easy but introduces bias with few strata.  
  - **Weighting:** Theoretically superior but sensitive to extreme scores.  
  - **Matching:** Intuitive but sample size reduction possible.  

- **Common Practices:**  
  - **5-10 strata** in subclassification.  
  - **Trimming thresholds** at 0.1 and 0.9 for propensity scores.  
  - **Stabilized weights** to improve finite sample performance.  

---

## **7. Conclusion and Next Steps**

The **propensity score** provides a versatile tool to adjust for confounding in observational studies. By balancing covariates, it allows for less biased estimates of causal effects through methods like **regression adjustment, subclassification, weighting, and matching**.

While **subclassification** offers simplicity, **weighting** provides theoretical advantages. Yet, practical issues like **model misspecification** and **insufficient overlap** must be addressed. Methods like **double robust estimation** ensure consistency even if one model is misspecified.

---

## **Next Modules Will Cover:**  
- **Advanced matching techniques** and trimming strategies.  
- **Machine learning approaches** to estimate the propensity score.  
- **Sensitivity analysis** for unobserved confounding.  
- **Longitudinal causal inference methods** using inverse probability weighting.

## Module 7
# **Title:**  
**Matching Methods in Causal Inference: Concepts, Techniques, and Practical Considerations**

---

## **Detailed Summary of Concepts and Equations**

This module focuses on **matching methods** for estimating **causal effects** in observational studies, building on prior discussions of **propensity scores** and **subclassification**. Matching aims to create a **balanced comparison group** where the distribution of covariates is similar between treated and control units, mimicking a randomized experiment.

---

## **1. Introduction to Matching**

### **1.1 Motivation and Goals**  
- **Goal:** Reduce confounding bias by pairing treated and untreated units with similar covariate profiles.  
- **Approach:** Create matched samples where the covariate distributions are balanced between groups.  
- **Focus:** Estimating the **Average Treatment Effect on the Treated (ATT)**, though methods apply to the **Average Treatment Effect (ATE)** and the **Average Treatment Effect on the Untreated (ATU)**.

---

## **2. Types of Matching Methods**

### **2.1 Exact Matching**  
- Matches units with **identical covariate values**.  
- **Limitation:** Rarely feasible with continuous covariates or many confounders due to the **curse of dimensionality**.  

---

### **2.2 Approximate Matching**  
Uses **distance metrics** to match treated units with the closest control units:

#### **2.2.1 Euclidean Distance**  
\[
d(i, i') = \sqrt{\sum_{k=1}^{K}(X_{ik} - X_{i'k})^2}
\]
- Simple but ignores scale differences between covariates.  

#### **2.2.2 Mahalanobis Distance**  
\[
d_M(i, i') = \sqrt{(X_i - X_{i'})^\top S^{-1}(X_i - X_{i'})}
\]
- Accounts for **covariate correlations** and **scales** (preferred over Euclidean distance).  
- \( S \): Covariance matrix of covariates.  

#### **2.2.3 Propensity Score Matching (PSM)**  
- Matches on the estimated **propensity score**:  
  \[
  e(X) = P(Z=1 \mid X)
  \]
- **Advantage:** Reduces high-dimensional covariates to a **single scalar**, facilitating easier matching.  
- **Distances used:**  
  - **Absolute difference:** \( | \hat{e}(X_i) - \hat{e}(X_j) | \)  
  - **Logit difference:** \( | \logit(\hat{e}(X_i)) - \logit(\hat{e}(X_j)) | \)  

---

## **3. Matching Strategies**

### **3.1 One-to-One Matching**  
- Each treated unit is paired with **one control unit**.  
- **With Replacement:** Controls can be reused; ensures better matches but may reduce sample variance efficiency.  
- **Without Replacement:** Controls used only once; ordering of matches matters.  

### **3.2 One-to-Many Matching**  
- Each treated unit matched to **multiple control units** (e.g., 1:2, 1:5 matching).  
- **Benefit:** Reduces variance but may increase bias if matches are less similar.  

### **3.3 Caliper Matching**  
- Matches only when the propensity score difference is within a **specified threshold (caliper)**.  
- **Prevents poor matches**; improves balance at the expense of discarding some treated units.  

### **3.4 Nearest Neighbor Matching**  
- Matches each treated unit to the **closest control unit** based on distance metrics.  
- Can be combined with **calipers** and **replacement options**.  

### **3.5 Genetic and Optimal Matching**  
- **Genetic Matching:** Uses evolutionary algorithms to find matches with the best covariate balance.  
- **Optimal Matching:** Minimizes overall distances between treated and control units, ensuring global balance.  

---

## **4. Assessing Covariate Balance**

### **4.1 Importance of Balance Checking**  
- Successful matching should yield **similar covariate distributions** between groups.  
- **Balance should be assessed without using outcome data** to avoid bias.  

### **4.2 Measures of Balance**  

#### **4.2.1 Standardized Mean Difference (SMD)**  
\[
\text{SMD} = \frac{\bar{X}_1 - \bar{X}_0}{\sqrt{\frac{s_1^2 + s_0^2}{2}}}
\]
- **Goal:** SMD < 0.1 for acceptable balance.  

#### **4.2.2 Mahalanobis Distance**  
- Measures **overall balance** across all covariates simultaneously.  

#### **4.2.3 Visual Tools**  
- **Love plots** and **histograms** of propensity scores before and after matching.  

---

## **5. Estimating Treatment Effects After Matching**

### **5.1 ATT Estimator**  
For **one-to-one matching**:  
\[
\widehat{\text{ATT}} = \frac{1}{n_1} \sum_{i=1}^{n_1} (Y_{i1} - \bar{Y}_{i2})
\]
- \( Y_{i1} \): Outcome for treated unit \( i \)  
- \( \bar{Y}_{i2} \): Average outcome of matched controls  

### **5.2 Bias Considerations**  
- Perfect matching: **No bias** in treatment effect estimates.  
- Imperfect matching: Bias arises from **covariate differences** between matched units.  

> **Regression Adjustment:**  
- Combine matching with **regression on covariates** to correct residual imbalance.  

---

## **6. Variance and Standard Error Estimation**

### **6.1 Variance Estimation Challenges**  
- Matching induces **dependence** among matched pairs.  
- **Bootstrapping** often fails due to non-independence of matched samples.  

### **6.2 Variance Estimators (Abadie & Imbens Method)**  
For ATT with **one-to-one matching without replacement**:  
\[
\widehat{\text{Var}}(\widehat{\text{ATT}}) = \frac{1}{n_1^2} \sum_{i=1}^{n_1} (Y_{i1} - \bar{Y}_{i2} - \widehat{\text{ATT}})^2
\]

For **one-to-many matching** or **matching with replacement**:  
- **Adjusted variance estimators** incorporate reuse of control units and matching weights.  

---

## **7. Practical Considerations and Issues**

### **7.1 Overlap and Common Support**  
- Poor overlap leads to **unreliable estimates**.  
- **Solution:** Trim observations with **extreme propensity scores**.  

### **7.2 Caliper Selection**  
- Too narrow: High-quality matches but many units discarded.  
- Too wide: Poor matches, increased bias.  

### **7.3 Matching with Categorical and Ordinal Covariates**  
- **Exact matching** often used for **categorical covariates** (e.g., gender, race).  
- **Ordinal variables:** Treat as continuous or collapse into fewer categories.  

### **7.4 Matching Quality and Model Re-estimation**  
- If balance is inadequate:  
  - Re-specify the **propensity score model** with higher-order terms and interactions.  
  - **Re-match** and reassess balance.  

---

## **8. Advanced Matching Techniques**

### **8.1 Genetic Matching**  
- Uses machine learning to **automatically optimize covariate balance**.  
- Iteratively adjusts weights to minimize imbalance.  

### **8.2 Cardinality and Optimal Subset Matching**  
- Finds **largest possible matched subset** with acceptable balance.  
- Prioritizes **balance over sample size**.  

---

## **9. Insights from NOTES**

- **Propensity scores serve as a balancing score:** Matching based on them ensures balanced covariate distributions.  
- **Iterative process:** Model adjustment and balance checking are crucial steps.  
- **Strong Ignorability:** Matching methods assume **no unmeasured confounding**.  
- **Bias-Variance Trade-Off:**  
  - **Fewer matches per treated unit:** Lower bias, higher variance.  
  - **More matches:** Higher bias, lower variance.  

---

## **10. Conclusion and Next Steps**

Matching is a powerful tool for causal inference, enabling the creation of comparable treatment and control groups from observational data. While **one-to-one propensity score matching** is common, methods like **genetic matching** and **optimal matching** offer improved balance. Researchers must carefully **check balance**, **adjust models**, and **select appropriate variance estimators** to ensure valid treatment effect estimates.

---

## **Upcoming Topics:**  
- **Doubly Robust Estimation:** Combining matching with regression adjustment.  
- **Sensitivity Analysis:** Assessing robustness to unobserved confounding.  
- **Advanced weighting methods** beyond propensity score weighting.

## Module 8

# **Title:**  
**Regression-Based Estimators, Double Robustness, and Machine Learning in Causal Inference**

---

## **Detailed Summary of Concepts and Equations**

This module explores **regression-based estimators** for causal inference, the principle of **double robustness**, and the application of **machine learning** to estimate treatment effects. Building on previous discussions of **propensity scores** and **matching**, this section focuses on how modeling either the **outcome regression function** or the **propensity score** (or both) can lead to **consistent** and **efficient** estimates of treatment effects.

---

## **1. Regression-Based Estimators in Causal Inference**

### **1.1 Motivation**  
- Under **unconfoundedness** (no unmeasured confounders), the **conditional expectation** of the potential outcome given covariates can be used to estimate the **Average Treatment Effect (ATE)** and the **Average Treatment Effect on the Treated (ATT)**.  
- **Imputation:**  
  - For treated units: Use observed outcomes directly.  
  - For untreated units: **Impute** potential treated outcomes using the estimated regression function.  

### **1.2 Estimating ATE via Regression**  
The ATE at covariate value \( X \) is:  
\[
\text{ATE}(X) = \mathbb{E}[Y(1) - Y(0) \mid X]
\]

To estimate the sample ATE:  
\[
\widehat{\text{ATE}} = \frac{1}{n} \sum_{i=1}^n \left(\hat{g}(X_i, 1) - \hat{g}(X_i, 0)\right)
\]

- \( \hat{g}(X, z) \): Estimated regression function for outcome given covariates \( X \) and treatment \( z \).  
- Even with correct unconfoundedness, **misspecification** of the regression model can cause **bias**.  

---

## **2. Inverse Probability Weighting (IPW) and Its Limitations**

### **2.1 Recap of IPW**  
- Uses the **propensity score** \( e(X) = P(Z=1 \mid X) \) to reweight observations.  
- **IPW Estimator for ATE:**  
\[
\widehat{\text{ATE}}_{\text{IPW}} = \frac{1}{n} \sum_{i=1}^n \left( \frac{Z_i Y_i}{\hat{e}(X_i)} - \frac{(1 - Z_i) Y_i}{1 - \hat{e}(X_i)} \right)
\]

- **Issue:** If the propensity score model is **misspecified**, the estimator becomes biased.  

---

## **3. Double Robustness (DR)**

### **3.1 Concept of Double Robustness**  
- An estimator is **doubly robust** if it remains **consistent** if **either** the **propensity score model** or the **outcome regression model** is correctly specified (but not necessarily both).  
- If **both models** are correct, the estimator is **efficient** and achieves the lowest variance.  

### **3.2 The Doubly Robust (DR) Estimator**  
The DR estimator for ATE:  
\[
\widehat{\text{ATE}}_{\text{DR}} = \frac{1}{n} \sum_{i=1}^n \left[ \hat{g}(X_i, 1) - \hat{g}(X_i, 0) + \frac{Z_i(Y_i - \hat{g}(X_i, 1))}{\hat{e}(X_i)} - \frac{(1 - Z_i)(Y_i - \hat{g}(X_i, 0))}{1 - \hat{e}(X_i)} \right]
\]

#### **Explanation of Terms:**  
- \(\hat{g}(X_i, z)\): Predicted outcome from the regression model.  
- \(\hat{e}(X_i)\): Estimated propensity score.  
- Residuals \((Y_i - \hat{g}(X_i, z))\) adjust for model misspecification.  

---

## **4. Properties and Intuition Behind Double Robustness**

### **4.1 Why Double Robustness Works**  
- If the **propensity score is correct**, the **IPW component** ensures consistency.  
- If the **outcome regression is correct**, the **regression component** ensures consistency.  
- **Residual adjustment** corrects for potential bias from one misspecified model.  

### **4.2 Efficiency Gains**  
- When **both models are correct**, the DR estimator achieves the **semiparametric efficiency bound**.  
- Offers **lower variance** compared to using just regression or IPW alone.  

---

## **5. Machine Learning for Treatment Effect Estimation**

### **5.1 Motivation for Machine Learning**  
- Traditional regression models (linear, logistic) can be **too restrictive**.  
- Machine learning methods can capture **nonlinear relationships** and **complex interactions**.  

### **5.2 Common Methods:**  
- **Bayesian Additive Regression Trees (BART):** Flexible modeling of the outcome function.  
- **Random Forests & Gradient Boosting:** Nonparametric estimators for both propensity scores and regression functions.  
- **Super Learner:** An ensemble of algorithms that combines multiple models to minimize prediction error.  

---

## **6. Doubly Debiased Machine Learning (DML)**

### **6.1 Motivation for DML**  
- Naive use of machine learning may introduce **regularization bias**.  
- **DML** approach adjusts for this bias to ensure **valid causal estimates**.  

### **6.2 DML Procedure:**  
1. **Sample Splitting:**  
   - Divide data into two groups: Train models on one half, estimate treatment effect on the other.  
2. **Estimate Regression & Propensity Models:**  
   - Use machine learning methods (e.g., random forests) to estimate \(\hat{g}\) and \(\hat{e}\).  
3. **Residualization:**  
   - Compute residuals:  
     \[
     \hat{U}_i = Y_i - \hat{g}(X_i, Z_i), \quad \hat{V}_i = Z_i - \hat{e}(X_i)
     \]  
4. **Treatment Effect Estimation:**  
   - Regress \(\hat{U}_i\) on \(\hat{V}_i\) to estimate the **ATE**.  

---

## **7. Practical Considerations**

### **7.1 Model Misspecification**  
- **Double robustness** mitigates but does not fully eliminate the effects of poor models.  
- Regular **balance checks** and **sensitivity analyses** are essential.  

### **7.2 Sample Splitting in DML**  
- Prevents **overfitting** and ensures **valid inference**.  
- Multiple splits and **cross-fitting** can improve stability.  

---

## **8. Variance and Standard Error Estimation**

### **8.1 Variance Formula for DR Estimator:**  
\[
\widehat{\text{Var}}(\widehat{\text{ATE}}_{\text{DR}}) = \frac{1}{n^2} \sum_{i=1}^n \left( \text{DR}_i - \widehat{\text{ATE}}_{\text{DR}} \right)^2
\]

- **Software tools:**  
  - **R:** `drtmle`, `tmle` packages.  
  - **Stata:** `teffects` with DR estimators.  
  - **SAS:** Macro implementations available.  

---

## **9. Connections to NOTES and Related Concepts**

- **Unconfoundedness:** Key assumption underlying DR estimators.  
- **Propensity Scores:** Serve as balancing scores to equate covariate distributions.  
- **Machine Learning Advances:** Enhance flexibility but require careful variance adjustment.  
- **Stability and Efficiency:** Achieved when both models are properly specified.  

---

## **10. Conclusion**

Regression-based estimators and the principle of **double robustness** provide powerful tools for causal inference. By leveraging **both** the outcome regression function and the propensity score, researchers gain protection against model misspecification. The integration of **machine learning** into this framework further improves flexibility but requires careful handling to avoid bias. **Doubly debiased machine learning (DML)** represents the state-of-the-art approach, combining **flexibility, consistency, and efficiency** in treatment effect estimation.

---

## **Next Topics:**  
- **Instrumental Variables (IV):** Addressing violations of the unconfoundedness assumption.  
- **Regression Discontinuity Designs (RDD):** Exploiting cutoffs for causal inference.  
- **Longitudinal Causal Inference:** Handling sequential treatments over time.





