import os
import re
from urllib.parse import quote

def get_video_id(filename):
    # YouTube ID is 11 chars.
    return filename[:11]

def clean_title(vid, filename):
    # Remove extension and standard suffix - adjust for AIE Europe
    name = filename.replace(" ｜ AIE Europe.en.srt", "").replace(".en.srt", "")
    # Remove Video ID prefix
    name = name.replace(f"{vid}_", "")
    # Strip underscores and leading/trailing whitespace
    return name.strip('_').strip()

transcripts_dir = 'transcripts'
insights_dir = 'insights'
meta_dir = 'meta'

transcripts = [f for f in os.listdir(transcripts_dir) if f.endswith('.srt')]
insights = [f for f in os.listdir(insights_dir) if f.endswith('.md')]

id_to_transcript = {get_video_id(f): f for f in transcripts}
id_to_insight = {get_video_id(f): f for f in insights}

all_ids = sorted(id_to_transcript.keys())

with open('README.md', 'w', encoding='utf-8') as f:
    f.write('# AI Engineer Europe Conference Index\n\n')

    f.write('## Meta Key Insights\n')
    f.write('*Overarching strategic themes synthesized from recurring topics across multiple conference sessions.*\n\n')

    # Meta insights will be populated as themes emerge
    # Example structure:
    # meta_mappings = [
    #     ("AI Engineering Practices", "META_AI_ENGINEERING.md", "Description of cross-cutting theme."),
    # ]
    #
    # for title, m_file, desc in meta_mappings:
    #     f.write(f"- **[{title}](./{meta_dir}/{m_file})**: {desc}\n")

    f.write('(To be populated as insights are extracted)\n\n')

    f.write('## Individual Talk Insights\n')
    f.write('*Key Insights from each talk, with links to original video and transcript*\n\n')

    f.write('| Video ID | Title | Key Insights | Transcript | Video |\n')
    f.write('| --- | --- | --- | --- | --- |\n')

    for vid in all_ids:
        t_file = id_to_transcript.get(vid)
        i_file = id_to_insight.get(vid)

        if not t_file:
            continue

        title = clean_title(vid, t_file)

        insight_link = f"[Insights](./insights/{quote(i_file)})" if i_file else "Pending"
        transcript_link = f"[Transcript](./transcripts/{quote(t_file)})"

        video_link = f"[YouTube](https://www.youtube.com/watch?v={vid})"

        f.write(f"| `{vid}` | {title} | {insight_link} | {transcript_link} | {video_link} |\n")

print("README.md generated successfully.")
