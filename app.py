import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="Our Calculator", page_icon="🧮", layout="centered")

# CSS للتوسيط وتكبير الحجم
st.markdown("""
    <style>
    .block-container {
        max-width: 700px;
        margin: auto;
        padding-top: 50px;
    }
    h2 {
        text-align: center;
        font-size: 32px !important;
    }
    .stTextInput>div>div>input {
        text-align: center;
        font-size: 20px !important;
        height: 50px !important;
    }
    .stButton>button {
        display: block;
        margin: auto;
        font-size: 20px !important;
        height: 60px !important;
        width: 60%;
    }
    </style>
    """, unsafe_allow_html=True)

# الحالة العامة
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "login"
if "material" not in st.session_state:
    st.session_state.material = None
if "calculation" not in st.session_state:
    st.session_state.calculation = None
if "history" not in st.session_state:
    st.session_state.history = []

# سايد منيو يظهر فقط بعد تسجيل الدخول
if st.session_state.logged_in:
    with st.sidebar:
        st.title("📌 Menu")
        if st.button("🏠 Home"):
            st.session_state.page = "select"
        if st.button("📊 Reports"):
            st.write("Reports section (Admin only)")
        if st.button("🎨 Design"):
            st.write("Design settings")
        if st.button("📞 Support"):
            st.write("Call: 07725406386")
        if st.button("🚪 Logout"):
            st.session_state.logged_in = False
            st.session_state.page = "login"
            st.experimental_rerun()

# تسجيل الدخول
if st.session_state.page == "login":
    st.markdown("<h2>🔐 Login</h2>", unsafe_allow_html=True)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # الضغط على Enter أو زر Login
    if st.button("Login") or (username == "user" and password == "123"):
        if username == "user" and password == "123":
            st.session_state.logged_in = True
            st.session_state.page = "select"
            st.experimental_rerun()
        elif username and password:
            st.error("❌ Invalid credentials")

# باقي الصفحات تجي بعد تسجيل الدخول (select, input, result ...)
elif st.session_state.page == "select":
    st.markdown("<h2>Select Material</h2>", unsafe_allow_html=True)
    if st.button("🌲 WOOD"):
        st.session_state.material = "WOOD"
        st.session_state.page = "input"
        st.experimental_rerun()
    if st.button("🔩 IRON"):
        st.session_state.material = "IRON"
        st.session_state.page = "input"
        st.experimental_rerun()
    if st.button("📦 CONTAINER"):
        st.session_state.material = "CONTAINER"
        st.session_state.page = "input"
        st.experimental_rerun()
    if st.button("🏗️ RAW MATERIALS"):
        st.session_state.material = "RAW MATERIALS"
        st.session_state.page = "input"
        st.experimental_rerun()
