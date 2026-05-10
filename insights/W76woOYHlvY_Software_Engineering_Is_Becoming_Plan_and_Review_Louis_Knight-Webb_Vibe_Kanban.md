# Overview

## Summary
Louis Knight-Webb, founder of Vibe Kanban, discusses shifting software engineering roles toward planning and reviewing AI-generated code.

## Key Takeaway
Five minutes of upfront planning saves thirty minutes reviewing AI-generated code afterward.

# Insights

## The Shift in Engineering Time Allocation
- AI coding tools have displaced coding time to planning and reviewing, not created free time.
- You gain roughly 20 minutes back per 30 minutes of coding, but remainder shifts to other activities.
- The ratio is accelerating: GitHub Copilot completed lines, Cursor completed files, Claude Code completes multi-file features.

## Plan-Heavy vs Review-Heavy Workflows
- Plan-heavy approach: invest time upfront with comprehensive specs, interrogative models, and exhaustive edge case elimination.
- Review-heavy approach: minimal planning, YOLO execution, multiple back-and-forth correction cycles with agent.
- Plan-heavy always saves human time despite higher upfront cost; context switching during review is expensive.

## Work Type Determines Planning Approach
- Front-end feature development requires review-heavy workflow due to stateful interactions, animations, and edge cases.
- Back-end development and migrations can be fully test-driven with minimal human-in-loop intervention.
- Migration and refactoring work should be completely automated with comprehensive test coverage upfront.

## The Five-Minute Execution Threshold
- When agent execution exceeds five minutes, human behavior must fundamentally change from synchronous to asynchronous.
- Parallelism becomes essential: run multiple agents simultaneously to avoid waiting, terminal-maxing approach.
- Future frontier: agents taking 20+ minutes will require complete workflow redesign around batch review.

## AI QA as the Next Breakthrough
- Playwright/Chrome MCP for front-end QA is demonstrated but not yet mainstream in production workflows.
- When AI can reliably QA front-end work by running and clicking through applications, most review back-and-forth disappears.
- Most current review cycles could be automated if models could verify their own front-end changes.

## The New Engineering Interface Requirements
- Tools must embrace managing multiple parallel work streams, not single deep-focus coding sessions.
- Interfaces should maximize agent run time before yielding to human, avoiding constant 30-second context switches.
- Must integrate planning assistance, QA tooling, code review helpers, and deployment shepherding in single workflow.

## Startup Monetization Realities
- Only two viable paths in AI coding tools: selling to enterprise or reselling tokens.
- Users spending $30 on workflow tool while spending $3,000 on underlying agent is unsustainable economics.
- Mature markets where you're competing for eighth place are not worth the founder stress.

## Focus-Maxing for Parallel Workflows
- Engineers must transition from deep focus on one task to managing multiple concurrent agent tasks.
- Human brains cannot handle context switching every 30 seconds; tools must batch notifications and reviews.
- Shepherding changes from completion to deployment becomes significant workflow component requiring automation.