import json
import base64
import os
import subprocess
import html

# Load fonts
font_dir = "fonts"
b64_regular = base64.b64encode(open(os.path.join(font_dir, "Vazirmatn-Regular.woff2"), "rb").read()).decode("utf-8")
b64_bold = base64.b64encode(open(os.path.join(font_dir, "Vazirmatn-Bold.woff2"), "rb").read()).decode("utf-8")
b64_semibold = base64.b64encode(open(os.path.join(font_dir, "Vazirmatn-SemiBold.woff2"), "rb").read()).decode("utf-8")
b64_medium = base64.b64encode(open(os.path.join(font_dir, "Vazirmatn-Medium.woff2"), "rb").read()).decode("utf-8")

# Load structured datasets
course_data = json.load(open("complete_course_raw.json", encoding="utf-8"))
quizzes_rich = json.load(open("all_quizzes_rich.json", encoding="utf-8"))
lessons_structured = {l["slug"]: l for l in json.load(open("all_lessons_structured.json", encoding="utf-8"))}
cheatsheet_data = json.load(open("cheatsheet_structured.json", encoding="utf-8"))
glossary_data = json.load(open("glossary_terms.json", encoding="utf-8"))

print("All datasets loaded successfully!")
