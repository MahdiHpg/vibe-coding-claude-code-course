from bs4 import BeautifulSoup
import json

soup = BeautifulSoup(open("lessons_raw/cheat-sheet.html", encoding="utf-8").read(), "html.parser")

main = soup.find("main") or soup.find("article") or soup

sections = []
current_sec = None

for el in main.find_all(['h2', 'h3', 'p', 'table', 'pre', 'ul', 'ol', 'div']):
    if el.name == 'h2':
        title = " ".join(el.get_text().split())
        current_sec = {"title": title, "subsections": [], "items": []}
        sections.append(current_sec)
    elif el.name == 'table' and current_sec:
        rows = []
        for tr in el.find_all('tr'):
            cells = [" ".join(c.get_text().split()) for c in tr.find_all(['th', 'td'])]
            rows.append(cells)
        current_sec["items"].append({"type": "table", "rows": rows})
    elif el.name == 'pre' and current_sec:
        current_sec["items"].append({"type": "code", "text": el.get_text().strip()})
    elif el.name in ['ul', 'ol'] and current_sec:
        # direct li
        lis = [" ".join(li.get_text().split()) for li in el.find_all('li', recursive=False)]
        if lis:
            current_sec["items"].append({"type": "list", "items": lis})

print(f"Extracted {len(sections)} sections from cheat sheet:")
for s in sections:
    tables = sum(1 for i in s['items'] if i['type'] == 'table')
    codes = sum(1 for i in s['items'] if i['type'] == 'code')
    print(f"- {s['title']}: {tables} tables, {codes} code blocks")

with open("cheatsheet_structured.json", "w", encoding="utf-8") as f:
    json.dump(sections, f, indent=2, ensure_ascii=False)
