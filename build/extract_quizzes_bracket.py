from bs4 import BeautifulSoup
import json
import glob

def extract_quiz(html_path):
    html = open(html_path, encoding="utf-8").read()
    soup = BeautifulSoup(html, "html.parser")
    for s in soup.find_all("script"):
        txt = s.get_text()
        if '\"correctIndex\"' in txt or '"correctIndex"' in txt:
            # find "quiz":[
            marker = '\"quiz\":['
            idx = txt.find(marker)
            if idx == -1:
                marker = '"quiz":['
                idx = txt.find(marker)
            if idx != -1:
                start = idx + len(marker) - 1 # starts at [
                # find matching ]
                open_brackets = 0
                in_str = False
                escape = False
                end = -1
                for i in range(start, len(txt)):
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
                        if ch == '[':
                            open_brackets += 1
                        elif ch == ']':
                            open_brackets -= 1
                            if open_brackets == 0:
                                end = i + 1
                                break
                if end != -1:
                    raw_sub = txt[start:end]
                    # It has escaped quotes like \"
                    # Let's decode JSON string or unescape
                    # If it's inside a JSON string literal, let's wrap it or replace \" with "
                    clean_json = raw_sub.replace('\\"', '"').replace('\\\\', '\\')
                    try:
                        return json.loads(clean_json)
                    except Exception as e:
                        # try without unescaping
                        try:
                            return json.loads(raw_sub)
                        except:
                            # Let's see what the error is
                            # print("Failed parse:", e, clean_json[:100])
                            pass
    return None

files = sorted(glob.glob("lessons_raw/cc-*.html"))
quizzes_dict = {}
for f in files:
    slug = f.replace("lessons_raw\\", "").replace(".html", "")
    q = extract_quiz(f)
    if q:
        quizzes_dict[slug] = q
        print(f"[{slug}] {len(q)} questions extracted successfully!")
    else:
        print(f"[{slug}] Failed")

with open("all_quizzes_rich.json", "w", encoding="utf-8") as f:
    json.dump(quizzes_dict, f, indent=2, ensure_ascii=False)
