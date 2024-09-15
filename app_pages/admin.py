import streamlit as st
from auth import auth

st.title("Home")

supabase = auth()
if supabase is None:
    st.warning("NO!")
    st.stop()

st.write("GOOD!")
