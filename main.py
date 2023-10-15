import streamlit as st
import numpy as np
import time
import random
#import enchant
#from itertools import chain, cycle

st.header("Group1 - Capstone project")
title = st.text_input('Activity', '')

if st.button('Submit'):
    if len(title) > 0:
        st.write(" The entered activity is ", title.upper())
    else:
        st.error('Enter a valid activity name .')            



# dict = enchant.Dict("en_US")

# if st.button('Submit'):
#     if len(title) > 0:
#         #if len(title) < 6:
#         #x = title.replace(" ","* *")
#         words = list(chain(*zip(title.split(), cycle(' '))))[:-1]
#         #words = x.split("*")
#       #  st.write(words)

#         valid_title = True

#         for word in words:
#           #  st.write (word.strip() , len(word.strip()))
#             if len(word.strip()) != 0:
#                 if dict.check(word) == False:
#                     valid_title = False
#                     break
                    
#                     #print("The misspelled words are : " + str(misspelled))

#         if valid_title == True:
#             st.write('The activity to search is .'+ title.upper())            
#         else:
#             st.error('Enter a valid activity name .')            

#         # if dict.check(title) == False:
#         #     st.error("Enter a valid activity name")
#         # else:
#         #     st.write('The activity to search is .', title.upper())
#     else: 
#         st.error("Activity to search is missing")

    

