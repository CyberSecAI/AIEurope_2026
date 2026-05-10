# Overview

## Summary
Patrick Debois from Tessl presents Context Development Lifecycle framework for treating AI coding context with software development rigor.

## Key Takeaway
Context is becoming code; apply SDLC discipline to testing, distributing, and optimizing context for agents.

# Insights

## Context as Code Transformation
- Complex code can transform back into skills: onboarding agents with multi-ecosystem support solved via workflow context, not code.
- Voice coding generates more elaborate context than typing, producing better agent instructions without additional cognitive effort.
- Skills replace thousands of lines of code: describe detection workflow steps instead of coding all package manager variations.

## Testing Context Like Code
- Context needs validation layers: format linting, comprehension checking via Grammarly-style LLM feedback, and behavioral evals.
- LLM-as-judge tests verify context rules: check if agent follows conventions like API prefix requirements across code changes.
- Run evals multiple times for error budgets: undeterministic outputs require probabilistic pass rates, not binary success/fail.

## Context Distribution and Packaging
- Package context like libraries: install skills across projects with registries, versioning, and dependency management for reusable workflows.
- 99.9% of public skills are low quality; evaluate with tests before using third-party context packages.
- Context dependency hell is inevitable: conflicting instructions from multiple skills will require resolution strategies like code libraries.

## Security and Observability
- Context needs security scanning: credentials, prompt injections, and third-party risks must be detected before agent loads files.
- Context filters act as WAFs: block malicious patterns before agent.md/skill.md files load, since sandboxes can't prevent initial context injection.
- AI SBOMs track context provenance: capture which model built the skill, with what data, to trace security lineage.

## Feedback Loops for Context Improvement
- Agent logs reveal missing context: surface what agents couldn't do to create team-wide context improvements automatically.
- PR feedback signals context gaps: incomplete reviews indicate missing instructions; fix context rather than argue on PRs.
- Production instrumentation creates test cases: capture input/output failures to auto-generate evals preventing future context-caused bugs.

## Organizational Context Scaling
- Individual loop: create and test context locally with rapid iteration and personal optimization.
- Team loop: share context via git, make adding missing context a reflex action across team members.
- Enterprise loop: aggregate agent logs at scale to identify common gaps and distribute fixes organization-wide automatically.

## Context Engineering Mindset
- LLMs are engines needing quality fuel: optimize context since you control it, unlike the underlying model capabilities.
- Spend time writing rigorous evals: testing context thoroughly requires as much effort as writing good code initially.
- Consistency as evaluation metric: run same prompt multiple times; high variation indicates poor context quality needing refinement.
