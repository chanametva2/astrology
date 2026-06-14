import sys, json
from graphify.build import build_from_json
from graphify.cluster import score_all
from graphify.analyze import god_nodes, surprising_connections, suggest_questions
from graphify.report import generate
from pathlib import Path

extraction = json.loads(Path('graphify-out/.graphify_extract.json').read_text(encoding='utf-8'))
detection  = json.loads(Path('graphify-out/.graphify_detect.json').read_text(encoding='utf-8'))
analysis   = json.loads(Path('graphify-out/.graphify_analysis.json').read_text(encoding='utf-8'))

G = build_from_json(extraction)
communities = {int(k): v for k, v in analysis['communities'].items()}
cohesion = {int(k): v for k, v in analysis['cohesion'].items()}
tokens = {'input': extraction.get('input_tokens', 0), 'output': extraction.get('output_tokens', 0)}

labels = {
    0: "Life Planning & Transits",
    1: "Core Wiki Concepts",
    2: "Houses & Hemispheres",
    3: "Tithi & Moon Phases",
    4: "Aspects & Patterns",
    5: "Moon Manifestation",
    6: "Essential Dignity",
    7: "Sect & Dispositors",
    8: "Annual Profection Technique",
    9: "Zodiac & Symbolism",
    10: "Planets & Houses Basics",
    11: "Air & Fire Signs",
    12: "Life Planning Concepts",
    13: "Elements & Modalities",
    14: "Trump Case Study",
    15: "Primal Triad",
    16: "Moon & Tithi Wiki",
    17: "Water & Earth Signs",
    18: "Sect Wiki",
    19: "Lunar Nodes",
    20: "Pluto Generations",
    21: "Test Scripts",
    22: "Collective Souls",
    23: "Run Scripts",
    24: "Devcontainer",
    25: "AGENTS.md",
    26: "GitHub Pages",
    27: "Jekyll Chirpy Theme",
    28: "Quintile Aspect",
    29: "Semisextile Aspect",
    30: "Sesquiquadrate Aspect",
    31: "Site Base URL",
    32: "Site Theme Mode",
    33: "Site Timezone",
    34: "Site Config",
    35: "Contact Data",
    36: "Share Data",
    37: "About Tab",
    38: "Archives Tab",
    39: "Categories Tab",
    40: "Tags Tab",
    41: "Wiki Tab",
    42: "File List Temp",
    43: "Site Index",
    44: "Home Layout",
    45: "Post Layout",
    46: "Wiki Layout",
    47: "Post Lastmod Plugin",
    48: "Result Temp",
}

questions = suggest_questions(G, communities, labels)

report = generate(G, communities, cohesion, labels, analysis['gods'], analysis['surprises'], detection, tokens, '.', suggested_questions=questions)
Path('graphify-out/GRAPH_REPORT.md').write_text(report, encoding='utf-8')
Path('graphify-out/.graphify_labels.json').write_text(json.dumps({str(k): v for k, v in labels.items()}, ensure_ascii=False), encoding='utf-8')
print('Report updated with community labels')
print(f'Labeled {len(labels)} communities')
