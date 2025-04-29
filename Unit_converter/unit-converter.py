import streamlit as st

st.title("Unit Converter App")

category = st.selectbox("Select Category", ["Distance", "Temperature", "Weight", "Pressure"])

if category == "Distance":
    st.selectbox("From", ["Meter", "Kilometer", "Feet", "Miles", ])
    st.selectbox("To", ["Meter", "Kilometer", "Feet", "Miles", ])
    st.number_input("Enter Value")
    if st.button("Convert"):
        st.success("Good")