from bs4 import BeautifulSoup
import json
import re
import os

def extract_rsc_data(html_path):
    soup = BeautifulSoup(open(html_path, encoding="utf-8").read(), "html.parser")
    for s in soup.find_all("script"):
        content = s.string or ""
        # Look for the payload containing lesson details
        if '"quiz":[' in content or '"correctIndex":' in content:
            # Let's extract the JSON substring or inspect it
            return content
    return None

data = extract_rsc_data("lessons_raw/cc-01-what-is-claude-code.html")
print("Found payload:", len(data) if data else "None")

# Let's find all occurrences of "quiz"
if data:
    # Find JSON objects inside
    matches = re.findall(r'(\{"id":"cc-\d+-[^"]+".*?\})(?:,\$|\);|\}\])', data)
    print(f"Matched objects: {len(matches)}")
    if not matches:
        # Let's find substring around "id":"cc-
        m = re.search(r'\{"id":"(cc-[^"]+)",.*?"title":"([^"]+)"', data)
        if m:
            print("Found match:", m.group(1), m.group(2))
