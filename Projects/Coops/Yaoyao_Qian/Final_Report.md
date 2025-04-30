# Final Project Report
**Name:** Freax Ruby (Yaoyao Qian)  
**Period:** January 8 – April 26, 2025  
**Project:** Think Before You Grasp (ThinkGrasp)

---

## Executive Summary

This report summarizes my contributions to the **Think Before You Grasp (ThinkGrasp)** project during the Spring 2025 semester. The project focuses on developing a vision-language robotic grasping system capable of reasoning in cluttered, unstructured environments through modular and extensible design.

Key accomplishments during this period include:

1. **System Refactoring and Modularization:** Reorganized the original codebase into structured modules (`vision`, `language`, `grasp`, `integration`) to improve maintainability, extensibility, and experimental flexibility.

2. **Grasp Policy Exploration:** Initiated research on upgrading the backend grasp policy by attempting to integrate **Granet**, a state-of-the-art grasp proposal network, aiming to surpass the capabilities of GraspNet.

3. **Equivariant Representation Investigation:** Explored the use of **SO(3)-equivariant geometric representations** to enhance grasp generalization, especially under complex cluttered scenarios.

4. **Evaluation Setup and Real-World Validation:** Established a minimal reproducibility evaluation framework for real-world cluttered tasks and conducted small-scale empirical tests to validate system robustness.

---

## Detailed Description of Contributions

### System Refactoring and Modularization (January – February)

- **Codebase Structuring:**
  - Separated major components into distinct, modular sub-systems: visual processing, language reasoning, grasp candidate generation, and integration control.
  - Built standardized internal APIs to manage data flow between perception, reasoning, and control modules.

- **Configuration and Debugging Improvements:**
  - Developed unified configuration schemas for experiment control.
  - Implemented tracing utilities to monitor the cascade from language goals to segmentation and grasp decisions.

- **Impact:**  
  This restructuring improved system transparency, reduced technical debt, and paved the way for backend policy swapping and evaluation experiments.

---

### Grasp Policy Upgrade Exploration (March)

- **Granet Integration Attempt:**
  - Evaluated Granet’s architecture for compatibility with ThinkGrasp’s pipeline.
  - Identified input-output format mismatches, especially in cropped scene handling and grasp pose representation.
  - Attempted preliminary integration, revealing limitations in direct plug-and-play feasibility.

- **Impact:**  
  This exploration uncovered deep architectural assumptions within the original system and informed the future need for a **grasp backend abstraction layer**.

---

### Equivariant Representation Investigation (April)

- **Motivation:**  
  To improve grasp pose prediction consistency under 3D scene variations (rotation, occlusion).

- **Experiments:**
  - Implemented preliminary SO(3)-equivariant encoding strategies.
  - Tested modified grasp representations under cluttered scene conditions.
  - Found instability in initial integration attempts, with open challenges around feature alignment and runtime efficiency.

- **Impact:**  
  Although still ongoing, this line of work initiated a promising direction for future **symmetry-aware grasp planning** research.

---

### Real-World Evaluation and Documentation

- **Evaluation Setup:**
  - Created a lightweight reproducibility framework to benchmark stepwise goal completion success.
  - Conducted manual tests for two object retrieval tasks (\"get the tape,\" \"get the knife\") under cluttered occlusion.

- **Results Summary:**
  - Demonstrated consistent pipeline execution with fallback triggering when necessary.
  - Documented system bottlenecks affecting multi-step success rate.

- **Presentation Preparation:**
  - Compiled technical slides summarizing system structure, architectural issues, and future improvement directions.

---


## Challenges Faced

### Challenge 1: Granet Adaptation Complexity
Granet’s design expects dense, full-scene point cloud inputs and produces grasp proposals under different assumptions compared to ThinkGrasp’s segmentation-cropped pipeline.  
Directly feeding cropped or localized regions led to degraded grasp prediction quality, unstable candidate scoring, and semantic drift from the original object-centric goals.

---

### Challenge 2: Equivariant Feature Integration Instability
Introducing SO(3)-equivariant geometric encodings into the grasp pipeline created misalignment between the transformed latent representations and the downstream grasp selection logic.  
Initial experiments showed unstable grasp predictions and inconsistent behavior across different scene orientations.

---

### Challenge 3: Fallback Behavior Under Heavy Clutter
In highly occluded scenarios, fallback segmentation (e.g., LangSAM) sometimes produced masks that deviated from the original language goal, leading to divergence between planned grasp targets and actual execution.  
This highlighted a structural sensitivity between goal conditioning, segmentation robustness, and grasp policy flexibility.

---

## Results and Impact

### System Evolution

- Transitioned ThinkGrasp into a **modular, research-ready platform**.
- Created initial experimental baselines for integrating and benchmarking new grasp backends.

### Research Advancement

- Initiated exploration into **geometric structure-aware grasp planning** using equivariant methods.
- Formulated a roadmap toward more flexible, symmetry-resilient grasp reasoning.

---

## Skills Acquired and Professional Growth

- **Robotic System Modularization:** Deepened skills in architecture restructuring and codebase refactoring.
- **Grasp Policy Research:** Gained experience in evaluating, adapting, and diagnosing modern grasp proposal networks.
- **Geometric Machine Learning:** Initiated understanding of equivariant representations in 3D spatial reasoning.
- **Research Documentation and Presentation:** Improved technical communication through structured reporting and slide preparation.

---

## Future Work

- **Develop a Grasp Backend Abstraction Layer:** Allow interchangeable grasp candidate generation modules within ThinkGrasp.
- **Formalize Equivariant Grasp Scoring:** Build end-to-end pipelines capable of leveraging geometric symmetries.
- **Expand Evaluation Framework:** Test system scalability with a broader range of goal tasks and unseen object sets.
- **Enhance Language-Conditioned Grasping:** Improve robustness of reasoning pipelines to better handle vague or partial goals.

---

This project period laid the foundation for the next stage of research-driven improvements to ThinkGrasp. The insights and partial prototypes developed during Spring 2025 will enable more advanced modular reasoning and adaptive robotic manipulation systems in future phases.
