import csv
import json

with open("repeat_questions.csv", "r", encoding="utf-8") as f:
    rep_csv = {r["id"]: r for r in csv.DictReader(f)}

target_qids = ["Q139", "Q144", "Q146", "Q153", "Q155", "Q158", "Q174", "Q175", "Q178", "Q179"]

subagents_payload = []
for qid in target_qids:
    q_row = rep_csv[qid]
    q_text = q_row["question"].strip()
    prompt = f"""Question ID: {qid}
Run ID: RUN-REPEAT-{qid}-WEB
Tool Mode: web_assisted
Consumer Question: "{q_text}"

Instructions:
Please follow your neutral respondent protocol. Conduct web research using search_web or read_url_content to answer the consumer question thoroughly and objectively for an ordinary shopper in Wyoming.
Distinguish local dealerships from regional alternatives.
Return your full consumer answer and structured record in the exact JSON format specified in your protocol.
Send the final JSON payload back to the controller via send_message."""

    subagents_payload.append({
        "TypeName": "audit_respondent",
        "Role": f"Repeat Fix {qid}",
        "Prompt": prompt,
        "Model": "inherit"
    })

with open("scripts/repeat_fixes_subagents.json", "w", encoding="utf-8") as f:
    json.dump(subagents_payload, f, indent=2)

print(f"Generated {len(subagents_payload)} subagent specs in scripts/repeat_fixes_subagents.json")
