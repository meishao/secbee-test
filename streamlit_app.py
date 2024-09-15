import streamlit as st
from auth import auth

def logout():
    if st.button("退出"):
        supabase.auth.sign_out()
        st.success("Signed out successfully")
        st.rerun()

def dashboard():
    logout_page = st.Page(logout, title="退出登录", icon=":material/logout:")
    pg = st.navigation(
        {
            "账号": [logout_page],
        }
    )
    pg.run()


st.title("Home")

supabase = auth()
if supabase is None:
    st.stop()

user = supabase.auth.get_user()
user_name = user.user.email

st.write(f"Hey {user_name}, welcome to your streamlit app!")
dashboard()
