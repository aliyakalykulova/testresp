import streamlit as st
import requests

breed = st.selectbox("Выбери породу", ["husky", "labrador"])

if st.button("Показать вес"):
    response = requests.post(
        "http://localhost:8000/get-weight",
        json={"breed": breed}
    )
    data = response.json()
    st.write("Вес:", data["weight"])
