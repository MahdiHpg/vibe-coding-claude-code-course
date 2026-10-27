import json

data = json.load(open("cheatsheet_structured.json", encoding="utf-8"))

for s in data:
    print(f"=== {s['title']} ===")
    for item in s['items'][:3]:
        print("  -", item['type'], ":", str(item.get('text') or item.get('rows') or item.get('items'))[:100])
