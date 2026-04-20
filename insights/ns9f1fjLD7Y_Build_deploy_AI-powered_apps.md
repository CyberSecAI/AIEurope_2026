# Build & Deploy AI-Powered Apps

**Speakers:** Paige Bailey & Guillaume Vernade

## Key Insights

### Evolution of ML Trust
* Trust in open source for business-critical ML has evolved significantly since 2009, moving from skepticism to industry-standard adoption.
* Early contributions to NumPy and SciPy laid the foundation for today's pervasive AI engineering and scientific computing stacks.

### Context Window Revolution
* Massive expansion of context windows (from 8k to 2M+ tokens) is fundamentally changing how developers approach data processing and RAG.
* Small context windows previously forced a "sprint" toward vector databases, whereas large windows allow for more direct in-context learning.

### Model Absorption of Capabilities
* Many external agent frameworks and "fine-tuned" features are being absorbed directly into base models like Gemini over time.
* Developers should be cautious of over-engineering custom agentic scaffolding for tasks that base models will eventually handle natively.

### Skills vs. Protocols
* The industry is shifting from complex protocols like MCP (Model Context Protocol) toward "skills" implemented as simple, structured Markdown files.
* Skills provide a leaner, more developer-friendly way to extend agent capabilities without the overhead of heavy backend integrations.

### Compute Optimization (GPU/TPU)
* AI app deployment requires deep understanding of distributed compute across CPUs, GPUs, and TPUs for both training and inference.
* Optimizing for specific hardware paths remains a critical performance differentiator for complex, large-scale AI applications.

### Developer UX with AI Studio
* Modern tools like Google AI Studio and Vertex AI drastically simplify the "reproducibility" challenge when building non-deterministic AI apps.
* Proactive use of opinionated platforms allows developers to solve specific customer problems faster than building generic agent frameworks.

### The Future of Autonomous Execution
* Future agents will include "listeners" that watch human workflows and automatically create skills to automate those tasks behind the scenes.
* The goal is to move beyond manual prompting toward systems that learn and adapt based on continuous observation of human expertise.
