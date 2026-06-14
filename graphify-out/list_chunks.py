import json
from pathlib import Path

root = Path('.').resolve()

for i in range(1, 7):
    content = Path(f'graphify-out/chunks/chunk_{i:02d}.txt').read_text('utf-8')
    files = [f.strip() for f in content.strip().split('\n') if f.strip()]
    rel_files = []
    for f in files:
        try:
            rel = str(Path(f).relative_to(root))
        except ValueError:
            rel = f
        rel_files.append(rel)
    print(f'=== Chunk {i} ({len(rel_files)} files) ===')
    for rf in rel_files:
        print(f'  {rf}')
    print()
