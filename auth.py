from time import sleep
import streamlit as st
import streamlit as st
from supabase import create_client, Client


def init_connection():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

AUTH_OPERATIONS = {
    "Login": "sign_in_with_password",
    "Sign up": "sign_up",
}

supabase = init_connection()   

def auth():
    if supabase.auth.get_user():
        return supabase

    placeholder1, form_col, placeholder2 = st.columns([.2, .6, .2])
    with form_col:
        st.title("🔐 Login or Signup")
        selected_auth_operation = st.radio(
            label="Select operation",
            options=AUTH_OPERATIONS.keys(),
            horizontal=True,
            label_visibility="hidden"
        )
        auth_operation = AUTH_OPERATIONS[selected_auth_operation]



        with st.form("auth_form"):
            email = st.text_input(
                label="Enter your email",
                placeholder="john@example.com",
                )
            password = st.text_input(
                label="Enter your password",
                placeholder="Min 6 characters",
                type="password",
                help="Password is encrypted",
            )
            # Login
            if auth_operation == "sign_in_with_password":

                constructed_auth_query = f"supabase.auth.{auth_operation}(dict({email=}, {password=}))"

            # Signup
            elif auth_operation == "sign_up":
                name = st.text_input(
                    label="Name",
                    placeholder="John Doe",
                )

                constructed_auth_query = f"supabase.auth.{auth_operation}(dict({email=}, {password=}, options=dict(data=dict({name=}))))"


            if st.form_submit_button(
                "Submit",
                type="primary",
                use_container_width=True,
                disabled=not constructed_auth_query,
                ):
                with st.spinner("Authenticating..."):
                    if auth_operation == "sign_up":
                        if len(password) < 6:
                            st.error("Password must be at least 6 characters")
                            return
                        if len(name) < 1:
                            st.error("Name must be at least 1 character")
                            return
                    try:
                        exec(constructed_auth_query)
                        supabase.auth.get_user()
                        st.success("Authentication successful")
                        # Wait until the success message is finished
                        sleep(.5)
                        st.rerun()
                        return supabase
                    except Exception as e:
                        st.error(f"Authentication failed: {e}")
                        return
