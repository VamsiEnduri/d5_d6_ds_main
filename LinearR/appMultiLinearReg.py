import streamlit as st 
import pickle 

with open("lr2.pkl","rb") as f:
    model=pickle.load(f)

st.title("house prediction")
st.info(" with sqreft,bedrooms,age etc.. factors ")  

with st.form("preductionForm"): # single feature Linear regression
    square_feet=st.number_input("sqrtfeet",min_value=300,max_value=3000,step=100)
    bedroom=st.number_input("bedroom",min_value=1,max_value=5,step=1)
    age=st.number_input("age",min_value=1,max_value=15,step=1)
    l_score=st.number_input("locationScore",min_value=1,max_value=10,step=1)
    btn=st.form_submit_button("predictPrice")

    if btn:
        predictionPriceValue=model.predict([[square_feet,bedroom,age,l_score]])
        st.success(f"predected price ${predictionPriceValue}")