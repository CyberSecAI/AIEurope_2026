# Edge & Local AI Strategy

## Summary
On-device models provide critical low latency and data privacy, complementing cloud models to enable a hierarchical, cost-effective AI strategy.

## Key Takeaway
Integrate local and edge models to achieve a high-performance, private, and scalable AI infrastructure.

# Insights

## Privacy and Latency
- On-device models provide critical low latency and data privacy for real-time tasks and sensitive personal workflows.
- Processing data locally on the user's hardware ensures that sensitive information is never exposed to external servers.
- Low-latency, local execution is essential for building interactive AI assistants that feel fast and responsive to users.

## Cross-Platform Runtimes
- System-level foundation models and specialized runtimes enable shared agentic capabilities across mobile, web, and IoT hardware.
- Standardized local runtimes like LiteRT-LM allow developers to build once and deploy agent behaviors across any device.
- Edge-optimized models can perform a wide variety of tasks from simple text processing to complex, real-time multimedia analysis.

## Hierarchical Model Usage
- A model hierarchy allows for cost-effective execution, utilizing local models for simple tasks while reserving cloud models for reasoning.
- Dynamically switching between models based on task complexity ensures that resources are allocated efficiently at all times.
- Integrating local and cloud capabilities provides a robust and scalable architecture that can handle any agentic workload.

## Specialized Small Models
- MLX enables 40 tokens/second on iPhone with Gemma 4, achieving production-ready on-device inference.
- Quantize between 4-bit and 8-bit for optimal quality-performance balance on edge devices.
- Small models need specialized architectures, not just scaled-down versions; embedding layers consume 63% of parameters.
- Task-specific training: focus on excelling at 2-3 narrow capabilities rather than being average across all tasks.

# Related Talks

- **[Running LLMs locally: Practical LLM Performance on DGX Spark — Mozhgan Kabiri chimeh, NVIDIA](../insights/c5-kx2bwoCk_Running_LLMs_locally_Practical_LLM_Performance_on_DGX_Spark_Mozhgan_Kabiri_chimeh_NVIDIA.md)**
- **[Training an LLM from Scratch, Locally — Angelos Perivolaropoulos](../insights/UsB70Tf5zcE_Training_an_LLM_from_Scratch_Locally.md)**
- **[TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick](../insights/BKWpYIWvAo4_Cormac_Brick_TLMs_Tiny_LLMs_and_Agents_on_Edge_Devices_with_LiteRT_LM.md)**
- **[Frontier AI at Home — Alex Cheema](../insights/ESbWpPT_9-o_Alex_Cheema_Frontier_AI_at_Home.md)**
- **[Running LLMs on your iPhone: 40 tok/s Gemma 4 with MLX — Adrien Grondin, Locally AI](../insights/a2muGkT4WD4_Running_LLMs_on_your_iPhone_40_tok_s_Gemma_4_with_MLX_Adrien_Grondin_Locally_AI.md)**
- **[Open Models at Google DeepMind — Cassidy Hardin, Google DeepMind](../insights/_A367W_qvc8_Open_Models_at_Google_DeepMind_Cassidy_Hardin_Google_DeepMind.md)**
- **[Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI](../insights/fLUtUkqYHnQ_Everything_I_Learned_Training_Frontier_Small_Models_Maxime_Labonne_Liquid_AI.md)**
