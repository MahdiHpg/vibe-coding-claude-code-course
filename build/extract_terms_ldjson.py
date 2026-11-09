from bs4 import BeautifulSoup
import json

soup = BeautifulSoup(open("lessons_raw/glossary.html", encoding="utf-8").read(), "html.parser")
scripts = soup.find_all("script", type="application/ld+json")
terms = []
for s in scripts:
    data = json.loads(s.string)
    if "hasDefinedTerm" in data:
        terms = data["hasDefinedTerm"]
        break

print(f"Extracted {len(terms)} defined terms!")
with open("glossary_terms.json", "w", encoding="utf-8") as f:
    json.dump(terms, f, indent=2, ensure_ascii=False)

for t in terms[:10]:
    print(f"- {t['name']}: {t['description'][:70]}...")
