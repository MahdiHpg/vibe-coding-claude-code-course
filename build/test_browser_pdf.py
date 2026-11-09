import subprocess
import os

brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

html_path = os.path.abspath("test.html")
pdf_path = os.path.abspath("test.pdf")

for browser in [brave_path, chrome_path]:
    if not os.path.exists(browser):
        continue
    print("Testing browser:", browser)
    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        f"--print-to-pdf={pdf_path}",
        "--no-pdf-header-footer",
        html_path
    ]
    p = subprocess.run(cmd, capture_output=True, text=True)
    print("Return code:", p.returncode)
    print("Stdout:", p.stdout)
    print("Stderr:", p.stderr)
    if os.path.exists(pdf_path):
        print(f"SUCCESS! {pdf_path} created, size: {os.path.getsize(pdf_path)} bytes")
        break
    else:
        print("Failed to create PDF.")
