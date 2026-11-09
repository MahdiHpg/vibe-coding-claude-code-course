import base64
import os

for f in ["Vazirmatn-Regular.woff2", "Vazirmatn-Bold.woff2", "Vazirmatn-SemiBold.woff2"]:
    path = os.path.join("fonts", f)
    size = os.path.getsize(path)
    b64_len = len(base64.b64encode(open(path, "rb").read()))
    print(f"{f}: {size} bytes -> {b64_len} chars base64")
