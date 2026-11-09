from bs4 import BeautifulSoup

for f in ["cc-03-first-conversation", "cc-04-the-agentic-loop", "cc-05-claude-md-and-memory", "cc-12-slash-commands"]:
    soup = BeautifulSoup(open(f"lessons_raw/{f}.html", encoding="utf-8").read(), "html.parser")
    article = soup.find("article", class_="lesson-content")
    print(f"\n=================== {f} ===================")
    print("TEXT:")
    print(article.get_text(separator="\n", strip=True))
