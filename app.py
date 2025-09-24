import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="Materials Calculator", layout="centered")

# --- سايد منيو (يظهر فقط بعد تسجيل الدخول)
def sidebar_menu():
    with st.sidebar:
        st.header("☰ Menu")
        st.page_link("app.py", label="🏠 Home", icon="🏠")
        st.page_link("app.py#calc", label="📊 Calculator", icon="📊")
        st.page_link("app.py#reports", label="📑 Reports", icon="📑")
        st.page_link("app.py#logout", label="🚪 Logout", icon="🚪")
        # --- USERS (simple, hard-coded) ---
# يمكنك تعديل / إضافة يوزرات هنا بسهولة
USERS = {
    "admin": {"password": "admin123", "role": "admin"},
    "user1": {"password": "user123", "role": "user"}
}

# --- صفحة تسجيل الدخول
def login_page():
    st.markdown("<h2 style='text-align:center;'>🔐 Login</h2>", unsafe_allow_html=True)
    username = st.text_input("Username", key="username", placeholder="Enter username")
    password = st.text_input("Password", key="password", type="password", placeholder="Enter password")

    if st.session_state.get("logged_in"):
        return True

    if st.button("Login", use_container_width=True):
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.success("✅ Login successful!")
            st.rerun()
        else:
            st.error("❌ Invalid credentials")
    return False

# --- اختيار المادة
def select_material():
    st.markdown("<h2 style='text-align:center;'>📦 Select Material</h2>", unsafe_allow_html=True)
    material = st.radio(
        "Choose material:",
        ["Wood", "Iron", "Container", "Raw Materials"],
        horizontal=False
    )
    if st.button("Next ➡️", use_container_width=True):
        st.session_state.material = material
        st.session_state.page = "input"
        st.rerun()

# --- إدخال الوزن أو عدد النماذج
def input_page():
    material = st.session_state.material
    st.markdown(f"<h2 style='text-align:center;'>✍️ Enter {material} data</h2>", unsafe_allow_html=True)

    if material == "Raw Materials":
        qty = st.number_input("Number of models:", min_value=1, step=1, format="%d", key="qty")
        unit_price = 75000
        st.session_state.calc = ("Raw Materials", qty, qty * unit_price)
    else:
        weight = st.number_input("Enter weight (KG):", min_value=1, step=1, format="%d", key="weight")
        if material == "Wood":
            unit_price = 1500
        elif material == "Iron":
            unit_price = 1000
        else:  # Container
            unit_price = 5000

        total = weight * unit_price
        st.session_state.calc = (material, weight, total)

    if st.button("Calculate ✅", use_container_width=True):
        st.session_state.page = "result"
        st.rerun()

# --- صفحة النتيجة
def result_page():
    material, qty, total = st.session_state.calc
    st.markdown("<h2 style='text-align:center;'>📊 Result</h2>", unsafe_allow_html=True)

    st.success(f"**Material:** {material}")
    st.info(f"**Quantity:** {qty}")
    st.warning(f"**Total Price:** {total:,} IQD")

    if st.button("✅ Save & Finish", use_container_width=True):
        st.session_state.saved = True
        st.success("💾 Saved successfully!")

    if st.button("⬅️ Back", use_container_width=True):
        st.session_state.page = "material"
        st.rerun()

# --- Main Control
def main():
    if not st.session_state.get("logged_in"):
        login_page()
        return

    # سايد منيو
    sidebar_menu()

    # التنقل بين الصفحات
    page = st.session_state.get("page", "material")

    if page == "material":
        select_material()
    elif page == "input":
        input_page()
    elif page == "result":
        result_page()

if __name__ == "__main__":
    main()
