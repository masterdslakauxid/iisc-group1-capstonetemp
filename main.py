import streamlit as st
import numpy as np
import time
import random

st.header("Group1 - Capstone project")
title = st.text_input('Activity', 'Archery')
if st.button('Submit'):
    st.write('The  keyword to search is .', title.upper())

