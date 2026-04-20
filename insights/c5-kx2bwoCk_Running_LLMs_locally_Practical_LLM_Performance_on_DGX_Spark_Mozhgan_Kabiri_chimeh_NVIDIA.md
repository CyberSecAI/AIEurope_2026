# Running LLMs locally: Practical LLM Performance on DGX Spark — Mozhgan Kabiri chimeh, NVIDIA

## Developer Challenges with AI Systems
- Developers face memory limitations and lack proper software stacks, forcing cloud or data center reliance unnecessarily.
- Iteration speed bottlenecks from shared infrastructure scheduling delays hinder development productivity and workflow efficiency significantly.

## DGX Spark Hardware Architecture
- GB10 Grace Blackwell superchip with 128 GB unified memory enables running models up to 200 billion parameters locally.
- Runs identical NVIDIA AI software stack as production, enabling seamless desktop to data center workflow transitions.

## Benchmarking Methodology and Reproducibility
- Automated harness uses strict protocols: Docker isolation, three mandatory warm-up runs, and one-second GPU metrics logging.
- Every model execution generates timestamped directories capturing full endpoint responses, metadata, and verification artifacts for reproducibility.

## NV4 Quantization Performance Impact
- 14 billion parameter NV4 model achieves 20.19 tokens per second, maintaining faster-than-human reading speed responsiveness.
- NV4 quantization delivers 3.4 times faster time-to-first-token versus unoptimized base models, critical for perceived performance.

## Memory Bandwidth Versus Capacity Trade-offs
- Memory capacity enables fitting massive models, but throughput depends critically on memory bandwidth and data movement efficiency.
- NV4 4-bit floating-point quantization increases intelligence per byte, making 14B models feel responsive as smaller ones.

## Time to First Token User Experience
- Time to first token defines whether applications feel instant or broken, more important than end-to-end latency alone.
- Larger models show expected increases in first token latency due to increased parameter computation before response generation.

## Local Development Workflow Benefits
- Ideal for steady-state workloads, privacy-sensitive data, and rapid prototyping without cloud dependency or cost unpredictability.
- Enables local building and fine-tuning with production software stacks, then seamless scaling to data center or cloud.

## Quantization Format Selection Importance
- On Blackwell hardware, quantization format choice is equally important as the hardware itself for practical performance.
- 14B base model drops to only 8.40 tokens per second without optimization, versus 20.19 with NV4 quantization.
