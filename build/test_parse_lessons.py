from bs4 import BeautifulSoup
import json

def parse_lesson(filepath):
    soup = BeautifulSoup(open(filepath, encoding="utf-8").read(), "html.parser")
    article = soup.find("article", class_="lesson-content")
    if not article:
        return None
    
    # Title & Subtitle
    h1 = article.find("h1")
    title = h1.get_text(strip=True) if h1 else ""
    
    # Subtitle / description
    desc_p = None
    if h1:
        parent = h1.parent
        desc_p = parent.find("p")
    subtitle = desc_p.get_text(strip=True) if desc_p else ""
    
    # Body
    body = article.find("div", class_="lesson-body")
    body_elements = []
    if body:
        for elem in body.find_all(['p', 'h2', 'h3', 'h4', 'pre', 'ul', 'ol', 'blockquote', 'table']):
            # Avoid nested duplicates
            if elem.parent != body and elem.parent.name in ['ul', 'ol', 'blockquote', 'table', 'pre']:
                continue
            tag = elem.name
            if tag == 'pre':
                body_elements.append({"type": "code", "content": elem.get_text(strip=True)})
            elif tag in ['ul', 'ol']:
                items = [li.get_text(strip=True) for li in elem.find_all('li', recursive=False)]
                body_elements.append({"type": "list", "items": items, "ordered": (tag == 'ol')})
            elif tag in ['h2', 'h3', 'h4']:
                body_elements.append({"type": "heading", "level": tag, "content": elem.get_text(strip=True)})
            elif tag == 'blockquote':
                body_elements.append({"type": "quote", "content": elem.get_text(strip=True)})
            elif tag == 'table':
                rows = []
                for tr in elem.find_all('tr'):
                    cells = [td.get_text(strip=True) for td in tr.find_all(['th', 'td'])]
                    rows.append(cells)
                body_elements.append({"type": "table", "rows": rows})
            elif tag == 'p':
                body_elements.append({"type": "p", "content": elem.get_text(strip=True)})
                
    # Terms
    terms = []
    terms_sec = article.find("section", class_="lesson-terms")
    if terms_sec:
        for t in terms_sec.find_all("a", class_="lesson-term"):
            name = t.find(class_="lesson-term-name")
            desc = t.find(class_="lesson-term-short")
            if name and desc:
                terms.append({
                    "name": name.get_text(strip=True),
                    "desc": desc.get_text(strip=True)
                })

    # Quiz
    quizzes = []
    quiz_sec = article.find("div", class_="lesson-quiz")
    if quiz_sec:
        for card in quiz_sec.find_all("div", class_="quiz-card"):
            q_text = card.find("div", class_="quiz-q")
            q_str = q_text.get_text(strip=True) if q_text else ""
            options = []
            for opt in card.find_all("button", class_="quiz-option"):
                letter = opt.find(class_="quiz-option-letter")
                l_str = letter.get_text(strip=True) if letter else ""
                # Get the rest of text
                full_t = opt.get_text(strip=True)
                if l_str and full_t.startswith(l_str):
                    full_t = full_t[len(l_str):].strip()
                options.append(f"{l_str}: {full_t}")
            if q_str:
                quizzes.append({
                    "question": q_str,
                    "options": options
                })
                
    return {
        "title": title,
        "subtitle": subtitle,
        "body_elements": body_elements,
        "terms": terms,
        "quizzes": quizzes
    }

for test_f in ["lessons_raw/cc-01-what-is-claude-code.html", "lessons_raw/cc-02-install-the-cli.html", "lessons_raw/cc-05-claude-md-and-memory.html"]:
    res = parse_lesson(test_f)
    print(f"=== {test_f} ===")
    print("Title:", res['title'])
    print("Subtitle:", res['subtitle'])
    print(f"Elements: {len(res['body_elements'])}")
    for e in res['body_elements'][:3]:
        print("  -", e['type'], ":", str(e.get('content') or e.get('items'))[:80])
    print(f"Terms: {len(res['terms'])}")
    print(f"Quizzes: {len(res['quizzes'])}")
