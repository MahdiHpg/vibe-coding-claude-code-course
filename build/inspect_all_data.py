import json

data = json.load(open("complete_course_raw.json", encoding="utf-8"))

for mod in data:
    print(f"\n==================== {mod['id']} : {mod['title']} ====================")
    print(f"Summary: {mod['summary']}")
    for l in mod['lessons']:
        print(f"  - [{l['id']}] {l.get('title')} ({l.get('kind')})")
        if 'body' in l:
            body_type = type(l['body']).__name__
            body_sample = str(l['body'])[:100]
            print(f"      body ({body_type}): {body_sample}...")
        if 'content' in l:
            print(f"      content ({type(l['content']).__name__}): {str(l['content'])[:100]}...")
        if 'steps' in l:
            print(f"      steps ({len(l['steps'])}): {[s.get('title') for s in l['steps']][:3]}...")
        if 'quiz' in l:
            print(f"      quiz ({len(l['quiz'])} questions): correct answers: {[q.get('correctIndex') for q in l['quiz']]}")
        if 'transcript' in l:
            print(f"      transcript ({len(l['transcript'])} steps)")
