import csv

with open('repeat_questions.csv', 'r', encoding='utf-8') as f:
    repeats = list(csv.DictReader(f))

print(f"Total repeat questions: {len(repeats)}")
for r in repeats[:10]:
    print(f"{r['id']} | {r['city']} | {r['oem']} | {r['intent']} | {r['question']}")
