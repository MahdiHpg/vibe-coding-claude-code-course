import os

pdf_path = "vibe_coding_claude_code_complete.pdf"
size = os.path.getsize(pdf_path)
print(f"PDF size: {size} bytes ({size/1024/1024:.2f} MB)")

# Let's count pages by scanning for /Type /Page
with open(pdf_path, "rb") as f:
    content = f.read()
    page_count = content.count(b"/Type /Page") - content.count(b"/Type /Pages")
    print(f"Estimated page count: {page_count}")
