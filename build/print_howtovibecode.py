from bs4 import BeautifulSoup

soup = BeautifulSoup(open("lessons_raw/how-to-vibe-code.html", encoding="utf-8").read(), "html.parser")
print("Title:", soup.title.get_text() if soup.title else "")

for h in soup.find_all(['h1', 'h2', 'h3']):
    print(f"[{h.name}] {h.get_text(strip=True)}")
