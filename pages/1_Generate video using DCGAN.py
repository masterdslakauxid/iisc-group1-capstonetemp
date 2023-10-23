import streamlit as st

from pages.scripts.app import predict_resume_with_rf, predict_resume_with_xgb, predict_resume_with_lgb 
from pages.scripts.content.util import get_classified_lable_file_path
from pages.scripts.app2 import generate_video

st.header("Generate video using DCGAN")
st.subheader("Executing Text Classification")

user_input = st.text_input("#1 Enter the Activity description", help="A man playing archery in front of the garage in the morning", placeholder="A person playing Archery or A person playing football" )


st.write("#2 Employ the model for classification.")

with st.container():
    model = st.radio(
    "select the model",
    ["RandomForest", "XGBoost", "Microsoft LGBM"],
    index=None,horizontal=True
    )
  

with st.container():
    button_clicked = False
    invalid_user_input = False
    model_selected = True
    classified_label = ""
    left_column, right_column = st.columns((1,2)) 
    with left_column:
        if st.button('Classify'):
            button_clicked = True
            if len(user_input) > 0: 
                if model == "RandomForest":
                    pred_action_label_rf = predict_resume_with_rf(user_input)
                    classified_label = pred_action_label_rf[0]
                elif model == "XGBoost":    
                    # Predicting the unknown action label
                    pred_action_label_xgb = predict_resume_with_xgb(user_input)
                    classified_label = pred_action_label_xgb[0]
                elif model == "Microsoft LGBM":  
                    # Predicting the unknown action label
                    pred_action_label_lgb = predict_resume_with_lgb(user_input)
                    classified_label = pred_action_label_lgb[0]
                else:
                    model_selected = False
            else:
                invalid_user_input = True
    
    with right_column:
        if button_clicked == True:
            if invalid_user_input == True:
                st.error("Enter the activity")
            elif model_selected == False:
                st.error("Select the model")
            elif len(classified_label) > 0: 
                #st.success("Result : "+ classified_label)
                st.markdown(f'Result <font style="color:#33ff33;font-size:15px;">{classified_label}</font>', unsafe_allow_html=True)
            else:
                st.warning("No matching action generated")

st.divider()                
with st.container():           
    st.subheader("Executing the GAN Model")
    st.write("#3 Generate the video")
    #New............................AK    
    with open(get_classified_lable_file_path(), 'r') as f:
        classified_label = f.read()
    st.write("The classified label for generating the video: ", classified_label)
    st.markdown(f'The classified text for generating the video: <font style="color:#33ff33;font-size:15px;">{classified_label}</font>', unsafe_allow_html=True)

    with st.expander("Advanced options"):    
        custom_customized_label = st.text_input("Enter the activity", help="Name of the activity", placeholder="Enter the exact action class")
    if st.button('Generate Video'):
        if len(custom_customized_label) > 0:
            generate_video(custom_customized_label)
        else:
            generate_video(classified_label)
            


