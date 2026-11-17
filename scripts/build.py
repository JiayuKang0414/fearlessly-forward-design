#!/usr/bin/env python3
"""Build only this independent project's approved public review pages."""
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def run(*args):
    subprocess.run([sys.executable, *args], cwd=ROOT, check=True)


run('scripts/build-chrome.py')
run('page-builder/tools/inline-critical.py', '--root', '.', 'pages')
run('scripts/check.py')

dist = ROOT / 'dist'
if dist.exists():
    shutil.rmtree(dist)
dist.mkdir()
for name in ('pages', 'images'):
    shutil.copytree(ROOT / name, dist / name)
(dist / 'scripts').mkdir()
for name in ('do-good-pathway.js', 'learning-pathway.js', 'do-good-hero.js'):
    shutil.copy2(ROOT / 'scripts' / name, dist / 'scripts' / name)
(dist / 'page-builder/scripts').mkdir(parents=True)
shutil.copy2(ROOT / 'page-builder/scripts/grid-animations.js', dist / 'page-builder/scripts/grid-animations.js')
shutil.copy2(ROOT / 'index.html', dist / 'index.html')
(dist / '.nojekyll').touch()
print('Built independent Fearlessly Forward site in dist/.')
