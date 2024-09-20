import streamlit as st

pg = st.navigation([
    st.Page("my.py", title="Раз два три", icon="🔥"),
    st.Page("your_app.py", title="Раз два триdfdf", icon="🔥"),
])
pg.run()