# Overview

## Summary
Maxime Labonne, Head of Pre-training at Liquid AI, shares lessons from training edge models (350M-24B parameters).

## Key Takeaway
Small models need specialized architectures and training approaches, not just scaled-down versions.

# Insights

## Architecture Design for Edge Models

- Embedding layers consume 63% of Gemma 3 270M parameters, reducing effective reasoning capacity significantly.
- On-device profiling identified gated short convolutions as fastest operators, outperforming sliding window attention and Delta Net.
- LFM 2 architecture maintains 90% effective parameters by minimizing embedding layer size compared to competitors.

## Extreme Data Scaling Laws

- LFM 2.5 350M trained on 28 trillion tokens, far beyond Chinchilla optimal compute ratios.
- New scaling laws from Roberts et al show small models benefit from continued pre-training beyond traditional estimates.
- Performance continues improving even at 80x the Chinchilla-optimal token count for this model size.

## Task-Specific Training Philosophy

- Focus training budget on excelling at 2-3 narrow capabilities rather than being average across all tasks.
- Small models optimized for data extraction and tool use outperform on specific benchmarks despite parameter constraints.
- Target narrow use cases like function calling where knowledge capacity limitations become irrelevant.

## Preference Alignment for Stability

- Preference alignment provides general quality improvements beyond benchmarks, making models subjectively "sound better" overall.
- On-policy length-normalized DPO proves more effective than supervised fine-tuning for small model quality.
- DPO stage delivers broad improvements while supervised fine-tuning and RL remain narrow and task-specific.

## Doom Loop Mitigation Strategies

- Generate 5 temperature-sampled rollouts plus 1 greedy rollout, using LLM jury to reject worst responses.
- Reinforcement learning with verifiable rewards naturally prevents doom loops by requiring extractable final answers.
- Combined approach reduced doom loop ratio from 16% after pre-training to near-zero after RL.

## Cold Start SFT Requirements

- Small models are extremely sensitive to cold start SFT data for reinforcement learning tasks.
- If RL task fails to train, solution is adding similar examples to SFT mixture before retrying.
- Unlike large models, small models cannot bootstrap new task types during RL without prior SFT exposure.

## N-gram Repetition Penalties

- Temperature sampling during RL generates diverse rollouts, reducing doom loop frequency naturally through exploration.
- Adding n-gram repetition penalty to verifiable reward signals creates robust anti-looping mechanism.
- Qwen 3.5 0.8B reasoning mode shows over 50% doom loops, proving scaled-down approach inadequate for small models.

## Agentic Tool Augmentation

- Small models excel at agentic tasks when given web search and Python tools to compensate for knowledge capacity.
- Low knowledge capacity becomes non-issue if model has strong reasoning and reliable tool-use capabilities.
- Recursive language model environments with Python allow small models to bypass long-context limitations entirely.
