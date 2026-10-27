from bs4 import BeautifulSoup

soup = BeautifulSoup(open("lessons_raw/cc-01-what-is-claude-code.html", encoding="utf-8").read(), "html.parser")
article = soup.find("article", class_="lesson-content")

for tag in article.find_all(['h1', 'h2', 'h3', 'p', 'div', 'section']):
    classes = tag.get('class', [])
    text = tag.get_text(separator=" ", strip=True)
    if any(c in classes for c in ['lesson-body', 'lesson-summary', 'lesson-section', 'quiz-card', 'lesson-term']):
        print(f"[{tag.name}.{classes}] -> {text[:100]}...")
