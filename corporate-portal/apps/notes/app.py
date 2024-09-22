from dataclasses import dataclass

@dataclass
class Note:
    id: str
    author: str
    text: str
    tags: list[str]

_notes: list[Note] = []

# def get_notes() -> list[Note]:
#     return _notes
get_notes = lambda: _notes

def add_note(note: Note):
    _notes.append(note)

find_by_author = lambda author: list(filter(lambda note: note["author"] == author, _notes))
find_by_tags = lambda tag: list(filter(lambda note: tag in note["tags"], _notes))
find_by_text = lambda text: list(filter(lambda note: text in note["text"], _notes))