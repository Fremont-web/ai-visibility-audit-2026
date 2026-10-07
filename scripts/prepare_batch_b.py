import csv
import json

with open('consumer_questions.csv', 'r', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

batch_b_ids = ['Q180', 'Q181', 'Q182', 'Q183', 'Q184', 'Q185', 'Q186', 'Q187', 'Q188', 'Q189', 'Q190', 'Q191', 'Q192', 'Q193', 'Q194']

subagents = []
for r in rows:
    if r['id'] in batch_b_ids:
        qid = r['id']
        run_id = f"RUN-BASE-{qid}-WEB"
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
        subagents.append({
            "TypeName": "audit_respondent",
            "Role": f"Automotive Respondent {qid}",
            "Prompt": prompt,
            "Model": "inherit"
        })

print(f"Prepared {len(subagents)} subagents.")
with open('scripts/batch_b_subagents.json', 'w', encoding='utf-8') as out:
    json.dump(subagents, out, indent=2)
print("Saved to scripts/batch_b_subagents.json")
