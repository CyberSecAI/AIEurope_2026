# Why and How You Need to Sandbox AI-Generated Code — Harshil Agrawal, Cloudflare

## The Security Risk of AI-Generated Code

- AI-generated code is fundamentally untrusted code from the internet that runs with full application privileges by default.
- LLMs are black boxes producing text that looks like code, sometimes correct, sometimes wrong, and sometimes dangerous through hallucination or manipulation.
- Running AI-generated code without sandboxing is like executing random scripts from the internet in production with your credentials.

## Three Major Threat Scenarios

- Hallucination threats: Model generates incorrect code like infinite loops, missing base cases, or non-existent package imports that crash services.
- Over-helpful LLM threats: Model tries to be helpful by reading environment variables, API keys, and secrets without malicious intent.
- Compromised prompt attacks: Direct and indirect prompt injection where adversarial instructions embedded in documents or user input exfiltrate data.

## Capability-Based Security Principle

- Don't enumerate what to block, enumerate what to allow — the fundamental principle underlying all successful sandboxing approaches.
- Default deny everything, then explicitly grant specific minimal capabilities that code actually needs to function properly.
- Similar to giving someone keys to three specific rooms versus a master key with a list of 10,000 blocked rooms.

## V8 Isolates for Lightweight Sandboxing

- V8 isolates provide quarter-millisecond startup times for JavaScript, TypeScript, Python, and WebAssembly without file system or process model access.
- Use globalOutbound:null to block all network requests and pass only specific bindings like restricted database interfaces through worker RPC.
- Ideal for quick functions, tool calling, plugins, skills, data transformation, and code interpreters requiring sub-millisecond response times.

## Containers for Full Environment Needs

- Containers provide real Linux environments with file systems, processes, and networking for tasks requiring git clone, npm install, and dev servers.
- Each user gets their own sandbox with complete isolation — user A's files literally don't exist in user B's container universe.
- Essential for building and deploying applications, running test suites, or anything requiring package installation and server processes.

## Critical Security Patterns

- User isolation: One user equals one sandbox always — shared sandboxes create data leak vectors that are architecturally difficult to undo.
- Secret management: Never pass API keys as environment variables into sandboxes; proxy requests through your worker that adds authentication headers.
- Cleanup discipline: Use try-finally blocks to destroy containers even when builds fail to prevent cost and security liability from idle containers.

## Choosing Between Isolates and Containers

- Ask one question: Does code need file system, processes, or package installs? If yes use containers, if no use isolates.
- Isolates are faster, cheaper, simpler with tighter isolation; containers are heavier, more expensive, more complex but enable real capabilities.
- In practice use both strategically: isolates for fast agent tool calling loops, containers when agents need to build and deploy applications.
