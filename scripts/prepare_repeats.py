import csv
import json

with open('repeat_questions.csv', 'r', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

subagents_pass1 = []
subagents_pass2 = []

for i, r in enumerate(rows):
    qid = r['id']
    run_id = f"RUN-REPEAT-{qid}-WEB"
    q_text = r['question']
    prompt = f"""Question ID: {qid}
Run ID: {run_id}
Tool Mode: web_assisted
Consumer Question: "{q_text}"

Instructions:
Please follow your neutral respondent protocol. Conduct web research using search_web or read_url_content to answer the consumer question thoroughly and objectively for an ordinary shopper in Wyoming.
Distinguish local dealerships from regional alternatives.
Return your full consumer answer and structured record in the exact JSON format specified in your protocol.
Send the final JSON payload back to the controller via send_message."""
    item = {
        "TypeName": "audit_respondent",
        "Role": f"Repeat Respondent {qid}",
        "Prompt": prompt,
        "Model": "inherit"
    }
    if i < 18:
        subagents_pass1.append(item)
    else:
        subagents_pass2.append(item)

print(f"Repeat Pass 1 count: {len(subagents_pass1)}")
print(f"Repeat Pass 2 count: {len(subagents_pass2)}")

with open('scripts/repeat_pass1_subagents.json', 'w', encoding='utf-8') as out:
    json.dump(subagents_pass1, out, indent=2)

with open('scripts/repeat_pass2_subagents.json', 'w', encoding='utf-8') as out:
    json.dump(subagents_pass2, out, indent=2)

print("Saved repeat batches.")
