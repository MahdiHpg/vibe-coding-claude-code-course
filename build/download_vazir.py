import urllib.request
import os

os.makedirs("fonts", exist_ok=True)

# Let's download Vazirmatn fonts from github releases or jsdelivr
urls = {
    "Vazirmatn-Regular.woff2": "https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/fonts/webfonts/Vazirmatn-Regular.woff2",
    "Vazirmatn-Bold.woff2": "https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/fonts/webfonts/Vazirmatn-Bold.woff2",
    "Vazirmatn-SemiBold.woff2": "https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/fonts/webfonts/Vazirmatn-SemiBold.woff2",
    "Vazirmatn-Medium.woff2": "https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/fonts/webfonts/Vazirmatn-Medium.woff2",
    "Vazirmatn-Regular.ttf": "https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/fonts/ttf/Vazirmatn-Regular.ttf",
    "Vazirmatn-Bold.ttf": "https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/fonts/ttf/Vazirmatn-Bold.ttf",
}

for name, url in urls.items():
    dest = os.path.join("fonts", name)
    if not os.path.exists(dest):
        try:
            print(f"Downloading {name}...")
            urllib.request.urlretrieve(url, dest)
            print(f"Saved {dest} ({os.path.getsize(dest)} bytes)")
        except Exception as e:
            print(f"Error {name}: {e}")
