# Viktor — AI Coworker That Lives in Slack

**Speaker:** Fryderyk Wiatrowski (Co-founder, Viktor)

## The AI Employee Concept
- **AI Employee Paradigm:** Shift from isolated web-app agents to "AI employees" that live where humans work, like Slack, to feel like true teammates.
- **Slack-Native Interface:** Avoid building custom web apps; instead, integrate agents directly into communication tools like Slack to reduce friction and increase adoption.

## Context & Tooling
- **Horizontal Context:** Unlike specialized human roles, AI employees can maintain horizontal context across the entire company, from codebase to marketing strategy.
- **Inherited Permissions:** Simplify team onboarding by allowing AI employees to inherit permissions from a single integration connection, making tools instantly accessible.

## Scalability & Proactivity
- **Memory Scalability:** Managing memory for hundreds of users requires advanced architectures to prevent clutter and ensure relevant context is retrieved without leaking data.
- **Proactive Agency:** Move beyond reactive chat interfaces to proactive agents that analyze tool context and autonomously propose necessary tasks to human teammates.

## Architecture & Reliability
- **Context Isolation:** Implement robust permission structures to prevent sensitive data leaks between department-specific channels and private messages in multi-user environments.
- **Compounding Reliability:** Multi-step agent loops suffer from compounding failure rates; optimize for direct tool/API calling over fragile browser-based interactions.
