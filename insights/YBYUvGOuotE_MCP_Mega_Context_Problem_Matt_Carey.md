# Overview

## Summary
Matt Carey from Cloudflare presents solutions to MCP's context window explosion problem when exposing large APIs to agents.

## Key Takeaway
Code generation via typed SDKs beats traditional tools for exposing massive APIs to agents.

# Insights

## Context Window Explosion Problem
- Cloudflare's 2,600 API endpoints generated 1.1 million tokens as tools, completely exploding agent context windows.
- Splitting APIs into 16 product-based MCP servers created incomplete coverage with only partial endpoint representation.
- Progressive discovery became critical requirement when serving thousands of endpoints rather than eight simple tools.

## Code Mode as Solution
- TypeScript types provide extremely concise input/output representation that agents can reason about effectively in minimal tokens.
- Generate typed SDK from OpenAPI spec, let model write code against types instead of exposing individual tools.
- Entire Cloudflare API accessible in roughly 1,000 tokens versus 1.1 million with traditional tool approach.

## Programmable Sandboxes Enable Safety
- Running untrusted LLM-generated code requires V8 isolates or similar lightweight sandboxes with programmable guardrails.
- Workers/Deno/Pydantic Monty enable controlled code execution by toggling network access, secrets, and resource limits programmatically.
- Code execution CVEs become acceptable when proper isolation primitives exist with domain whitelisting and timeout controls.

## CLI vs Tool Search Tradeoffs
- CLI approach requires shell access and agents parsing help output, works "mostly" but brittle for production.
- Tool search loads K=6-8 relevant tools into context, wastes tokens on unused tools but structured.
- Both approaches hit fundamental scaling limits when APIs exceed hundreds of endpoints per service.

## Code as Compact Plans
- Code has exponentially more degrees of freedom than individual tool calls for expressing complex operations.
- Agents naturally improve at code generation as models advance, automatically benefiting API providers without re-tooling.
- Saved mini-scripts enable cron jobs and automation workflows that self-heal when breaking, re-generating on failures.

## MCP Client Evolution Needed
- Building performant MCP clients is currently "absolute pain" requiring stateful connection management and resumability logic.
- Future clients will embrace programmatic tool calling, treating code execution as primary interaction mode over discrete tools.
- Stateless agent loops become necessary when scaling from millions of agents total to hundreds per person.

## Infrastructure Primitive Shift
- Pre-LLM era treated untrusted code execution as vulnerability; AI era requires it as fundamental capability.
- Services must implement aggressive rate limiting as agents can hammer APIs via parallelized sandbox execution.
- Workers/Deno/Monty represent first wave of primitives; expect proliferation as code becomes primary agent interaction method.

## MCP as Middleware Future
- MCP SDK will shrink to become lightweight middleware, natively integrated into major TypeScript frameworks by year-end.
- API services will expose MCP as simple boolean flag in Next.js/other frameworks alongside existing REST/GraphQL.
- Protocol becomes invisible plumbing rather than explicit integration, enabling thousand-endpoint exposure with programmatic tool calling.
