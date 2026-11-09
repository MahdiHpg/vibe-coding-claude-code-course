import json

mods = json.load(open("complete_course_raw.json", encoding="utf-8"))

for m in mods:
    print(f"=== {m['id']} : {m['title']} ===")
    for l in m['lessons']:
        print(f"  Lesson {l['id']}: {l.get('title')}")
        if 'body' in l:
            body = l['body']
            if isinstance(body, list):
                print(f"    Body items: {len(body)} paragraphs/snippets")
                for b in body:
                    print(f"      - {str(b)[:60]}...")
            elif isinstance(body, str):
                print(f"    Body string: {body[:80]}...")
        if 'steps' in l:
            print(f"    Steps: {len(l['steps'])}")
            for s in l['steps']:
                print(f"      * Step: {s.get('title')} -> {s.get('prompt') or s.get('body')}")
        if 'transcript' in l:
            print(f"    Transcript: {len(l['transcript'])} dialogue turns")
