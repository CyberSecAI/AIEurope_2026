# How to Build Agents That Run for Hours (Without Losing the Plot)

**Speakers:** Ash Prabaker & Andrew Wilson

## Key Insights

### Long-Running Agent Challenges
* Scaling agents from minutes to 12+ hour sessions requires addressing context management, planning, and self-judgment failures.
* Agents often "lose the plot" due to finite context windows and lack of persistence across long execution loops.

### Context Management (Rot & Anxiety)
* "Context Rot" causes agents to lose coherence as sessions deepen, leading to amnesia about initial goals or constraints.
* "Context Anxiety" occurs when models rush to finish a task as they approach the end of their token limit.

### Planning Primitives
* Standard models often struggle with one-shot planning; robust agents require iterative scaffolds that break complex tasks down.
* Using an agent SDK with first-class support for sub-agents and tool delegation helps maintain focus during multi-hour runs.

### Overcoming Coding Sycophancy
* Models are prone to judging their own output too leniently, often claiming a feature is "done" when half-baked.
* Harnesses must implement rigorous verification steps (like running tests or builds) rather than trusting the model's self-assessment.

### Scaffolding and Scaffolds
* Scaffolding (the code around the model) is as critical as the model weights for sustaining long-term agentic sessions.
* Evolution of scaffolds (like Claude Code) has enabled a shift from simple bash commands to days-long autonomous sessions.

### Co-Evolution of Models and Tools
* Model improvements and harness enhancements co-evolve; as models gain more internal capability, external scaffolds can become leaner.
* Integrating primitives like MCP (Model Context Protocol) and skills directly into the harness improves tool discovery and use.

### Verification-Led Iteration
* Long-running agents succeed by continuously verifying their work against the environment (e.g., using "computer use" to check UIs).
* A robust "feedback loop" within the scaffold ensures the agent can recover from errors without manual human correction.
