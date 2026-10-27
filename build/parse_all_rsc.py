import json
import re
import glob
import os
from bs4 import BeautifulSoup

def extract_lesson_full_data(slug):
    path = f"lessons_raw/{slug}.html"
    if not os.path.exists(path):
        return None
    
    html = open(path, encoding="utf-8").read()
    soup = BeautifulSoup(html, "html.parser")
    
    # Find script with lesson data
    target_script = None
    for s in soup.find_all("script"):
        txt = s.get_text()
        if f'"{slug}"' in txt or '"correctIndex"' in txt:
            target_script = txt
            break
            
    if not target_script:
        return None
        
    chunks = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', target_script, re.DOTALL)
    if not chunks:
        # maybe unescaped or in single string
        chunks = [target_script]
        
    full_data = "".join(chunks).replace('\\"', '"').replace('\\\\', '\\')
    
    # Try finding the JSON object starting with {"id":"slug" or {"lesson":{"id":"slug"
    # Search for "id":"{slug}"
    pattern = r'\{"id":"' + re.escape(slug) + r'".*?\"quiz\":\[.*?\].*?\}'
    # More flexible: find the slice
    start_str = f'{{"id":"{slug}"'
    start_pos = full_data.find(start_str)
    if start_pos == -1:
        # try without starting curly
        start_str = f'"id":"{slug}"'
        start_pos = full_data.find(start_str)
        if start_pos != -1:
            # step back to find enclosing {
            curly = full_data.rfind('{', 0, start_pos)
            if curly != -1:
                start_pos = curly
                
    if start_pos == -1:
        return None
        
    # Match braces to get the full JSON object
    open_braces = 0
    in_string = False
    escape = False
    end_pos = -1
    
    for i in range(start_pos, len(full_data)):
        ch = full_data[i]
        if escape:
            escape = False
            continue
        if ch == '\\':
            escape = True
            continue
        if ch == '"':
            in_string = not in_string
            continue
        if not in_string:
            if ch == '{':
                open_braces += 1
            elif ch == '}':
                open_braces -= 1
                if open_braces == 0:
                    end_pos = i + 1
                    break
                    
    if end_pos != -1:
        json_str = full_data[start_pos:end_pos]
        try:
            parsed = json.loads(json_str)
            return parsed
        except Exception as e:
            # Let's save the failed string to debug
            # print(f"JSON load failed for {slug}: {e}")
            return None
    return None

# Test on cc-01 and cc-02
for test_s in ["cc-01-what-is-claude-code", "cc-02-install-the-cli", "cc-05-claude-md-and-memory", "cc-12-slash-commands"]:
    res = extract_lesson_full_data(test_s)
    if res:
        print(f"[{test_s}] SUCCESS! Keys:", list(res.keys()))
        if "quiz" in res:
            print(f"   Quiz items: {len(res['quiz'])}")
        if "video" in res:
            print(f"   Video: {res['video'].get('title')}")
        if "steps" in res:
            print(f"   Steps: {len(res['steps'])}")
    else:
        print(f"[{test_s}] FAILED")
