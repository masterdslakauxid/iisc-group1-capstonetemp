import streamlit as st
from pathlib import Path

def test_function():
    st.write("I'm declared in a different package but succesffuly inovked by this")
    st.write(Path.cwd())
    return Path.cwd()