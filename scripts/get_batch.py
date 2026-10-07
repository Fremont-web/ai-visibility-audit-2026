import csv
import sys
import os

sys.path.append(os.path.dirname(__file__))
from append_observations import get_completed_ids

def get_next_batch(batch_size=15):
    completed = get_completed_ids()
    comp_qids = {qid for qid, runid in completed}
    with open("consumer_questions.csv", "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    remaining = [r for r in rows if r["id"] not in comp_qids]
    return remaining[:batch_size]

if __name__ == "__main__":
    b = get_next_batch(15)
    print(f"Batch size: {len(b)}")
    for r in b:
        print(f"{r['id']} | {r['city']} | {r['oem']} | {r['intent']} | {r['question']}")
