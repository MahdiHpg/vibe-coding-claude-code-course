from bs4 import BeautifulSoup
import json
import os
import glob

lessons_meta = [
    ("cc-01-what-is-claude-code", "01", "Setup & Foundations", "01. What Is Claude Code"),
    ("cc-02-install-the-cli", "01", "Setup & Foundations", "02. Install the CLI"),
    ("cc-03-first-conversation", "01", "Setup & Foundations", "03. Your First Conversation"),
    ("cc-04-the-agentic-loop", "01", "Setup & Foundations", "04. The Agentic Loop"),
    ("cc-05-claude-md-and-memory", "01", "Setup & Foundations", "05. CLAUDE.md and Project Memory"),
    ("cc-06-reading-and-editing", "02", "Core Workflows", "06. Reading and Editing Files"),
    ("cc-07-searching-the-codebase", "02", "Core Workflows", "07. Searching the Codebase"),
    ("cc-08-running-tests", "02", "Core Workflows", "08. Running Tests with Claude"),
    ("cc-09-git-and-commits", "02", "Core Workflows", "09. Git Operations and Commits"),
    ("cc-10-multi-file-refactors", "02", "Core Workflows", "10. Multi-File Refactors"),
    ("cc-11-debugging", "02", "Core Workflows", "11. Debugging with Claude"),
    ("cc-12-slash-commands", "03", "Power Features", "12. Slash Commands"),
    ("cc-13-custom-slash-commands", "03", "Power Features", "13. Writing Your Own Slash Command"),
    ("cc-28-agent-skills", "03", "Power Features", "14. Agent Skills"),
    ("cc-14-subagents", "03", "Power Features", "15. Subagents and the Agent Tool"),
    ("cc-15-plan-mode", "03", "Power Features", "16. Plan Mode"),
    ("cc-16-hooks", "03", "Power Features", "17. Hooks: Pre and Post Tool"),
    ("cc-17-mcp-servers", "03", "Power Features", "18. MCP Servers"),
    ("cc-18-spec-tests-code", "04", "Vibe Coding Patterns", "19. Spec -> Tests -> Code"),
    ("cc-19-iterative-refinement", "04", "Vibe Coding Patterns", "20. Iterative Refinement"),
    ("cc-20-when-to-interrupt", "04", "Vibe Coding Patterns", "21. When to Interrupt vs Let It Run"),
    ("cc-21-code-review", "04", "Vibe Coding Patterns", "22. Code Review with Claude"),
    ("cc-22-pair-programming-flow", "04", "Vibe Coding Patterns", "23. The Pair-Programming Flow"),
    ("cc-23-nextjs-feature", "05", "Real Projects", "24. Building a Next.js Feature"),
    ("cc-24-tests-first", "05", "Real Projects", "25. Writing Tests-First"),
    ("cc-25-legacy-migration", "05", "Real Projects", "26. Migrating Legacy Code"),
    ("cc-26-shipping-to-production", "05", "Real Projects", "27. Shipping to Production"),
    ("cc-27-capstone", "05", "Real Projects", "28. Capstone: Ship a Side Project"),
]

def clean_text(text):
    if not text:
        return ""
    return " ".join(text.split())

def extract_lesson(slug, mod_num, mod_title, lesson_full_title):
    path = f"lessons_raw/{slug}.html"
    if not os.path.exists(path):
        return None
    soup = BeautifulSoup(open(path, encoding="utf-8").read(), "html.parser")
    article = soup.find("article", class_="lesson-content")
    if not article:
        return None

    eyebrow = ""
    eyebrow_el = article.find(class_="lesson-eyebrow")
    if eyebrow_el:
        eyebrow = clean_text(eyebrow_el.get_text())

    title = ""
    title_el = article.find(class_="lesson-title") or article.find("h1")
    if title_el:
        title = clean_text(title_el.get_text())

    summary = ""
    summary_el = article.find(class_="lesson-summary")
    if summary_el:
        summary = clean_text(summary_el.get_text())

    # Extract all content items in order
    content_items = []

    # 1. Lesson Body
    body = article.find("div", class_="lesson-body")
    if body:
        for child in body.children:
            if not child.name:
                continue
            if child.name == 'p':
                content_items.append({"type": "paragraph", "text": clean_text(child.get_text())})
            elif child.name in ['h2', 'h3', 'h4']:
                content_items.append({"type": "heading", "level": child.name, "text": clean_text(child.get_text())})
            elif child.name in ['ul', 'ol']:
                items = [clean_text(li.get_text()) for li in child.find_all('li')]
                content_items.append({"type": "list", "items": items, "ordered": (child.name == 'ol')})
            elif child.name == 'pre':
                content_items.append({"type": "code", "text": child.get_text().strip()})
            elif child.name == 'blockquote':
                content_items.append({"type": "quote", "text": clean_text(child.get_text())})

    # 2. Lesson Blocks
    blocks = article.find("div", class_="lesson-blocks")
    if blocks:
        for b in blocks.children:
            if not b.name:
                continue
            classes = b.get('class', [])
            if 'gb-callout' in classes:
                kind = 'info'
                for k in ['info', 'success', 'warning', 'danger']:
                    if k in classes:
                        kind = k
                c_title = b.find(class_="gb-callout-title")
                c_body = b.find(class_="gb-callout-body") or b
                t_str = clean_text(c_title.get_text()) if c_title else ""
                b_str = clean_text(c_body.get_text()) if c_body else clean_text(b.get_text())
                if t_str and b_str.startswith(t_str):
                    b_str = b_str[len(t_str):].strip()
                content_items.append({"type": "callout", "kind": kind, "title": t_str, "text": b_str})
            elif 'gb-code' in classes:
                head = b.find(class_="gb-code-head")
                head_str = clean_text(head.get_text()) if head else ""
                code_el = b.find("pre") or b.find("code")
                c_str = code_el.get_text().strip() if code_el else clean_text(b.get_text())
                content_items.append({"type": "code", "title": head_str, "text": c_str})
            elif 'gb-expand' in classes or b.name == 'details':
                sum_el = b.find("summary")
                sum_str = clean_text(sum_el.get_text()) if sum_el else ""
                det_text = clean_text(b.get_text())
                if sum_str and det_text.startswith(sum_str):
                    det_text = det_text[len(sum_str):].strip()
                content_items.append({"type": "expand", "title": sum_str, "text": det_text})
            elif 'gb-tabbar' in classes:
                tabs = [clean_text(btn.get_text()) for btn in b.find_all("button")]
                content_items.append({"type": "tabbar", "tabs": tabs})
            else:
                txt = clean_text(b.get_text())
                if txt:
                    content_items.append({"type": "block", "text": txt})

    # 3. Lesson Steps
    steps_list = article.find("ol", class_="lesson-steps")
    steps = []
    if steps_list:
        for s in steps_list.find_all("li", class_="lesson-step"):
            s_title = s.find(class_="lesson-step-title")
            s_body = s.find(class_="lesson-step-body")
            s_verify = s.find(class_="lesson-step-verify")
            steps.append({
                "title": clean_text(s_title.get_text()) if s_title else "",
                "body": clean_text(s_body.get_text()) if s_body else "",
                "verify": clean_text(s_verify.get_text()) if s_verify else ""
            })

    # 4. Quizzes
    quizzes = []
    quiz_sec = article.find("div", class_="lesson-quiz")
    if quiz_sec:
        for card in quiz_sec.find_all("div", class_="quiz-card"):
            q_el = card.find("div", class_="quiz-q")
            q_str = clean_text(q_el.get_text()) if q_el else ""
            options = []
            for opt in card.find_all("button", class_="quiz-option"):
                letter = opt.find(class_="quiz-option-letter")
                l_str = clean_text(letter.get_text()) if letter else ""
                full_t = clean_text(opt.get_text())
                if l_str and full_t.startswith(l_str):
                    full_t = full_t[len(l_str):].strip()
                options.append({"letter": l_str, "text": full_t})
            if q_str:
                quizzes.append({"question": q_str, "options": options})

    # 5. Vocabulary / Terms
    terms = []
    terms_sec = article.find("section", class_="lesson-terms")
    if terms_sec:
        for t in terms_sec.find_all("a", class_="lesson-term"):
            name = t.find(class_="lesson-term-name")
            desc = t.find(class_="lesson-term-short")
            if name and desc:
                terms.append({
                    "term": clean_text(name.get_text()),
                    "definition": clean_text(desc.get_text())
                })

    return {
        "slug": slug,
        "module_num": mod_num,
        "module_title": mod_title,
        "lesson_num_title": lesson_full_title,
        "eyebrow": eyebrow,
        "title": title,
        "summary": summary,
        "content_items": content_items,
        "steps": steps,
        "quizzes": quizzes,
        "terms": terms
    }

all_extracted = []
for slug, m_num, m_title, l_title in lessons_meta:
    data = extract_lesson(slug, m_num, m_title, l_title)
    if data:
        all_extracted.append(data)

with open("all_lessons_structured.json", "w", encoding="utf-8") as f:
    json.dump(all_extracted, f, indent=2, ensure_ascii=False)

print(f"Extracted {len(all_extracted)} lessons successfully!")
