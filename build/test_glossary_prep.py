import json

glossary = json.load(open("glossary_terms.json", encoding="utf-8"))

# Let's inspect the terms
print(f"Glossary has {len(glossary)} terms")

# Sample terms
for t in glossary[:5]:
    print(t['name'], "->", t['description'][:60])
