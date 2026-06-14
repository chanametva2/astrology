import sys, json, glob
from pathlib import Path

# 1. Load AST
ast = json.loads(Path('graphify-out/.graphify_ast.json').read_text(encoding='utf-8'))
print(f'AST: {len(ast["nodes"])} nodes, {len(ast["edges"])} edges')

# 2. Load all semantic chunks
chunks = sorted(glob.glob('graphify-out/chunks/result_*.json'))
all_sem_nodes = []
all_sem_edges = []
total_in = 0
total_out = 0

for c in chunks:
    d = json.loads(Path(c).read_text(encoding='utf-8'))
    nodes = d.get('nodes', [])
    edges = d.get('edges', [])
    all_sem_nodes += nodes
    all_sem_edges += edges
    total_in += d.get('input_tokens', 0)
    total_out += d.get('output_tokens', 0)
    print(f'{Path(c).name}: {len(nodes)} nodes, {len(edges)} edges')

# 3. Merge: AST nodes first, semantic nodes deduped by id
seen = {n['id'] for n in ast['nodes']}
merged_nodes = list(ast['nodes'])
for n in all_sem_nodes:
    if n['id'] not in seen:
        merged_nodes.append(n)
        seen.add(n['id'])

merged_edges = ast['edges'] + all_sem_edges

merged = {
    'nodes': merged_nodes,
    'edges': merged_edges,
    'hyperedges': [],
    'input_tokens': total_in,
    'output_tokens': total_out,
}

Path('graphify-out/.graphify_extract.json').write_text(
    json.dumps(merged, indent=2, ensure_ascii=False), encoding='utf-8'
)

print(f'\nMerged: {len(merged_nodes)} nodes, {len(merged_edges)} edges')
print(f'  ({len(ast["nodes"])} AST + {len(all_sem_nodes)} semantic)')
print(f'  Tokens: {total_in:,} in / {total_out:,} out')
