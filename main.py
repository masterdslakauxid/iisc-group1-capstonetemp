import streamlit as st
import numpy as np
import time
import random

st.header("Group1 - Capstone project")
title = st.text_input('Activity', 'Archery')

if st.button('Submit'):
    if len(title) > 0:
        if len(title) < 6:
            st.error("Activity name should be at least 5 charaters")
        else:
            st.write('The  keyword to search is .', title.upper())
    else: 
        st.error("Activity to search is missing")

    

