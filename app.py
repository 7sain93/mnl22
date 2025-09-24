import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="Our Calculator", page_icon="🧮", layout="centered")

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

# تسجيل الدخول
if st.session_state.page == "login":
    st.markdown("<h2 style='text-align:center;'>🔐 Login</h2>", unsafe_allow_html=True)
    username = st.text_input("Username", key="login_user")
    password = st.text_input("Password", type="password", key="login_pass")

    if st.button("Login") or (username == "user" and password == "123" and st.session_state.get("enter_pressed")):
        if username == "user" and password == "123":
            st.session_state.logged_in = True
            st.session_state.page = "select"
            st.experimental_rerun()
        else:
            st.error("❌ Invalid credentials")

# اختيار المادة
elif st.session_state.page == "select":
    st.markdown("<h2 style='text-align:center;'>Select Material</h2>", unsafe_allow_html=True)
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

# إدخال الوزن/العدد
elif st.session_state.page == "input":
    st.markdown(f"<h2 style='text-align:center;'>Enter {st.session_state.material}</h2>", unsafe_allow_html=True)
    value = st.text_input("Enter value:", key="input_value")

    if st.button("Calculate") or (value and st.session_state.get("enter_pressed")):
        try:
            num = float(value)
            result = {}

            if st.session_state.material == "WOOD":
                trucks = int(num / 40) if num % 40 == 0 else int(num / 40) + 1
                result = {"trucks": trucks, "price": trucks * 200_000}
            elif st.session_state.material == "IRON":
                trucks = int(num / 40) if num % 40 == 0 else int(num / 40) + 1
                result = {"trucks": trucks, "price": trucks * 150_000}
            elif st.session_state.material == "CONTAINER":
                result = {"quantity": int(num), "price": int(num) * 200_000}
            elif st.session_state.material == "RAW MATERIALS":
                result = {"quantity": int(num), "price": int(num) * 75_000}

            result["material"] = st.session_state.material
            result["input"] = num
            st.session_state.calculation = result
            st.session_state.page = "result"
            st.experimental_rerun()
        except ValueError:
            st.error("Enter a valid number")

    if st.button("↩️ Back"):
        st.session_state.page = "select"
        st.experimental_rerun()

# صفحة النتيجة
elif st.session_state.page == "result":
    data = st.session_state.calculation
    st.markdown(f"<h2 style='text-align:center;'>{data['material']} Result</h2>", unsafe_allow_html=True)

    if "trucks" in data:
        st.write(f"**Trucks:** {data['trucks']} 🚛")
    if "quantity" in data:
        st.write(f"**Quantity:** {data['quantity']}")
    st.write(f"**Price:** {data['price']} IQD")

    if st.button("✅ Confirm & Save"):
        st.session_state.history.append(data)
        st.session_state.page = "select"
        st.success("Saved Successfully!")
        st.experimental_rerun()

    if st.button("↩️ Back"):
        st.session_state.page = "input"
        st.experimental_rerun()

# عرض التاريخ
if st.session_state.history:
    st.subheader("📜 Saved History")
    for i, h in enumerate(st.session_state.history, 1):
        trucks = h.get("trucks", "")
        qty = h.get("quantity", "")
        st.write(f"{i}. {h['material']} → {trucks or qty} → {h['price']} IQD")
