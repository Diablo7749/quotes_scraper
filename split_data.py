import json

with open("quotes.json", encoding="utf-8") as f:
    data = json.load(f)

quotes = []
authors = []

seen = set()
for item in data:
    if "quote" in item and "tags" in item:
        quotes.append(item)
    elif "fullname" in item:
        if item["fullname"] not in seen:
            authors.append(item)
            seen.add(item["fullname"])

# збережи правильно
with open("quotes_cleaned.json", "w", encoding="utf-8") as f:
    json.dump(quotes, f, ensure_ascii=False, indent=2)

with open("authors_cleaned.json", "w", encoding="utf-8") as f:
    json.dump(authors, f, ensure_ascii=False, indent=2)
