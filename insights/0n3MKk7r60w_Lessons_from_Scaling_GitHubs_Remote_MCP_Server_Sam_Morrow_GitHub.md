# Overview

## Summary
Sam Morrow from GitHub shares lessons from scaling GitHub's remote MCP server to 7 million weekly tool calls.

## Key Takeaway
Context reduction and security are essential when scaling remote MCP servers for real-world production use.

# Insights

## Tool Overload and Context Management
- Adding 100+ tools degraded agent performance; agents got confused and context windows blew out faster.
- Reduced context by 49% by focusing tools on general use cases, then grouped CRUD operations further.
- Everyone uses default settings despite elegant configuration options; design for defaults, not customization.

## Tool Design and Evaluation
- Test tool descriptions against each other, not in isolation, to prevent fighting for agent attention.
- Encode agent intent into tool surface by making 5 API calls server-side to reduce round trips.
- Tool output optimization yielded 75% token reduction by tailoring exactly what data each tool returns.

## Security and Authentication
- Plain text access tokens stored where agents can access them are the biggest security vulnerability currently.
- OAuth with step-up challenges enables clean installs with minimal permissions, expanding scope only when needed interactively.
- Filter tools automatically by token scopes and user type to eliminate constant failure sources preemptively.

## Dynamic Client Registration Challenges
- Dynamic client registration creates unbounded app database growth, unreliable identity, and impossible rate limit bucketing.
- GitHub rejected dynamic client registration as well-intentioned mistake; client ID metadata is the pragmatic path.
- MCP spec moved away from dynamic registration; practical experience showed theoretical elegance doesn't scale.

## Stateless Architecture at Scale
- Create brand new server instance per request with tools added dynamically based on authentication and policies.
- Serving 7 million tool calls weekly without session affinity by treating each request as independent operation.
- Redis sessions only track self-reported client identity for understanding usage patterns, not maintaining state.

## Prompt Injection and Security Trade-offs
- Prompt injection exfiltration attacks apply to almost every agent setup, not just GitHub's MCP implementation.
- Agent utility directly conflicts with security; no solved solution exists for the lethal trifecta yet.
- Wildly different user risk profiles range from air-gapped enterprise to full-access hobbyists; one size doesn't fit.

## Human-in-the-Loop Design Patterns
- MCP apps feature enables editing AI-generated issues before posting to avoid bot-generated appearance in communities.
- Insiders mode deploys experimental features via feature flags to users willing to test bleeding-edge functionality.
- Review-before-submit prevents social reputation damage while maintaining agent utility for professional open source contributors.

## Future Vision and Compositional Tools
- Thousands of tools will become normal soon via approaches like bash-style piping or Anthropic's tool search API.
- Server discovery and OAuth setup will become autonomous; users won't need to know what MCP is.
- Tool use will become compositional with streaming data through pipelines, enabling more complex agentic workflows.
