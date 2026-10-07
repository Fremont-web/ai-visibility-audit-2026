import json
import re

p = r"C:\Users\Temp\.gemini\antigravity\brain\ab21db2f-9d47-4f90-a70d-12244e825966\.system_generated\logs\transcript_full.jsonl"
with open(p, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
for idx in range(320, len(lines)):
    d = json.loads(lines[idx])
    content = str(d.get("content", ""))
    if "Q047" in content or "Q056" in content or "RUN-BASE-Q0" in content:
        print(f"Line {idx}: step={d.get('step_index')}, type={d.get('type')}, source={d.get('source')}, content_len={len(content)}")
        # print first 100 chars
        print(content[:150])
        print("---")
