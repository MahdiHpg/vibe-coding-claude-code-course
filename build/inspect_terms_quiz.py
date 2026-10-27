from bs4 import BeautifulSoup

soup = BeautifulSoup(open("lessons_raw/cc-01-what-is-claude-code.html", encoding="utf-8").read(), "html.parser")
terms_sec = soup.find("section", class_="lesson-terms")
if terms_sec:
    print(terms_sec.prettify()[:1000])

print("\n--- QUIZ ---")
quiz_sec = soup.find("div", class_="lesson-quiz") or soup.find(lambda t: t.has_attr('class') and any('quiz' in c for c in t['class']))
if quiz_sec:
    print(quiz_sec.prettify()[:1000])
