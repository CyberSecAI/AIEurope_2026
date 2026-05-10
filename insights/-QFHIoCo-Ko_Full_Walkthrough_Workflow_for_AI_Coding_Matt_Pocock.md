# Overview

## Summary
Matt Pocock presents a systematic workflow for AI-assisted coding, emphasizing software engineering fundamentals still apply when working with AI agents.

## Key Takeaway
Design alignment before implementation: reach shared understanding with AI through structured questioning, not passive spec-writing.

# Insights

## LLM Constraints & The Smart Zone

- LLMs have a smart zone around 100k tokens; beyond that attention degrades quadratically making decisions unreliable.
- Size tasks to stay within smart zone by breaking large work into smaller isolated sessions, not endless continuation.
- Clearing context resets to base state better than compacting, ensuring consistent starting conditions for each task.

## The Grill Me Approach

- Interview yourself relentlessly before coding to reach shared design concept with AI, not just produce planning documents.
- Alignment phase must be human-in-loop; implementation can become AFK task once destination is clearly defined.
- Recommended AI responses reveal gaps in your thinking; accepting them speeds alignment more than debating details.

## Avoiding Specs-to-Code Trap

- Specs-to-code workflow fails because code is your battleground; you must maintain handle throughout entire process.
- Keep code in mind during planning by proposing modules to modify, not treating specs as abstract documents.
- Reviewing AI-generated PRDs wastes time; if shared understanding exists through grilling, summarization quality is already proven.

## Product Requirements Documents

- PRDs document destination not journey; define user stories and acceptance criteria as testable endpoints for implementation.
- Implementation decisions should specify which modules change, linking abstract requirements directly to codebase architecture from start.
- Testing decisions belong in PRD to prevent post-implementation scrambling; define verification approach before writing code.

## Human vs AFK Tasks

- Planning and alignment are human-in-loop tasks requiring active participation; trying to automate creates misalignment downstream.
- Implementation becomes AFK-capable once destination is precisely defined; agent can execute while you're away from keyboard.
- Pair programming with AI works when domain expert and AI together answer questions neither has alone.

## Context Window Economics

- Larger context windows mostly ship more dumb zone, not smarter reasoning; retrieval improves but coding quality doesn't.
- Monitor exact token usage constantly; essential observability for knowing when approaching performance degradation threshold before errors occur.
- Sub-agents isolate token-heavy exploration in separate context, reporting summaries back to keep orchestrator's context lean and smart.

## Repository as Agent Foundation

- Bad codebases make bad agents; garbage code produces garbage AI output regardless of prompting sophistication employed.
- Own your planning stack rather than outsourcing to frameworks; understanding internals enables debugging when approaches fail.
- Understanding code and TypeScript deeply makes you better at AI development, not obsolete as tools improve capabilities.

## Workflow Structure

- Multi-phase plans are loops in disguise; recognize iterative patterns and design for phase N, not hardcoded sequences.
- Ralph method specifies destination then makes small incremental changes, but lacks structure for complex requirements needing decomposition.
- Write grill-me first to align, write-PRD to document, then implement with clear destination eliminating ambiguity during execution.
