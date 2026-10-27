from bs4 import BeautifulSoup
import json
import re

html = open("lessons_raw/cc-01-what-is-claude-code.html", encoding="utf-8").read()
soup = BeautifulSoup(html, "html.parser")
target_script = [s.get_text() for s in soup.find_all("script") if 'correctIndex' in s.get_text()][0]

mod_ids = ['cc-m1-setup', 'cc-m2-core-workflows', 'cc-m3-power-features', 'cc-m4-vibe-patterns', 'cc-m5-real-projects']
decoder = json.JSONDecoder()
modules_data = []

for mid in mod_ids:
    needle = f'{{\\"id\\":\\"{mid}\\"'
    pos = target_script.find(needle)
    if pos == -1:
        needle = f'{{"id":"{mid}"'
        pos = target_script.find(needle)
    if pos != -1:
        raw_slice = target_script[pos:pos+50000]
        clean_slice = raw_slice.replace('\\"', '"').replace('\\\\', '\\')
        try:
            mod_obj, idx = decoder.raw_decode(clean_slice)
            modules_data.append(mod_obj)
            print(f"Loaded {mid}: {mod_obj.get('title')} with {len(mod_obj.get('lessons', []))} lessons (len: {idx})")
        except Exception as e:
            print(f"Error parsing {mid}: {e}")

with open("complete_course_raw.json", "w", encoding="utf-8") as f:
    json.dump(modules_data, f, indent=2, ensure_ascii=False)

print("TOTAL MODULES:", len(modules_data))
total_lessons = sum(len(m.get('lessons', [])) for m in modules_data)
print("TOTAL LESSONS:", total_lessons)
