#!/usr/bin/env python3
"""
Rebuild README.md table with all insights from the insights/ directory.

This script:
1. Extracts video IDs correctly (handling IDs with underscores like O_IMsEg91g8)
2. Maps insights to their corresponding transcript files
3. Generates a complete markdown table with all 85 talks

Usage:
    python scripts/rebuild_readme_table.py > README.md

Or to update in place:
    python scripts/rebuild_readme_table.py
"""

import os
import glob
import re
import urllib.parse


def generate_readme():
    """Generate complete README.md with corrected table."""

    # Write the header section
    header = """# AI Engineer Europe Conference Index

## Meta Key Insights
*Overarching strategic themes synthesized from recurring topics across multiple conference sessions.*

### Summary
AI Engineer Europe 2026 showcased the transformation of software engineering through standardized agent protocols, modular skill architectures, and the evolution from implementation speed to strategic product judgment as the key competitive differentiator.

### Key Takeaway
Master the fundamentals, build for taste over velocity, and architect systems where agents amplify human judgment rather than replace it.

---

### Overarching Themes

#### Infrastructure & Connectivity
1.  **[Standardized Connectivity (MCP)](./meta/Standardized_Connectivity_MCP.md)**: Establish a universal language for agent-to-tool integration.
2.  **[Code-Centric Agency](./meta/Code_Centric_Agency.md)**: Reduce latency and enable native loops through executable scripts.
3.  **[Modular Skill Architectures](./meta/Modular_Skill_Architectures.md)**: Folderize agent logic into versionable, hierarchical "skills."
4.  **[Agentic Security & Sandboxing](./meta/Agentic_Security_Sandboxing.md)**: Enforce "default deny" and safe execution environments.
5.  **[Edge & Local AI Strategy](./meta/Edge_Local_AI_Strategy.md)**: Prioritize privacy and latency with on-device model execution.

#### Context & Intelligence
6.  **[Agentic RAG & Context Engineering](./meta/Agentic_RAG_Context_Engineering.md)**: Replace static retrieval with dynamic, autonomous search.
7.  **[Evaluation & Observability Infrastructure](./meta/Evaluation_And_Observability_Infrastructure.md)**: Build sophisticated eval platforms combining observability and experimentation.
8.  **[Model Capabilities & Limitations](./meta/Model_Capabilities_And_Limitations.md)**: Understand real-world model performance beyond benchmarks.

#### Human-Agent Collaboration
9.  **[Vibe Engineering & Human Steering](./meta/Vibe_Engineering_Human_Steering.md)**: Transition from manual coding to directional intent management.
10. **[Parallel Agent Orchestration](./meta/Parallel_Agent_Orchestration.md)**: Decompose complex work into isolated, concurrent agent sessions.
11. **[Multimodal & Canvas Interfaces](./meta/Multimodal_And_Canvas_Interfaces.md)**: Enable spatial AI collaboration beyond traditional chat.
12. **[Voice & Conversational Agents](./meta/Voice_And_Conversational_Agents.md)**: Eliminate friction through natural voice interfaces.

#### Strategy & Business Impact
13. **[AI Product Strategy & Taste](./meta/AI_Product_Strategy_And_Taste.md)**: Knowing what NOT to build becomes the primary competitive advantage.
14. **[Software Fundamentals in AI Era](./meta/Software_Fundamentals_In_AI_Era.md)**: Good codebases amplify AI effectiveness exponentially.
15. **[AI Business Model Evolution](./meta/AI_Business_Model_Evolution.md)**: Shift from per-seat SaaS to hybrid outcome-based pricing.

#### Enterprise & Adoption
16. **[Enterprise AI Adoption Patterns](./meta/Enterprise_AI_Adoption_Patterns.md)**: Custom infrastructure investments reveal competitive positioning.
17. **[Application Layer Transformation](./meta/Application_Layer_Transformation.md)**: Agents become the new application layer.
18. **[Agent for Operational Automation](./meta/Agent_For_Operational_Automation.md)**: Enable non-technical employees to ship autonomously.


## Individual Talk Insights
*Key Insights from each talk, with links to original video and transcript*


| Video ID | Title | Key Insights | Transcript | Video |
| --- | --- | --- | --- | --- |
"""

    print(header, end='')

    # Build video ID map from insight filenames
    video_ids = {}
    for insight_path in glob.glob('insights/*.md'):
        filename = os.path.basename(insight_path)
        base = filename.replace('.md', '')

        # Extract 11-char video ID first (standard YouTube format)
        match = re.match(r'^([A-Za-z0-9_-]{11})_', base)
        if match:
            video_id = match.group(1)
        else:
            # Fallback for shorter or longer IDs
            match = re.match(r'^([A-Za-z0-9_-]+?)_', base)
            video_id = match.group(1) if match else base.split('_')[0]

        video_ids[base] = video_id

    # Build transcript map
    transcript_map = {}
    for transcript_path in glob.glob('transcripts/*.srt'):
        trans_filename = os.path.basename(transcript_path)
        for base, vid in video_ids.items():
            if trans_filename.startswith(vid + '_') or trans_filename.startswith(vid + ' '):
                if vid not in transcript_map:
                    transcript_map[vid] = trans_filename
                break

    # Generate table rows
    for insight_path in sorted(glob.glob('insights/*.md')):
        insight_filename = os.path.basename(insight_path)
        base = insight_filename.replace('.md', '')
        video_id = video_ids[base]

        # Extract title using the known video_id length
        # This ensures we handle video IDs with underscores correctly
        title = base[len(video_id) + 1:].replace('_', ' ')

        # Build transcript link with URL encoding
        transcript_link = f"./transcripts/{urllib.parse.quote(transcript_map.get(video_id, ''))}" if video_id in transcript_map else "./transcripts/"

        # Generate table row
        entry = f"| `{video_id}` | {title} | [Insights](./insights/{insight_filename}) | [Transcript]({transcript_link}) | [YouTube](https://www.youtube.com/watch?v={video_id}) |"
        print(entry)


if __name__ == '__main__':
    generate_readme()
