from bs4 import BeautifulSoup
import re
import glob

files = sorted(glob.glob("lessons_raw/cc-*.html"))
for f in files:
    html = open(f, encoding="utf-8").read()
    soup = BeautifulSoup(html, "html.parser")
    slug = f.replace("lessons_raw\\", "").replace(".html", "")
    ids = []
    for s in soup.find_all("script"):
        txt = s.get_text()
        if 'correctIndex' in txt:
            matches = re.findall(r'\"id\":\"(cc-[^\"]+)\"', txt.replace('\\"', '"'))
            ids.extend(matches)
    print(f"[{slug}] found ids:", list(dict.fromkeys(ids)))
