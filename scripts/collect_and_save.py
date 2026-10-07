import json
import re
import sys
import os

sys.path.append(os.path.dirname(__file__))
from append_observations import append_observation, get_completed_ids

p = r"C:\Users\Temp\.gemini\antigravity\brain\ab21db2f-9d47-4f90-a70d-12244e825966\.system_generated\logs\transcript_full.jsonl"
if not os.path.exists(p):
    p = r"C:\Users\Temp\.gemini\antigravity\brain\ab21db2f-9d47-4f90-a70d-12244e825966\.system_generated\logs\transcript.jsonl"

with open(p, "r", encoding="utf-8") as f:
    lines = f.readlines()

completed = get_completed_ids()
existing_keys = {(qid, runid) for qid, runid in completed}

decoder = json.JSONDecoder()
found_records = {}

for idx, line in enumerate(lines):
    if "questionId" in line or "runId" in line:
        try:
            d = json.loads(line)
            content = str(d.get("content", ""))
            
            # Method 1: Check for "content={"
            pos = content.find("content={")
            if pos != -1:
                start_idx = pos + len("content=")
                try:
                    obj, _ = decoder.raw_decode(content[start_idx:].strip())
                    qid = obj.get("questionId")
                    rid = obj.get("runId")
                    if qid and rid:
                        found_records[(qid, rid)] = obj
                except Exception as e:
                    pass

            # Method 2: Check for markdown code blocks ```json { ... } ```
            blocks = re.findall(r'```json\s*(\{[\s\S]*?\})\s*```', content)
            for b in blocks:
                try:
                    data = json.loads(b)
                    qid = data.get("questionId")
                    rid = data.get("runId")
                    if qid and rid:
                        found_records[(qid, rid)] = data
                except:
                    pass

            # Method 3: Direct JSON string
            content_stripped = content.strip()
            if content_stripped.startswith("{") and content_stripped.endswith("}"):
                try:
                    data, _ = decoder.raw_decode(content_stripped)
                    qid = data.get("questionId")
                    rid = data.get("runId")
                    if qid and rid:
                        found_records[(qid, rid)] = data
                except:
                    pass

        except Exception as e:
            pass

print(f"Total parsed valid records in transcript: {len(found_records)}")

new_saved = 0
for key, record in sorted(found_records.items()):
    if key not in existing_keys:
        append_observation(record)
        existing_keys.add(key)
        new_saved += 1
        print(f"Appended: {key[0]} ({key[1]})")

print(f"New observations added: {new_saved}")
current_total = get_completed_ids()
print(f"Total completed observations in file: {len(current_total)}")
