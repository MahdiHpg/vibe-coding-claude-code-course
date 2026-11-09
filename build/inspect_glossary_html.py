from bs4 import BeautifulSoup

soup = BeautifulSoup(open("lessons_raw/glossary.html", encoding="utf-8").read(), "html.parser")
print(soup.prettify()[:1500])
