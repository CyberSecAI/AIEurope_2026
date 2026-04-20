# Skills at Scale

**Speakers:** Nick Nisi & Zack Poser (Applied AI, WorkOS)

## Portability & Efficiency
- **Portable Skills:** Treat agent capabilities as discrete, portable skills to avoid manual context reloading and maintain consistency across different projects.
- **Context Window Optimization:** Replace massive, static memory files with small, composable skills that activate only when needed to optimize the context window.

## Reliability & Determinism
- **Deterministic Logic:** Use scripts within skills to inject real-time, deterministic data into non-deterministic LLM conversations for more reliable outcomes.
- **Agentic DRY:** Apply the "Don't Repeat Yourself" (DRY) principle by encoding common workflows and conventions into reusable skills for all agents.

## Project Standards
- **Hyperspecific Feedback:** Even 30 lines of specific markdown in a skill can transform generic agent advice into hyperspecific project-aligned guidance.
- **Convention Enforcement:** Automate the enforcement of project conventions, such as semantic commits or routing patterns, through targeted agent skills.

## Maintenance & Onboarding
- **Addressing Drift:** Use skills to detect and correct "readme drift" and other documentation inconsistencies automatically during the development process.
- **Repo Onboarding:** Streamline new team member onboarding by using skills to provide instant, automated "roasts" or reviews based on internal standards.
