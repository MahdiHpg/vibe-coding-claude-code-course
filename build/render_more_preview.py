import pymupdf

doc = pymupdf.open("vibe_coding_claude_code_complete.pdf")
for pno in [58, 60, 65, 67]:
    if pno < len(doc):
        page = doc[pno]
        pix = page.get_pixmap(dpi=150)
        pix.save(f"pdf_preview/page_{pno+1:02d}.png")
        print(f"Saved page_{pno+1:02d}.png")
