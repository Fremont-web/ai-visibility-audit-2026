import json

p = r"C:\Users\Temp\.gemini\antigravity\brain\ab21db2f-9d47-4f90-a70d-12244e825966\.system_generated\logs\transcript_full.jsonl"
with open(p, "r", encoding="utf-8") as f:
    lines = f.readlines()

decoder = json.JSONDecoder()
found = {}

for idx in range(355, len(lines)):
    d = json.loads(lines[idx])
    content = str(d.get("content", ""))
    # Look for "content={"
    pos = content.find("content={")
    if pos != -1:
        start_idx = pos + len("content=")
        try:
            obj, end_pos = decoder.raw_decode(content[start_idx:].strip())
            qid = obj.get("questionId")
            if qid:
                found[qid] = obj
                print(f"Decoded {qid} from line {idx}!")
        except Exception as e:
            print(f"Error on line {idx}: {e}")

print(f"Total decoded from lines 355+: {len(found)}")
