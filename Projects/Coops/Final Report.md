# **Deep Research Engine**

The **Deep Research Engine** is an AI-driven research assistant engineered to redefine academic discovery.  
By intelligently expanding queries and retrieving content from trusted sources like **Arxiv**, **PubMed**, and **Google Scholar**,  
it semantically ranks, extracts, and compiles highly relevant findings.  
The result is a precise, metadata-rich report that minimizes manual review time while maximizing research depth and transparency.

---

## **My Core Contributions**

During my co-op term, I played an instrumental role in building key infrastructure and logic behind the engine.  
My main contributions include:

- **Semantic Query Expansion**: Developed transformer-driven query expansion logic to convert broad input into domain-specific terminology.
- **Cross-Platform Retrieval Engine**: Built adapters for Arxiv, PubMed, and Google APIs via a unified Model Context Protocol (MCP).
- **Paper & Metadata Cache System**: Implemented structured file and metadata caching to eliminate redundancy and preserve audit trails.
- **Relevance Scoring Pipeline**: Integrated a hybrid scoring algorithm based on semantic match, authority indicators, and recency.
- **Markdown & HTML Report Generator**: Constructed formatting logic for readable, reference-linked summaries tailored for academic contexts.

---

## **Tools, Technologies & Design Components**

### **Technologies Applied**
- **Languages**: Python  
- **Libraries/Models**: OpenAI Embeddings, SentenceTransformers, GROQ , MCP Server
- **Data Sources**: Arxiv, PubMed, Google Custom Search  
- **Storage**: DuckDB, ChromaDB, Local Filesystem

---

## **Modular System Components**
- `query_processing/`: Parses and expands research input  
- `data_retrieval/`: Fetches structured content from academic APIs  
- `extraction/` + `chunking_engine/`: Gathers insightful segments  
- `ranking/`: Prioritizes data using a composite scoring mechanism  
- `report_generation/`: Compiles findings into polished deliverables  
- `metadata_processing/`: Ensures full citation, date, and DOI traceability

---

## **System Layout & File Architecture**

The engine uses a modular and scalable directory structure, as shown below:

```
deep-research-engine/
├── cache/                     # Temporary API responses
├── chroma_data/               # Vector store for semantic lookups
├── config/                    # API keys and runtime settings
├── data/, data_storage/       # Input/output data files
├── docs/                      # Documentation and usage guides
├── logs/                      # System logs
├── mcp-service/               # Academic source unifier
├── output/                    # Final report outputs
├── paper_cache/               # Stored PDFs + metadata
├── scripts/                   # Helper scripts
├── src/
│   ├── chunking/, chunking_engine/
│   ├── data_retrieval/, database/
│   ├── extraction/, metadata_processing/
│   ├── ml/, model_services/
│   ├── query_processing/, ranking/
│   ├── report_generation/, storage/, utils/
├── test_output/, tests/       # Testing output and suites
```

---

## **Challenges & How I Solved Them**

| **Problem**                             | **Solution**                                                  |
|----------------------------------------|---------------------------------------------------------------|
| Inconsistent metadata from different APIs | Created a normalization layer to unify structure             |
| Latency in embedding generation         | Batched processing and cached results in ChromaDB             |
| Format inconsistencies in documents     | Streamlined extraction logic with fallback options            |
| Citation traceability                   | Enforced metadata binding at chunk level                      |
| API rate limits                         | Used parallel fetch with backoff retry logic                  |

---

## **Outcome & Measurable Impact**

- Achieved **~80% time reduction** in literature review workflows  
- Successfully retrieved, parsed, and ranked **1,00 sources** during stress testing  
- Maintained **100% source traceability** in output reports  
- Built foundation for integration with UI interfaces, PDF exporting, and graph visualizations  
- Enabled real-time analysis with **multi-query support** under 5 minutes  

---

## **Skills Sharpened & Professional Growth**

- **AI Proficiency**: Real-world applications of embeddings, semantic search, and LLM summarization  
- **API & Retrieval Architecture**: Gained hands-on experience with scalable data pipeline construction  
- **Modular Coding Practices**: Learned to write plug-and-play components that are independently testable  
- **Metadata-Driven Design**: Built traceable systems for academic rigor and explainability  
- **Agile Collaboration**: Participated in sprints, code reviews, and documentation cycles  

---

## **Next Steps & Future Possibilities**

- Add a no-code interface with **Streamlit** or **Gradio** for user-friendly querying  
- Enable PDF export for formatted academic submissions  
- Expand source coverage to include domain-specific libraries like IEEE, SSRN, and JSTOR  
- Graph-based visual insights powered by Neo4j
- Fine-tune chunkers and rankers for industry-specific domains

---

## **Conclusion: A Transformative Experience**

This co-op at **Humanitarians AI × Stellis Labs** has been a deep dive into the practical application of AI for academic intelligence.  
The opportunity to contribute to a system that enhances research workflows was both intellectually rewarding and technically challenging.
I developed systems that didn’t just work—but explained why they worked, traceable to every data point.  
The exposure to high-impact infrastructure, problem-solving under constraint, and mission-driven development has left a lasting impression on my approach to both AI systems and professional responsibility.  
I walk away more capable, more curious, and more aligned with the goal of building transparent, human-centered technology.
