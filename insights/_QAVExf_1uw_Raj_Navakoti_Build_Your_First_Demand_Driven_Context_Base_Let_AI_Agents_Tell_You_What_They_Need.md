# Overview
## Summary
Enterprises struggle with AI value creation because monolithic knowledge is often tribal and undocumented. Demand-driven context allows agents to identify and pull the specific information they need.

## Key Takeaway
Apply TDD principles to agent knowledge by assigning tasks that reveal specific information gaps for systematic curation.

# Insights
## Enterprise AI Challenges
- Enterprises often fail to realize AI value because models lack access to specific institutional and tribal knowledge.
- McKenzie data shows 88% of companies use AI, but only 6% see significant value creation due to knowledge gaps.

## The Knowledge Monolith
- Monolithic knowledge bases are often outdated or unreliable, making simple RAG retrieval ineffective for complex agentic tasks.
- Institutional knowledge remains trapped in silos like Confluence, Jira, and SharePoint, often containing redundant or conflicting information.

## Retrieval Strategy Pitfalls
- Building numerous Model Context Protocol servers without rigorous evaluations leads to unreliable outputs and high data-entry overhead.
- Simply plugging in more retrieval layers often results in non-deterministic and untested data that fails in production.

## Demand-Driven Context
- A demand-driven approach allows agents to proactively identify and request missing information needed to complete a task.
- Instead of pushing all data to agents, assign problems and let the agents "pull" specific context as needed.

## Tribal Knowledge Bottleneck
- Forty percent of enterprise knowledge is tribal and undocumented, requiring agents to "pull" insights from human experts.
- Institutional knowledge sits within people rather than documents, creating a significant hurdle for standard automated retrieval systems.

## Knowledge TDD
- Treat knowledge gaps like failed test cases in TDD to systematically build a high-quality context base for agents.
- Assigning problems that agents will fail at reveals exactly what institutional knowledge is missing and requires documentation.

## Context Microservices
- Break down monolithic institutional knowledge into modular context blocks, similar to transforming legacy software into microservices.
- Curating knowledge into smaller, specific blocks makes information much more reusable and reliable for diverse multi-agent systems.

## Agent Onboarding
- Onboard agents like new employees by assigning tasks and allowing them to gradually build domain expertise through inquiry.
- High-performing agents curate their own knowledge base by documenting the answers to the questions they ask experts.
