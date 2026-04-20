# Overview

## Summary
David Soria Parra from Anthropic discusses MCP's evolution from local-only tools to production-ready agents with remote capabilities, authorization, and UI shipping features.

## Key Takeaway
2026 focuses on connectivity: combine skills, MCP, and CLI seamlessly for production agents beyond coding.

# Insights

## MCP Applications Ship Their Own Interfaces

- Agents can ship UI over MCP protocol without plugins, SDKs, or client-side rendering from models.
- MCP servers work portably across Claude, ChatGPT, VS Code, and Cursor without modification.
- Servers ship both tools for model interaction and UIs for human interaction simultaneously.

## Rapid Ecosystem Growth and Adoption

- MCP reached 110 million monthly downloads, taking half the time React needed for same milestone.
- Adoption includes OpenAI, Google ADK, LangChain, and thousands of frameworks pulling MCP as dependency.
- Most MCP servers built behind closed doors connect company systems to agents in production.

## Progressive Discovery Reduces Context Bloat

- Use tool search to defer loading tools until model actually needs them, not upfront.
- Massive reduction in context window usage by loading tools on-demand via model requests.
- Clients must implement progressive discovery patterns instead of dumping all tools into context.

## Programmatic Tool Calling Composes Operations

- Models should write scripts in V8/Python/Lua isolates instead of chaining individual tool calls sequentially.
- MCP's structured output feature provides type information enabling models to compose operations efficiently.
- Reduces latency and token usage by having model orchestrate through code, not repeated inference.

## Design for Agents, Not REST Conversions

- Stop building one-to-one REST-to-MCP converters; design tools considering how agents actually work.
- Think about human interaction patterns when designing agent interfaces; they're surprisingly similar.
- Server-side execution environments enable better orchestration than client-side tool composition.

## Three-Tier Connectivity Stack for Production

- Skills provide domain knowledge in simple reusable files with minor platform differences.
- CLI excels for local coding agents with sandboxes where tools exist in pretraining.
- MCP adds rich semantics, authorization, governance, platform independence when sandboxes unavailable or enterprise features needed.

## Stateless Transport Protocol Improves Scalability

- Google proposing stateless HTTP transport to treat MCP servers like REST for hyperscaler deployment.
- Enables deploying MCP servers to Kubernetes, Cloud Run without maintaining stateful connections.
- Specification launching June 2026 with SDK support for easier enterprise deployment.

## Skills Over MCP Enable Dynamic Updates

- Shipping skills with MCP servers provides domain knowledge about tool usage patterns.
- Server authors can continuously update skills without relying on plugin registries or client updates.
- MCP extension mechanisms let clients selectively support features like applications for web interfaces only.
