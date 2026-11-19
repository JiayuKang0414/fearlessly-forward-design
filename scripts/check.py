#!/usr/bin/env python3
"""Verify migrated copy, components, navigation and local runtime assets."""
from collections import Counter
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / 'briefs/migration-manifest.json').read_text())


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.in_main = False
        self.main_text = []
        self.components = Counter()
        self.sections = []
        self.tags = []
        self.stack = []
        self.links = []
        self.current_link = None
        self.feed(source)

    def handle_starttag(self, tag, pairs):
        attrs = dict(pairs)
        self.tags.append((tag, attrs))
        if tag == 'main':
            self.in_main = True
        if self.in_main:
            if tag.startswith(('umd-element-', 'umd-layout-', 'umd-feed-')):
                self.components[tag] += 1
            if tag == 'section':
                self.sections.append(attrs)
        if tag == 'a':
            group = 'desktop' if attrs.get('slot') == 'primary-link' else None
            if any(a.get('slot') == 'primary-slide-links' for t, a in self.stack):
                group = 'mobile'
            self.current_link = {'attrs': attrs, 'group': group, 'text': ''}
            self.links.append(self.current_link)
        if tag not in {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}:
            self.stack.append((tag, attrs))

    def handle_endtag(self, tag):
        if tag == 'main':
            self.in_main = False
        if tag == 'a':
            self.current_link = None
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                self.stack = self.stack[:index]
                break

    def handle_data(self, text):
        if self.in_main:
            self.main_text.append(text)
        if self.current_link:
            self.current_link['text'] += text


def local_target(page, value):
    parts = urlsplit(value)
    if parts.scheme or parts.netloc or not parts.path:
        return
    target = (page.parent / unquote(parts.path)).resolve()
    assert target.is_relative_to(ROOT), 'Local reference escapes project'
    assert target.is_file() or (target / 'index.html').is_file(), f'Missing local asset: {parts.path}'


for slug, expected in MANIFEST['pages'].items():
    path = ROOT / expected['path']
    source = path.read_text()
    page = Page(source)
    text = re.sub(r'\s+', ' ', ''.join(page.main_text)).strip()
    assert sha256(text.encode()).hexdigest() == expected['content_sha256'], 'Approved main text changed'
    assert dict(page.components) == expected['components'], 'Approved component structure changed'
    assert len(page.sections) == expected['sections']
    for index, attrs in enumerate(page.sections):
        classes = set(attrs.get('class', '').split())
        next_classes = set(page.sections[index + 1].get('class', '').split()) if index + 1 < len(page.sections) else set()
        adjacent_dark = 'umd-layout-background-full-dark' in classes and 'umd-layout-background-full-dark' in next_classes
        footer_flush = index == len(page.sections) - 1 and attrs.get('id') == 'connect-with-maryland'
        if footer_flush:
            assert 'umd-layout-vertical-landing' not in classes, 'Closing card row must meet the footer without a bottom margin'
        elif adjacent_dark:
            assert 'umd-layout-vertical-landing' not in classes, 'Adjacent dark sections must not introduce a white margin'
        else:
            assert 'umd-layout-vertical-landing' in classes, 'Section missing native landing spacing'
    assert 'github.io/admissions-design' not in source, 'Old hosting URL remains'
    assert not re.search(r'\{\{[A-Z_]+\}\}', source), 'Unresolved template placeholder'
    ids = [a['id'] for t, a in page.tags if 'id' in a]
    assert len(ids) == len(set(ids)), 'Duplicate ID'
    for tag, attrs in page.tags:
        for name in ('src', 'href'):
            value = attrs.get(name)
            if value:
                local_target(path, value)
                if value.startswith('#'):
                    assert value[1:] in ids, 'Broken internal anchor'
        for value in re.findall(r"this\.src='([^']+)'", attrs.get('onerror', '')):
            local_target(path, value)
        if tag == 'img':
            assert attrs.get('alt', '').strip(), 'Missing image description'
    selected_label = 'A Do Good Campus' if slug == 'do-good-now' else 'Innovations in Teaching and Learning'
    for group in ('desktop', 'mobile'):
        links = [link for link in page.links if link['group'] == group]
        assert len(links) == 3
        selected = [link for link in links if 'data-selected' in link['attrs']]
        assert len(selected) == 1 and selected[0]['text'] == selected_label
        assert selected[0]['attrs'].get('aria-current') == 'page'
        destinations = {link['text']: link['attrs']['href'] for link in links}
        assert destinations['A Do Good Campus'].endswith('pages/do-good-now/')
        assert destinations['Innovations in Teaching and Learning'].endswith('pages/we-reimagine-learning/')
    print(f'{slug}: approved copy/components, navigation, spacing classes and local assets OK')

for asset in json.loads((ROOT / 'briefs/asset-manifest.json').read_text()):
    assert sha256((ROOT / asset['path']).read_bytes()).hexdigest() == asset['sha256'], 'Migrated photo changed'
print('All migrated images match their approved source bytes.')
