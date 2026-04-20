# Code-Centric Agency (Code Mode)

## Summary
Shifting from simple JSON tool-calling to executable scripts allows agents to "inhabit" systems, drastically reducing latency and enabling native loops and state management.

## Key Takeaway
Empower agents with executable runtimes to move beyond simple reasoning and achieve concrete, verifiable system interaction.

# Insights

## Executable Runtimes
- Shifting from JSON tool-calling to executable scripts drastically reduces latency and token consumption for complex, multi-step workflows.
- Providing agents with a sandbox environment for running code allows them to perform tasks that require iterative loops and logical branching.
- Executable agents can self-correct by running their own generated code and observing the results in a closed feedback loop.

## System Inhabitation
- Agents "inhabit" systems by running programs against typed APIs, enabling native loops and state management in a single session.
- System inhabitation allows agents to maintain complex internal state across multiple steps without having to pass it back to the model.
- High-fidelity interaction with systems requires agents to have a grounded understanding of the specific environment and its available interfaces.

## Verifiable Implementation
- Executable agents bridge the gap between simple text reasoning and concrete, verifiable software implementation within secure runtime environments.
- Running generated code provides an empirical verification step that ensures the agent's actions are both correct and safe for the system.
- Integration with existing automated testing suites allows agents to validate their own changes against established project standards and requirements.

# Related Talks

- **[Code Mode — Sunil Pai, Cloudflare](../insights/8txf05vVVl4_Code_Mode_Sunil_Pai_Cloudflare.md)**
- **[Why and how you need to sandbox AI-Generated Code — Harshil Agrawal, Cloudflare](../insights/AHtGAgQ0Q_Q_Why_and_how_you_need_to_sandbox_AI_Generated_Code_Harshil_Agrawal_Cloudflare.md)**
