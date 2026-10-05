import streamlit as st

st.title("AI Web App")

user_input = st.text_input("اپنا سوال:")

if st.button("جواب حاصل کریں"):
    # یہاں اپنا AI ماڈل کا کوڈ شامل کریں
    response = f"آپ نے پوچھا: {user_input} - اس کا جواب یہاں آئے گا۔"
    st.write(response)

