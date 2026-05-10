# Overview

## Summary
Jacob Lauritzen, CTO of Legora, discusses why complex vertical AI agents require richer collaboration interfaces beyond traditional chat.

## Key Takeaway
Chat is one-dimensional; complex agent work needs high-bandwidth artifacts enabling control and progressive steering.

# Insights

## The Verifier's Rule Framework
- Tasks that are solvable and easy to verify will be solved by AI agents.
- Writing contracts is easy to solve but extremely difficult to verify until courtroom validation occurs.
- Litigation strategy has no objective truth, making it impossible to verify and hard for AI.

## New Economics of AI Production
- Planning and reviewing work are now bottlenecks; executing work itself has become extremely cheap.
- Reviewing massive AI-generated outputs is painful, similar to reviewing large GitHub pull requests without context.
- The shift from doing-focused to planning-reviewing-focused fundamentally changes how humans work with AI.

## Increasing Trust Through Verification
- Move tasks down the verifiability spectrum using browser access and test-driven development for coding.
- Create verification proxies like comparing new contracts to golden reference contracts that are proven.
- Decompose complex tasks into verifiable subtasks, leaving judgment-heavy decisions to humans while automating linting-like checks.

## Control Through Skills vs Planning
- Skills encode human judgment into workflow nodes, enabling contingencies that planning cannot handle beforehand.
- Planning forces humans to do all the work upfront just to know what to tell agents.
- Skills allow progressive discovery, agents handle special cases encountered during execution without re-planning everything.

## Guardrails Increase Trust
- Limiting agent capabilities increases trust by preventing unexpected behaviors during complex workflows.
- Claude Code's low-trust mode requiring constant approval becomes useless; YOLO mode risks production database deletion.
- Scoping agents to specific files, directories, and websites balances autonomy with safety boundaries.

## Elicitation and Decision Logs
- Tell agents to make decisions and unblock themselves, but write uncertain choices to decision logs.
- Humans review decision logs post-hoc and reverse bad choices rather than blocking agent progress.
- Complex work trees with 10-100x more nodes cannot be managed in linear chat interfaces.

## High-Bandwidth Collaboration Artifacts
- Humans and agents should collaborate in persistent, vertical-specific artifacts like documents and tabular reviews.
- Documents enable clause-level highlighting, comments, tagging agents, and handing off specific sections to specialized agents.
- Tabular reviews let agents flag items needing human judgment, providing high control and easy reviewing.

## Beyond Language-Only Interfaces
- Language is universal for human-to-human communication but constrains humans who can't draw org charts mid-conversation.
- Agents aren't humans and shouldn't be constrained to human language limitations for collaboration.
- Chat as input is great for flexibility, but complex agents need richer output interfaces.
