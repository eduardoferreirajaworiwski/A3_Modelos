import streamlit as st

def home_view():
    if st.session_state.logged_in:
        st.write("You are logged in!")
        st.write("You can now access the app.")

    else:
        st.write("You are not logged in!")
        st.write("Please log in to access the app.")
