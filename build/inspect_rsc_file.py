import json
import re

with open("rsc_sample.txt", encoding="utf-8") as f:
    text = f.read()

# Let's find where the JSON data starts
# In Next.js App Router, self.__next_f.push([1, "..."]) contains escaped JSON
# Let's find the unescaped data or parse the push calls
chunks = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', text, re.DOTALL)
print(f"Found {len(chunks)} chunks")

full_data = "".join(chunks).replace('\\"', '"').replace('\\\\', '\\')
with open("rsc_unescaped.txt", "w", encoding="utf-8") as f:
    f.write(full_data)

# Now let's search for "id":"cc-01
m = re.search(r'\{"id":"cc-01[^"]*".*?\}', full_data)
if m:
    print("Found direct lesson object:", m.group(0)[:300])
else:
    # Look for "quiz":
    q_idx = full_data.find('"quiz":[')
    if q_idx != -1:
        print("Found quiz at index:", q_idx)
        print(full_data[q_idx-200:q_idx+600])
