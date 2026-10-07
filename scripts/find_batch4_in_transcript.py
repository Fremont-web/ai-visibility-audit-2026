import json
import re

p = r"C:\Users\Temp\.gemini\antigravity\brain\ab21db2f-9d47-4f90-a70d-12244e825966\.system_generated\logs\transcript_full.jsonl"
with open(p, "r", encoding="utf-8") as f:
    lines = f.readlines()

for idx in range(270, min(len(lines), 290)):
    d = json.loads(lines[idx])
    content = str(d.get("content", ""))
    # Look for runId or JSON objects with questionId
    qids = re.findall(r'Q0[34]\d', content)
    if qids:
        print(f"Line {idx} (step {d.get('step_index')}) mentions QIDs: {set(qids)}, length={len(content)}")
