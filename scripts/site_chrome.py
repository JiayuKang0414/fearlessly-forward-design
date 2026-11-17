"""Project-owned current-page state for the shared native UMD navigation."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'page-builder/tools'))
from chrome import Chrome


class SiteChrome(Chrome):
    def _mark_current(self, text, rel):
        text = super()._mark_current(text, rel)
        text = re.sub(r'\s+data-selected(?:="[^"]*")?|\s+aria-current="[^"]*"', '', text)
        for href in self._self_hrefs(rel):
            text = text.replace(f'href="{href}"', f'href="{href}" data-selected aria-current="page"')
        return text
