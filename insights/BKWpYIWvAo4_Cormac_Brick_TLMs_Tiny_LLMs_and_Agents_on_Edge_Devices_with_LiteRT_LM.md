# Overview
## Summary
Cormac Brick explores the deployment of "Tiny LLMs" (TLMs) and agentic skills on edge devices using Google’s LiteRT-LM runtime and the Gemma 4 model series.
## Key Takeaway
On-device AI enables high-performance, private, and cost-effective applications through specialized runtimes and memory-efficient model architectures like Gemma E2B.

# Insights
## Edge AI Advantages
- Running models on the edge provides critical low latency for real-time tasks like live voice translation and interface interactions.
- On-device processing ensures user privacy by keeping sensitive data, such as private messages, encrypted and local to the hardware.

## LiteRT-LM Framework
- LiteRT and LiteRT-LM provide a standardized, cross-platform runtime for deploying LLMs on mobile, web, and IoT devices.
- A single LiteRT-LM package includes the model, tokenizer, and configuration, simplifying deployment across Android, iOS, Windows, and Linux.

## System-level GenAI
- Mobile OS vendors are integrating 2-5B parameter foundation models directly into the system to provide global APIs for developers.
- System-level models enable shared capabilities like summarization and proofreading without requiring each app to download its own massive model.

## In-app Tiny LLMs (TLMs)
- Task-specific "Tiny LLMs" can achieve over 90% reliability when fine-tuned for specialized functions like voice-to-action or summarization.
- Tiny models are ideal for broad reach, as they can run on non-premium devices with limited RAM and processing power.

## Effective RAM Management
- Memory mapping (mmap) allows models to run with limited RAM by loading only essential layer embeddings during the autoregressive loop.
- Models like Gemma E2B are optimized to remain resident in memory while maintaining high reasoning performance on mobile hardware.

## Hardware Acceleration
- LiteRT-LM leverages various hardware accelerators, including GPU and NPU, to maximize on-device inference speed and energy efficiency.
- While CPU and GPU can use a single model file, NPUs often require specialized compilation to fully exploit their efficiency.

## Multimodal On-Device AI
- The latest tiny models, such as Gemma E2B and E4B, support multimodal inputs including text, images, and audio directly on-device.
- Multimodality combined with built-in function calling enables sophisticated agentic "skills" that can interact with the physical and digital world.

## Open Ecosystem
- Releasing Gemma models under the Apache 2.0 license encourages widespread adoption and experimentation across the global developer community.
- Standardizing on open-source frameworks like LiteRT helps combat environment fragmentation and ensures consistent performance across diverse device ecosystems.
