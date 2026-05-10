# Evaluation and Observability Infrastructure

## Summary
Production AI systems require sophisticated eval platforms combining observability, experimentation, and multi-persona collaboration over specialized data infrastructure.

## Key Takeaway
Eval platforms are fundamentally systems problems requiring specialized data infrastructure, not just UI challenges.

# Insights

## Observability-Eval Flywheel
- Observability-eval flywheel: production trace data reveals failure modes synthetic test cases miss.
- Agent traces combine high velocity, massive size (10-20MB spans), and semi-structured text requiring specialized storage.
- Production monitoring reveals edge cases that cannot be anticipated during development phase.

## Experimentation Infrastructure
- True experimentation requires sandboxed parameter tweaking, automatic comparison scoring, and side-by-side configuration analysis.
- Simple evals using headless mode with two scorers enable rapid iteration and prompt improvement patterns.
- Build eval datasets with train/dev/test splits; perfect dev score signals overfitting unless test matches.

## Systems Engineering Challenge
- Eval platforms require specialized data infrastructure handling high-velocity, large-span traces with semi-structured text.
- Multi-persona collaboration (engineers, domain experts, product managers) requires different views into the same underlying data.
- Integration between observability and evaluation creates feedback loops that improve model behavior over time.

# Related Talks

- **[Why building eval platforms is hard — Phil Hetzel, Braintrust](../insights/_fQ7Z_Wfouk_Why_building_eval_platforms_is_hard_Phil_Hetzel_Braintrust.md)**
- **[Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor](../insights/WE_Gnowy3uw_Replacing_12K_LoC_with_a_200_LoC_Skill_David_Gomes_Cursor.md)**
- **[Context Is the New Code — Patrick Debois, Tessl](../insights/bSG9wUYaHWU_Context_Is_the_New_Code_Patrick_Debois_Tessl.md)**
- **[Full Workshop: Build Your Own Deep Research Agents — Louis-François Bouchard](../insights/mYSRn6PC1mc_Full_Workshop_Build_Your_Own_Deep_Research_Agents_Louis-Francois_Bouchard.md)**
