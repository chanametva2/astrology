import json, os
from pathlib import Path

detect = json.loads(Path('graphify-out/.graphify_detect.json').read_text(encoding='utf-8'))

# Use doc files only (code handled by AST, images are decorative blog assets)
doc_files = detect['files']['document']
print(f'Total doc files: {len(doc_files)}')

# Group by directory
from collections import defaultdict
by_dir = defaultdict(list)
for f in doc_files:
    p = Path(f)
    parent = p.parent.name if p.parent.name else '(root)'
    by_dir[parent].append(f)

for d, files in sorted(by_dir.items()):
    print(f'  {d}: {len(files)} files')

# Split into chunks of ~20 files, keeping same-directory files together
chunks = []
current_chunk = []
current_dir = None

# Sort by directory then path
all_sorted = []
for d in sorted(by_dir.keys()):
    all_sorted.extend(sorted(by_dir[d]))

for f in all_sorted:
    p = Path(f)
    parent = p.parent.name if p.parent.name else '(root)'
    
    if current_dir is None:
        current_dir = parent
    elif parent != current_dir and len(current_chunk) >= 20:
        chunks.append(current_chunk)
        current_chunk = []
        current_dir = parent
    
    if len(current_chunk) >= 25:
        chunks.append(current_chunk)
        current_chunk = []
        current_dir = parent
    
    current_chunk.append(f)

if current_chunk:
    chunks.append(current_chunk)

print(f'\nTotal chunks: {len(chunks)}')
for i, chunk in enumerate(chunks):
    dirs = set(Path(f).parent.name for f in chunk)
    print(f'  Chunk {i+1}: {len(chunk)} files [{", ".join(sorted(dirs))}]')
    
# Write chunk files
os.makedirs('graphify-out/chunks', exist_ok=True)
for i, chunk in enumerate(chunks):
    content = '\n'.join(chunk)
    Path(f'graphify-out/chunks/chunk_{i+1:02d}.txt').write_text(content, encoding='utf-8')
    print(f'  Written: chunks/chunk_{i+1:02d}.txt')

print(f'\nDone. Created {len(chunks)} chunks')
