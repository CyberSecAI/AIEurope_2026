# Overview

## Summary
Louis-François Bouchard, Paul Iusztin, and Samridhi present a hands-on workshop on building production-ready deep research agents using MCP and agentic workflows.

## Key Takeaway
Choose simplest solution first; avoid agent overhead when deterministic workflows suffice for predictable tasks.

# Insights

## Architecture Decision-Making

- Start with simple prompts; only add workflows when context or routing needed, agents when dynamic branching required.
- Most client "agent" requests are actually simple sequential workflows; building agents adds unnecessary cost and complexity overhead.
- Context window budget matters more than limit; performance degrades around 200K tokens due to lost-in-middle problem.

## Agent vs Workflow Design

- Agents need autonomous action and environmental reactivity; workflows execute predetermined steps regardless of tool count or complexity.
- Tools can encapsulate specialist logic with own prompts, validation, and LLM calls without multi-agent coordination overhead.
- Split systems when research needs flexibility but writing needs constraints; don't force same architecture for opposing requirements.

## Deep Research Implementation

- Use MCP servers to expose tools, prompts, and resources; tools do actions, prompts guide behavior, resources provide data.
- Progressive disclosure in skills loads only name and description initially, expands on use, then wipes from context automatically.
- Store intermediate results in memory folders for debugging and verification; third tool reads consolidated output from previous tools.

## Content Quality Control

- AI-generated content needs human-written guidelines specifying angle, audience, key points, tone, and character limits to avoid slop.
- Generating multiple post versions with refinement loops significantly outperforms single-pass generation for avoiding generic AI patterns.
- Explicit constraints in prompts override default profiles; freedom without guidance produces meaningless content regardless of model capability.

## Model and Tool Selection

- Gemini handles YouTube URLs natively without downloading videos; use API capabilities before building custom extraction pipelines.
- Fast MCP library hides protocol complexity; focus on tool definitions with name, arguments schema, and implementation function.
- Use Firecrawl for agentic scraping on dynamic sites; simple scraping fails on JavaScript-heavy or anti-scraping protected websites.

## Evaluation Strategy

- Build eval datasets with train/dev/test splits; perfect dev score signals overfitting unless test score matches within margin.
- LLM-as-judge needs calibration on 20-30 dev samples with human labels before production; five samples insufficient for reliability.
- F1 score dynamics between dev and test reveal overfitting; absolute score value depends on your data quality standards.

## Observability and Debugging

- Threads capture conversation flows, traces capture individual tool/LLM calls; monitoring both reveals patterns invisible in terminal logs.
- Track cost per model, latency per operation, and token usage at granular level; aggregate metrics hide optimization opportunities.
- Online evaluation runs judges on production traces continuously; simulated scenarios validate judge calibration before deployment mistakes.

## Production Considerations

- MCP servers distribute business logic at scale; skills personalize usage but become dependency nightmares without cohesive platform.
- Skills work for local hacks; MCP servers required when distributing to teams needing credentials, dependencies, and consistent environments.
- Human-in-loop essential for content creation; automation accelerates research but connection and relatability still require human touch.
