import zipfile
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "audit_output"
ZIP_PATH = BASE_DIR / "audit_evidence.zip"

def package_zip():
    print(f"Creating evidence archive: {ZIP_PATH}")
    files_to_include = [
        ("report.html", BASE_DIR / "report.html"),
        ("observations.jsonl", OUTPUT_DIR / "observations.jsonl"),
        ("scorecard_model.csv", OUTPUT_DIR / "scorecard_model.csv"),
        ("scorecard_city.csv", OUTPUT_DIR / "scorecard_city.csv"),
        ("scorecard_oem.csv", OUTPUT_DIR / "scorecard_oem.csv"),
        ("scorecard_intent.csv", OUTPUT_DIR / "scorecard_intent.csv"),
        ("repeat_comparison.csv", OUTPUT_DIR / "repeat_comparison.csv"),
        ("alias_table.csv", OUTPUT_DIR / "alias_table.csv"),
        ("owned_domains.csv", OUTPUT_DIR / "owned_domains.csv"),
        ("attempt_log.csv", OUTPUT_DIR / "attempt_log.csv"),
        ("resume_queue.json", OUTPUT_DIR / "resume_queue.json"),
        ("manifest.json", OUTPUT_DIR / "manifest.json"),
        ("score_audit.py", BASE_DIR / "scripts" / "score_audit.py"),
        ("score_audit_helpers.py", BASE_DIR / "scripts" / "score_audit_helpers.py"),
        ("consumer_questions.csv", BASE_DIR / "consumer_questions.csv"),
        ("repeat_questions.csv", BASE_DIR / "repeat_questions.csv"),
        ("neutral_respondent_protocol.txt", BASE_DIR / "neutral_respondent_protocol.txt")
    ]

    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
        for arcname, filepath in files_to_include:
            if filepath.exists():
                zipf.write(filepath, arcname=arcname)
                print(f"  Added: {arcname} ({filepath.stat().st_size:,} bytes)")
            else:
                print(f"  WARNING: File missing: {filepath}")

        # Also add all raw individual answers
        raw_answers_dir = OUTPUT_DIR / "raw_answers"
        if raw_answers_dir.exists():
            for p in sorted(raw_answers_dir.glob("*.md")):
                arcname = f"raw_answers/{p.name}"
                zipf.write(p, arcname=arcname)
            print(f"  Added {len(list(raw_answers_dir.glob('*.md')))} raw answer markdown files into raw_answers/")

    print(f"\nSuccessfully created {ZIP_PATH} ({ZIP_PATH.stat().st_size:,} bytes)")

if __name__ == "__main__":
    package_zip()
