import streamlit as st
import uuid
from apps.notes.app import get_notes, add_note, find_by_author, find_by_tags, find_by_text

################

notes = get_notes()

def create_new_note(author, text, tags):
    add_note({
        "id": str(uuid.uuid4()),
        "author": author,
        "text": text,
        "tags": tags
    })

################

st.title("Доска заметок")

form = st.form(key='my_form')
author = form.text_input(label='Ты кто?')
text = form.text_input(label='Текст сообщения')
tags_text = form.text_input(label='Теги через запятую')
submit_button = form.form_submit_button(label='Запостить')
if submit_button:
    tags = tags_text.split(", ")
    create_new_note(author, text, tags)

################

for note in notes:
    st.text(note["author"])
    st.code(note["text"])
    st.caption(", ".join(note["tags"]))
    st.divider()

st.dataframe(notes)
notes