from bs4 import BeautifulSoup

soup = BeautifulSoup(open("lessons_raw/cc-01-what-is-claude-code.html", encoding="utf-8").read(), "html.parser")
article = soup.find("article", class_="lesson-content")

for child in article.children:
    if child.name:
        print(f"[{child.name}.{child.get('class')}] -> {child.get_text(separator=' ', strip=True)[:150]}")
