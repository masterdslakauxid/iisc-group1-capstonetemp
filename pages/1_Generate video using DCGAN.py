import streamlit as st

from pages.scripts.app import predict_resume_with_rf, predict_resume_with_xgb, predict_resume_with_lgb 
from pages.scripts.content.util import get_classified_lable_file_path
from pages.scripts.app2 import generate_video

st.header("Generate video using DCGAN")
st.subheader("Text Classification")

user_input = st.text_input("Enter the Activity", help="Archery, Play Basket ball", placeholder="A person playing Archery" )

col1, col2, col3 = st.columns([3,3,3])
classified_label = ""

with col1:
    st.subheader("RandomForest", divider='orange')
    if st.button('classify with RandomForest'):
        if len(user_input) == 0: 
            st.error("Enter the activity")
        else: 
            # Predicting the unknown action label
            pred_action_label_rf = predict_resume_with_rf(user_input)
            classified_label = pred_action_label_rf[0]
            if len(classified_label) > 0: 
                st.success("Result "+ pred_action_label_rf[0])
            else:
                st.warning("No matching action generated")
with col2:
    st.subheader("XGBoost", divider='orange')
    if st.button('classify with XGBoost'):
        if len(user_input) == 0: 
            st.error("Enter the activity")
        else: 
           # Predicting the unknown action label
           pred_action_label_xgb = predict_resume_with_xgb(user_input)
           classified_label = pred_action_label_xgb[0]
           if len(classified_label) > 0: 
                st.success("Result "+ pred_action_label_xgb[0])
           else:
                st.warning("No matching action generated")
with col3:
    st.subheader("Microsoft LGBM", divider='orange')
    if st.button('classify with Microsoft LGBM'):
        if len(user_input) == 0: 
            st.error("Enter the activity")
        else: 
            # Predicting the unknown action label
            pred_action_label_lgb = predict_resume_with_lgb(user_input)
            classified_label = pred_action_label_lgb[0]
            if len(classified_label) > 0: 
                st.success("Result "+ pred_action_label_lgb[0])
            else:
                st.warning("No matching action generated")
st.divider()                
st.header("Test the GAN Model")
#New............................AK    
with open(get_classified_lable_file_path(), 'r') as f:
    classified_label = f.read()
st.write("The classified label:", classified_label)

custom_customized_label = st.text_input("Enter the activity", help="Name of the activity", placeholder="Enter the exact action class")
if st.button('Generate Video'):
    if len(custom_customized_label) > 0:
        generate_video(custom_customized_label);
    else:
        generate_video(classified_label);


