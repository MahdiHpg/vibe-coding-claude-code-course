import urllib.request
import os
from bs4 import BeautifulSoup

extras = [
    ("cheat-sheet", "https://vibecodeschool.com/claude-code-cheat-sheet"),
    ("glossary", "https://vibecodeschool.com/glossary"),
    ("how-to-vibe-code", "https://vibecodeschool.com/how-to-vibe-code"),
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for name, url in extras:
    path = f"lessons_raw/{name}.html"
    if not os.path.exists(path):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as resp:
                data = resp.read().decode('utf-8')
            with open(path, "w", encoding="utf-8") as f:
                f.write(data)
            print(f"Downloaded {name}: {len(data)} bytes")
        except Exception as e:
            print(f"Failed {name}: {e}")
