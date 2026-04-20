# Code Mode - Sunil Pai, Cloudflare

## Overview

**Summary:** Code Mode replaces traditional tool calling with LLMs generating executable JavaScript for APIs, drastically reducing tokens and latency.

**Key Takeaway:** Generate code, not JSON - models execute programs against systems rather than chaining tool calls.

---

## API Surface Compression Through Code Generation

- Cloudflare's 2,600 API endpoints (1.2M tokens) compressed to just 1,000 tokens using two tools: search and execute
- Both tools accept code as input; search queries OpenAPI spec, execute provides functions for discovered endpoints
- Achieved 99.9% token reduction by having model generate code that searches and calls APIs in one run

## Code Mode's Fundamental Advantages

- Models trained on terabytes of code already; typed APIs provide syntax errors and type checking automatically
- Enables looping, state management, sequencing, and parallelization - fundamental programming capabilities unavailable to JSON tool calling
- Single execution replaces multiple back-and-forth round trips, eliminating slow model-to-tool-to-model cycles for complex operations

## Emergent System Inhabitation

- Kenton's tic-tac-toe demo: model didn't generate a game app, it inspected canvas stroke state and played directly
- LLM analyzed array of drawing strokes, recognized tic-tac-toe board, and drew perfect circle response without any game logic
- Models "inhabit the state machine" rather than generating separate programs - interacting with system state as first-class interface

## Harness Architecture Requirements

- Start with zero capabilities; explicitly grant APIs rather than defending against exploits from full-featured containers
- Must support fast startup (V8 isolates recommended), full observability for debugging decisions, and controlled outgoing network access
- Default configuration: no outgoing fetches allowed, only exposed APIs - code executes adjacent to API surface for speed

## Generative UI and Personalization at Scale

- Each user can receive completely custom UI generated for their specific context, orders, preferences, and current state
- E-commerce breaks free from lowest-common-denominator interfaces; personalization beyond just changing button colors becomes feasible
- Long-running workflows with persistent state enable programs that run for days, months, or years on behalf of users

## Developer Experience for AI Agents

- Your next billion users are code-generating robots; optimize for DX with markdown docs, clear error messages, searchable APIs
- Capability-based security model: agents dream in types and syntax errors, hang out in registries not pubs
- Code becomes the primary interface - let executable programs do the talking rather than forcing non-technical users into buttons

## Democratization of Programmatic System Access

- LLMs break the boundary between programmers (who write scripts) and non-technical users (who get pre-built apps)
- Everyone now has access to a "buddy" that generates executable code for system interaction tasks
- Examples: Rename 200 photos by date and location using vision models - previously required programming skills, now natural language

## Safe Execution Sandbox Properties

- Events-based architecture, embeddable for fast ephemeral startup, capability-based security as core design principle
- Language-agnostic: JavaScript, Python, WASM, even Lisp - execution mechanism matters less than security and capability model
- Absolute observability required: must trace why specific decisions happened (e.g., why a $2.3M trade executed last Tuesday)
