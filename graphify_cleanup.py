import json
from pathlib import Path
from datetime import datetime, timezone
from graphify.detect import save_manifest

detection = json.loads(Path("graphify-out/.graphify_detect.json").read_text(encoding="utf-8"))
save_manifest(detection["files"])

extract = json.loads(Path("graphify-out/.graphify_extract.json").read_text(encoding="utf-8"))
input_tok = extract.get("input_tokens", 0)
output_tok = extract.get("output_tokens", 0)

cost_path = Path("graphify-out/cost.json")
if cost_path.exists():
    cost = json.loads(cost_path.read_text(encoding="utf-8"))
else:
    cost = {"runs": [], "total_input_tokens": 0, "total_output_tokens": 0}

cost["runs"].append({
    "date": datetime.now(timezone.utc).isoformat(),
    "input_tokens": input_tok,
    "output_tokens": output_tok,
    "files": detection.get("total_files", 0),
})
cost["total_input_tokens"] += input_tok
cost["total_output_tokens"] += output_tok
cost_path.write_text(json.dumps(cost, indent=2), encoding="utf-8")

print(f"This run: {input_tok:,} input tokens, {output_tok:,} output tokens")
print(f"All time: {cost['total_input_tokens']:,} input, {cost['total_output_tokens']:,} output ({len(cost['runs'])} runs)")

# Cleanup
import os
for f in [
    "graphify-out/.graphify_detect.json",
    "graphify-out/.graphify_extract.json",
    "graphify-out/.graphify_ast.json",
    "graphify-out/.graphify_semantic.json",
    "graphify-out/.graphify_analysis.json",
    "graphify-out/.graphify_analysis_updated.json",
    "graphify-out/.graphify_labels.json",
    "graphify-out/.graphify_cached.json",
    "graphify-out/.graphify_uncached.txt",
    "graphify-out/.graphify_python",
]:
    try:
        os.remove(f)
    except FileNotFoundError:
        pass

# Cleanup helper scripts
for f in [
    "graphify_setup.py",
    "graphify_detect.py",
    "graphify_detect_source.py",
    "graphify_cache_check.py",
    "graphify_ast.py",
    "graphify_merge.py",
    "graphify_merge_full.py",
    "graphify_verify.py",
    "graphify_build.py",
    "graphify_label.py",
]:
    try:
        os.remove(f)
    except FileNotFoundError:
        pass

print("Cleanup complete")
