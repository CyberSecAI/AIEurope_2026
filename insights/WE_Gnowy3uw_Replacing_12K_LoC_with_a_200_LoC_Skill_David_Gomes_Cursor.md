# Overview

## Summary
David Gomes from Cursor describes replacing 15,000 lines of complex worktree infrastructure with 200 lines of markdown skills.

## Key Takeaway
Skills as prompts can replace thousands of lines of code with better flexibility and maintainability.

# Insights

## Skill-Based Architecture

- Replaced 15K lines of worktree code with 200 lines markdown by leveraging agent skills and sub-agents primitives.
- Commands stored server-side allow instant prompt iteration without requiring user app updates, enabling continuous improvement without releases.
- Advanced power-user features benefit from reduced code complexity since maintenance cost outweighs usage by small user base.

## Model Trust vs Hard Constraints

- Previous implementation physically prevented models from escaping worktrees; new approach trusts models with aggressive prompting instead.
- Smaller models like Haiku frequently deviate and work outside designated directories; larger models like Composer stay on track.
- Long sessions expose model memory degradation where context about worktree location gets forgotten, requiring system reminders.

## Evaluation-Driven Development

- Simple evals using Cursor CLI headless mode with two scorers: did work happen in worktree, nothing in primary.
- Braintrust makes eval writing trivial for beginners; agent can scaffold entire eval infrastructure through prompting alone.
- Cannot yet simulate extremely long sessions in evals where models perform worst, limiting current eval effectiveness.

## Benefits of Skill Implementation

- Users can switch into worktrees mid-conversation via slash commands versus needing dropdown selection at conversation start.
- Multi-repo setups now supported; agent creates worktrees per repo and opens separate PRs automatically for each.
- Parent agent has full context over sub-agent implementations, enabling mixing different model outputs into single solution.

## Trade-Offs and User Experience

- Discoverability decreased removing UI dropdown; users must know slash commands exist to access advanced parallelization features.
- Perceived slowness from watching agent create worktrees in chat, though actual execution time unchanged from before.
- Mixed feedback from power users accustomed to old implementation shows resistance to vibes-based trust over hard constraints.

## Training and Reinforcement Learning

- Composer 2 had zero RL tasks involving worktree prompts; future versions will include thousands of tasks.
- Sharing feedback with all model providers helps ecosystem improve even for models Cursor cannot directly train.
- Evals reveal prompt improvement patterns enabling iterative refinement cycle: eval, find patterns, improve prompts, repeat.

## Future Parallelization

- Git worktrees slow to create, consume disk space, and only work in git repositories limiting applicability.
- New cursor 3.0 agent window provides more natural home for native worktree implementation versus skill approach.
- Exploring non-git parallelization primitives to enable local multi-agent work without version control system dependency.

## Platform Strategy

- Power user features acceptable to hide behind commands when maintenance burden high and usage percentage low.
- Best-of-N skill at 40 lines replaces 4,000 lines judging code, with parent comparing sub-agent outputs.
- Cross-platform compatibility requires OS-specific instructions embedded in single skill for Windows, Linux, Mac environments.
