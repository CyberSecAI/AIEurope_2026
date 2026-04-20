# The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil

## Overview

### Summary
AI coding tools create productivity illusions while enabling faster technical debt accumulation and requiring intentional friction for quality control.

### Key Takeaway
Friction in AI-assisted development is necessary judgment, not waste to eliminate.

---

## The Productivity Paradox

- AI tools initially increased productivity and free time, but quickly became baseline expectations requiring faster shipping.
- Baseline shifted from competitive advantage to mandatory requirement, transforming fun into pressure and eliminating thinking time.
- High code output volume creates illusion of efficiency while reducing actual time for design and reflection.

## The Psychological Trap

- AI coding tools are addictive through variable reward patterns - never knowing if next prompt succeeds or fails.
- Engineers produce massive output volumes while being tricked into believing they're more efficient than they actually are.
- Difficult for both humans and agents to stop once in flow, leading to reading unnecessary files and uncontrolled exploration.

## Team Composition Shifts

- Engineers now have multiples of producing power compared to reviewing power, creating massive PR backlogs and review bottlenecks.
- Non-engineers (marketing, CEOs) now shipping code without carrying ultimate responsibility, expanding total code creators beyond accountable engineers.
- Code reviews increasingly skipped or rubber-stamped due to overwhelming volume, violating small PR best practices.

## Agent Code Quality Issues

- Agents optimize for making progress and passing tests, not for robust error handling or failure prevention.
- Agent-generated code creates more failure conditions than human code - reading defaults silently instead of failing fast explicitly.
- Agents lack emotional feedback that prevents humans from writing brittle code with try-catch blocks that hide problems.

## Code Entropy and Brittleness

- Agents create services that hobble along recovering from local failures instead of failing clearly, producing very brittle systems.
- Codebases quickly reach size and complexity where agents can no longer navigate effectively, duplicating functionality across files.
- Technical debt accumulates in days or weeks that would normally take months, making codebase understanding extremely difficult.

## Libraries vs Products

- Agents excel at library development with clearly defined problems, tight API constraints, and simple pluggable cores.
- Products are much harder due to interacting concerns - UI, permissions, feature flags, billing - impossible to fit in context windows.
- Agents locally reasonable but globally demented when facing product complexity, unable to understand entire system structure.

## Agent-Legible Codebase Design

- Codebases must be designed as infrastructure for agents, with modularization of components and code flow itself.
- Follow known patterns and lean into reinforcement learning rather than fighting it for scalability and better output.
- Push complexity to abstraction layers with simple cores, making code easier for both humans and agents to read.

## Mechanical Enforcement Strategies

- No bare catch blocks enforced via linting rules to prevent agents from hiding errors silently.
- Single query interface for all SQL to prevent agents hunting across codebase and missing critical locations.
- One primitives component library for UI consistency, no dynamic imports, unique function names for token efficiency.

## Advanced TypeScript Patterns

- Erasable syntax-only TypeScript mode eliminates transpiling friction, creating single source of truth between code and compiler.
- Agents better at finding errors when no confusion exists between source code and compiled output.
- Unique function names improve agent grep efficiency and reduce context window pollution from duplicate results.

## Human Judgment Triggers

- PR review extensions separate mechanical bugs (agent auto-fixes) from human judgment calls (database migrations, new dependencies, permissions).
- Database migrations require human review due to locks, production data size, and underdocumented permission implications.
- Dependency additions need human evaluation of maintainers, licensing, and strategic fit beyond agent's capability.

## Beneficial Use Cases

- Agents excel at reproduction cases when customers report issues, creating perfect starting points for exploration.
- Productive for prototyping different product directions as long as humans commit to thorough code review afterward.
- System architecture and reliability creation still require humans to go slow despite agent assistance.

## The Nature of Friction

- Friction traditionally viewed as obstacle to remove, but SLOs intentionally designed as friction for reliability decisions.
- Friction is physically necessary for steering - without it there's no directional control or quality judgment.
- Engineering teams need friction to decide reliability needs, service criticality, and appropriate staffing levels.

## The Call to Judgment

- Humans must feel the pain that agents don't experience and wake up when review is truly needed.
- Friction represents where human judgment, experience, and expertise should be inserted into AI-assisted development process.
- Speed benefits are real and addictive, but dangerous when relied upon for areas requiring careful thought.
