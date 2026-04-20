import os
import re

def get_video_id(filename):
    # YouTube ID is 11 chars.
    return filename[:11]

transcripts = os.listdir('transcripts')
insights = os.listdir('insights')

# Build a set of video IDs that have insights
insight_ids = {get_video_id(f) for f in insights if f.endswith('.md')}
missing = []

for t in sorted(transcripts):
    if t.endswith('.srt'):
        vid = get_video_id(t)
        if vid not in insight_ids:
            missing.append(t)

if not missing:
    print("All insights are complete.")
else:
    for m in missing:
        print(f"Missing: {m}")
