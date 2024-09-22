from app import get_notes, add_note, find_by_author, find_by_tags, find_by_text

add_note({
    "id": "1",
    "author": "papen",
    "text": "afa dfasf safdsd f",
    "tags": ["write", "main"]
})

assert get_notes() == [{
    "id": "1",
    "author": "papen",
    "text": "afa dfasf safdsd f",
    "tags": ["write", "main"]
}]

# print(find_by_author("papen"))
# print(find_by_tags("main"))
# print(find_by_text("sf"))