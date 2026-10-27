import pymupdf
import os

doc = pymupdf.open("vibe_coding_claude_code_complete.pdf")
print("Total pages in doc:", len(doc))

os.makedirs("pdf_preview", exist_ok=True)

pages_to_render = [0, 1, 2, 4, 15, 30, 48, 55]

for pno in pages_to_render:
    if pno < len(doc):
        page = doc[pno]
        pix = page.get_pixmap(dpi=150)
        out_file = f"pdf_preview/page_{pno+1:02d}.png"
        pix.save(out_file)
        print(f"Saved {out_file} ({pix.width}x{pix.height})")

print("Preview rendering complete!")
