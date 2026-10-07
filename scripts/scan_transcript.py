import json
import re
import os

p = r"C:\Users\Temp\.gemini\antigravity\brain\ab21db2f-9d47-4f90-a70d-12244e825966\.system_generated\logs\transcript_full.jsonl"
with open(p, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
records = {}

for idx, line in enumerate(lines):
    if "questionId" in line:
        try:
            d = json.loads(line)
            content = str(d.get("content", ""))
            matches = re.findall(r'```json\s*(\{[\s\S]*?\})\s*```', content)
            for m in matches:
                try:
                    obj = json.loads(m)
                    qid = obj.get("questionId")
                    rid = obj.get("runId")
                    if qid and rid:
                        records[(qid, rid)] = obj
                except:
                    pass
        except:
            pass

print(f"Total records found via codeblocks: {len(records)}")
qids = set(k[0] for k in records.keys())
print(f"Unique QIDs: {len(qids)}")
print("Sample QIDs:", sorted(list(qids))[:10], "...", sorted(list(qids))[-10:])
