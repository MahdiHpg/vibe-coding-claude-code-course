from bs4 import BeautifulSoup
import json
import glob

def extract_lesson_full_rsc(html_path):
    html = open(html_path, encoding="utf-8").read()
    soup = BeautifulSoup(html, "html.parser")
    for s in soup.find_all("script"):
        txt = s.get_text()
        if 'correctIndex' in txt:
            # find {"id":"cc-
            pos = txt.find('{\\"id\\":\\"cc-')
            if pos != -1:
                # bracket matching
                open_braces = 0
                in_str = False
                escape = False
                end = -1
                for i in range(pos, len(txt)):
                    ch = txt[i]
                    if escape:
                        escape = False
                        continue
                    if ch == '\\':
                        escape = True
                        continue
                    if ch == '"':
                        in_str = not in_str
                        continue
                    if not in_str:
                        if ch == '{':
                            open_braces += 1
                        elif ch == '}':
                            open_braces -= 1
                            if open_braces == 0:
                                end = i + 1
                                break
                if end != -1:
                    raw_sub = txt[pos:end]
                    clean_json = raw_sub.replace('\\"', '"').replace('\\\\', '\\')
                    try:
                        res = json.loads(clean_json)
                        return res
                    except Exception as e:
                        pass
    return None

files = sorted(glob.glob("lessons_raw/cc-*.html"))
all_rsc_lessons = {}
for f in files:
    slug = f.replace("lessons_raw\\", "").replace(".html", "")
    data = extract_lesson_full_rsc(f)
    if data:
        all_rsc_lessons[slug] = data
        print(f"[{slug}] Full RSC extracted! Keys: {list(data.keys())}")
    else:
        print(f"[{slug}] RSC failed")

with open("all_rsc_lessons.json", "w", encoding="utf-8") as f:
    json.dump(all_rsc_lessons, f, indent=2, ensure_ascii=False)

print(f"Total full RSC extracted: {len(all_rsc_lessons)}/{len(files)}")
