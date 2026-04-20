# Building Conversational Agents
**Speakers:** Thor Schaeff & Philipp Schmid (Google DeepMind)

## Gemini Interactions API

- New stateful API simplifies multi-turn conversations by managing context server-side, eliminating need for client-side history management.
- Supports both models and agents with unified interface; previous interaction IDs enable conversation continuation without managing full context locally.
- Implicit caching significantly improved with server-side state: cache hit rates 2-3x better, with 90% cost reduction on cached input tokens.

## Agent Architecture Components

- Brain (model) decides actions; tools provide hands/eyes for environment interaction; context contains all model knowledge and constraints; loop orchestrates execution.
- Stateful interactions enable branching from any previous point, allowing parallel execution from single base while maintaining full context retrieval capabilities.
- Built-in agents like Deep Research run background tasks asynchronously with webhook notifications, avoiding long HTTP connections for multi-minute operations.

## Tool Use and Function Calling

- Interactions API supports built-in tools, remote MCP servers, and tool combination (e.g., Google Search with custom functions) launched weeks prior.
- System instructions critical for agent behavior; coding agents require explicit prompts to use file/bash tools rather than generating text responses.
- Tool calling pattern: check interaction status for "requires_action", iterate output types, execute functions, append results, continue until text generation completes.

## Developer Experience Improvements

- API moved from proto-oriented to JSON-based format familiar to web developers, reducing learning curve and integration complexity significantly.
- Google AI Studio skills provide web-fetchable documentation links instead of static skill content, maintaining up-to-date information without requiring skill updates.
- Free tier stores interactions 1 day, paid tier 55 days; Vertex AI version offers additional customization for enterprise retention requirements.

## Gemini 3.1 Flash Live

- Native audio model processes sound-token-to-sound-token without cascading pipeline (transcribe → LLM → TTS), preserving paralinguistic cues and emotional nuance.
- Real-time WebSocket API supports audio/video streams (1fps max), with built-in Google Search grounding and automatic voice activity detection for interruptions.
- Multilingual support across 97 languages with mixed-language understanding (e.g., "Denglish" - German/English code-switching) and context-aware language switching capabilities.

## Coding Agent Implementation

- AI-assisted development using Gemini skills: agents read API documentation, generate implementations, and verify correctness through execution testing automatically.
- Built complete coding agent with file operations and bash execution in workshop; Gemini 3 Flash effective for structured tasks with good instructions.
- Integration partners (LiveKit, Pipecat, Vox Implant) provide WebRTC bridges for Gemini Live API, simplifying real-time voice application development significantly.

## Live Jukebox Demo

- Conversational DJ agent uses tool calling to trigger music generation, demonstrating multimodal agent orchestration with audio input/output and external service integration.
- Architecture separates conversation handling from content generation: agent manages dialogue while delegating specialized tasks (music creation) to appropriate tools.
- Demo built entirely in Google AI Studio showcasing rapid prototyping capabilities; requires paid API key for music generation features.

## Workshop Approach

- Hands-on development without manual coding: participants used AI agents to build agents, demonstrating meta-programming and self-improving development workflows practically.
- Skills-based architecture enables context injection: agents fetch current documentation ensuring latest features available without model retraining or skill version updates.
- Multiple programming languages supported through agent flexibility: participants successfully built TypeScript, Python implementations simultaneously demonstrating language-agnostic approach.
