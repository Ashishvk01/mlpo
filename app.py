import streamlit as st

# ML Pkg

import joblib

def main():
    """Password Strength Classifier"""

    st.title("Password Strength Classifier ML App")

    st.subheader("With Streamlit")

    activities = ["Classify Password", "Generate Password", "About"] 
    choice = st.sidebar.selectbox("Select Activity", activities)

    if choice== "Classify Password":

     st.subheader("Classifying Password with ML")

    elif choice == "Generate Password":

     st.subheader("Generate Random Password")
     
    elif choice == 'About':

        st.subheader("About App")



    