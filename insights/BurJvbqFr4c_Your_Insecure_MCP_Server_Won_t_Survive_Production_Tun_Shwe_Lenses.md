# Overview
## Summary
Tun Shwe from Lenses discusses the critical security challenges of deploying MCP (Model Context Protocol) servers in production, advocating for a product-engineering approach to secure agentic design.
## Key Takeaway
Secure agentic design requires treating MCP servers as specialized interfaces where design choices directly determine the system's security posture.

# Insights
## The Security Shadow
- Every design decision in an MCP server casts a "security shadow" where poor architecture creates immediate vulnerabilities for agent exploitation.
- Robust security cannot be bolted on later; it must be an inherent part of the product engineering process for agentic interfaces.

## Surface Area Reduction
- Shrink the attack surface by squashing fine-grained operations into coarse-grained tools that produce a single, well-defined outcome.
- Fewer tools mean fewer "doors" for attackers to probe, simplifying permission checks, audit logging, and authorization enforcement.

## Schema-Level Constraints
- Constrain all tool inputs at the schema level using enums or strict typing libraries like Pydantic to prevent command injection flaws.
- Rejecting free-form nested payloads ensures that unconstrained strings cannot be passed downstream to vulnerable shells, query engines, or APIs.

## Defensive Documentation
- Treat tool descriptions as a defensive layer; clear and unambiguous instructions prevent malicious neighboring servers from "shadowing" your tools.
- Complete documentation crowds out the space for tool poisoning, where attackers embed hidden, malicious instructions inside invisible tool descriptions.

## Minimal Payload Responses
- Strip all tool responses to the absolute minimum data required for the agent’s immediate task to prevent context oversharing.
- Oversharing PII, credentials, or internal system details turns the agent’s context window into a high-risk liability for prompt injection.

## Blast Radius Minimization
- Scope permissions at the individual tool and resource level rather than the session level to limit the impact of a compromise.
- Use read-only annotations and convert non-destructive tools into MCP resources to enforce clear operational boundaries for the agent.

## The Production Security Cliff
- Moving from local StdIO to remote HTTP (SSE) transport introduces a "security cliff" requiring immediate mastery of OAuth, TLS, and CORS.
- Standard IO transport fails under concurrency; production-grade MCP requires a robust authorization server and horizontally scalable HTTP infrastructure.

## Dynamic Client Registration
- The unbounded nature of MCP clients makes traditional pre-registration impossible, necessitating the use of dynamic client registration for OAuth flows.
- Dynamic registration allows diverse clients like Cursor or CLI tools to self-register and obtain short-lived, scoped tokens for secure access.
