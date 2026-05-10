# Overview

## Summary
Peter Gostev from Arena.ai presents BullshitBench and real-world data revealing where LLMs fail despite benchmark improvements.

## Key Takeaway
Benchmark charts show progress, but models still fail 9-13% on real tasks, especially nonsense detection.

# Insights

## BullshitBench: Testing Nonsense Detection
- Models trained to solve tasks at any cost often hallucinate answers to nonsensical questions instead of pushing back.
- Claude Sonnet models push back effectively on nonsense; GPT and Gemini accept nonsense roughly 50% of the time.
- Reasoning models often perform worse at detecting nonsense, spending paragraphs trying to solve unanswerable questions.

## Arena User Dissatisfaction Trends
- Top 25 models still produce unsatisfactory responses 9% of the time, down from 17% pre-reasoning era.
- Quantitative tasks showed dramatic improvement after reasoning models launched, dropping dissatisfaction from 25% to under 10%.
- Medical tasks improved significantly, while creative writing improvement was minimal, indicating uneven progress across domains.

## Expert Category Performance Gaps
- Among 40,000 expert-level prompts, dissatisfaction dropped from 23.5% to 13% overall in software tasks.
- Gaming development remains problematic with little improvement; models struggle with game mechanics and lack creative challenge design.
- Finance, law, and medical fields show flat improvement curves, suggesting these domains haven't been training priorities.

## Model Size and Reasoning Ineffectiveness
- Bigger model parameters show no clear correlation with better nonsense detection in open-source models tested.
- Extended reasoning doesn't help with fundamental judgment tasks and can make responses worse by over-rationalizing.
- Training focused on task completion at all costs created models that accommodate wrong premises rather than question them.

## Dynamic Benchmark Reality
- User expectations and prompt complexity have shifted dramatically over three years, making comparisons challenging over time.
- Static benchmarks measure narrow, well-defined tasks that don't capture the fuzziness of real white-collar work.
- Arena's continuously evolving user prompts reveal gaps that traditional exhaustible benchmarks miss completely.

## GPU Compute and Agent Systems
- GPU compute category shows volatile satisfaction rates, likely because users ask progressively harder infrastructure questions.
- Agent systems requests include production-level needs like unsupervised daily execution, exposing reliability and autonomy gaps.
- Security configuration tasks reveal models struggle with specific technical implementations despite understanding high-level concepts.

## The Distribution Problem
- Progress concentrates at the top of narrow benchmark tasks while the broader distribution lags significantly behind.
- Model improvements focus on highly-specified domains, leaving messy real-world domains like gaming and creative work behind.
- The gap between benchmark line-goes-up and user experience reflects unmeasured aspects of judgment and contextual reasoning.
