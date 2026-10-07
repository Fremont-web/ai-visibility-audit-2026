import json

p = r"C:\Users\Temp\.gemini\antigravity\brain\ab21db2f-9d47-4f90-a70d-12244e825966\.system_generated\logs\transcript.jsonl"
with open(p, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Scanning {len(lines)} lines for Q032 or subagent outputs...")
for i, l in enumerate(lines):
    if "Q032" in l or "RUN-BASE-Q032" in l:
        d = json.loads(l)
        print(f"Match on line {i}, step {d.get('step_index')}, type={d.get('type')}, source={d.get('source')}")
