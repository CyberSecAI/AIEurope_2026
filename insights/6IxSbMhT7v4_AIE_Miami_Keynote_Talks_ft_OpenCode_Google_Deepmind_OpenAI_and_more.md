# Overview

## Summary
Multi-day AI engineering conference compilation featuring OpenCode, OpenAI, OpenRouter, Google DeepMind, and Langraph on coding agent productivity, taste, model ecosystems.

## Key Takeaway
AI coding velocity exposes product strategy weakness; friction previously protected teams from shipping bad ideas instantly.

# Insights

## AI Productivity Paradox (Dax - OpenCode)

- Engineering friction historically forced product/design validation before implementation, preventing premature feature shipping and technical debt accumulation.
- Token leaderboards measure wrong metric; shipping velocity without strategic filter creates bloated products nobody asked for or wants.
- Design now lags engineering for first time ever; prototypes ship faster than mockups can validate ideas or user workflows.
- Companies removing all process guardrails believing speed alone wins, but competitors with taste will outcompete raw velocity players.
- AI removes the natural pushback that saved teams from bad ideas; lazy engineer's "no" was product quality protection.

## Evidence-Based AI Development (Dexter/swyx - RPI Methodology)

- 85-instruction system prompts dilute model focus; they measured 200-token responses turning into 2000-token rambles with prompt bloat creep.
- Minimal context windows force better reasoning; stripped prompts from 85 instructions to 12 core rules, improving output quality significantly.
- RPI shifts when models change; every three weeks new model releases invalidate your carefully tuned prompts and workflows entirely.
- Agentic scaffolding beats mega-prompts for complex tasks; switching from one massive prompt to orchestrated smaller calls improved success measurably.
- Vibes-based development fails at scale; without measurement you'll spend months optimizing the wrong things while quality degrades silently.
- Document control flow explicitly before letting AI generate; pseudo-code architecture planning prevents spaghetti code and improves agent output quality.
- Human-in-loop reviews cost less than debugging autonomous mistakes; 30-second approval gates prevent hours of rollback and customer-facing bugs later.

## Taste Scaling with AI (Max - OpenAI Panel)

- Taste is knowing which 90% to throw away; AI generates infinite options but executives must rapidly identify the 10% worth building.
- AI amplifies both good and bad taste equally; teams with poor judgment ship terrible features 10x faster than before creating existential risk.
- Bottlenecks shift from implementation to decision-making; anyone can generate code but curating the right features is now the scarce skill.
- Exploration velocity creates option paralysis; generating 20 prototypes weekly requires stronger conviction frameworks to choose the winner quickly.
- Disagre

ement quality matters more with AI speed; fast shipping requires teams to debate direction harder before committing to wrong path.
- Background agents enable parallel exploration; running 100 experimental branches simultaneously requires new workflows for comparison and selection at scale.

## Model Ecosystem Dynamics (Shashank - OpenRouter)

- Model dominance rotates every 3-6 months; top model share dropped 30%+ as Claude, GPT, Gemini leapfrog in capabilities and preference.
- Agentic workloads concentrate on fewer models; tool-calling users show 40% higher model concentration than chat users across the ecosystem globally.
- Tool call failure rates collapsed in 2024; session failure dropped from 40% in August to under 10% as models improved tool-use reasoning.
- Real-world usage diverges from benchmarks; models ranking mid-tier on HumanEval dominate production traffic when latency and cost matter more.
- Breakout apps drive inference volume disproportionately; top 5 apps generate 45% of all API calls, making app distribution the new moat.
- Provider consolidation accelerating despite model proliferation; 60 providers and 300 models available but users default to 3-5 known endpoints.

## Multimodal AI Capabilities (Google DeepMind - AI Studio)

- Overly long prompts reduce image understanding; models perform better with concise image analysis requests than detailed multi-paragraph instructions for vision.
- Search grounding transforms generation quality; real-time web search integration prevents hallucinations and grounds factual responses in current information automatically.
- Nano models handle local inference well; on-device models like Gemma 2B achieve 40 tokens/second on consumer hardware enabling privacy-first applications.
- Audio reasoning requires different prompting; music and sound analysis needs temporal markers and explicit rhythm/melody decomposition instructions for accuracy.
- Transparent background generation is trivial now; what took designers hours in Photoshop happens in single prompt with modern vision models.

## Enterprise AI Governance (Anna - Langraph MCP)

- Unbounded AI access creates audit nightmares; snowflake permissions require human approval gates before SQL generation to prevent data leakage.
- Deterministic checkpoints enable workflow resumption; saving state at decision points allows human review without rerunning entire 20-minute agent pipelines.
- Tool call validation prevents production disasters; schema enforcement and dry-run modes catch 80% of errors before agents touch live databases.
- Reusable workflows beat one-off agents; templated patterns for intake-gather-generate-review reduce development time 90% for similar use cases organization-wide.
- Bounded work scope critical for governance; agents with clear input/output contracts and limited actions easier to audit and secure than autonomous systems.
- SOC2 compliance possible with AI agents; proper logging, approval workflows, and deterministic execution satisfy enterprise security requirements when designed intentionally.

## Coding Agents as Programming Paradigm (Ben Davis)

- Skills are shareable AI micro-apps; one developer's YouTube API integration becomes reusable tool for entire team through shared skill libraries.
- Agents enable non-coder contributions; product managers write natural language skills that become executable tools without touching Python or APIs directly.
- Cron job automation trivializes with agents; scheduling periodic API checks and notifications takes minutes instead of infrastructure setup hours.
- Tool registry democratizes capability sharing; central skill repository means discoveries propagate instantly across teams instead of siloed developer knowledge.
- Natural language replaces configuration files; describing desired behavior in plain English generates working code faster than YAML or JSON setup.
- Experimentation velocity transforms development; trying new API integration takes 5 minutes not 5 days, enabling rapid prototyping previously impossible economically.
