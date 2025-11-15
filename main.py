#!/usr/bin/env python3
import json
from pathlib import Path

# ===== Điền nội dung sách tại đây =====
book_name = "Clean Code"
book_note = "Ghi chú chung cho toàn bộ cuốn sách."

book_sections = [
    {"title": "Lời nói đầu", "note": "Giới thiệu sơ lược về cuốn sách."},
    {"title": "Checklist tổng quan", "note": "Các nguyên tắc quan trọng cần nhớ."},
]

chapters = [
    {
        "title": "Chương 1 - Nguyên tắc cơ bản",
        "sections": [
            {"title": "1.1 Ý nghĩa Clean Code", "note": "Giải thích tầm quan trọng của code sạch."},
            {"title": "1.2 Code Smell phổ biến", "note": "Liệt kê các smell thường gặp."},
            {"title": "1.3 Quy tắc đặt tên", "note": "Các ví dụ đặt tên tốt/xấu."},
        ],
    },
    {
        "title": "Chương 2 - Refactoring",
        "sections": [
            {"title": "2.1 Kỹ thuật Extract Method", "note": "Khi nào nên tách hàm, ví dụ minh hoạ."},
            {"title": "2.2 Tái cấu trúc lớp", "note": "Tái cấu trúc nhiều lớp phối hợp với nhau."},
        ],
    },
    {
        "title": "Chương 3 - Testing",
        "sections": [
            {"title": "3.1 Unit Test hiệu quả", "note": "Nguyên tắc AAA, ví dụ."},
            {"title": "3.2 Integration Test", "note": "Kịch bản test dữ liệu thực tế."},
            {"title": "3.3 Mock vs Stub", "note": "Phân biệt và khi nào dùng mỗi loại."},
            {"title": "3.4 Coverage và chất lượng", "note": "Hiểu đúng về 100% coverage."},
        ],
    },
]

output_file = Path("cleancode.txt")
# =======================================

payload = {
    "name": book_name,
    "bookNote": book_note,
    "bookSections": book_sections,
    "chapters": chapters,
}

with output_file.open("w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)

print(f"Saved JSON to {output_file.resolve()}")
