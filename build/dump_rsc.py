from bs4 import BeautifulSoup
import re
import json

soup = BeautifulSoup(open("lessons_raw/cc-01-what-is-claude-code.html", encoding="utf-8").read(), "html.parser")
target_script = None
for s in soup.find_all("script"):
    txt = s.get_text()
    if 'correctIndex' in txt:
        target_script = txt
        break

if target_script:
    print("Found script of length:", len(target_script))
    # Write to a file to inspect
    with open("rsc_sample.txt", "w", encoding="utf-8") as f:
        f.write(target_script)
    print("Wrote rsc_sample.txt")
