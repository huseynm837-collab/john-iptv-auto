import re
import urllib.request
from pathlib import Path

BASE = 'https://iptv-org.github.io/iptv'
SOURCES = [f'{BASE}/countries/{c}.m3u' for c in ('az','tr','ru')]
SOURCES += [f'{BASE}/categories/{c}.m3u' for c in ('news','sports','movies','music','kids','documentary','education','entertainment')]
BLOCK = re.compile(r'adult|xxx|porn|erotic|18\+|для взрослых|эротик|porno|yetişkin|знакомства', re.I)
OUTPUT = Path('docs/playlist.m3u')

def download(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'JOHN-IPTV-AUTO/1.0'})
    with urllib.request.urlopen(req, timeout=25) as response:
        return response.read().decode('utf-8-sig', errors='replace')

def parse(text):
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if not line.startswith('#EXTINF:'):
            continue
        j = index + 1
        extras = []
        while j < len(lines) and lines[j].startswith('#') and not lines[j].startswith('#EXTINF:'):
            extras.append(lines[j]); j += 1
        if j < len(lines) and lines[j].strip().startswith(('http://','https://')):
            yield line, extras, lines[j].strip()

def main():
    seen = set()
    entries = []
    succeeded = 0
    for source in SOURCES:
        try:
            content = download(source)
            succeeded += 1
        except Exception as exc:
            print(f'WARNING: {source}: {exc}')
            continue
        for meta, extras, url in parse(content):
            if BLOCK.search(meta):
                continue
            if url in seen:
                continue
            seen.add(url)
            entries.extend([meta, *extras, url])
    if succeeded == 0 or not entries:
        raise RuntimeError('No channels collected: keep the previous playlist')
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    tmp = OUTPUT.with_suffix('.tmp')
    tmp.write_text('#EXTM3U\n' + '\n'.join(entries) + '\n', encoding='utf-8')
    tmp.replace(OUTPUT)
    print(f'Collected {len(seen)} unique stream URLs from {succeeded} sources')

if __name__ == '__main__':
    main()
