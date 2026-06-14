from graphify.export import to_html
from graphify.build import build_from_json
import json
from pathlib import Path

extraction = json.loads(Path('graphify-out/.graphify_extract.json').read_text(encoding='utf-8'))
G = build_from_json(extraction)

analysis = json.loads(Path('graphify-out/.graphify_analysis.json').read_text(encoding='utf-8'))
communities = {int(k): v for k, v in analysis['communities'].items()}

labels_path = Path('graphify-out/.graphify_labels.json')
if labels_path.exists():
    raw_labels = json.loads(labels_path.read_text(encoding='utf-8'))
    labels = {int(k): v for k, v in raw_labels.items()}
    to_html(G, communities, 'graphify-out/graph.html', community_labels=labels)
else:
    to_html(G, communities, 'graphify-out/graph.html')
print('Wrote graph.html')
