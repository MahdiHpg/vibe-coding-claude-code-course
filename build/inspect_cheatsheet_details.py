from bs4 import BeautifulSoup

soup = BeautifulSoup(open("lessons_raw/cheat-sheet.html", encoding="utf-8").read(), "html.parser")

for h2 in soup.find_all("h2"):
    title = h2.get_text(strip=True)
    if any(k in title for k in ["Cost", "Best", "FAQ", "Worktrees", "Modes"]):
        print(f"\n--- H2: {title} ---")
        curr = h2.next_sibling
        while curr and curr.name != 'h2':
            if curr.name:
                txt = curr.get_text(strip=True)
                if txt:
                    print(f"[{curr.name}]: {txt[:120]}...")
            curr = curr.next_sibling
