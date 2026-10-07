import json
import re
import os
import sys

sys.path.append(os.path.dirname(__file__))
from append_observations import append_observation, get_completed_ids

CONV_ID = "6cc0d098-773b-4a25-a987-1031f3388c21"
p = rf"C:\Users\Temp\.gemini\antigravity\brain\{CONV_ID}\.system_generated\logs\transcript_full.jsonl"
if not os.path.exists(p):
    p = rf"C:\Users\Temp\.gemini\antigravity\brain\{CONV_ID}\.system_generated\logs\transcript.jsonl"

if not os.path.exists(p):
    print("Transcript not found yet:", p)
    sys.exit(0)

with open(p, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Transcript lines in current conversation: {len(lines)}")

completed = get_completed_ids()
existing_qids = {qid for qid, runid in completed}
print(f"Existing completed observations count: {len(completed)}")

found_records = {}
decoder = json.JSONDecoder()

for idx, line in enumerate(lines):
    if "questionId" in line or "runId" in line:
        try:
            d = json.loads(line)
            content = str(d.get("content", ""))
            
            # Check markdown blocks
            blocks = re.findall(r'```json\s*(\{[\s\S]*?\})\s*```', content)
            for b in blocks:
                try:
                    obj = json.loads(b)
                    qid = obj.get("questionId")
                    rid = obj.get("runId")
                    if qid and rid:
                        found_records[(qid, rid)] = obj
                except:
                    pass

            # Check direct JSON search
            pos = 0
            while True:
                qpos = content.find('"questionId"', pos)
                if qpos == -1:
                    break
                brace_pos = content.rfind('{', 0, qpos)
                if brace_pos != -1:
                    try:
                        obj, _ = decoder.raw_decode(content[brace_pos:].strip())
                        qid = obj.get("questionId")
                        rid = obj.get("runId")
                        if qid and rid:
                            found_records[(qid, rid)] = obj
                    except:
                        pass
                pos = qpos + len('"questionId"')
        except:
            pass

print(f"Found {len(found_records)} valid records in current transcript.")
new_added = 0
for (qid, rid), record in sorted(found_records.items()):
    if (qid, rid) not in completed:
        append_observation(record)
        completed.add((qid, rid))
        new_added += 1
        print(f"Appended {qid} ({rid})")

print(f"New records added to observations.jsonl: {new_added}")
print(f"Total completed observations now: {len(completed)}")
