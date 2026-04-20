# Building Your Own Software Factory

**Speaker:** Eric Zakariasson (Engineer, Cursor)

## Autonomy & Throughput
- **Autonomy Levels:** Progress from "spicy autocomplete" to "dark factories" where agents autonomously ship and test code with minimal human oversight.
- **Consistent Throughput:** Leverage the 24/7 availability of agent swarms to achieve massive throughput and consistent code output without human fatigue.

## Codebase Architecture
- **Modular Architecture:** Structure codebases modularly to allow agents to discover relevant files through simple directory listing rather than exhaustive global searches.
- **Co-location Advantage:** Co-locate related code to reduce the cognitive (and token) distance for agents, significantly improving their ability to understand and modify features.

## Safety & Governance
- **Dynamic Rules:** Avoid bloated, static rule sets; instead, let rules emerge dynamically as "Standard Operating Procedures" (SOPs) based on observed agent failures.
- **Sensitive Guardrails:** Implement strict hooks to prevent agents from modifying critical security logic, such as encryption or authentication, where mistakes are most costly.

## The Human Role
- **Factory Management:** Shift your role from manual coder to "factory manager," focusing on providing clear intent, goals, and high-level architectural constraints.
- **Onboarding Symmetry:** A codebase that is easy for humans to onboard is naturally easier for agents to navigate and master quickly.
