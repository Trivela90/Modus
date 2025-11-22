import streamlit as st

st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")

st.markdown("<h2 style='text-align:center;'>Modus</h2>", unsafe_allow_html=True)

with st.container():
    _, container_center, _ = st.columns([0.34,0.46,0.2])
    with container_center: 
        st.image("static/modus.png", width=200)

# Center the box
_, center, _ = st.columns([0.1, 0.9, 0.1])

with center:
    # Box with border (Streamlit >= 1.32)
    with st.container(border=True):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        login_btn = st.button("Login")

        if login_btn:
            # 🔑 Dummy check – replace with real auth
            if username == "admin" and password == "1234":
                st.session_state.logged_in = True
                st.success("Logged in successfully!")
            else:
                st.error("Invalid username or password.")

# Example: show app content if logged in
if st.session_state.logged_in:
    st.write("---")
    st.success("🎉 You can now see the protected content!")
    st.write("Put your app here...")
