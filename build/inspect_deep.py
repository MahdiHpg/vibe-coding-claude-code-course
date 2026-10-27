from bs4 import BeautifulSoup
import glob
import json

files = sorted(glob.glob("lessons_raw/cc-*.html"))

sample = files[0]
soup = BeautifulSoup(open(sample, encoding="utf-8").read(), "html.parser")

article = soup.find("article", class_="lesson-content")

# Let's inspect all classes and tags inside article
print("Sample:", sample)
for section in article.find_all("section"):
    classes = section.get("class", [])
    print("Section:", classes)
    h = section.find(['h2', 'h3', 'h4', 'div'])
    if h:
        print("   Header:", h.get_text(strip=True)[:100])

body = article.find("div", class_="lesson-body")
if body:
    print("\n--- Lesson Body Elements ---")
    for el in body.children:
        if el.name:
            print(f"<{el.name}>: {el.get_text(strip=True)[:80]}")

terms = article.find("section", class_="lesson-terms")
if terms:
    print("\n--- Terms ---")
    for t in terms.find_all("div", class_="lesson-term"):
        term_name = t.find(class_=lambda c: c and "name" in c or "title" in c) or t.find("dt") or t.find("strong")
        print("Term:", t.get_text(strip=True)[:80])

quiz = article.find("section", class_="lesson-quiz")
if quiz:
    print("\n--- Quiz ---")
    print(quiz.get_text(separator="\n", strip=True)[:300])
