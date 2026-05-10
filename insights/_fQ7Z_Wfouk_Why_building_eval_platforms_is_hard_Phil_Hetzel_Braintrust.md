# Overview

## Summary
Phil Hetzel from Braintrust explains the technical and organizational challenges of building production-grade evaluation platforms for AI agents.

## Key Takeaway
Eval platforms are fundamentally systems problems, not just UI challenges requiring specialized data infrastructure.

# Insights

## Maturity Stages of Eval Platforms
- Spreadsheet-based evals enable documentation but actively discourage experimentation by making comparison between experiments cumbersome and slow.
- Vibe-coded custom UIs improve accessibility for non-technical users but remain reporting tools rather than true experimentation platforms.
- Playground features unlock real iteration when users can modify agent parameters and immediately compare configurations side-by-side.

## The Observability-Eval Flywheel
- Production trace data reveals failure modes that synthetic test cases miss, making observability essential for discovering what to eval.
- Connecting observability to eval creates continuous improvement loops where real usage informs offline experimentation which improves production performance.
- Customer discovered this pattern themselves by piping production traffic into eval databases hourly, prompting Braintrust to build native support.

## Multi-Persona Collaboration Requirements
- Eval platforms must serve engineers, domain experts, and non-technical stakeholders simultaneously since agent quality requires diverse expertise types.
- Non-technical users with domain knowledge and user proximity provide critical insights but won't engage with spreadsheet-based or code-heavy eval workflows.
- Team sport dynamics mean platforms that only serve one persona type will miss essential perspectives on agent behavior.

## Unique Data Infrastructure Challenges
- Agent traces combine high velocity, massive size (10-20MB spans vs typical kilobyte spans), and semi-structured text requiring specialized storage solutions.
- Traditional databases fail because LLM traces need both low-latency individual retrieval and high-performance aggregate analytics across unstructured text simultaneously.
- Full-text search across millions of traces is a functional requirement, not a nice-to-have, making standard observability tools inadequate.

## Query Pattern Complexity
- Two contradictory access patterns must coexist: instant visibility for debugging production issues and deep analytical queries over historical aggregate data.
- Braintrust's initial architecture with ClickHouse, custom DSL, and DuckDB browser layer worked initially but collapsed under real customer scale.
- SQL queryability becomes critical for headless use cases where coding agents need to extract patterns from eval data autonomously.

## Experimentation vs Documentation Distinction
- Early-stage eval platforms document what happened rather than enabling rapid iteration, slowing the feedback loop engineers need for improvement.
- True experimentation requires sandboxed parameter tweaking, automatic comparison scoring, and side-by-side configuration analysis built into the workflow itself.
- Analytics must surface both technical metrics and functional behavior scores to support different stakeholder decision-making needs simultaneously.

## Future-Proofing for Agentic Workflows
- Building for agent-readable interfaces (not just human UIs) is essential as coding agents become primary consumers of eval platforms.
- Topic modeling and unknown-unknown discovery must be automated since engineers can't manually review millions of production traces for patterns.
- AI proxies enabling automatic tracing remove instrumentation burden and enforce governance centrally rather than relying on developer discipline.

## Systems Over Surfaces
- The UI of eval platforms is easy to vibe code, but the data layer supporting scale and functionality is exponentially harder.
- Non-functional requirements like RBAC, data masking, and multi-tenancy become blockers at enterprise scale regardless of feature completeness.
- Maintenance burden grows continuously as the industry evolves, making build-vs-buy calculations increasingly favor specialized platforms over custom solutions.
