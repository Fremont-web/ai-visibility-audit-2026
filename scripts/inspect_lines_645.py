import json

p = r"C:\Users\Temp\.gemini\antigravity\brain\ab21db2f-9d47-4f90-a70d-12244e825966\.system_generated\logs\transcript_full.jsonl"
with open(p, "r", encoding="utf-8") as f:
    lines = [json.loads(l) for l in f]

for idx in [645, 647, 649, 651, 652, 653, 654, 656, 664, 665, 666]:
    item = lines[idx]
    content = str(item.get("content", ""))
    print(f"=== Line {idx} ===")
    first_line = content.split("\n")[0]
    print(first_line[:120])
    for line in content.split("\n"):
        if "questionId" in line or "runId" in line or "Q1" in line:
            print("   ", line[:100])
