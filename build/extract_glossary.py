from bs4 import BeautifulSoup
import json

soup = BeautifulSoup(open("lessons_raw/glossary.html", encoding="utf-8").read(), "html.parser")
terms = []

for a in soup.find_all("a", href=True):
    if "/ai-coding-dictionary/" in a['href']:
        name = a.find(class_=lambda c: c and "name" in c) or a.find("strong")
        desc = a.find(class_=lambda c: c and ("short" in c or "desc" in c or "text" in c))
        name_t = " ".join(name.get_text().split()) if name else ""
        desc_t = " ".join(desc.get_text().split()) if desc else ""
        if not name_t:
            name_t = " ".join(a.get_text().split())
        if name_t:
            terms.append({"term": name_t, "desc": desc_t, "url": a['href']})

print(f"Glossary terms found: {len(terms)}")
for t in terms[:10]:
    print(f"- {t['term']}: {t['desc'][:60]}")

with open("glossary_structured.json", "w", encoding="utf-8") as f:
    json.dump(terms, f, indent=2, ensure_ascii=False)
