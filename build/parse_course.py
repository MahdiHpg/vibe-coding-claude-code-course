import sys
from bs4 import BeautifulSoup
import json

with open('page_dump.html', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("Title:", soup.title.get_text() if soup.title else "")

# Print all headings
for h in soup.find_all(['h1', 'h2', 'h3', 'h4']):
    print(f"[{h.name}] {h.get_text(strip=True)}")

# Find all links
print("\n--- ALL LINKS ---")
for a in soup.find_all('a', href=True):
    href = a['href']
    txt = a.get_text(strip=True)
    if txt or 'course' in href or 'lesson' in href:
        print(f"{txt} -> {href}")
