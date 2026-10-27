import json
import re
from bs4 import BeautifulSoup

html = open("lessons_raw/cc-01-what-is-claude-code.html", encoding="utf-8").read()
soup = BeautifulSoup(html, "html.parser")
for s in soup.find_all("script"):
    txt = s.get_text()
    if 'correctIndex' in txt:
        # Find where {"id":"cc-01 begins
        pos = txt.find('{"id":"cc-01')
        print("pos in raw script:", pos)
        print("Substring around pos:")
        print(txt[pos:pos+400])
        break
