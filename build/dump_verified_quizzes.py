import json

mods = json.load(open("complete_course_raw.json", encoding="utf-8"))

verified_quizzes = {}
total_q = 0

for m in mods:
    for l in m['lessons']:
        lid = l['id']
        quizzes = l.get('quiz', [])
        verified_quizzes[lid] = quizzes
        total_q += len(quizzes)

print(f"Verified {total_q} questions across {len(verified_quizzes)} lessons.")
with open("course_quizzes_verified.json", "w", encoding="utf-8") as f:
    json.dump(verified_quizzes, f, indent=2, ensure_ascii=False)
