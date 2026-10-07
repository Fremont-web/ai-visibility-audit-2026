import json
import re

p = r"C:\Users\Temp\.gemini\antigravity\brain\ab21db2f-9d47-4f90-a70d-12244e825966\.system_generated\logs\transcript_full.jsonl"
with open(p, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Collect all text from lines 280 to 287
combined_text = ""
for idx in [280, 282, 283, 284, 285, 286]:
    if idx < len(lines):
        d = json.loads(lines[idx])
        combined_text += "\n" + str(d.get("content", ""))

# Look for json code blocks or raw json structures
matches = re.findall(r'```json\s*(\{[\s\S]*?\})\s*```', combined_text)
print(f"Found {len(matches)} markdown code blocks with json.")

# Also look for content={ ... } or raw json
raw_matches = re.findall(r'content=(\{[\s\S]*?\n\})\s*(?:priority=|$)', combined_text)
print(f"Found {len(raw_matches)} content= blocks.")

found_qids = {}

for m in matches:
    try:
        data = json.loads(m)
        qid = data.get("questionId")
        if qid:
            found_qids[qid] = data
    except Exception as e:
        pass

# Also check transcript transcripts of subagents if needed
print(f"Successfully parsed QIDs from code blocks: {sorted(list(found_qids.keys()))}")
