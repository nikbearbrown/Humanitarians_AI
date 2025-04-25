# Deep Research Engine


## Overview

Deep Research Engine is an advanced artificial intelligence research assistant designed to bridge the gap between vast academic resources and targeted research needs. This comprehensive system retrieves, analyzes, and ranks academic papers from multiple sources to provide researchers with highly relevant information tailored to complex research queries. By combining natural language processing, content-aware ranking algorithms, and automated research synthesis, the engine delivers thorough literature reviews and research reports that would traditionally require hours of manual effort.

The system distinguishes itself through intelligent understanding of research context, semantic content evaluation, and authoritative source assessment. Unlike traditional academic search tools that rely primarily on keyword matching, Deep Research Engine comprehends the nuanced relationships between concepts within a research domain and delivers results that reflect true relevance to the original research question. The end-to-end pipeline transforms broad research problems into focused summaries of the most pertinent literature.

## Key Features

- **Intelligent Query Processing**: The system transforms complex, natural language research questions into optimized search parameters. It identifies key concepts, expands them with domain-specific terminology, and structures queries to maximize relevance in academic repositories. This process handles even lengthy research proposals with detailed background contexts, extracting the essential concepts and relationships.

- **Multi-Source Data Retrieval**: Seamlessly integrates with multiple academic resources including ArXiv, PubMed, Google Scholar, and specialized web sources. The retrieval system respects rate limits and implements proper caching mechanisms to minimize redundant requests. Each source's unique search characteristics are handled through specialized adapters that normalize results into a consistent format.

- **Smart Document Management**: Automatically retrieves full-text documents in PDF format and organizes them in a sophisticated storage hierarchy based on query context. The cache structure maintains relationships between queries and results while implementing efficient duplicate detection. Metadata extraction captures essential bibliographic information, authority signals, and publication dates.

- **Advanced Content Ranking**: Employs a multi-signal ranking system that evaluates content based on semantic relevance, source authority, and publication recency. The semantic evaluation uses transformer-based embeddings to match content against the original query intent. Authority assessment considers publication venue, citation metrics, and institutional reputation. Publication recency is weighted according to field-specific dynamics, recognizing that currency has different importance across domains.

- **Comprehensive Report Generation**: Synthesizes findings into professionally formatted research reports with proper academic citations and clear organization. Reports maintain full traceability back to source documents while presenting information in a coherent narrative structure. Both Markdown and HTML formats are supported, with customizable templates and citation styles.

- **Modular, Extensible Architecture**: Built with a component-based design that allows for easy extension and customization. Each module communicates through well-defined interfaces that enable replacement or enhancement of individual components without disrupting the overall system. This architecture supports integration of new data sources, ranking algorithms, or output formats with minimal modification to the core system.

## System Architecture

The Deep Research Engine architecture consists of four primary modules, each composed of specialized components that work together to transform research questions into valuable insights:

### 1. Query Processing Module

- **QueryParser**: Analyzes and deconstructs research queries to identify key concepts, relationships, and constraints. It handles various query formats from simple keyword lists to complex research proposals with background information. The parser uses the GROQ language model to extract core concepts while filtering out explanatory text and filler content.

- **QueryExpander**: Enhances query effectiveness by augmenting extracted keywords with domain-specific terminology and related concepts. This component understands academic domains and can add synonyms, field-specific jargon, and conceptually related terms to improve recall. Expansion is context-aware, avoiding inappropriate term additions that would dilute the search focus.

### 2. Data Retrieval Module

- **Model Context Protocol (MCP) Client**: Serves as the unified interface to multiple data sources, leveraging Anthropic's open-standard Model Context Protocol. This powerful integration allows the system to seamlessly connect with academic repositories and knowledge bases through a standardized approach. The MCP Client manages authentication, request throttling, and connection lifecycle while providing a consistent interaction model.

- **MCP Server**: Implements the backend data retrieval logic using Anthropic's MCP architecture to provide standardized access to academic resources. This sophisticated component handles the complexities of different query syntaxes, pagination approaches, and rate limiting requirements specific to each source. The server includes robust error handling and retry logic to ensure reliability and performance under diverse conditions. By building on the MCP standard, our system benefits from Anthropic's continued development of this powerful protocol.

- **Paper Cache Manager**: Manages the downloading, storage, and organization of full-text documents. This component creates an intelligent folder hierarchy based on query contexts and timestamps, stores document metadata, and implements efficient document lookup. Each query execution creates a dedicated storage folder that maintains the relationship between the search parameters and retrieved documents.

### 3. Content Ranking Module

- **Content Embedder**: Transforms textual content into dense vector representations that capture semantic meaning. This component supports multiple embedding models including OpenAI's embeddings API and local SentenceTransformers implementations, with fallback mechanisms for offline operation.

- **Relevance Scorer**: Evaluates how well each content piece addresses the original query by computing semantic similarity between query and content embeddings. The scorer also assesses content quality based on factors like comprehensiveness, clarity, and information density.

- **Rank Aggregator**: Combines multiple ranking signals (semantic relevance, source authority, content recency) into a unified scoring model. This component applies domain-appropriate weightings to each signal and normalizes scores across heterogeneous content types. The aggregator also handles content diversity to prevent homogeneous result sets.

### 4. Report Generation Module

- **Report Generator**: Creates structured research reports from ranked content pieces. This component organizes information into coherent sections, adds proper citations, and ensures consistent formatting. The generator preserves relationships between report sections and original sources to maintain academic integrity.

- **Export Formatters**: Transform internal report representations into user-facing formats including Markdown for simplicity and HTML for rich formatting. Each formatter applies appropriate styling and layout while maintaining consistent structure across output formats.

## Configuration

The Deep Research Engine requires configuration for API access and system behavior:

### API Keys and External Services

The system integrates with several external services that require authentication credentials:

- **Google Custom Search**: For web content retrieval, requiring both an API key and Custom Search Engine ID
- **Google Scholar**: For academic paper discovery, requiring specialized access credentials
- **GROQ Language Models**: For advanced query processing and expansion
- **OpenAI API**: For generating high-quality embeddings to represent document content semantically

These credentials are stored in a dedicated configuration file that is excluded from version control for security reasons. A template configuration is provided to guide setup.

### System Settings

Beyond authentication, the system behavior is controlled through a comprehensive settings file that defines:

- **Search Parameters**: Controls how many results are retrieved from each source, timeout thresholds, and retry behavior
- **Ranking Weights**: Defines the relative importance of different ranking signals (semantic relevance vs. authority vs. recency)
- **Content Processing**: Controls how documents are chunked, analyzed, and represented
- **Report Generation**: Defines formatting preferences, citation styles, and output organization

## Output Organization

For each research query, the Deep Research Engine produces a comprehensive set of outputs organized as follows:

### Timestamped Research Folder

Each query execution creates a dedicated output directory named with a timestamp and query identifier. This organization ensures that research results are isolated and traceable to specific queries.

### Retrieved Documents

Full-text documents are downloaded and stored in a dedicated paper cache structure. The system creates a folder for each query execution that contains:

- **PDF Documents**: Complete copies of relevant academic papers
- **Metadata File**: A JSON file containing bibliographic information, source details, and query relationships

### Research Report

The primary output is a comprehensive research report available in multiple formats:

- **Markdown Report**: A clean, text-based format suitable for further editing or integration into other documents
- **HTML Report**: A richly formatted version with proper styling, organized sections, and clickable citations

The report structure includes:

- **Executive Summary**: Overview of the research question and key findings
- **Key Findings**: Detailed presentation of the most relevant content, organized by significance
- **Sources Section**: Complete bibliographic information for all referenced documents
- **Academic Citations**: Properly formatted citations throughout the document

### Raw Data

The system also preserves the raw retrieval and analysis results in JSON format, enabling further processing or integration with other research tools.

## Workflow Description

The Deep Research Engine operates through a carefully orchestrated workflow that transforms research questions into valuable insights:

### Query Understanding and Expansion

The process begins with the analysis of a research query, which can range from a simple question to a complex research proposal with background information. The system extracts key concepts, identifies relationships between them, and expands the query with domain-relevant terminology. This expansion is context-aware, adding terms that enhance recall without diluting precision.

### Multi-Source Content Retrieval

The expanded query is executed against multiple academic sources through the MCP client-server architecture. The system respects rate limits and implements proper error handling to ensure reliable data collection. Retrieved results are normalized into a consistent format and enriched with source-specific metadata.

### Document Processing and Analysis

Full-text documents are retrieved where available and processed to extract the most relevant content. The system employs intelligent chunking that preserves semantic coherence while enabling fine-grained analysis. Document metadata is extracted and standardized across sources.

### Content Ranking and Selection

Each content piece is evaluated through a multi-signal ranking system that considers:

- **Semantic Relevance**: How well the content addresses the query intent
- **Source Authority**: The reputation and credibility of the publication venue
- **Content Recency**: The publication date, weighted by field-specific considerations
- **Content Quality**: The comprehensiveness, clarity, and information density

These signals are combined into a unified score that determines which content pieces are most valuable for addressing the research question.

### Report Synthesis and Generation

The top-ranked content is synthesized into a cohesive research report that presents findings in a logical structure with appropriate citations. The report maintains academic integrity through proper attribution while organizing information for clarity and comprehension.

## Project Structure

The Deep Research Engine code is organized into a modular structure that reflects the system architecture:

```
deep-research-engine/
├── config/                    # Configuration files
├── src/                       # Source code for all major components
├── mcp-service/               # Modular Content Provider service
├── scripts/                   # Utility scripts
├── tests/                     # Test suites
└── output/                    # Generated research reports
```

Each module contains specialized components that implement specific aspects of the system functionality. The modular design enables independent development, testing, and enhancement of individual components.

## License and Attribution

The Deep Research Engine is a collaborative development between Bear Brown and Co and Stellis Labs, combining expertise in artificial intelligence, information retrieval, and research synthesis to create a powerful academic research assistant.

The system builds upon numerous open-source libraries and academic resources, with appropriate attributions provided in the acknowledgments section of the documentation.

## Acknowledgments

The Deep Research Engine gratefully acknowledges:

- **Anthropic** for their Model Context Protocol (MCP), which provides the standardized framework for our data retrieval system
- **ArXiv** for providing access to their extensive academic paper database
- **GROQ** for their powerful language models used in query processing
- **OpenAI** for embedding generation capabilities
- **Bear Brown and Co** and **Stellis Labs** for their collaborative vision and development expertise that made this project possible

We also extend our thanks to the open-source community whose libraries and frameworks form the foundation of this system.
