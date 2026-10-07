import json

p = r"C:\Users\Temp\.gemini\antigravity\brain\ab21db2f-9d47-4f90-a70d-12244e825966\.system_generated\logs\transcript_full.jsonl"
with open(p, "r", encoding="utf-8") as f:
    lines = [json.loads(l) for l in f]

print(f"Total lines: {len(lines)}")
for idx in range(600, len(lines)):
    item = lines[idx]
    src = item.get("source")
    typ = item.get("type")
    content = str(item.get("content", ""))
    tcalls = item.get("tool_calls", [])
    if tcalls:
        tc_names = [tc.get("toolAction") or tc.get("toolSummary") for tc in tcalls]
        print(f"Line {idx} [{src} / {typ}]: tool_calls={tc_names}")
    elif "questionId" in content or "RUN-" in content:
        print(f"Line {idx} [{src} / {typ}]: content len={len(content)}, preview={content[:100]}...")
