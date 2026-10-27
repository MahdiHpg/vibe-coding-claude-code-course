# -*- coding: utf-8 -*-
import json
import os
import sys

target_dir = r"H:\MyWork\Web Projects\4 - آموزش ها توسط AI\19 - vibe-coding-claude-code"
build_dir = os.path.join(target_dir, "build")
sys.path.append(build_dir)

# Load datasets from build_dir
course_data = json.load(open(os.path.join(build_dir, "complete_course_raw.json"), encoding="utf-8"))
quizzes_map = json.load(open(os.path.join(build_dir, "quizzes_persian_ready.json"), encoding="utf-8"))
cheatsheet_fa = json.load(open(os.path.join(build_dir, "cheatsheet_persian_ready.json"), encoding="utf-8"))
glossary_fa = json.load(open(os.path.join(build_dir, "glossary_persian_ready.json"), encoding="utf-8"))
lessons_structured = {l["slug"]: l for l in json.load(open(os.path.join(build_dir, "all_lessons_structured.json"), encoding="utf-8"))}

from persian_course_content import MODULES_TRANSLATION, LESSONS_TRANSLATION

print("Loaded all inputs. Generating 7 markdown chapter files...")

# Module file map
module_filenames = [
    ("cc-m1-setup", "01-setup-and-foundations.md", "۰۲ — جریان‌های کاری هسته", "./02-core-workflows.md"),
    ("cc-m2-core-workflows", "02-core-workflows.md", "۰۳ — قابلیت‌های پیشرفته و قدرت‌بخش", "./03-power-features.md"),
    ("cc-m3-power-features", "03-power-features.md", "۰۴ — الگوها و تکنیک‌های وایب کدینگ", "./04-vibe-coding-patterns.md"),
    ("cc-m4-vibe-patterns", "04-vibe-coding-patterns.md", "۰۵ — پروژه‌های دنیای واقعی و استقرار", "./05-real-projects.md"),
    ("cc-m5-real-projects", "05-real-projects.md", "۰۶ — چیت‌شیت جامع کلود کد", "./06-cheatsheet.md"),
]

for mid, fname, next_title, next_link in module_filenames:
    mod_obj = [m for m in course_data if m["id"] == mid][0]
    m_info = MODULES_TRANSLATION.get(mid, {})
    m_title_fa = m_info.get("title_fa", mod_obj["title"])
    m_summary_fa = m_info.get("summary_fa", mod_obj.get("summary", ""))
    
    lines = []
    lines.append(f"# {m_title_fa}")
    lines.append("")
    lines.append(f"> 📖 **منبع رسمی:** [Vibe Code School — Claude Code Course](https://vibecodeschool.com/courses/claude-code-vibe-coding)")
    lines.append(f"> 🎯 **هدف این فصل:** {m_summary_fa}")
    lines.append("")
    lines.append("---")
    lines.append("")

    for idx, l in enumerate(mod_obj["lessons"], 1):
        lid = l["id"]
        l_info = LESSONS_TRANSLATION.get(lid, {})
        title_fa = l_info.get("title_fa", l.get("title", ""))
        kind_fa = l_info.get("kind_fa", l.get("kind", ""))
        duration = l_info.get("duration_fa", "۵ دقیقه")
        intro_fa = l_info.get("intro_fa", l.get("summary", ""))
        concept_fa = l_info.get("concept_deep_fa", "").strip()

        lines.append(f"## {title_fa}")
        lines.append("")
        lines.append(f"**برچسب:** `{kind_fa}` | **شناسه درس:** `{lid}` | **زمان مطالعه:** {duration}")
        lines.append("")
        lines.append(f"> 💡 **خلاصه اجرایی:** {intro_fa}")
        lines.append("")
        lines.append("### تبیین مفهومی و اصول مهندسی")
        lines.append(concept_fa)
        lines.append("")

        # Content blocks
        if "content" in l and isinstance(l["content"], list):
            for c_item in l["content"]:
                kind = c_item.get("kind")
                if kind == "callout":
                    tone = c_item.get("tone", "info")
                    text = c_item.get("text", "")
                    emoji = "💡" if tone == "info" else ("✅" if tone == "success" else "⚠️")
                    lines.append(f"> {emoji} **نکته کلیدی:** {text}")
                    lines.append("")
                elif kind == "tabs":
                    tabs = c_item.get("tabs", [])
                    lines.append("#### دستورات نصب پلتفرم‌های مختلف:")
                    for tb in tabs:
                        lines.append(f"- **{tb.get('label')}:**")
                        lines.append(f"  ```{tb.get('lang', 'bash')}")
                        lines.append(f"  {tb.get('code')}")
                        lines.append("  ```")
                    lines.append("")

        # Steps
        if "steps" in l and isinstance(l["steps"], list) and len(l["steps"]) > 0:
            lines.append("### 🛠️ کارگاه عملی و مراحل گام‌به‌گام (Hands-on Walkthrough)")
            for s_idx, st in enumerate(l["steps"], 1):
                s_title = st.get("title", "")
                s_body = st.get("body", "") or st.get("prompt", "")
                s_verify = st.get("verify", "")
                lines.append(f"#### گام {s_idx:02d}: {s_title}")
                lines.append(f"{s_body}")
                if s_verify:
                    lines.append(f"- **روش راستی‌آزمایی:** `{s_verify}`")
                lines.append("")

        # Sandbox Transcripts
        if "transcript" in l and isinstance(l["transcript"], list) and len(l["transcript"]) > 0:
            lines.append("### 💬 شبیه‌ساز مکالمه زنده و اجرای چرخه ایجنت (Sandbox Transcript)")
            lines.append("```text")
            for t_turn in l["transcript"][:8]:
                role = t_turn.get("role")
                t_text = t_turn.get("text", "")
                if role == "user":
                    lines.append(f"[کاربر]: {t_text}")
                elif role == "assistant":
                    lines.append(f"[کلود کد]: {t_text}")
                elif role == "tool_call":
                    lines.append(f"  -> [Tool Call] {t_turn.get('tool')}: {t_turn.get('input')}")
                elif role == "tool_result":
                    lines.append(f"  <- [Tool Result]: {t_turn.get('result')[:120]}...")
            lines.append("```")
            lines.append("")

        # Quiz & Practice
        quizzes = l.get("quiz", [])
        if quizzes:
            lines.append("### 📝 آزمون سنجش درک مطلب و تمرین فصل")
            for q_idx, q in enumerate(quizzes, 1):
                raw_q = q.get("q", "")
                c_idx = q.get("correctIndex", 0)
                q_data = quizzes_map.get(raw_q, {})
                q_text_fa = q_data.get("q_fa", raw_q)
                options_fa = q_data.get("options_fa", q.get("options", []))
                exp_fa = q_data.get("explanation_fa", q.get("explanation", ""))

                letters = ["الف", "ب", "ج", "د"]
                lines.append(f"**پرسش {q_idx}:** {q_text_fa}")
                for o_idx, opt in enumerate(options_fa):
                    l_badge = letters[o_idx] if o_idx < len(letters) else chr(65+o_idx)
                    lines.append(f"- **{l_badge})** {opt}")
                
                correct_letter = letters[c_idx] if c_idx < len(letters) else chr(65+c_idx)
                lines.append("")
                lines.append("<details><summary>💡 مشاهده پاسخ صحیح و تحلیل تشریحی</summary>")
                lines.append(f"<p><strong>پاسخ صحیح: گزینه «{correct_letter}»</strong></p>")
                lines.append(f"<p>{exp_fa}</p>")
                lines.append("</details>")
                lines.append("")

        # Terms
        struct_info = lessons_structured.get(lid, {})
        terms = struct_info.get("terms", [])
        if terms:
            lines.append("#### 📚 واژگان تخصصی این درس:")
            for tm in terms:
                lines.append(f"- **{tm.get('term')}:** {tm.get('definition')}")
            lines.append("")

        lines.append("---")
        lines.append("")

    # Summary of module
    lines.append(f"## ✅ جمع‌بندی {m_title_fa}")
    lines.append(f"- تسلط بر مفاهیم و فرامین مطرح‌شده در این فصل پایه و اساس موفقیت شما در ادامه مسیر است.")
    lines.append(f"- همواره پیش از ورود به فصل بعد، تمرینات و فرامین را در یک پروژه واقعی تست کنید.")
    lines.append("")
    lines.append(f"➡️ **گام بعدی:** [رفتن به {next_title}]({next_link})")

    file_path = os.path.join(target_dir, fname)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Created: {fname}")

# 6. Cheatsheet Markdown (06-cheatsheet.md)
cs_lines = []
cs_lines.append("# فصل ۶ — چیت‌شیت جامع و مرجع سریع کلود کد (Claude Code Cheat Sheet)")
cs_lines.append("")
cs_lines.append("> 📖 **مرجع:** [Claude Code Cheat Sheet — Vibe Code School](https://vibecodeschool.com/claude-code-cheat-sheet)")
cs_lines.append("> 🎯 **هدف:** دسترسی سریع به تمامی دستورات اسلش، کلیدهای میانبر، تنظیمات دسترسی، هوک‌ها و گیت ورک‌تری.")
cs_lines.append("")
cs_lines.append("---")
cs_lines.append("")

for cs in cheatsheet_fa:
    cs_lines.append(f"## {cs['title_fa']}")
    cs_lines.append(f"> {cs['desc_fa']}")
    cs_lines.append("")
    cs_lines.append("| دستور / کلید | شرح عملکرد به فارسی |")
    cs_lines.append("|---|---|")
    for it in cs["items"]:
        cmd_clean = it['cmd'].replace('|', '\\|')
        desc_clean = it['desc_fa'].replace('|', '\\|')
        cs_lines.append(f"| `{cmd_clean}` | {desc_clean} |")
    cs_lines.append("")

cs_lines.append("---")
cs_lines.append("➡️ **گام بعدی:** [رفتن به ۰۷ — واژه‌نامه تخصصی هوش مصنوعی و وایب کدینگ](./07-glossary.md)")

with open(os.path.join(target_dir, "06-cheatsheet.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(cs_lines))
print("Created: 06-cheatsheet.md")

# 7. Glossary Markdown (07-glossary.md)
gl_lines = []
gl_lines.append("# فصل ۷ — واژه‌نامه و اصطلاح‌نامه تخصصی هوش مصنوعی و وایب کدینگ (AI Glossary)")
gl_lines.append("")
gl_lines.append("> 📖 **مرجع:** [Vibe Code School AI Glossary](https://vibecodeschool.com/glossary)")
gl_lines.append("> 🎯 **هدف:** فرهنگ تشریحی و دقیق ۸۳ اصطلاح کلیدی مهندسی هوش مصنوعی، مدل‌های زبانی بزرگ، یادگیری عمیق و ایجنت‌ها.")
gl_lines.append("")
gl_lines.append("---")
gl_lines.append("")

for g in glossary_fa:
    gl_lines.append(f"### {g['name_fa']} (`{g['name_en']}`)")
    gl_lines.append(f"{g['desc_fa']}")
    gl_lines.append("")
    gl_lines.append(f"> *English Reference:* {g['desc_en']}")
    gl_lines.append("")
    gl_lines.append("---")
    gl_lines.append("")

gl_lines.append("## ✅ پایان دوره و آغاز سفر وایب کدینگ")
gl_lines.append("شما اکنون مجهز به تمام دانش مفهومی و ابزارهای عملی وایب کدینگ هستید. برای مرور دوباره به [README.md](./README.md) یا فایل PDF دوره مراجعه کنید.")

with open(os.path.join(target_dir, "07-glossary.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(gl_lines))
print("Created: 07-glossary.md")

print("All 7 markdown files generated successfully!")
