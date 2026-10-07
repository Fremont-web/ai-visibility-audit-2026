import json
import re
import sys
import os

sys.path.append(os.path.dirname(__file__))
from append_observations import append_observation, get_completed_ids

p = r"C:\Users\Temp\.gemini\antigravity\brain\ab21db2f-9d47-4f90-a70d-12244e825966\.system_generated\logs\transcript_full.jsonl"
with open(p, "r", encoding="utf-8") as f:
    lines = f.readlines()

combined_text = ""
for idx in [280, 282, 283, 284, 285, 286]:
    if idx < len(lines):
        d = json.loads(lines[idx])
        combined_text += "\n" + str(d.get("content", ""))

matches = re.findall(r'```json\s*(\{[\s\S]*?\})\s*```', combined_text)

found_qids = {}
for m in matches:
    try:
        data = json.loads(m)
        qid = data.get("questionId")
        if qid:
            found_qids[qid] = data
    except Exception as e:
        print(f"Error parsing json: {e}")

print(f"Found {len(found_qids)} parsed question responses.")
completed = get_completed_ids()
existing_qids = {qid for qid, runid in completed}

saved_count = 0
for qid in sorted(found_qids.keys()):
    record = found_qids[qid]
    if qid in existing_qids:
        print(f"Question {qid} already in observations. Skipping.")
    else:
        append_observation(record)
        saved_count += 1
        print(f"Appended {qid} ({record.get('runId')})")

print(f"Total new records appended: {saved_count}")
new_completed = get_completed_ids()
print(f"Total observations now on disk: {len(new_completed)}")
