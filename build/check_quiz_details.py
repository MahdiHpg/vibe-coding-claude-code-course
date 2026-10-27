from bs4 import BeautifulSoup
import glob

soup = BeautifulSoup(open("lessons_raw/cc-01-what-is-claude-code.html", encoding="utf-8").read(), "html.parser")
quiz_cards = soup.find_all("div", class_="quiz-card")
for card in quiz_cards:
    print("--- CARD ---")
    print(card.prettify()[:600])
