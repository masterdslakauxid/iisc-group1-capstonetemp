import streamlit as st
from pathlib import Path

from pages.scripts.myapp import test_function

a = test_function()

st.write(a, '/pages/scripts/content/')