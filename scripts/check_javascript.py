#!/usr/bin/env python3
"""Check shared and inline script syntax without executing page content."""
from html.parser import HTMLParser
from pathlib import Path
import subprocess
import tempfile

class Scripts(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = False
        self.current = []
        self.scripts = []
    def handle_starttag(self, tag, attrs):
        if tag == 'script':
            self.active = not any(key == 'src' for key, _ in attrs)
            self.current = []
    def handle_endtag(self, tag):
        if tag == 'script':
            if self.active:
                self.scripts.append(''.join(self.current))
            self.active = False
    def handle_data(self, data):
        if self.active:
            self.current.append(data)

ROOT = Path(__file__).resolve().parents[1]
for path in (ROOT / 'js').glob('*.js'):
    subprocess.run(['node', '--check', str(path)], check=True)
for path in ROOT.glob('*.html'):
    parser = Scripts()
    parser.feed(path.read_text(encoding='utf-8'))
    for script in parser.scripts:
        if script.strip():
            with tempfile.NamedTemporaryFile('w', suffix='.js') as temporary:
                temporary.write(script)
                temporary.flush()
                subprocess.run(['node', '--check', temporary.name], check=True)
print('PASS: shared and inline JavaScript syntax')
