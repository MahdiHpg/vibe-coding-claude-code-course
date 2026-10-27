import json

with open("all_lessons_structured.json", encoding="utf-8") as f:
    lessons = json.load(f)

print(f"Total lessons: {len(lessons)}")
total_items = 0
total_quizzes = 0
total_terms = 0

for idx, l in enumerate(lessons):
    items_count = len(l['content_items'])
    q_count = len(l['quizzes'])
    t_count = len(l['terms'])
    steps_count = len(l['steps'])
    total_items += items_count
    total_quizzes += q_count
    total_terms += t_count
    print(f"[{idx+1:02d}] {l['slug']} (Mod {l['module_num']}): {items_count} items, {steps_count} steps, {q_count} quizzes, {t_count} terms")

print(f"\nTotals: {total_items} content items, {total_quizzes} quizzes, {total_terms} vocabulary terms")
