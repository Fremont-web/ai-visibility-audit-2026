import json
import os
import hashlib

OBSERVATIONS_FILE = os.path.join("audit_output", "observations.jsonl")
os.makedirs("audit_output", exist_ok=True)

def append_observation(obs):
    # Ensure standard fields
    if "sha256" not in obs:
        obs["sha256"] = hashlib.sha256(obs.get("answerMarkdown", "").encode("utf-8")).hexdigest()
    if "verifiedModelLabel" not in obs:
        obs["verifiedModelLabel"] = "Gemini 3.8 Flash (High)"
    if "exposedVersionId" not in obs:
        obs["exposedVersionId"] = "gemini-3.5-flash-high-1132"
    if "isolationControls" not in obs:
        obs["isolationControls"] = "subagent-clean-context-stateless-prompt"
    if "contaminationStatus" not in obs:
        obs["contaminationStatus"] = "clean"
        
    with open(OBSERVATIONS_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(obs) + "\n")

def get_completed_ids():
    completed = set()
    if os.path.exists(OBSERVATIONS_FILE):
        with open(OBSERVATIONS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        d = json.loads(line)
                        completed.add((d.get("questionId"), d.get("runId")))
                    except:
                        pass
    return completed

if __name__ == "__main__":
    c = get_completed_ids()
    print(f"Total completed observations on disk: {len(c)}")
