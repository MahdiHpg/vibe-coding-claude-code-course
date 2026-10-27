from bs4 import BeautifulSoup
import json

soup = BeautifulSoup(open("lessons_raw/cc-01-what-is-claude-code.html", encoding="utf-8").read(), "html.parser")
for s in soup.find_all("script"):
    t = s.get("type", "")
    src = s.get("src", "")
    content = s.string or ""
    print(f"Script type='{t}' src='{src}' len={len(content)}")
    if "self.__next_f" in content:
        print("Found App Router self.__next_f!")
