import streamlit as st
from .db_connector import load_db


def login_user(username, password):
    db = load_db()
    
    user = db.users.find_one({"username": username, "password": password})
    
    if user:
        st.success(f'Logged in as {username}')
        st.session_state['user'] = user
        st.experimental_rerun()

    else:
        st.error('Incorrect username/password')
        st.session_state['user'] = None
        st.experimental_rerun()