import json

data = json.load(open("all_rsc_lessons.json", encoding="utf-8"))

all_modules = {}
all_lessons_by_id = {}

for slug, mod in data.items():
    mod_id = mod.get("id")
    if mod_id not in all_modules:
        all_modules[mod_id] = {
            "id": mod_id,
            "title": mod.get("title"),
            "summary": mod.get("summary"),
            "lessons_count": len(mod.get("lessons", []))
        }
    for l in mod.get("lessons", []):
        lid = l.get("id")
        if lid not in all_lessons_by_id:
            all_lessons_by_id[lid] = l
            l["module_id"] = mod_id
            l["module_title"] = mod.get("title")

print(f"Unique modules: {len(all_modules)}")
for mid, m in all_modules.items():
    print(f"- {mid}: {m['title']} ({m['lessons_count']} lessons)")

print(f"\nUnique lessons: {len(all_lessons_by_id)}")
for lid, l in all_lessons_by_id.items():
    print(f"  [{lid}] {l.get('title')} ({l.get('kind')}) keys: {list(l.keys())}")

with open("master_curriculum.json", "w", encoding="utf-8") as f:
    json.dump({
        "modules": all_modules,
        "lessons": all_lessons_by_id
    }, f, indent=2, ensure_ascii=False)
