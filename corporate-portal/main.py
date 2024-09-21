import streamlit as st

pg = st.navigation([
    st.Page("frontend/calculator.py", title="Калькулятор", icon="🧮"),
    st.Page("frontend/notes.py", title="Доска сообщений", icon="📝"),
])
pg.run()