from bs4 import BeautifulSoup
import json

soup = BeautifulSoup(open("lessons_raw/cheat-sheet.html", encoding="utf-8").read(), "html.parser")

cheat_sections = []
for sec in soup.find_all("section"):
    h2 = sec.find("h2")
    if not h2:
        continue
    title = h2.get_text(strip=True)
    body_items = []
    for el in sec.find_all(['p', 'pre', 'table', 'ul', 'ol', 'div'], recursive=False):
        t = el.get_text(separator=" ", strip=True)
        if t and t != title:
            body_items.append(t)
    # also check nested callouts, cards, grids
    cards = []
    for card in sec.find_all(class_=lambda c: c and ('card' in c or 'item' in c or 'row' in c or 'entry' in c)):
        ct = card.get_text(separator=" ", strip=True)
        if ct:
            cards.append(ct)
    cheat_sections.append({
        "title": title,
        "text_sample": "\n".join(body_items[:5]),
        "cards_count": len(cards),
        "cards_sample": cards[:3]
    })

print(f"Parsed {len(cheat_sections)} cheat sheet sections:")
for cs in cheat_sections:
    print(f"- {cs['title']} (cards: {cs['cards_count']})")
    if cs['cards_sample']:
        print(f"    sample: {cs['cards_sample'][0][:80]}")
