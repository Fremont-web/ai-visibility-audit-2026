import json
import re
import os
import sys

sys.path.append(os.path.dirname(__file__))
from append_observations import append_observation, get_completed_ids

p = r"C:\Users\Temp\.gemini\antigravity\brain\ab21db2f-9d47-4f90-a70d-12244e825966\.system_generated\logs\transcript_full.jsonl"
with open(p, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total transcript lines: {len(lines)}")

completed = get_completed_ids()
existing_qids = {qid for qid, runid in completed}
print(f"Currently in observations.jsonl: {len(existing_qids)} QIDs")

found_records = {}
decoder = json.JSONDecoder()

for idx, line in enumerate(lines):
    if "questionId" in line or "runId" in line:
        try:
            d = json.loads(line)
            content = str(d.get("content", ""))
            
            # Check markdown blocks ```json ... ```
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

            # Check if there is an embedded JSON object
            pos = 0
            while True:
                qpos = content.find('"questionId"', pos)
                if qpos == -1:
                    break
                # search backwards for '{'
                brace_pos = content.rfind('{', 0, qpos)
                if brace_pos != -1:
                    try:
                        obj, _ = decoder.raw_decode(content[brace_pos:].strip())
                        qid = obj.get("questionId")
                        rid = obj.get("runId")
                        if qid and rid:
                            found_records[(qid, rid)] = obj
                    except Exception as e:
                        pass
                pos = qpos + len('"questionId"')
        except:
            pass

print(f"Total valid unique (qid, rid) records found in transcript: {len(found_records)}")

new_added = 0
for (qid, rid), record in sorted(found_records.items()):
    if qid not in existing_qids:
        append_observation(record)
        existing_qids.add(qid)
        new_added += 1
        print(f"Appended {qid} ({rid})")

print(f"New records appended: {new_added}")
print(f"Total unique QIDs now: {len(existing_qids)}")
