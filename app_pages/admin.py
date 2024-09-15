import streamlit as st
from auth import auth

supabase = auth()
if supabase is None:
    st.write("NO!")
    st.stop()

st.write("GOOD!")
