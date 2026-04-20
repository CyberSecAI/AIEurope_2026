# Playground in Prod: Optimising Agents in Production Environments
**Speaker:** Samuel Colvin (Pydantic)
**Event:** AI Engineer Europe

---

## DSPy Genetic Algorithm Framework (Jepper)

- Jepper uses genetic programming combined with Pareto optimization to optimize agent prompts automatically
- Creates candidate prompts from best-performing examples, mixing and testing them iteratively across generations
- Achieved 87% to 96.7% accuracy improvement through automated prompt optimization versus manual approaches

## Evaluation-Driven Optimization

- Golden datasets with human-annotated or high-quality model outputs essential for measuring optimization progress
- Precision/recall metrics track improvements across multiple assertion types during iterative prompt refinement
- Compare runs side-by-side in observability platforms to identify specific failure patterns driving optimization

## Managed Variables for Production Control

- Separate prompt content and configuration from code using managed variables stored in platform
- Enable A/B testing by routing percentage of traffic to different prompt versions without redeployment
- Update system prompts, models, and temperatures in real-time through platform UI affecting live production

## Private Data Optimization Advantage

- Optimization provides greatest value when working with private internal data not in model training sets
- Public data examples demonstrate techniques but understate real-world benefits for proprietary use cases
- Domain-specific instructions and context become critical when models lack pre-trained knowledge on your data

## Cost-Performance Tradeoffs

- Shopify reduced costs from $5M/year to $73K/year using Jepper optimization with smaller models
- Optimization enables cheaper or faster models to match performance of expensive state-of-the-art models
- Hold quality constant while reducing latency and cost, or improve quality with same model

## Production Optimization Workflow

- Run evals locally first to establish baseline performance metrics before optimization begins
- Use validation set separate from training set to prevent overfitting during genetic optimization
- Monitor optimization progress through multiple generations, tracking Pareto frontier of quality vs other metrics

## Structured Output Optimization

- Structured outputs using Pydantic models enable precise evaluation of complex extraction tasks
- Optimize both what information to extract and how to format it through schema constraints
- Relation filtering (ancestors vs descendants) demonstrates subtle prompt optimization challenges requiring multiple iterations

## Self-Driving Agent Optimization

- Future direction: autonomous optimization running continuously in production without manual intervention
- Platform pulls evaluation results, runs optimization, and deploys improved prompts automatically through managed variables
- Hill climbing toward performance peaks while maintaining safety constraints and rollback capabilities

---

**Generated with Claude**
