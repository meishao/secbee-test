import streamlit as st
from auth import auth

def logout():
    if st.button("退出"):
        supabase.auth.sign_out()
        st.success("Signed out successfully")
        st.rerun()


def dashboard():
    st.title("Home")
    admin_page = st.Page("app_pages/admin.py", title="用户信息", icon=":material/dashboard:", default=True)
    logout_page = st.Page(logout, title="退出登录", icon=":material/logout:")
    pg = st.navigation(
        {
            "账号管理": [admin_page, logout_page],
        }
    )
    pg.run()

    st.write(f"Hey {user_name}, welcome to your streamlit app!")


supabase = auth()
if supabase is None:
    st.stop()

user = supabase.auth.get_user()
user_name = user.user.email
dashboard()
