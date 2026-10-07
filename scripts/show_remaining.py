import csv
import sys
import os

sys.path.append(os.path.dirname(__file__))
from append_observations import get_completed_ids

completed = get_completed_ids()
comp_qids = {qid for qid, runid in completed}

with open("consumer_questions.csv", "r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

remaining = [r for r in rows if r["id"] not in comp_qids]
print(f"Total questions in bank: {len(rows)}")
print(f"Already completed: {len(comp_qids)}")
print(f"Remaining in baseline: {len(remaining)}")

with open("repeat_questions.csv", "r", encoding="utf-8") as f:
    repeats = list(csv.DictReader(f))
print(f"Total repeat questions scheduled: {len(repeats)}")
