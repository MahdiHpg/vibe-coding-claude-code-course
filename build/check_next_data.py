from bs4 import BeautifulSoup
import json

soup = BeautifulSoup(open("lessons_raw/cc-01-what-is-claude-code.html", encoding="utf-8").read(), "html.parser")
next_data = soup.find("script", id="__NEXT_DATA__")
if next_data:
    data = json.loads(next_data.string)
    print("Found __NEXT_DATA__! Keys:", list(data.keys()))
    print("Page props keys:", list(data.get("props", {}).get("pageProps", {}).keys()))
    pageProps = data.get("props", {}).get("pageProps", {})
    with open("sample_page_props.json", "w", encoding="utf-8") as f:
        json.dump(pageProps, f, indent=2, ensure_ascii=False)
    print("Saved sample_page_props.json")
else:
    print("No __NEXT_DATA__ found")
