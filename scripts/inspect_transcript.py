import json

p = r"C:\Users\Temp\.gemini\antigravity\brain\ab21db2f-9d47-4f90-a70d-12244e825966\.system_generated\logs\transcript.jsonl"
with open(p, "r", encoding="utf-8") as f:
    lines = f.readlines()

for idx in range(max(0, len(lines)-25), len(lines)):
    d = json.loads(lines[idx])
    content = str(d.get("content", ""))
    tool_calls = d.get("tool_calls", [])
    print(f"--- Line {idx} | step {d.get('step_index')} | type {d.get('type')} | source {d.get('source')} ---")
    if tool_calls:
        for tc in tool_calls:
            print(f"  Tool Call: {tc.get('name') or tc.get('function', {}).get('name')}")
    if content:
        print(f"  Content preview: {content[:150]}...")
