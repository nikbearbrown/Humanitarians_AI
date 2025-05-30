---
title: Final Project Report - AI Textbook Development at Humanitarians AI
description: Comprehensive report detailing Dharun Ramaraj's contributions to AI textbook development during the Humanitarians AI Co-op from January 6 to May 31, 2025.
---

# Final Project Report: AI Textbook Development at Humanitarians AI
**January 6 - May 31, 2025**

## Executive Summary

This report details my contributions as an AI Agentic Engineer during a five-month Co-op with Humanitarians AI, from January 6 to May 31, 2025. My work focused on developing scalable AI textbook infrastructure, emphasizing automation, advanced querying, and user-friendly chat interfaces. Key projects included:

- **Textbook-Engine MVP**: Built an initial automation pipeline for AI textbook generation using Fumadocs, with scripts for content structuring and a chatbot interface.
- **Ask AI Feature Iterations**: Researched Orama’s chatbot capabilities, integrated OpenWebUI’s textbook upload and chat feature with login-based memory for customized responses, developed a custom RAG-based Ask AI feature (facing scalability issues), and implemented a generative AI textbook with OpenWebUI for demos.
- **OpenStax Physics Volume 1 Conversion**: Converted OpenStax Physics Volume 1 into an AI textbook format, integrating Orama’s chatbot with a sync script for content indexing, with manual corrections for missing examples and chapter review problems.
- **Additional Textbooks**: Supported setup for textbooks like ENGR-0201, INFO-6205, and others.

The Textbook-Engine MVP provided the automation foundation, while OpenWebUI’s chat feature, enhanced by a login-based memory system, and Orama’s chatbot with sync script enabled dynamic user interactions. OpenWebUI drove successful product demos, and Orama enhanced OpenStax querying. Scalability concerns led to prioritizing open-source solutions like OpenWebUI and Orama over earlier ChromaDB/Pinecone experiments. AWS Amplify optimized builds for large content volumes. My contributions delivered robust AI textbook solutions, supported by comprehensive documentation.

## Project Contributions

### Textbook-Engine MVP
- Developed a Minimum Viable Product (MVP) for the Textbook-Engine, automating AI textbook generation using Fumadocs.
- Implemented scripts including `setup.py` (project initialization), `config.py` (Tailwind CSS and page configuration), `generate_toc.py` (Table of Contents generation), `generate_sections.py` (section expansion), `generate_pagecontent_titles.py` (content titles), `generate_folder_structure.py` (docs structure), `generate_content.py` (MDX content), `generate_firstpage.py` (index page), `enhance_content.py` (content refinement), `document_indexer.py` (initial indexing experiments), `chromadb_explorer.py` (embedding exploration), and `doc_chatbot.py` (AI chatbot using Groq’s Llama3).
- Tested the MVP pipeline, ensuring MDX compatibility and interactive user feedback for content refinement, with early indexing experiments using ChromaDB/Pinecone (later scrapped for scalability).
- **Outcome**: Established a foundational automation pipeline, enabling structured content generation and initial chatbot-based querying.

### Ask AI Feature Iterations
- **Orama Research**: Explored Orama’s chatbot for context-aware Q&A, evaluating its built-in indexing and retrieval capabilities with a sync script for textbook content. Avoided Inkeep due to its paid model, prioritizing open-source solutions.
- **OpenWebUI Integration**: Leveraged OpenWebUI’s built-in textbook upload and chat feature, using backend calls to enable querying, with a login-based memory system for customized user responses.
- **Custom Ask AI Feature**: Developed a FastAPI-based backend with a custom RAG system, but scalability issues with large datasets led to its deprioritization.
- **Generative AI Textbook with OpenWebUI**: Built the ENGR-0201 generative AI textbook using OpenWebUI’s chat feature and memory system to address scalability, enabling interactive content generation and product demos that received positive stakeholder feedback.
- **Outcome**: Delivered a scalable Ask AI solution through OpenWebUI’s memory-enhanced chat, with Orama research guiding OpenStax integration, overcoming custom RAG limitations.

### OpenStax Physics Volume 1 Conversion
- Extended the Textbook-Engine MVP to convert OpenStax Physics Volume 1 into an AI textbook format, using automation scripts for MDX structuring. The pipeline produced formatting errors, content inaccuracies, and missing content, particularly examples and chapter review problems, requiring extensive manual corrections.
- Integrated Orama’s chatbot, using a sync script to index textbook content for dynamic, context-aware querying, validated for educational accuracy.
- Used AWS Amplify to optimize build performance, addressing high RAM usage during processing of large content volumes.
- Manually validated mathematical expressions, figures, examples, and chapter review problems to ensure alignment with educational standards.
- **Outcome**: Delivered a functional AI-formatted Physics textbook with Orama’s chatbot, despite pipeline challenges, ready for educational use.
- 🔗 [GitHub Repo](https://github.com/stellis-labs/physics-volume-1)

### Additional Textbook Contributions
- Supported setup and content planning for textbooks, including:
  - ENGR-0201 Textbook ([GitHub](https://github.com/stellis-labs/engr-0201-textbook))
  - INFO-6205 Textbook ([GitHub](https://github.com/stellis-labs/info-6205))
  - Data Structures and Algorithms ([GitHub](https://github.com/stellis-labs/Data-Structures-and-Algorithms-textbook))
  - Data Science and Engineering ([GitHub](https://github.com/stellis-labs/data-science-and-engineering-textbook))
- Collaborated with teams to initialize scripts and resolve content issues, leveraging the Textbook-Engine MVP.
- **Outcome**: Established consistent automation workflows for multiple AI textbooks.

### OpenWebUI Integration
- Integrated OpenWebUI’s built-in textbook upload and chat feature with the Textbook-Engine and ENGR-0201 generative AI textbook, using backend calls to enable querying.
- Implemented a login-based memory system, allowing the chat to recognize users and provide customized responses based on their interaction history.
- Tested functionality for low-latency responses, critical for product demos showcasing personalized textbook access for ENGR-0201.
- Presented demos highlighting OpenWebUI’s memory feature and user-friendly interface, earning stakeholder approval.
- **Outcome**: Elevated user experience through a personalized, backend-driven chat interface, pivotal for demo success and engagement.

### Orama Chatbot Integration
- Implemented Orama’s chatbot for the OpenStax Physics Volume 1 Ask AI feature, using a sync script to index content for dynamic, context-aware Q&A.
- Researched Orama’s compatibility with Fumadocs, documenting its built-in indexing and scalability benefits for broader textbook use.
- Laid the groundwork for future Orama integration across other textbooks, complementing OpenWebUI’s capabilities.
- **Outcome**: Enhanced OpenStax interactivity with Orama’s chatbot and provided a roadmap for conversational features.

### Final Optimizations and Support
- Debugged and optimized scripts for Fumadocs compatibility, regenerating textbooks with updated configurations.
- Assisted teams in setting up Textbook-Engine scripts, providing guidance and resolving issues.
- Documented workflows, including MVP scripts, Orama sync script, OpenWebUI memory feature, and Amplify processes, on GitHub.
- **Outcome**: Ensured a stable, user-friendly AI textbook system with robust team support.

## Technical Architecture

### Textbook-Engine MVP
- **Components**:
  - **Automation Scripts**: Python scripts (`setup.py`, `config.py`, `generate_toc.py`, etc.) for project setup, content structuring, and MDX generation.
  - **Framework**: Fumadocs with Tailwind CSS, remark-math, rehype-katex, and Mermaid for styling and diagrams.
  - **Chatbot**: `doc_chatbot.py` using Groq’s Llama3 for context-aware responses, with initial indexing experiments (later scrapped).
- **Technology Stack**: Python, FastAPI, LangChain (RAG), GitHub, Groq, Fumadocs, Next.js.

### Ask AI Feature with OpenWebUI
- **Components**:
  - **Backend**: FastAPI server for initial custom RAG pipeline, later supplemented by OpenWebUI backend calls for the ENGR-0201 generative AI textbook.
  - **Frontend**: OpenWebUI’s textbook upload and chat feature with login-based memory for personalized responses.
  - **Retrieval**: OpenWebUI backend for content querying and response generation.
- **Implementation**: Enabled textbook uploads and real-time, customized querying via OpenWebUI’s chat interface and memory system, ensuring demo-ready performance for ENGR-0201.

### OpenStax Conversion
- **Pipeline**:
  - Extended MVP scripts to ingest OpenStax Physics Volume 1, generating MDX files with manual corrections for formatting errors, content inaccuracies, and missing examples and chapter review problems.
  - Structured content with Fumadocs, validated expressions.
  - Used AWS Amplify for builds, reducing RAM usage for large content.
  - Integrated Orama’s chatbot with a sync script for content indexing and querying.
- **Significance**: Orama’s chatbot and OpenWebUI’s chat feature delivered interactive access, while Amplify optimized build performance.

### Orama Chatbot Integration
- **Approach**:
  - Integrated Orama’s chatbot with OpenStax textbook, using a sync script for built-in content indexing and dynamic Q&A.
  - Researched Orama’s architecture for Fumadocs compatibility, planning scalable, context-aware workflows.
- **Potential Impact**: Orama transforms textbooks into interactive platforms, complementing OpenWebUI’s personalized chat.

## Challenges and Solutions

- **Challenge**: OpenStax conversion pipeline produced formatting errors, content inaccuracies, and missing content, particularly examples and chapter review problems.
  - **Solution**: Performed extensive manual corrections to validate and restore examples, review problems, equations, and figures, ensuring educational standards.
- **Challenge**: High RAM usage during builds for large content volumes.
  - **Solution**: Adopted AWS Amplify to offload build processes, improving efficiency.
- **Challenge**: Custom Ask AI feature faced scalability issues with large datasets.
  - **Solution**: Leveraged OpenWebUI’s upload and chat feature with memory system for a generative AI textbook, ensuring scalability and demo success.
- **Challenge**: Seamless OpenWebUI integration with backend calls and memory feature.
  - **Solution**: Optimized backend API calls and tested memory-based personalization for low latency.

## Results and Impact

- **Successful Deliveries**:
  - Textbook-Engine MVP for automated content generation.
  - Scalable Ask AI via OpenWebUI’s memory-enhanced chat feature for ENGR-0201.
  - OpenStax Physics Volume 1 textbook with Orama’s chatbot, despite pipeline challenges.
- **Demonstrations**:
  - Showcased OpenWebUI’s textbook upload, memory-based chat for ENGR-0201, and Orama-enhanced OpenStax demos, earning praise for interactivity and personalization.
  - Highlighted Orama’s sync script efficiency in presentations.
- **Orama Integration Impact**: Enabled OpenStax interactivity and set the stage for conversational features across textbooks.
- **Documentation**:
  - Created guides for MVP scripts, Fumadocs, OpenWebUI memory feature, Orama sync script, and Amplify workflows.
  - Documented Orama research and scalability findings.

## Skills Acquired

- **Technical Skills**:
  - Automation scripting with Textbook-Engine MVP.
  - Custom Chatbot with effective RAG.
  - OpenWebUI backend integration with login-based memory for personalized chat.
  - Orama chatbot integration with sync script for content indexing.
  - AWS Amplify for build optimization.
- **Professional Skills**:
  - Stakeholder presentations and demo production.
  - User support and collaborative debugging.
  - Project planning and documentation.

## Conclusion

My Co-op with Humanitarians AI provided hands-on experience in developing scalable AI textbook solutions. The Textbook-Engine MVP established a robust automation foundation, while OpenWebUI’s memory-enhanced chat feature for ENGR-0201 and Orama’s chatbot with sync script for OpenStax transformed user interaction. OpenStax querying excelled with Orama, despite pipeline challenges with missing examples and review problems. Scalability solutions like OpenWebUI, Orama, and AWS Amplify ensured success over earlier ChromaDB/Pinecone experiments. My contributions delivered innovative AI textbook systems, and the skills gained will fuel my growth as an AI and data engineering professional.

---

🔗 **Project Repositories**:  
- [Textbook Engine](https://github.com/stellis-labs/textbook-engine)  
- [Physics Volume 1](https://github.com/stellis-labs/physics-volume-1)  
- [Additional Textbooks](/profile.md)
