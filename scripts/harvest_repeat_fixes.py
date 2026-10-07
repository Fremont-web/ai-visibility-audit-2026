import json
import csv
import hashlib
from pathlib import Path

def get_hash(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def main():
    transcript_path = Path(r"C:\Users\Temp\.gemini\antigravity\brain\6cc0d098-773b-4a25-a987-1031f3388c21\.system_generated\logs\transcript_full.jsonl")
    obs_path = Path("audit_output/observations.jsonl")
    repeat_csv_path = Path("repeat_questions.csv")

    with open(repeat_csv_path, "r", encoding="utf-8") as f:
        repeat_questions = {r["id"]: r for r in csv.DictReader(f)}

    target_qids = {"Q139", "Q144", "Q146", "Q153", "Q155", "Q158", "Q174", "Q175", "Q178", "Q179"}

    # Harvest latest messages for these target QIDs
    harvested = {}
    with open(transcript_path, "r", encoding="utf-8") as f:
        for line in f:
            line_str = line.strip()
            if not line_str:
                continue
            try:
                row = json.loads(line_str)
            except Exception:
                continue

            content = row.get("content", "")
            if not isinstance(content, str):
                continue
            if '"runId"' in content and '"RUN-REPEAT-' in content:
                # Find JSON block
                s_idx = content.find("{")
                e_idx = content.rfind("}")
                if s_idx != -1 and e_idx != -1 and e_idx > s_idx:
                    cand = content[s_idx:e_idx+1]
                    try:
                        record = json.loads(cand)
                    except Exception:
                        continue
                    qid = record.get("questionId")
                    run_id = record.get("runId", "")
                    if qid in target_qids and run_id == f"RUN-REPEAT-{qid}-WEB":
                        # Check question match
                        expected_q = repeat_questions[qid]["question"].strip()
                        actual_q = record.get("question", "").strip()
                        if expected_q == actual_q:
                            record["rawAnswerHash"] = get_hash(record.get("answerMarkdown", ""))
                            record["receivedTimestamp"] = row.get("created_at", "")
                            harvested[qid] = record

    print(f"Harvested {len(harvested)} exact matching repeat records out of {len(target_qids)} targeted.")

    if harvested:
        # Read existing observations
        existing_obs = []
        with open(obs_path, "r", encoding="utf-8") as f:
            for line in f:
                existing_obs.append(json.loads(line))

        # Replace or update the target repeat observations
        updated_obs = []
        replaced_count = 0
        for o in existing_obs:
            run_id = o.get("runId", "")
            qid = o.get("questionId", "")
            if "REPEAT" in run_id and qid in harvested:
                # Replace with the exact harvested record
                updated_obs.append(harvested[qid])
                replaced_count += 1
                del harvested[qid] # Avoid duplicate addition
            else:
                updated_obs.append(o)

        # If any remained that weren't in existing_obs, append them
        for qid, record in harvested.items():
            updated_obs.append(record)
            replaced_count += 1

        # Write back updated observations
        with open(obs_path, "w", encoding="utf-8") as f:
            for o in updated_obs:
                f.write(json.dumps(o, ensure_ascii=False) + "\n")

        print(f"Successfully updated {replaced_count} repeat records in {obs_path}. Total records now: {len(updated_obs)}")

if __name__ == "__main__":
    main()
