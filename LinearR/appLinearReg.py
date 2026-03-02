import streamlit as st 
import pickle 

with open("lr.pkl","rb") as f:
    model=pickle.load(f)

st.title("house prediction")
st.info(" with sqreft,bedrooms,age etc.. factors ")  

with st.form("preductionForm"): # single feature Linear regression
    square_feet=st.number_input("sqrtfeet",min_value=300,max_value=3000,step=100)
    btn=st.form_submit_button("predictPrice")

    if btn:
        predictionPriceValue=model.predict([[square_feet]])
        st.success(f"predected price ${predictionPriceValue}")