import json

p = r"C:\Users\Temp\.gemini\antigravity\brain\ab21db2f-9d47-4f90-a70d-12244e825966\.system_generated\logs\transcript_full.jsonl"
with open(p, "r", encoding="utf-8") as f:
    lines = f.readlines()

for idx in [266, 267, 268, 272, 273, 280, 281, 283]:
    if idx < len(lines):
        d = json.loads(lines[idx])
        print(f"=== Line {idx} | step {d.get('step_index')} | type {d.get('type')} | source {d.get('source')} ===")
        content = d.get("content", "")
        if isinstance(content, str):
            print(f"Content length: {len(content)}")
            print(content[:300])
        elif isinstance(content, list):
            print(f"Content list items: {len(content)}")
            print(str(content)[:300])
        print("\n")
