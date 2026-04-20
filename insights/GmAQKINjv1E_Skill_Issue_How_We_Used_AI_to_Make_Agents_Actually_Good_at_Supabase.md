# Overview
## Summary
Pedro Rodrigues details how Supabase utilizes "Skills" to improve agent performance through progressive disclosure, structured instructions, and environment-aware scripts for better agentic experiences.

## Key Takeaway
Skills solve "context bloat" by providing agents with structured, environment-aware information exactly when they need it.

# Insights
## Developer Agent Experience (DAX)
- DAX focuses on optimizing how AI agents interact with product ecosystems, analogous to traditional Developer Experience (DX).
- Making products "agent-friendly" requires building intuitive interfaces and tools specifically designed for LLM consumption.
- Improving the agentic experience directly correlates to higher task success rates and more reliable automation in production.

## The Concept of "Skills"
- Skills are structured folders containing a `skill.md` file, providing high-level instructions and tool references for agents.
- They act as a "secret sauce" for improving agent performance by encapsulating repeated workflows and custom information.
- Unlike generic prompts, skills provide a permanent, versionable foundation for specific agent behaviors and capabilities.

## Progressive Disclosure
- Progressive disclosure prevents model context bloat by loading only essential metadata initially rather than entire files.
- The agent uses high-level descriptions to decide which deep-dive information or sub-files to load during execution.
- This technique preserves the model's "reasoning budget" by keeping the active context focused on the current sub-task.

## Skill File Structure
- The `skill.md` front matter (YAML) contains critical metadata like the skill name and a concise agent-facing description.
- Skill files serve as an "index on steroids," providing a graph-like structure that references other markdown and script files.
- Referencing files within other reference files allows for complex, hierarchical knowledge structures that agents can navigate autonomously.

## Skills vs. MCP
- MCP is ideal for remote integrations and exposing individual tools without requiring a local execution environment.
- Skills are better for defining complex workflows and providing deep, structured context that doesn't fit into tool descriptions.
- Using both in tandem allows for a "best of both worlds" approach: remote tool access plus local workflow intelligence.

## Environment-Aware Scripts
- Skills can include local bash or Python scripts that run directly on the machine where the agent is operating.
- These scripts enable agents to perform direct actions on the local filesystem, network, or system processes.
- Script-based tools are inherently tied to the host OS, requiring cross-platform considerations for widely distributed agentic systems.

## Skill Testing & Evaluation
- Testing skills begins with manual verification of agent behavior before moving to automated LLM-based evaluation frameworks.
- Automated evaluations (Evals) are essential for ensuring that skill updates don't introduce regressions in agent reasoning or accuracy.
- Lessons from production show that robust testing is the only way to maintain reliable agentic performance at scale.

## Lessons from Production
- Transitioning from simple chatbots to agentic systems at Supabase required moving logic from prompts into reusable skills.
- Production agents benefit from "low-noise" instructions that prioritize specific, actionable workflows over broad general knowledge.
- Continuous refinement of skill descriptions is necessary as models evolve and their interpretation of instructions changes.
