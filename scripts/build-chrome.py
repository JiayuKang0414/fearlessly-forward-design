#!/usr/bin/env python3
"""Run the canonical chrome inliner with this project's current-page state."""
from pathlib import Path
import runpy
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from site_chrome import SiteChrome
import chrome

chrome.Chrome = SiteChrome
runpy.run_path(str(ROOT / 'page-builder/tools/build-chrome.py'), run_name='__main__')
