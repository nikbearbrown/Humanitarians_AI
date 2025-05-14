# Multi AI Agents Infrastructure

---

This repository contains an implementation of a scalable infrastructure for dynamic agent management. The project focuses on two core modules: **Dynamic Subagent Creation & Role Assignment** and **Agent Registry & Metadata Database**. Together, these modules enable the dynamic creation of subagents based on problem statements, the assignment of specific roles and tasks, and the effective management of all agents in the ecosystem through metadata storage and graph-based relationships.

## Overview

This project provides a framework to:

- **Dynamically create subagents** based on incoming problem statements.
- **Assign roles, descriptions, and task prompts** to each created subagent using structured JSON outputs from LLMs.
- **Manage a registry of agents** to ensure that duplicate agents are not created.
- **Store agent metadata and relationships** by integrating Chroma DB (for metadata) and Neo4j (for mapping relationships).

## Key Features

- **Dynamic Subagent Creation & Role Assignment:**
    - Accepts an external problem statement.
    - Determines if existing agents can handle the task through an agent registry check.
    - Dynamically creates new subagents (if necessary) with unique roles, detailed role descriptions, and task prompts.
    - Ensures structured agent creation using JSON outputs from LLM APIs (via Ollama).
- **Agent Registry & Metadata Database:**
    - Stores agent metadata (role, description, task prompt, creation timestamp, and LLM used) in Chroma DB.
    - Manages agent-agent relationships (including parent-child, sibling, and dependency mappings) using Neo4j.
    - Provides APIs for agent querying and registration to avoid duplication.

## Workflow

1. **Problem Statement Input:**
    
    An external agent sends a problem statement or query to the Dynamic Subagent Creation & Role Assignment module.
    
2. **Agent Registry Consultation:**
    
    The system checks the Agent Registry & Metadata Database to determine if an appropriate agent already exists.
    
3. **Agent Creation:**
    - If no suitable agent is found, new subagents are dynamically created.
    - Each new subagent is assigned a role, role description, and a task prompt generated via LLM.
    - The output (structured in JSON) includes fields like `agent_id`, `role`, `role_description`, `task_prompt`, `parent_agent_id`, `dependencies`, and `metadata`.
4. **Registration and Dependency Handling:**
    - The new agents are registered in the metadata database (Chroma DB).
    - Graph relationships such as parent-child and other agent dependencies are mapped and stored in Neo4j.
5. **Query Response:**
    
    The final list of agents (both existing and newly created) is returned to the external agent.
    

---

## **Project Structure**

## **Setup Instructions**

### **Prerequisites**

- Python 3.8 or later
- Neo4j database instance (local or cloud-based)
- ChromaDB installed and configured
- Access to an LLM API (via Ollama)

### **Installation**

1. Clone the repository:
    
    ```bash
    git clone <repository-url>
    cd project
    
    ```
    
2. Create a virtual environment:
    
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/MacOS
    venv\\Scripts\\activate     # For Windows
    
    ```
    
3. Install dependencies:
    
    ```bash
    pip install -r requirements.txt
    
    ```
    
4. Configure environment variables:
    - Create a `.env` file in the root directory with the following variables:
        
        ```
        NEO4J_URI=bolt://localhost:7687
        NEO4J_USER=neo4j
        NEO4J_PASSWORD=password
        
        ```
        
    - Update these values as per your Neo4j setup.

---

## **How to Run**

1. Start the FastAPI application:
    
    ```bash
    uvicorn app.main:app --reload
    
    ```
    
2. Access the API documentation at:
    
    ```
    <http://127.0.0.1:8000/docs>
    
    ```
    
3. Use the `/submit_problem/` endpoint to submit problem statements.

---

## **Modules Documentation**

### **1. `agent_creation.py`**

### Purpose:

Handles dynamic generation of agents based on problem statements using an LLM API (via Ollama).

### Key Features:

- Generates agents dynamically with structured JSON output.
- Adds metadata like creation timestamp and LLM model used.

### Usage Example:

```python
from agents.agent_creation import AgentCreator

creator = AgentCreator(model="llama3.2")
problem_statement = "Optimize supply chain logistics."
agent = creator.generate_agent(problem_statement)
print(agent)

```

---

### **2. `chroma_db.py`**

### Purpose:

Manages agent metadata storage and retrieval in ChromaDB.

### Key Features:

- Stores agent metadata with fields like `role`, `description`, `task_prompt`, etc.
- Retrieves agents based on similarity to a given problem statement.

### Usage Example:

```python
from db.chroma_db import ChromaDBManager

db_manager = ChromaDBManager()
agent_data = {
    "elementId": "12345",
    "problem_statement": "Optimize supply chain logistics.",
    "role": "Logistics Optimizer",
    "role_description": "Handles optimization of supply chains.",
    "task_prompt": "Analyze logistics data.",
    "creation_timestamp": 1672531200,
    "llm_used": "Llama 3.2"
}
db_manager.store_agent(agent_data)
result = db_manager.retrieve_agent_by_problem("Optimize supply chain logistics.")
print(result)

```

---

### **3. `neo4j_db.py`**

### Purpose:

Manages agent nodes and their relationships in Neo4j.

### Key Features:

- Creates or merges agent nodes with properties like role, description, etc.
- Maps relationships between agents (e.g., parent-child).

### Usage Example:

```python
from db.neo4j_db import create_agent_node, create_relationship

agent_data = {
    "problem_statement": "Optimize supply chain logistics.",
    "role": "Logistics Optimizer",
    "role_description": "Handles optimization of supply chains.",
    "task_prompt": "Analyze logistics data.",
    "creation_timestamp": 1672531200,
    "llm_used": "Llama 3.2"
}
element_id = create_agent_node(agent_data)
create_relationship("dummy_agent_123", element_id)

```

---

### **4. `agent_service.py`**

### Purpose:

Integrates all modules to process problem statements by either finding existing agents or creating new ones.

### Key Features:

- Checks ChromaDB for similar agents.
- Creates new agents if no match is found.
- Maps relationships between dummy agents and real agents in Neo4j.

### Usage Example:

```python
from services.agent_service import AgentService

service = AgentService()
result = service.process_problem("dummy_agent_123", "Optimize supply chain logistics.")
print(result)

```

---

### **5. `config.py`**

### Purpose:

Centralizes configuration settings for databases and APIs using environment variables.

### Example `.env` File:

```
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=password

```

---

### **6. `main.py`**

### Purpose:

Serves as the entry point for the application, exposing an API endpoint using FastAPI.

### Key Features:

- Provides a POST endpoint (`/submit_problem/`) to process problem statements.
- Integrates with `AgentService` to handle requests.

### Example Request:

Send a POST request to `/submit_problem/` with the following JSON body:

```json
{
  "dummy_agent_id": "dummy_001",
  "problem_statement": "Optimize supply chain logistics."
}

```

Expected Response:

```json
{
  "message": "New agent created and stored; dummy agent mapped to new execution id.",
  "problem_statement": "Optimize supply chain logistics.",
  "agent": {
    "elementId": "<generated_element_id>"
  }
}

```

---
