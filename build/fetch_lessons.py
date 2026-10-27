import urllib.request
import os
import time
import json
from bs4 import BeautifulSoup

lessons = [
    ("cc-01-what-is-claude-code", "Module 01: Setup & Foundations", "01. What Is Claude Code"),
    ("cc-02-install-the-cli", "Module 01: Setup & Foundations", "02. Install the CLI"),
    ("cc-03-first-conversation", "Module 01: Setup & Foundations", "03. Your First Conversation"),
    ("cc-04-the-agentic-loop", "Module 01: Setup & Foundations", "04. The Agentic Loop"),
    ("cc-05-claude-md-and-memory", "Module 01: Setup & Foundations", "05. CLAUDE.md and Project Memory"),
    ("cc-06-reading-and-editing", "Module 02: Core Workflows", "06. Reading and Editing Files"),
    ("cc-07-searching-the-codebase", "Module 02: Core Workflows", "07. Searching the Codebase"),
    ("cc-08-running-tests", "Module 02: Core Workflows", "08. Running Tests with Claude"),
    ("cc-09-git-and-commits", "Module 02: Core Workflows", "09. Git Operations and Commits"),
    ("cc-10-multi-file-refactors", "Module 02: Core Workflows", "10. Multi-File Refactors"),
    ("cc-11-debugging", "Module 02: Core Workflows", "11. Debugging with Claude"),
    ("cc-12-slash-commands", "Module 03: Power Features", "12. Slash Commands"),
    ("cc-13-custom-slash-commands", "Module 03: Power Features", "13. Writing Your Own Slash Command"),
    ("cc-28-agent-skills", "Module 03: Power Features", "14. Agent Skills"),
    ("cc-14-subagents", "Module 03: Power Features", "15. Subagents and the Agent Tool"),
    ("cc-15-plan-mode", "Module 03: Power Features", "16. Plan Mode"),
    ("cc-16-hooks", "Module 03: Power Features", "17. Hooks: Pre and Post Tool"),
    ("cc-17-mcp-servers", "Module 03: Power Features", "18. MCP Servers"),
    ("cc-18-spec-tests-code", "Module 04: Vibe Coding Patterns", "19. Spec -> Tests -> Code"),
    ("cc-19-iterative-refinement", "Module 04: Vibe Coding Patterns", "20. Iterative Refinement"),
    ("cc-20-when-to-interrupt", "Module 04: Vibe Coding Patterns", "21. When to Interrupt vs Let It Run"),
    ("cc-21-code-review", "Module 04: Vibe Coding Patterns", "22. Code Review with Claude"),
    ("cc-22-pair-programming-flow", "Module 04: Vibe Coding Patterns", "23. The Pair-Programming Flow"),
    ("cc-23-nextjs-feature", "Module 05: Real Projects", "24. Building a Next.js Feature"),
    ("cc-24-tests-first", "Module 05: Real Projects", "25. Writing Tests-First"),
    ("cc-25-legacy-migration", "Module 05: Real Projects", "26. Migrating Legacy Code"),
    ("cc-26-shipping-to-production", "Module 05: Real Projects", "27. Shipping to Production"),
    ("cc-27-capstone", "Module 05: Real Projects", "28. Capstone: Ship a Side Project"),
]

os.makedirs("lessons_raw", exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

all_data = []

for slug, mod, title in lessons:
    url = f"https://vibecodeschool.com/learn/{slug}"
    cache_path = os.path.join("lessons_raw", f"{slug}.html")
    
    if os.path.exists(cache_path):
        with open(cache_path, "r", encoding="utf-8") as f:
            html = f.read()
    else:
        print(f"Fetching {slug}...")
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as resp:
                html = resp.read().decode("utf-8")
            with open(cache_path, "w", encoding="utf-8") as f:
                f.write(html)
            time.sleep(0.3)
        except Exception as e:
            print(f"Error fetching {slug}: {e}")
            continue

    soup = BeautifulSoup(html, "html.parser")
    
    # Try finding main article or content
    article = soup.find("article") or soup.find("main") or soup.find("div", class_=lambda c: c and "content" in c)
    
    # Also extract interactive sections, code blocks, checklists, exercises
    content_text = ""
    if article:
        content_text = article.get_text(separator="\n", strip=True)
    else:
        content_text = soup.get_text(separator="\n", strip=True)
        
    all_data.append({
        "slug": slug,
        "module": mod,
        "title": title,
        "raw_length": len(html),
        "text_length": len(content_text)
    })

print("Done. Downloaded and parsed summary:")
for item in all_data:
    print(f"- {item['slug']}: {item['text_length']} chars")
