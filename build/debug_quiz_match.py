from bs4 import BeautifulSoup

html = open('lessons_raw/cc-01-what-is-claude-code.html', encoding='utf-8').read()
soup = BeautifulSoup(html, 'html.parser')
s = [s.get_text() for s in soup.find_all('script') if 'correctIndex' in s.get_text()][0]

idx = s.find('correctIndex')
print("idx of correctIndex:", idx)
# Find closest 'quiz' before idx
q_idx = s.rfind('quiz', 0, idx)
print("q_idx:", q_idx)
print("Slice around q_idx:", repr(s[q_idx-10:q_idx+30]))
