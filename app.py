import streamlit as st
import google.generativeai as genai

st.title("AI Web App")

api_key = st.text_input("Gemini API Key Ask your question", type="password")
user_input = st.text_input("اپنا سوال:")

if st.button("Get Answer"):
    if api_key and user_input:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(user_input)
            st.write(response.text)
        except Exception as e:
            st.error(f"ایرر: {e}")
    else:
        st.warning("براہ کرم API کی اور سوال درج کریں۔")
