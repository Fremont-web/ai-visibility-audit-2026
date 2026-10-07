import json

p = r"C:\Users\Temp\.gemini\antigravity\brain\ab21db2f-9d47-4f90-a70d-12244e825966\.system_generated\logs\transcript_full.jsonl"
with open(p, "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        if "invoke_subagent" in line:
            d = json.loads(line)
            for tc in d.get("tool_calls", []):
                args = tc.get("Arguments", {})
                for sa in args.get("Subagents", []):
                    print(f"Line {i} | Role: {sa.get('Role')}")
                    print("Prompt:\n", sa.get("Prompt")[:500])
                    print("="*60)
                    break
