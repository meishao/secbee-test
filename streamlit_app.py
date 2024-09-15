import streamlit as st
from auth import auth

st.title("Home")

supabase = auth()
if supabase is None:
    st.stop()

user = supabase.auth.get_user()
user_name = user.user

st.write(f"Hey {user_name}, welcome to your streamlit app!")


# Sign out
if st.button("Sign out"):
    supabase.auth.sign_out()
    st.success("Signed out successfully")
    st.rerun()
