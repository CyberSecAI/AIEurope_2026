# Harness Engineering: How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI

## Overview

**Summary**: OpenAI engineer shares nine months of building software exclusively with AI agents, banning traditional code editors.

**Key Takeaway**: Code is free; optimize for human delegation and agent guardrails, not implementation.

---

## The New Software Engineering Paradigm

- **GPT 5.2 marked the inflection point**: models became isomorphic to human engineers in code production capability.
- **Implementation is no longer scarce**: every engineer has access to 5-5000 engineers worth of capacity constrained only by tokens.
- **Skill sets shift to systems thinking**: focus moves from coding to system design, delegation, and orchestration strategies.

## Scarce Resources in the Agent Era

- **Human time and attention are now precious**: move synchronous work to asynchronous agent-driven workflows for higher leverage.
- **Model context window requires management**: defer non-functional requirements until relevant, avoid overwhelming agents with upfront instructions.
- **P3 tasks now get done**: infinite parallel capacity means all backlog items can execute simultaneously instead of never.

## Making Codebases Agent-Native

- **Optimize repositories for agents first**: entry point is the agent harness, not developer environments or editors.
- **Enforce context efficiency through tests**: limit files to 350 lines, write tests that assert source code structure.
- **Make everything the same for predictability**: large-scale refactoring is free, so standardize patterns to reduce attention requirements.

## Prompt Injection as Infrastructure

- **Guardrails are prompts in disguise**: lints, test failures, reviewer agents, and error messages all inject prompts into workflow.
- **Error messages must provide remediation steps**: guide agents with actionable next steps, not just failure notifications.
- **Skills stack and compose well**: use agent-written prompts from OpenAI cookbooks to generate more prompts for local needs.

## Non-Functional Requirements Documentation

- **500 micro-decisions per patch require specification**: agents have seen all possible choices; documentation constrains them to acceptable ones.
- **Write down what good looks like**: ADRs, persona-oriented docs, and historical tickets teach agents team standards.
- **One expert lifts entire team**: a single QA plan spec means every agent trajectory gets good testing automatically.

## Review and Quality Assurance

- **Reviewer agents run continuously in CI**: security, reliability, and quality agents check every push against documented requirements.
- **Bespoke lints solve durable failure classes**: write custom ESLint rules for codebase-specific patterns like network retries.
- **Tests about source code enforce constraints**: verify package privacy, dependency edges, schema deduplication, and canonical utility usage.

## Workflow and Collaboration Strategies

- **GitHub PRs are collaboration hubs**: treat PRs like Google Docs where agents and humans comment, suggest, and iterate.
- **Agents make autonomous decisions on feedback**: implementation agents can acknowledge, defer, or reject review comments using reasoning.
- **Bias toward code acceptance over perfection**: avoid catastrophic failure modes where coding agents get bullied by reviewer feedback.

## Practical Getting Started Advice

- **Begin by increasing test coverage**: agents excel at reading code and writing behavior-asserting tests to build confidence.
- **Automate where you spend time waiting**: target CI delays, flaky tests, or slow human review cycles for delegation.
- **Don't over-engineer harnesses**: focus on surfacing right text at right time; model capability improvements won't obsolete good context management.
