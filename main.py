#!/usr/bin/env python3
import json
from pathlib import Path

# ==== TODO: điền dữ liệu sách tại đây ====
book_name = "Clean Code"
book_note = "Ghi chú cấp book (có thể bỏ trống)."

book_sections = [
    {
        "title": "Section trực tiếp dưới book",
        "note": "Nội dung section này."
    },
    # thêm section khác nếu cần
]

chapters = [
    {
        "title": "Chapter 1",
        "sections": [
            {"title": "Section 1.1", "note": "Nội dung 1.1"},
            {"title": "Section 1.2", "note": "Nội dung 1.2"},
        ],
    },
    {
        "title": "Chapter 2",
        "sections": [
            {"title": "Section 2.1", "note": ""},
        ],
    },
    # thêm chapter khác nếu cần
]

output_file = Path("cleancode.txt")
# =========================================

payload = {
    "name": book_name,
    "bookNote": book_note,
    "bookSections": book_sections,
    "chapters": chapters,
}

with output_file.open("w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)

print(f"Saved JSON to {output_file.resolve()}")
