import streamlit as st

st.title("AI Web App")

user_input = st.text_input("آپ کا سوال:")

if user_input:
    # یہاں آپ کا AI ماڈل کا لاجک آئے گا
    response = f"آپ نے پوچھا: {user_input}"
    st.write(response)
