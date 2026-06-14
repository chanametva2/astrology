import sys, json
from pathlib import Path
from graphify.detect import classify_file, _is_sensitive, count_words

SKIP_DIRS = {'venv','.venv','env','.env','node_modules','__pycache__','.git','dist','build','target','out','site-packages','.pytest_cache','.mypy_cache','.ruff_cache','.tox','.eggs','graphify-out','coverage','.next','.nuxt','.turbo','.angular','.idea','.cache','.svelte-kit','.terraform','.serverless','.graphify','.worktrees','_site','.jekyll-cache','.bundle','temp'}
SKIP_FILES = {'package-lock.json','yarn.lock','pnpm-lock.yaml','Cargo.lock','poetry.lock','Gemfile.lock','composer.lock','go.sum','go.work.sum'}
root = Path('.').resolve()

files_by_type = {'code': [], 'document': [], 'paper': [], 'image': [], 'video': []}
skipped_sensitive = []
total_words = 0

with open('filelist.txt') as f:
    for line in f:
        p = Path(line.strip())
        try:
            rel = p.relative_to(root)
        except ValueError:
            continue
        if any(part in SKIP_DIRS for part in rel.parts[:-1]):
            continue
        if p.name in SKIP_FILES:
            continue
        if _is_sensitive(p):
            skipped_sensitive.append(str(p))
            continue
        ftype = classify_file(p)
        if ftype:
            files_by_type[ftype.value].append(str(p))
            if ftype.value != 'video':
                wc = count_words(p)
                total_words += wc

for ftype in files_by_type:
    files_by_type[ftype].sort()

total_files = sum(len(v) for v in files_by_type.values())

result = {
    'files': files_by_type,
    'total_files': total_files,
    'total_words': total_words,
    'needs_graph': total_words >= 50000,
    'warning': None,
    'skipped_sensitive': skipped_sensitive,
    'scan_root': str(root),
}
with open('graphify-out/.graphify_detect.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
print(f'DONE: {total_files} files, ~{total_words:,} words')
for k, v in files_by_type.items():
    if v: print(f'  {k}: {len(v)}')
