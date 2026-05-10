# Agentic RAG & Context Engineering

## Summary
The evolution from static RAG to Agentic RAG allows AI to dynamically decide what context to fetch, optimizing the reasoning budget and leveraging historical intent.

## Key Takeaway
Shift from fixed retrieval pipelines to agentic search to empower AI to discover and utilize context across diverse sources.

# Insights

## Dynamic Context Retrieval
- Agentic retrieval replaces static top-K searches with agents that dynamically decide what information to fetch based on immediate need.
- Moving reasoning about retrieval into the agent itself reduces the need for complex, hand-coded orchestration logic in the pipeline.
- Autonomous retrieval allows agents to handle ambiguous or poorly defined requests by exploring multiple potential information paths independently and thoroughly.

## Reasoning Budget Optimization
- Surgical context management through progressive disclosure preserves the model's "reasoning budget" while maintaining high quality in large-scale systems.
- High-fidelity context engineering requires a deep understanding of which data sources are most relevant for a given engineering task.
- Agents must be able to selectively filter retrieved information to avoid overwhelming the model with irrelevant or low-quality data.

## Historical Intent Discovery
- High-fidelity context requires identifying organizational experts and understanding the historical intent behind past architectural decisions and code deletions.
- Critical "below-the-surface" information includes past rejections, failed experiments, and the original reasoning behind specific logic choices in the codebase.
- Understanding why information was deleted or changed is essential for making informed decisions in a legacy environment with years of technical history.

## Context Development Lifecycle
- LLMs have smart zone around 100k tokens; beyond that attention degrades quadratically making decisions unreliable.
- Sub-agents isolate token-heavy exploration in separate context, reporting summaries back to keep orchestrator lean.
- Context Development Lifecycle: treat AI coding context with software development rigor including testing and distribution.
- Design concept alignment via "Grill Me" approach forces shared understanding through structured questioning.

# Related Talks

- **[Agentic Search for Context Engineering — Leonie Monigatti](../insights/ynJyIKwjonM_Leonie_Monigatti_Agentic_Search_for_Context_Engineering.md)**
- **[OpenRAG: An open-source stack for RAG — Phil Nash](../insights/4TxOBhDRRCM_OpenRAG_An_open_source_stack_for_RAG_Phil_Nash.md)**
- **[Mergeable by default: Building the context engine to save time and tokens — Peter Werry](../insights/5ID22ACI7IM_Peter_Werry_Mergeable_by_default_Building_the_context_engine_to_save_time_and_tokens.md)**
- **[Build Your First Demand-Driven Context Base — Raj Navakoti](../insights/_QAVExf_1uw_Raj_Navakoti_Build_Your_First_Demand_Driven_Context_Base_Let_AI_Agents_Tell_You_What_They_Need.md)**
- **[Context Is the New Code — Patrick Debois, Tessl](../insights/bSG9wUYaHWU_Context_Is_the_New_Code_Patrick_Debois_Tessl.md)**
- **[Full Walkthrough: Workflow for AI Coding — Matt Pocock](../insights/-QFHIoCo-Ko_Full_Walkthrough_Workflow_for_AI_Coding_Matt_Pocock.md)**
- **[Software Fundamentals Matter More Than Ever — Matt Pocock](../insights/v4F1gFy-hqg_Software_Fundamentals_Matter_More_Than_Ever_Matt_Pocock.md)**
