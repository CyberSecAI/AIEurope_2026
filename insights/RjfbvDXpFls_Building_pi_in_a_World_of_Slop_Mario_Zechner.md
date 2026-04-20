# Building Pi in a World of Slop - Mario Zechner

## 1. Building Pi: Motivation and Philosophy

- Frustration with Claude Code's evolving complexity, bugs, and lack of control over context management.
- Pi built as minimal, self-modifying agent harness with four core tools and extensible architecture via TypeScript.
- Philosophy: agent adapts to user workflow, not other way around; users retain full control and observability.

## 2. Context Control and Minimalism

- Claude Code's hidden context manipulation (system prompts, tool definitions, system reminders) broke workflows and reduced predictability.
- Pi ships minimal system prompt, simple tool definitions, and documentation enabling self-modification through agent-written extensions.
- Terminal benchmark shows minimal harness (just keystrokes/output) outperforms complex harnesses, suggesting less is more for agent performance.

## 3. Extensibility and Self-Modification

- Extensions are TypeScript modules that hook into everything: tools, slash commands, events, session state, compaction.
- Agent can modify itself by reading docs and code examples, writing extensions during sessions with hot reload.
- Ecosystem uses npm/GitHub instead of proprietary marketplaces; users build what fits their specific security and workflow needs.

## 4. Open Source Under Siege by Clankers

- AI agents flooding GitHub with low-quality issues and pull requests destroyed maintainer workflows and mental health.
- Created vouch system: auto-close PRs, require human-voice issue submission to earn trust; clankers don't read responses.
- Invented "OSS vacation" - closing tracker whenever needed to reclaim life; deprioritized issues from known agent users.

## 5. Agent-Generated Code Complexity Crisis

- Agents compound "boooos" (errors with zero learning): code review scales impossibly when 10 agents generate enterprise complexity.
- Models learn complexity from internet's mediocre code; local decisions create global mess through abstractions, duplication, backward compatibility.
- Review agents fail at detecting issues; users lose understanding of codebase, can't debug when production breaks.

## 6. Human Bottlenecks as Feature, Not Bug

- Humans are bottlenecks limiting daily "boooos" added to codebase; humans feel pain triggering refactoring or quitting.
- Agents never feel pain, happily continue adding complexity until codebase becomes unmaintainable and exceeds context windows.
- Friction of writing code by hand builds mental model critical for debugging and learning new concepts.

## 7. Good Agent Tasks: Scope and Evaluation

- Ideal tasks: scoped so agent finds all needed context, modular codebase, evaluable with function for hill climbing.
- Use agents for non-critical code, boring tasks, reproduction cases with partial information, rubber ducking without humans nearby.
- Evaluate output carefully, take reasonable parts (most isn't), finalize by hand; never blindly trust agent-generated code/tests.

## 8. Slow Down: Discipline and Agency Required

- Don't build just because agent can; learn to say no, focus on fewer features that matter.
- Critical code must be read line-by-line and written by hand; agents assist but don't make architectural decisions.
- Maintain discipline and agency; understanding system requires human involvement; "everything still requires humans."
