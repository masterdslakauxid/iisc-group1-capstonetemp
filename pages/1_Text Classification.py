import streamlit as st

from pages.scripts.app import predict_resume_with_rf, predict_resume_with_xgb, predict_resume_with_lgb 

st.header("Text Classification")

user_input = st.text_input("Enter the Activity", help="Archery, Play Basket ball", placeholder="A person playing Archery" )

col1, col2, col3 = st.columns([3,3,3])
classified_label = ""

with col1:
    st.header("RandomForest", divider='orange')
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
    st.header("XGBoost", divider='orange')
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
    st.header("MS LGBM", divider='orange')
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





