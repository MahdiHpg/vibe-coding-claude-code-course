from bs4 import BeautifulSoup

soup = BeautifulSoup(open("lessons_raw/cc-02-install-the-cli.html", encoding="utf-8").read(), "html.parser")
article = soup.find("article", class_="lesson-content")

print("All elements with classes in cc-02 article:")
for el in article.find_all(True, recursive=False):
    print(el.name, el.get('class'))
    for sub in el.find_all(True, recursive=False):
        print("  ->", sub.name, sub.get('class'))
