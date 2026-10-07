import csv
import json

with open('consumer_questions.csv', 'r', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

batch_a_ids = ['Q159', 'Q160', 'Q161', 'Q163', 'Q169', 'Q170', 'Q171', 'Q172', 'Q173', 'Q174', 'Q175', 'Q176', 'Q177', 'Q178', 'Q179']

subagents = []
for r in rows:
    if r['id'] in batch_a_ids:
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
with open('scripts/batch_a_subagents.json', 'w', encoding='utf-8') as out:
    json.dump(subagents, out, indent=2)
print("Saved to scripts/batch_a_subagents.json")
