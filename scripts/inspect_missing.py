import csv

with open('consumer_questions.csv', 'r', encoding='utf-8') as f:
    all_q = list(csv.DictReader(f))

print(f"Total questions: {len(all_q)}")
for q in all_q[153:]:
    print(f"{q['id']} | {q['city']} | {q['oem']} | {q['intent']} | {q['question']}")
