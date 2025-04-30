# Collaboration with Bear Brown and Co. & Stellis Labs

This repository documents the high-level details of three key projects developed under the **Humanitarians AI** initiative, focused on improving healthcare, education, and intelligent systems with AI-driven solutions.

---

## Project 1: AI-Powered Doctor Recommendation System

The **AI-Powered Doctor Recommendation System** provides an AI-based platform that matches patients with relevant medical specialists based on their clinical history, symptoms, and reports. The system uses a combination of **natural language processing (NLP)**, **vector similarity search**, and **explainable language generation** to deliver personalized doctor suggestions. This system aims to improve healthcare accessibility by offering transparent, data-driven, and tailored recommendations to patients.

### Key Features:
- Extracts key medical information from patient records.
- Performs a **vector similarity search** to find doctors with expertise matching the patient’s needs.
- Generates an explanation for each doctor suggestion using **Ollama**, an explainable AI model that provides insights into the reasoning behind recommendations.
- The recommendation engine is designed with a **terminal-based interactive UI** using the **Rich** library for easy interaction.

### Tech Stack:
- **ChromaDB**: A vector database used for efficient similarity search based on patient data.
- **Ollama**: LLM runtime for generating the explanation of doctor recommendations.
- **Python**: For backend development and integrating the system components.
- **Rich**: A Python library used to create a terminal-based interactive UI for users.
- **Jupyter Notebooks**: For documenting and testing the system’s functionalities interactively.

---

## Project 2: Model Context Protocol (MCP)

**MCP** is an orchestration protocol designed to facilitate seamless interaction between large language models (LLMs) and external tools, structured data sources, and real-time APIs. The goal of MCP is to enhance LLMs from passive responders to proactive agents capable of contextual reasoning and action.

With **MCP**, LLMs can intelligently integrate with external data sources, such as databases or APIs, and take actions based on contextual information. A sample use case involves querying live clinical trial data from a database and utilizing the LLM to summarize and recommend doctors based on the results.

This protocol supports multi-agent intelligence, enabling multiple LLMs to work together and execute tasks autonomously in a dynamic, real-time environment.

### Key Features:
- Supports intelligent chaining of actions and tool-awareness.
- Can interact with structured data sources (e.g., clinical trial databases) in real-time.
- Designed to integrate with systems such as **Groq**, **Claude**, and **OpenAI**.

### Tech Stack:
- **SQL**: For structured data storage and querying.
- **Claude**: An LLM used for summarization and decision-making.
- **AnyQuery**: For querying external data sources in real-time.

---

## Project 3: AI Textbooks Platform

The **AI Textbooks Platform** aims to revolutionize educational content creation by leveraging large language models to generate, cite, and store textbook-quality content. It provides a system for creating dynamic educational material with traceable sources and real-time LLM assistance, making content creation easier and more accessible for educators and students alike.

The platform integrates an LLM runtime using **OpenAI**, connects with various tools and a knowledge base, and offers a user-friendly interface through **OpenWebUI**. 


### Key Features:
- Allows the creation of textbook-quality content in real-time with LLM assistance.
- Integrates citation generation and maintains full traceability of sources.
- Offers seamless content storage and retrieval via structured databases.

### 🛠 Tech Stack:
- **OpenAI**: Local LLM engine used to generate content.
- **OpenWebUI**: Interface for users to interact with the LLM-based content creation system.
- **Python**: For developing the backend infrastructure and API integrations.

---

# Contributors:
**Saranya Machavaram**