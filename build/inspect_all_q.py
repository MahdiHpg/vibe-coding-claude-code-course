# -*- coding: utf-8 -*-
import json

raw_quizzes = json.load(open("all_quizzes_rich.json", encoding="utf-8"))

# Let's inspect all questions to make sure we have accurate Persian translations
print("Total lessons with quizzes:", len(raw_quizzes))
all_q_list = []
for slug, qlist in raw_quizzes.items():
    for q in qlist:
        all_q_list.append((slug, q.get("q")))

print(f"Total quiz questions: {len(all_q_list)}")
for slug, q_text in all_q_list[:10]:
    print(f"[{slug}] {q_text}")
