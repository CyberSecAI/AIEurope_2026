# OpenRAG: An open-source stack for RAG - Phil Nash

## Why RAG Still Matters

- RAG isn't dead; context windows don't solve cost and data scale challenges for businesses.
- RAG is complex and hard, varying by documents, users, questions, and interaction patterns.
- Modern RAG requires experimentation with chunking strategies, embeddings, and advanced search techniques like query rewriting.

## Document Processing with Docling

- Docling is an open-source tool from IBM Research handling PDFs, HTML, Word, slides, audio, and video.
- Multiple pipelines: simple text extraction, ASR for audio/video, and specialized PDF processing with small models.
- VLM pipeline uses Granite Docling 258M vision model for all-in-one extraction of text, tables, and images.

## OpenSearch for Hybrid Search

- OpenSearch provides powerful vector and keyword hybrid search with sophisticated filtering and aggregation capabilities.
- Supports multiple embedding models simultaneously, enabling smooth migration when upgrading embedding models over time.
- Uses JVector KNN plugin for live indexing with disk-based architecture, avoiding in-memory constraints for scalability.

## LangFlow Visual Orchestration

- LangFlow is a drag-and-drop visual editor integrating Docling, OpenSearch, embeddings, and data enrichment pipelines.
- Enables visual customization of RAG flows including adding guardrails, tools, and modifying agent behavior easily.
- Provides extensibility through visual components, allowing non-code modifications to ingestion and generation workflows.

## Agentic Retrieval Approach

- OpenRAG uses agentic retrieval where agents decide what searches to perform and handle results dynamically.
- Traditional RAG embeds query once; agentic RAG gives agents tools to perform multiple searches as needed.
- Agent receives instructions and tools, making retrieval more adaptive and effective than fixed top-K approaches.

## Flexible Model Support

- Supports external providers like OpenAI, Anthropic, and local models via Ollama for complete offline operation.
- Entire stack can run air-gapped with locally hosted models, embeddings, and document processing pipelines.
- Easy configuration of language models, embedding models, chunk sizes, and Docling settings through UI.

## Cloud Connectors and Syncing

- Integrates with Google Drive, SharePoint, and OneDrive for automatic document synchronization without manual uploads.
- Enables users to connect personal document directories that sync automatically, keeping knowledge bases current.
- OAuth-based authentication allows secure access to external cloud storage for seamless content ingestion.

## Extensibility and Integration

- Front-end built with Next.js, backend in Python, fully open-source for community contributions and customization.
- Provides API access and MCP server support for integrating OpenRAG search into other applications and agents.
- Knowledge filters leverage OpenSearch filtering to restrict searches to specific document subsets based on metadata.
