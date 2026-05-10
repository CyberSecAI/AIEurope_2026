# Overview

## Summary
Boris Starkov from ElevenLabs reverse-engineered a legacy Viking VoIP phone protocol using Claude Code for an AI-powered demo booth.

## Key Takeaway
Claude Code enabled a non-security engineer to reverse-engineer proprietary hardware through autonomous protocol discovery and iterative problem-solving.

# Insights

## AI as Orchestrator vs Tool
- Human acts as physical agent executing Claude's commands, not providing intellectual direction or domain expertise.
- Claude orchestrated multi-hour debugging sessions autonomously, proposing solutions like TCP proxies and brute-force strategies independently.
- Success required surrendering control: following AI instructions even when you don't understand what's happening intellectually.

## Protocol Discovery Through Brute Force
- Claude systematically tested all 676 two-letter command combinations, discovering 80 valid commands from proprietary protocol.
- Random string testing revealed error patterns, enabling Claude to infer command structure without any documentation.
- Single-byte checksum weakness made protocol crackable through enumeration, demonstrating importance of proper cryptographic protection.

## Man-in-the-Middle Development Workflow
- Set up TCP proxy between Windows VM and phone to intercept traffic and reverse-engineer protocol.
- Virtual machine served as protocol Rosetta Stone: run proprietary software, capture communications, extract command sequences.
- Proxy logging revealed missing TS command with binary payload, which Claude decoded to enable persistent memory.

## Enabling Context Over Direct Access
- Windows XP-only software blocked for year without Windows machines; Claude suggested VM workaround when direct approach failed.
- WiFi bridging limitation on macOS VM solved by routing through host TCP proxy for network access.
- Final skill packaging eliminated VM dependency entirely, making protocol accessible from any platform.

## Closed-Loop Verification Methodology
- Claude didn't just hypothesize checksum algorithm, it tested hypothesis with multiple values to confirm correctness iteratively.
- Physical verification loop required human interaction: Claude asked for beep counts, corrected human counting errors.
- Multi-phase approach: discover ports, test commands, analyze responses, intercept traffic, decode protocols, verify solutions.

## Making Impossible Problems Possible
- Not 10x faster development, but enabling non-security engineer to complete impossible task without domain knowledge.
- Previous team of three senior engineers plus ChatGPT failed after one year; Claude succeeded in days.
- Hexadecimal protocol analysis became accessible to regular software engineer who didn't understand 0x notation.

## Open-Sourcing Hardware Knowledge
- Final deliverable was reusable skill for programming Viking phones, not just working demo booth.
- Methodology extends beyond Viking-specific hardware to any proprietary protocol reverse-engineering challenge.
- Eliminated vendor lock-in: no longer need proprietary Windows software to configure legacy hardware.

## Problem-Solving Through Persistence
- Claude suggested Windows VM solution after brute-force command discovery hit dead-end with volatile memory.
- Multi-hour operations testing three-letter commands and reasonable word combinations before finding alternative approach.
- Dead-end situations that stopped human teams became stepping stones to next creative solution strategy.
