import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="Our Calculator", page_icon="🧮", layout="centered")

# CSS مخصص
st.markdown("""
    <style>
    /* توسيط */
    .block-container {
        max-width: 700px;
        margin: auto;
        padding-top: 50px;
    }
    h2 {
        text-align: center;
        font-size: 32px !important;
        margin-bottom: 30px;
    }
    .stTextInput>div>div>input {
        text-align: center;
        font-size: 20px !important;
        height: 50px !important;
    }
    .stButton>button {
        font-size: 20px !important;
        height: 60px !important;
        width: 100%;
        margin: 10px 0;
        border-radius: 12px;
    }
    /* زر المنيو */
    .menu-btn {
        position: fixed;
        top: 20px;
        left: 20px;
        font-size: 30px;
        cursor: pointer;
        z-index: 1000;
    }
    /* المنيو الجانبي */
    .sidemenu {
        height: 100%;
        width: 0;
        position: fixed;
        z-index: 1500;
        top: 0;
        left: 0;
        background-color: #111;
        overflow-x: hidden;
        transition: 0.5s;
        padding-top: 60px;
    }
    .sidemenu a {
        padding: 12px 24px;
        text-decoration: none;
        font-size: 22px;
        color: #f1f1f1;
        display: block;
        transition: 0.3s;
    }
    .sidemenu a:hover {
        background-color: #575757;
    }
    .sidemenu .closebtn {
        position: absolute;
        top: 10px;
        right: 25px;
        font-size: 40px;
    }
    </style>

    <script>
    function openMenu() {
        document.getElementById("mySidemenu").style.width = "250px";
    }
    function closeMenu() {
        document.getElementById("mySidemenu").style.width = "0";
    }
    </script>
    """, unsafe_allow_html=True)

# الحالة
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "login"

# سايد منيو يظهر فقط بعد تسجيل الدخول
if st.session_state.logged_in:
    st.markdown('<span class="menu-btn" onclick="openMenu()">☰</span>', unsafe_allow_html=True)
    st.markdown("""
        <div id="mySidemenu" class="sidemenu">
            <a href="javascript:void(0)" class="closebtn" onclick="closeMenu()">&times;</a>
            <a onclick="window.location.reload()">🏠 Home</a>
            <a>📊 Reports</a>
            <a>🎨 Design</a>
            <a>📞 Support</a>
            <a onclick="window.location.reload()">🚪 Logout</a>
        </div>
    """, unsafe_allow_html=True)

# تسجيل الدخول
if st.session_state.page == "login":
    st.markdown("<h2>🔐 Login</h2>", unsafe_allow_html=True)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login") or (username and password):
        if username == "user" and password == "123":
            st.session_state.logged_in = True
            st.session_state.page = "select"
            st.experimental_rerun()
        elif username and password:
            st.error("❌ Invalid credentials")

# اختيار المواد
elif st.session_state.page == "select":
    st.markdown("<h2>Select Material</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌲 WOOD"):
            st.write("Go to WOOD input page...")
    with col2:
        if st.button("🔩 IRON"):
            st.write("Go to IRON input page...")
    col3, col4 = st.columns(2)
    with col3:
        if st.button("📦 CONTAINER"):
            st.write("Go to CONTAINER input page...")
    with col4:
        if st.button("🏗️ RAW MATERIALS"):
            st.write("Go to RAW MATERIALS input page...")
