# Final Co-op Report  
**Name:** Samhita Kolluri  
**Period:** January 28 – May 2, 2025  
**Organization:** Humanitarians AI, in collaboration with Bear Brown & Co and Stellis Labs.  
**Project:** Contrastive Ideas Search Module  

## Executive Summary

The Contrastive Ideas Search Module aims to surface documents that are not merely topically similar, but also express semantically opposing perspectives. During my co-op at Humanitarians AI in collaboration with Bear Brown and Co and Stellis Labs, I developed key components of this system, including hybrid embedding strategies, fine-tuned stance-aware models, a two-phase retrieval pipeline, and a contrastive scoring engine.  
This project bridges the gap between traditional semantic search and critical thinking-driven search by combining topic relevance with stance opposition detection.

My contributions encompassed system design, technical development, model fine-tuning, benchmarking, and documentation  resulting in a deployable module that enhances diverse idea exploration across various domains such as healthcare, energy, and policy.

## Detailed Description of Contributions

**System Architecture & Design**  
- Designed a modular system that separately handles topic relevance and stance contrast detection.
- Developed a hybrid scoring methodology balancing both aspects for optimal result ranking.
- Created project-wide configuration files for reproducibility and modularity.


![Untitled diagram-2025-02-27-131708](bi-weekly-reports\sys-design.png)

> For a detailed architecture, see [`system_design.md`](https://github.com/Samhita-kolluri/contrastive-module)

**LLM Fine-tuning and Embedding Generation**  
- Fine-tuned a stance-aware model [`Samhita-kolluri/llama-contrastive-module-stance`](https://huggingface.co/Samhita-kolluri/llama-contrastive-module-stance) based on SNLI-style contradiction generated data [`Samhita-kolluri/snli-contrastive-json-dataset`](https://huggingface.co/datasets/Samhita-kolluri/snli-contrastive-json-dataset).
- Generated dual embeddings for documents:
  - **Topic Embedding** (for semantic closeness)
  - **Stance Embedding** (for detecting conceptual contrast)

**Vector Storage and Retrieval**  
- Structured ChromaDB with multi-vector indexing to allow efficient dual-embedding retrieval.
- Implemented vector storage schema for storing text along with topic and stance embeddings.

**Contrastive Scoring Engine**  
- Built contrastive scoring functions:

  `final_score = (topic_similarity) * (1 + stance_opposition) `
- Ensured that retrieval results prioritize documents that are both topically aligned and semantically divergent.

**Project Documentation**  
- Developed comprehensive documentation:
  - Updated the main `README.md`
  - Created technical specifications for system architecture and model fine-tuning.
  - Wrote internal guides for model fine-tuning and benchmarking procedures.

## Technical Documentation of Work

- **Fine-Tuned Model**: [`Samhita-kolluri/llama-contrastive-module-stance`](https://huggingface.co/Samhita-kolluri/llama-contrastive-module-stance)
- **Dataset**: [`Samhita-kolluri/snli-contrastive-json-dataset`](https://huggingface.co/datasets/Samhita-kolluri/snli-contrastive-json-dataset)

- **Vector Database**: ChromaDB with multi-vector schema support.
- **Key Modules Developed**:
  - `src/llm/llm_handler.py` (Contrastive generation)
  - `src/embeddings/vectorizer.py` (Dual embedding generator)
  - `src/scoring/scoring.py` (Contrastive scorer)
  - `src/database/vector_db.py` (Storage and retrieval interface)
- **Benchmarking**:  
  `src/benchmarking/contrastive_eval.py`, `src/benchmarking/rlhf_tuning.py`

All modules are modularized for reuse across different contrastive or retrieval-based applications.


## Challenges Faced and Solutions Implemented

| Challenge | Solution |
|:---|:---|
| LLM output inconsistency during stance generation | Applied structured prompts and schema validation to normalize outputs |
| Low stance contrast in initial results | Fine-tuned stance model on SNLI-style contradiction datasets to increase contrastiveness |
| Retrieval imbalance favoring topic similarity | Designed hybrid contrastive scoring to equally weight stance divergence |
| Inefficient vector search speed with dual embeddings | Optimized ChromaDB schema and batched retrieval queries |
| Token length limitations in fine-tuning large models | Applied smart batching and dynamic padding during training |

## Results and Impact

- Fine-tuned and achieved a higher stance opposition score which is now available publicly for wider reuse.
- Developed a flexible search system that can be adapted for diverse applications like argument retrieval, debate preparation, and critical idea generation.


## Skills Acquired and Professional Growth

| Category | Skills |
|:---|:---|
| AI/ML | Fine-tuning LLMs, triplet loss training, stance-aware embeddings |
| NLP | Semantic search, contrastive learning, vector-based retrieval |
| Research & Benchmarking | Evaluation metric design (Precision, Recall) |
| Technical Writing | Documentation of technical processes, user guides, model cards |

This experience deepened my understanding of contrastive NLP pipelines, modular AI design, retrieval system architecture, and advanced LLM fine-tuning techniques.


## Recommendations for Future Work

- **Expand Multi-Modality**: Extend contrastive search to images, tables, and graphs (using CLIP or LLaVA-style models).
- **Enhance Opposition Modeling**: Incorporate adversarial training to generate even more sharply opposing perspectives.
