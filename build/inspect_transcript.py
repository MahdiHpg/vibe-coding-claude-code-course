import json

data = json.load(open("complete_course_raw.json", encoding="utf-8"))

for mod in data:
    for l in mod['lessons']:
        if 'transcript' in l:
            print(f"[{l['id']}] Transcript length: {len(l['transcript'])}")
            print("First 2 steps:")
            for s in l['transcript'][:2]:
                print("   ", s)
            break
    break
