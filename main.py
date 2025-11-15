import json
from pathlib import Path

# ==== TODO: điền dữ liệu sách tại đây ====
book_name = "Clean Code"
chapters = [
    "Chapter 1",
    "Chapter 2",
]

sections = [
    {"chapter": "Chapter 1", "title": "Section 1.1"},
    {"chapter": "Chapter 1", "title": "Section 1.2"},
    {"chapter": "Chapter 2", "title": "Section 2.1"},
    {"chapter": None, "title": "Book-level section"},
]

notes = [
    {"chapter": None, "section": None, "content": "Book level note"},
    {"chapter": "Chapter 1", "section": "Section 1.1", "content": "Nội dung section 1.1"},
    {"chapter": None, "section": "Book-level section", "content": "Note cho section trực tiếp"},
]

output_file = Path("cleancode.txt")
# =========================================

payload = {
    "name": book_name,
    "chapters": chapters,
    "sections": sections,
    "notes": notes,
}

with output_file.open("w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)

print(f"Saved JSON to {output_file.resolve()}")
