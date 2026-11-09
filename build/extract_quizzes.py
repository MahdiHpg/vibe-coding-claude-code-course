from bs4 import BeautifulSoup
import re
import json
import glob

def extract_quiz_from_html(html_path):
    html = open(html_path, encoding="utf-8").read()
    soup = BeautifulSoup(html, "html.parser")
    for s in soup.find_all("script"):
        txt = s.get_text()
        if 'correctIndex' in txt:
            # find quiz array
            m = re.search(r'\\"quiz\\":(\[.*?\]),\\"terms\\":', txt)
            if not m:
                m = re.search(r'"quiz":(\[.*?\]),"terms":', txt)
            if not m:
                m = re.search(r'\\"quiz\\":(\[.*?\]),\\"', txt)
            if not m:
                m = re.search(r'"quiz":(\[.*?\]),"', txt)
            if m:
                raw_json = m.group(1).replace('\\"', '"').replace('\\\\', '\\')
                try:
                    return json.loads(raw_json)
                except Exception as e:
                    # Let's clean up or parse manually
                    pass
    return None

files = sorted(glob.glob("lessons_raw/cc-*.html"))
success = 0
for f in files:
    q = extract_quiz_from_html(f)
    slug = f.replace("lessons_raw\\", "").replace(".html", "")
    if q:
        success += 1
        print(f"[{slug}] {len(q)} questions extracted! Sample Q1 correct: opt {q[0].get('correctIndex')} -> {q[0].get('explanation')[:60]}")
    else:
        print(f"[{slug}] Failed to extract quiz")

print(f"Total quiz extracted: {success}/{len(files)}")
