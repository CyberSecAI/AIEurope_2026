# Overview

## Summary
Leonie Monigatti explores the evolution from fixed RAG pipelines to Agentic RAG, where AI autonomously decides when and what context to retrieve for engineering.

## Key Takeaway
Replace static retrieval with agentic search to empower AI to dynamically discover and utilize context across diverse distributed sources.

# Insights

## Context Engineering
- Deciding what goes into the context window is a crucial art; 80% of this process is driven by search.
- High-quality context engineering requires a deep understanding of which data sources are most relevant for a given engineering task.
- Agents must be able to selectively filter retrieved information to avoid overwhelming the model with irrelevant or low-quality data.

## The Evolution of RAG
- Fixed retrieval pipelines are being replaced by Agentic RAG, where agents dynamically decide when and what to retrieve.
- Shifting from "retrieve then generate" to an iterative "search-reason-act" loop significantly improves the accuracy of complex engineering responses.
- Agentic RAG allows the model to identify gaps in its own knowledge and proactively seek out the missing information.

## Diverse Context Sources
- Vital context lies distributed across local files, working memory, agent skills, databases, the web, and long-term memory sources.
- Engineers must build systems that allow agents to access and synthesize information from multiple disparate silos in real-time.
- Leveraging diverse sources ensures that agents have a holistic view of the project, including current code and historical decisions.

## Versatile Tooling
- Shell and bash tools allow agents to execute scripts, interact with CLIs, and perform complex searches across disparate systems.
- Providing agents with low-level system access enables them to perform tasks that go beyond simple text processing or generation.
- Tool-augmented agents can automate repetitive engineering workflows by combining reasoning with the ability to execute concrete commands and scripts.

## Search Complexity
- Doing good search is incredibly difficult, often requiring custom stacks of vector, keyword, and semantic search tools together.
- Engineers must balance search latency with retrieval accuracy to ensure that agents can operate effectively in fast-paced development environments.
- Continuous evaluation and optimization of the search stack are necessary to adapt to the changing needs of the engineering team.

## Autonomous Decision Making
- Agents should be empowered to decide which search tool is most appropriate for a specific query or task context.
- Moving reasoning about retrieval into the agent itself reduces the need for complex, hand-coded orchestration logic in the pipeline.
- Autonomous retrieval allows agents to handle ambiguous or poorly defined requests by exploring multiple potential information paths independently and thoroughly.
