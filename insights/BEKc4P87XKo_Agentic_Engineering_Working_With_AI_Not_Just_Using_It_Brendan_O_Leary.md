# Overview
## Summary
Brendan O'Leary defines "Agentic Engineering" as a collaborative paradigm where engineers act as directors for AI agents, emphasizing context management and human judgment over simple automation.
## Key Takeaway
Treat AI agents as high-speed, judgment-free junior developers that require careful context engineering to remain effective and accurate.

# Insights
## Agentic Paradigm
- Agentic engineering shifts AI from a simple auto-complete tool to a collaborator capable of executing complex, multi-step tasks.
- Successful collaboration requires moving beyond just "using" machines to actively "working with" them through strategic task direction.

## The Junior Developer Model
- Conceptualize AI agents as incredibly fast, ego-less junior developers who possess vast knowledge but lack critical business judgment.
- Agents will confidently produce technically correct but contextually wrong code if not guided by an engineer’s architectural experience.

## Context Engineering
- Context engineering is the delicate art of filling the model’s window with only the essential information for the current step.
- Overfilling the context window past 50% capacity often leads to quality degradation and significantly increases operational token costs.

## Managing Context Poisoning
- Outdated comments or failed debugging paths can "poison" the context, causing the agent to repeat previous mistakes or lose focus.
- Start fresh sessions immediately when an agent goes "off the rails" to prevent negative patterns from compounding in the history.

## Selective Information Loading
- Use memory files like agents.md or selective file @mentions to provide the agent with targeted, relevant project context.
- Disabling unnecessary MCP servers prevents the context window from becoming cluttered with irrelevant tool definitions and data.

## Workflow: Research-Plan-Implement
- Avoid jumping straight to code; instead, follow a structured "Research, Plan, Implement" loop to minimize wrong assumptions and rework.
- Require the agent to summarize its understanding of the problem and the proposed plan before allowing it to execute changes.

## Human-in-the-Loop Judgment
- The engineer’s primary value in the agentic era is providing the business context and judgment that LLMs fundamentally lack.
- Directing the work means knowing exactly what to hand off to the agent and what critical logic to retain personally.

## Scaling with Parallel Agents
- Isolate tasks by splitting work across multiple parallel agents or sessions to prevent information overload and maintain high output quality.
- Use one agent to summarize long sessions into concise prompts for the next, ensuring a clean transfer of relevant knowledge.
