# Overview

## Summary
Cassidy Hardin from Google DeepMind presents Gemma 4's technical architecture, highlighting breakthroughs in multimodal small models.

## Key Takeaway
Per-layer embeddings enable 2B models to outperform predecessors without VRAM overhead.

# Insights

## Attention Architecture Optimization
- Interleaving 5:1 local-to-global attention layers with sliding windows dramatically reduces memory costs while maintaining performance.
- Global layers use 8:1 grouped query attention with doubled key-value head length to offset performance loss.
- Last layer is always global, ensuring final token attends to entire context for better output quality.

## Mixture of Experts Innovation
- 128 experts with only 8 active per forward pass achieves 31B performance with 3.9B active parameters.
- Shared expert is 3x larger than regular experts and activates on every pass for knowledge consistency.
- First Gemma MoE ranks top-six globally while being efficient enough for practical deployment at scale.

## Per-Layer Embeddings (PLE) Breakthrough
- PLE tables stored in flash memory instead of VRAM eliminate primary on-device constraint for small models.
- 256-dimension per-layer embeddings project up to full size only when needed, drastically reducing memory footprint.
- E2B has 2.3B active parameters but 5.1B representational depth, enabling rich understanding without device limitations.

## Variable Vision Processing
- Five resolution options let developers trade token budget for image quality based on task requirements.
- 3x3 patch pooling creates single embeddings, turning 280 soft tokens into 2,520 actual image patches.
- Spatial positional encoding preserves patch relationships across variable aspect ratios, eliminating Gemma 3's inefficient pan-and-scan approach.

## Audio Multimodal Integration
- 305M parameter conformer processes audio embeddings through mel spectrogram downsampling with 4:1 token compression ratio.
- Audio natively integrated from training start, not bolted on, enabling translation and speech recognition on-device.
- Convolutional layers in conformer architecture specifically designed for audio's temporal nature unlike vision or text.

## Licensing and Accessibility Strategy
- Apache 2.0 license deliberately chosen to maximize developer accessibility throughout entire development lifecycle from testing to deployment.
- Self-hosting available via Hugging Face, Kaggle, Ollama; cloud hosting via AI Studio and Vertex AI.
- Small models designed for phones and laptops without expensive API calls, democratizing powerful AI capabilities.

## Benchmark Performance Leadership
- 31B model ranks third globally, outperforming models over 20 times its size on arena leaderboards.
- Gemma 4 sets new frontier across agentic capabilities, coding, multimodal, and multilingual tasks simultaneously.
- E4B and E2B significantly outperform all prior generation small models across every benchmark category measured.

## Token Budget Flexibility
- Developers control soft token allocation for images, enabling OCR tasks at 1,120 tokens or lightweight tasks.
- Variable resolution support allows same model to handle vastly different use cases without retraining or architecture changes.
- 256K context length on 31B purpose-built for autonomous workflows with thinking, function calling, and structured outputs.
