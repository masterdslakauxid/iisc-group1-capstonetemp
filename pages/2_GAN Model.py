import streamlit as st


st.header("GAN Model")

user_input1 = st.text_input("Enter the batch size", help="The recommended size is 1 or 2 for testing", placeholder="1")
user_input2 = st.text_input("Enter the no. of epochs", help="The recommended size is 1 or 2 for testing", placeholder="1" )

valid_inputs = True

if st.button('Generate Video'):
    if len(user_input1) > 0: 
        batch_size = int(user_input1)
        if batch_size == 0 or  batch_size > 2:
            valid_inputs = False
            st.error("The recommended batch size is 1-2 only")
    else:
        valid_inputs = False
        st.error("Enter the batch size")

    if len(user_input2) > 0: 
        num_epochs = int(user_input2)
        if num_epochs == 0 or num_epochs > 2:
            valid_inputs = False
            st.error("The recommended epoch size is 1-2 only")
    else:
        valid_inputs = False
        st.error("Enter the epoch size")

    if valid_inputs == True:
        st.write("Video link")
