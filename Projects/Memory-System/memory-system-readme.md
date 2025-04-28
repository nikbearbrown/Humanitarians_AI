# Memory System for Agent Collaboration

## Overview

This project is a collaboration between Bear Brown and Co. and Stellis Labs, focused on developing a comprehensive memory system for AI agents. The system enables intelligent agents to store, retrieve, and share information through a human-inspired memory architecture.

## Memory Architecture

The system implements four distinct types of memory, each serving a specific purpose:

1. **Short-Term Memory**: Manages transient execution data and task context
2. **Long-Term Memory**: Stores persistent document-based knowledge 
3. **Episodic Memory**: Records conversation histories and agent interactions
4. **Ecosystem Memory**: Maintains immutable audit logs for compliance and monitoring

## Key Components

### Memory Storage

- **ChromaDB**: Vector database for semantic search capabilities in Short-Term, Long-Term, and Episodic Memory
- **OpenSearch**: Document database for immutable audit logs in Ecosystem Memory

### Processing Utilities

- **Embedding Model**: Converts text to vector embeddings for semantic search
- **Text Chunker**: Splits documents into manageable pieces while preserving context
- **File Processor**: Handles document ingestion and metadata extraction

### Communication Protocol

- **Inter-Agent Communication Protocol (IACP)**: Framework for structured message exchange between agents
- **Collaboration Engine**: Facilitates agent discovery and problem-solving
- **Agent Registry**: Maintains records of agent capabilities and availability

## System Features

- Natural language queries through vector embeddings
- Semantic search across different memory types
- Document chunking and vectorization for efficient storage
- Conversation tracking and retrieval
- Audit logging for compliance
- Agent collaboration for distributed problem-solving

## Interface Components

- **API Layer**: REST endpoints for system interaction
- **Document Q&A Interface**: Gradio-based UI for document upload and querying
- **Collaboration Web Interface**: FastAPI-powered endpoints for agent interaction

## Architecture Diagram

```
┌───────────────────┐     ┌───────────────────┐     ┌───────────────────┐
│                   │     │                   │     │                   │
│   Short-Term      │     │   Long-Term       │     │   Episodic        │
│   Memory          │     │   Memory          │     │   Memory          │
│                   │     │                   │     │                   │
└─────────┬─────────┘     └─────────┬─────────┘     └─────────┬─────────┘
          │                         │                         │
          │       ┌─────────────────┴─────────────────┐       │
          │       │                                   │       │
          └───────┤       ChromaDB Storage Layer     ├───────┘
                  │                                   │
                  └─────────────────┬─────────────────┘
                                    │
                  ┌─────────────────┴─────────────────┐
                  │                                   │
                  │     Embedding & Vector Search     │
                  │                                   │
                  └─────────────────┬─────────────────┘
                                    │
          ┌─────────────────────────┼─────────────────────────┐
          │                         │                         │
┌─────────┴─────────┐     ┌─────────┴─────────┐     ┌─────────┴─────────┐
│                   │     │                   │     │                   │
│   Collaboration   │     │   Agent Registry  │     │   Ecosystem       │
│   Engine          │     │                   │     │   Memory (Audit)  │
│                   │     │                   │     │                   │
└───────────────────┘     └───────────────────┘     └───────────────────┘
```

## Key Benefits

- Human-inspired memory structure enables natural information retrieval
- Semantic search allows retrieval of information even when phrased differently
- Multiple memory types provide comprehensive context for agent decision-making
- Structured collaboration framework for multi-agent problem-solving
- Secure audit logging for accountability and compliance

## Technical Implementation

The system is implemented in Python with the following key dependencies:
- ChromaDB and OpenSearch for storage
- FastAPI for API endpoints
- SentenceTransformers for embedding generation
- Gradio for interactive interfaces

## Future Directions

- Enhanced integration with large language models
- Multi-modal memory support (images, audio, etc.)
- Distributed agent collaboration at scale
- Improved memory consolidation and forgetting mechanisms

---

This project represents a significant advancement in agent memory systems, providing a robust foundation for intelligent agent collaboration and knowledge management.
