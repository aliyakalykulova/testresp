import streamlit as st
import requests

API_URL = "http://localhost:8000"  # потом поменяем при деплое

breed = st.selectbox("Выбери породу", ["husky", "labrador"])

if st.button("Показать вес"):
    response = requests.post(
        f"{API_URL}/get-weight",
        json={"breed": breed}
    )
    data = response.json()
    st.write("Вес:", data["weight"])
