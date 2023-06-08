import streamlit as st
from app.models.auth import login_user

def login_view():
    st.title("Login")
    input_username = st.text_input("Username")
    input_password = st.text_input("Password", type="password")
    
    if st.button("Submit"):
        print(f'Username: {input_username} tried to login')
        login_user(input_username, input_password)