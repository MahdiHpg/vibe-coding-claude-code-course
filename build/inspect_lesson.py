from bs4 import BeautifulSoup
import sys

soup = BeautifulSoup(open("lessons_raw/cc-01-what-is-claude-code.html", encoding="utf-8").read(), "html.parser")

# Find main content container
for tag in ['article', 'main', 'div']:
    matches = soup.find_all(tag, class_=True)
    for m in matches:
        classes = " ".join(m.get('class', []))
        if any(k in classes for k in ['lesson', 'prose', 'content', 'markdown']):
            print(f"Tag <{tag} class='{classes}'> len: {len(m.get_text())}")

print("\n--- Direct H1, H2, H3 ---")
for h in soup.find_all(['h1', 'h2', 'h3']):
    print(f"<{h.name}> {h.get_text(strip=True)}")
