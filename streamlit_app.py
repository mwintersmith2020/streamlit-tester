__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

import sys
st.write(f"Python version: {sys.version}")

import sqlite3
st.write(f"SQLite version: {sqlite3.sqlite_version}")


