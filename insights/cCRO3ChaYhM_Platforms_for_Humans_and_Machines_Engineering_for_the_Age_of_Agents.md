# Platforms for Humans and Machines: Engineering for the Age of Agents

**Speaker:** Juan Herreros Elorza

## Key Insights

### Agentic Friction
* Human developers often tolerate broken pipelines and manual handoffs, but these "friction points" are fatal for AI agents.
* Best practices like self-service infrastructure are no longer optional; they are mandatory for agentic productivity and success.

### Self-Service Architecture
* Platforms must be fully automated to allow agents to provision resources without waiting for human intervention or approvals.
* Intuitive self-service flows prevent agents from getting lost in complex, multi-step resource acquisition processes across different teams.

### API-First Design
* Agents excel at calling well-defined APIs with schema validation rather than navigating graphical user interfaces or text documents.
* Every platform capability should be exposed via API or CLI to ensure discoverability and secure, credentialed access.

### Shifting Left for Agents
* Validation must happen locally and early; agents shouldn't wait for remote CI/CD failures to detect simple errors.
* Local iteration loops enable agents to debug and refine their work much faster than traditional remote-heavy development cycles.

### Machine-Readable Observability
* Traditional dashboards are for humans; agents need observability data like logs and metrics accessible through structured API endpoints.
* Closing the loop requires providing agents with the same telemetry humans use, but in formats they can programmatically consume.

### LLM-Optimized Documentation
* Documentation should be structured and placed next to the code to provide immediate, relevant context for working agents.
* Centralized documentation repositories should offer "bit-sized" API access instead of requiring agents to parse entire HTML pages.

### Agent-Specific Context
* Use specialized files like `agent.md` or `skills.md` to codify project-specific conventions, build instructions, and testing requirements.
* Providing precise success criteria within these files ensures the agent knows exactly when a task is completed correctly.
