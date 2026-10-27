from bs4 import BeautifulSoup
import re
import json

soup = BeautifulSoup(open("lessons_raw/cc-01-what-is-claude-code.html", encoding="utf-8").read(), "html.parser")
scripts = soup.find_all("script")
for s in scripts:
    content = s.string or ""
    if "quiz" in content.lower() or "Which of these best describes" in content:
        print("Found matching script, length:", len(content))
        # Search for pattern around question
        idx = content.find("Which of these best describes")
        print(content[max(0, idx-200):min(len(content), idx+600)])
