# Overview

## Summary
Karan Sampath from Anthropic discusses scaling MCP to enterprise, why gateways solve critical infrastructure problems.

## Key Takeaway
Gateways enable decentralized MCP development by establishing one blessed root of trust.

# Insights

## Enterprise MCP Bottleneck
- Security teams block MCP adoption due to lack of observability, access control, and credential management infrastructure.
- Enterprises stuck with handful of tools fundamentally restricts protocol potential and limits agent effectiveness across organization.
- Paper cuts in enterprise deployment require upfront investment to solve, preventing teams from building their own servers.

## Gateway Architecture Pattern
- Gateway acts as middleman handling auth, access control, observability, routing, tunneling, and registry for all MCP servers.
- Teams focus solely on business logic; gateway abstracts away security, scaling, authentication, and deployment complexity entirely.
- Single CLI enables any team to deploy new MCP servers without repeated security reviews or infrastructure work.

## Root of Trust Strategy
- Security teams should bless one platform instead of vetting each individual MCP server implementation separately.
- Gateway establishes centralized trust root allowing decentralized server development across all teams without bottlenecking security reviews.
- Enterprises successfully using this pattern explore MCP usage exponentially, making agents significantly more powerful organization-wide.

## Separation of Concerns
- Agent harness must be decoupled from data layer to enable flexibility across multiple agent surfaces.
- Gateway makes infrastructure invariant to new surfaces; same servers work across Claude.ai, Code, and Work simultaneously.
- Enterprises gain flexibility to choose in-house versus external agents without restructuring their entire MCP infrastructure.

## Delegation and Access Control
- Delegated identity for users and agents becomes critical as agents require novel identity definitions beyond users.
- Role-based access scoping enables read-only access for some teams while restricting write operations to specific groups.
- Gateway provides single access control panel across all agents and MCPs instead of per-server configurations.

## Faster Iteration Velocity
- Teams iterate workflows rapidly without repeated security reviews once gateway receives initial blessing from security team.
- Legal team can modify contract review MCP independently using coding agents without depending on technical teams.
- Decentralized development compounds organizational value; each new MCP benefits all agents exponentially rather than individually.

## Standard Enterprise Primitives
- Gateway encodes standard operating procedures and primitives that all new MCP servers must adhere to.
- Pluggable credential systems allow company-wide, team-wide, or service account authentication patterns based on use case.
- Enterprises define expected tools, forbidden operations, and compliance requirements centrally rather than per-server enforcement.

## Scalability and Security
- Gateway handles tens to hundreds to thousands of agents requesting hundreds of MCP servers intelligently.
- Encrypted secured tunnels between untrusted remote clients and internal MCP servers prevent data exfiltration risks.
- Enterprises derive exponential value only when using real sensitive data, not toy examples with play data.
