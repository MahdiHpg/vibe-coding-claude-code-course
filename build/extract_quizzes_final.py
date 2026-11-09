from bs4 import BeautifulSoup
import json
import glob

def extract_quiz(html_path):
    html = open(html_path, encoding="utf-8").read()
    soup = BeautifulSoup(html, "html.parser")
    for s in soup.find_all("script"):
        txt = s.get_text()
        if 'correctIndex' in txt:
            q_idx = txt.find('quiz')
            while q_idx != -1:
                # check if followed by [
                open_b = txt.find('[', q_idx)
                if open_b != -1 and open_b - q_idx < 15:
                    # found the array start!
                    open_brackets = 0
                    in_str = False
                    escape = False
                    end = -1
                    for i in range(open_b, len(txt)):
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
                        raw_sub = txt[open_b:end]
                        # unescape:
                        clean_json = raw_sub.replace('\\"', '"').replace('\\\\', '\\')
                        try:
                            res = json.loads(clean_json)
                            if isinstance(res, list) and len(res) > 0 and 'correctIndex' in res[0]:
                                return res
                        except:
                            pass
                q_idx = txt.find('quiz', q_idx + 1)
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
print(f"Total quizzes found: {len(quizzes_dict)}/{len(files)}")
