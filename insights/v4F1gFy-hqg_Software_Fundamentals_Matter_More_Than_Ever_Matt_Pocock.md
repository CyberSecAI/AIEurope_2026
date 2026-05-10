# Overview

## Summary
Matt Pocock, teacher and AI coding expert, argues software fundamentals are more critical now than ever in the AI era.

## Key Takeaway
Good codebases amplify AI effectiveness; bad code compounds into exponentially worse results through entropy.

# Insights

## Design Concept Alignment

- AI and humans must reach shared understanding before implementation to avoid misalignment and wasted iterations.
- Use "Grill Me" skill to force AI through 40-100 questions until true design concept emerges from conversation.
- The design concept is ephemeral and invisible; you cannot just put it in a markdown file.

## Ubiquitous Language

- Create explicit markdown glossary of domain terminology shared between developer, AI, and code to reduce verbosity.
- Ubiquitous language reduces AI thinking overhead, making implementation align better with actual plans and reducing token waste.
- DDD principles solve the domain expert communication gap that now exists between you and your AI assistant.

## Specs-to-Code Fallacy

- Repeatedly running AI compiler on specs without reviewing code produces progressively worse output through software entropy.
- Code is not cheap; bad code is the most expensive it has ever been because it prevents leveraging AI's full potential.
- Ignoring code quality while relying on AI regeneration is just vibe coding with extra steps.

## Feedback Loops and Speed Limits

- AI outpaces its feedback loops by producing massive code changes before type-checking, testing, or browser verification.
- Rate of feedback is your speed limit; LLMs outrun their headlights when not forced into incremental steps.
- Use TypeScript, automated tests, browser access for frontend, and TDD to constrain AI into deliberate small iterations.

## Deep Modules Over Shallow Modules

- Deep modules hide complexity behind simple interfaces, making codebases navigable for both AI and human cognition.
- Shallow modules create fragmented tiny blobs forcing AI to traverse dependencies it cannot fully understand or track.
- Use "Improve Codebase Architecture" skill to wrap related code into testable deep modules with controlled interfaces.

## Test-Driven Development Constraints

- TDD forces AI into small deliberate steps: write test, make it pass, refactor for design considerations.
- Testing difficulty correlates directly with codebase quality; good codebases are easy to test at module boundaries.
- Design interfaces yourself, delegate implementation to AI, then verify from the outside through boundary tests.

## Cognitive Load Management

- Shallow module architectures exhaust your brain because both you and AI must hold fragmented information simultaneously.
- Deep modules act as gray boxes you can ignore internally if the interface is well-designed and tested.
- Treat non-critical modules as black boxes tested from boundaries, reserving mental energy for strategic architecture decisions.

## Strategic vs Tactical Roles

- AI excels as tactical on-the-ground programmer; humans must provide strategic architectural thinking and design investment.
- Invest in system design every single day; specs-to-code approach divests from design, guaranteeing long-term failure.
- Software fundamentals from 20+ year-old books provide the strategic framework AI cannot replace or generate alone.
