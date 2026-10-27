# -*- coding: utf-8 -*-
import os
import shutil
import stat

def on_rm_error(func, path, exc_info):
    try:
        os.chmod(path, stat.S_IWRITE)
        func(path)
    except Exception:
        pass

base_dir = r"H:\MyWork\Web Projects\4 - آموزش ها توسط AI\19 - vibe-coding-claude-code"
nested_dir = os.path.join(base_dir, "vibe-coding-claude-code")
build_dir = os.path.join(base_dir, "build")
os.makedirs(build_dir, exist_ok=True)

# 1. If nested_dir exists, move its contents into base_dir or build_dir
if os.path.exists(nested_dir):
    for root, dirs, files in os.walk(nested_dir, topdown=False):
        for f in files:
            fp = os.path.join(root, f)
            rel = os.path.relpath(fp, nested_dir)
            target_p = os.path.join(base_dir, rel)
            os.makedirs(os.path.dirname(target_p), exist_ok=True)
            if os.path.exists(target_p):
                os.chmod(target_p, stat.S_IWRITE)
                os.remove(target_p)
            shutil.move(fp, target_p)
    shutil.rmtree(nested_dir, onerror=on_rm_error)
    print("Flattened nested folder.")

# 2. Files that belong in build/
build_items = [
    "fonts",
    "lessons_raw",
    "pdf_preview",
    "all_lessons_structured.json",
    "all_quizzes_rich.json",
    "all_rsc_lessons.json",
    "cheatsheet_persian_ready.json",
    "cheatsheet_structured.json",
    "complete_course_raw.json",
    "course_quizzes_verified.json",
    "course_structure.txt",
    "debug_quiz_match.py",
    "debug_rsc_extract.py",
    "download_vazir.py",
    "dump_rsc.py",
    "dump_verified_quizzes.py",
    "extract_all.py",
    "extract_all_modules.py",
    "extract_all_rsc_lessons.py",
    "extract_cheatsheet.py",
    "extract_full_rsc.py",
    "extract_glossary.py",
    "extract_master_curriculum.py",
    "extract_quizzes.py",
    "extract_quizzes_bracket.py",
    "extract_quizzes_final.py",
    "extract_terms_ldjson.py",
    "fetch_extras.py",
    "fetch_lessons.py",
    "find_browser.py",
    "find_quiz_answers.py",
    "generate_persian_glossary.py",
    "glossary_persian_ready.json",
    "glossary_structured.json",
    "glossary_terms.json",
    "inspect_all_data.py",
    "inspect_all_lessons.py",
    "inspect_all_q.py",
    "inspect_cc02.py",
    "inspect_cheatsheet_details.py",
    "inspect_cheatsheet_json.py",
    "inspect_deep.py",
    "inspect_glossary_html.py",
    "inspect_lesson.py",
    "inspect_lesson_details.py",
    "inspect_rsc_file.py",
    "inspect_terms_quiz.py",
    "inspect_transcript.py",
    "master_curriculum.json",
    "page_dump.html",
    "parse_all_rsc.py",
    "parse_cheatsheet_deep.py",
    "parse_course.py",
    "persian_course_content.py",
    "prepare_persian_cheatsheet.py",
    "print_article.py",
    "print_cc01_all.py",
    "print_cheatsheet.py",
    "print_howtovibecode.py",
    "print_samples_full.py",
    "quizzes_persian_ready.json",
    "render_more_preview.py",
    "render_pdf_preview.py",
    "rsc_sample.txt",
    "rsc_unescaped.txt",
    "test.html",
    "test.pdf",
    "test_browser_pdf.py",
    "test_glossary_prep.py",
    "test_init_book.py",
    "test_load_all.py",
    "test_parse_lessons.py",
    "translate_all_quizzes.py",
    "build_full_book.py",
    "check_all_ids.py",
    "check_font_b64.py",
    "check_next_data.py",
    "check_pdf_pages.py",
    "check_quiz_details.py",
    "check_scripts.py"
]

for b_item in build_items:
    src = os.path.join(base_dir, b_item)
    if os.path.exists(src):
        dst = os.path.join(build_dir, b_item)
        if os.path.exists(dst):
            if os.path.isdir(dst):
                shutil.rmtree(dst, onerror=on_rm_error)
            else:
                os.chmod(dst, stat.S_IWRITE)
                os.remove(dst)
        shutil.move(src, dst)

# Rename or copy html/pdf in build as course.html / course.pdf
vibe_html = os.path.join(base_dir, "vibe_coding_claude_code_complete.html")
if os.path.exists(vibe_html):
    shutil.copy(vibe_html, os.path.join(build_dir, "course.html"))
    shutil.move(vibe_html, os.path.join(build_dir, "vibe_coding_claude_code_complete.html"))

vibe_pdf = os.path.join(base_dir, "vibe_coding_claude_code_complete.pdf")
if os.path.exists(vibe_pdf):
    shutil.copy(vibe_pdf, os.path.join(build_dir, "course.pdf"))
    shutil.move(vibe_pdf, os.path.join(build_dir, "vibe_coding_claude_code_complete.pdf"))

# Ensure root has the main Persian named PDF
main_pdf_root = os.path.join(base_dir, "دوره کامل وایب کدینگ با کلود کد.pdf")
if not os.path.exists(main_pdf_root) and os.path.exists(os.path.join(build_dir, "course.pdf")):
    shutil.copy(os.path.join(build_dir, "course.pdf"), main_pdf_root)

print("Files organized into build/ successfully!")
