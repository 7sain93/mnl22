import streamlit as st

# إعداد صفحة التطبيق
st.set_page_config(page_title="Our Calculator", page_icon="🧮", layout="centered")

# حالة الجلسة
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "calculation_result" not in st.session_state:
    st.session_state.calculation_result = None
if "history" not in st.session_state:
    st.session_state.history = []

# تسجيل الدخول
if not st.session_state.logged_in:
    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "user" and password == "123":
            st.session_state.logged_in = True
            st.success("✅ Welcome ADMIN!")
        else:
            st.error("❌ Invalid credentials")
    st.stop()

# الصفحة الرئيسية
st.title("🧮 Main Calculator")

# إذا عندنا نتيجة لم يتم تأكيدها → عرض صفحة المعاينة
if st.session_state.calculation_result:
    st.subheader("📊 Preview Result")

    data = st.session_state.calculation_result
    st.write(f"**Material:** {data['material']}")
    st.write(f"**Quantity:** {data['quantity']}")
    if data.get("trucks"):
        st.write(f"**Trucks:** {data['trucks']} 🚛")
    st.write(f"**Price:** {data['price']} IQD")

    if st.button("✅ Confirm & Save"):
        st.session_state.history.append(data)
        st.session_state.calculation_result = None
        st.success("Saved Successfully!")
        st.stop()
    if st.button("↩️ Back"):
        st.session_state.calculation_result = None
    st.stop()

# الخشب
st.subheader("🌲 Wood")
wood = st.text_input("Enter weight (tons):", "", key="wood")
if st.button("Calculate Wood"):
    try:
        tons = float(wood)
        trucks = int(tons / 40) if tons % 40 == 0 else int(tons / 40) + 1
        price = trucks * 200_000
        st.session_state.calculation_result = {
            "material": "Wood",
            "quantity": tons,
            "trucks": trucks,
            "price": price
        }
        st.experimental_rerun()
    except ValueError:
        st.error("Enter valid number")

# الحديد
st.subheader("🔩 Iron")
iron = st.text_input("Enter weight (tons):", "", key="iron")
if st.button("Calculate Iron"):
    try:
        tons = float(iron)
        trucks = int(tons / 40) if tons % 40 == 0 else int(tons / 40) + 1
        price = trucks * 150_000
        st.session_state.calculation_result = {
            "material": "Iron",
            "quantity": tons,
            "trucks": trucks,
            "price": price
        }
        st.experimental_rerun()
    except ValueError:
        st.error("Enter valid number")

# الحاويات
st.subheader("📦 Containers")
containers = st.text_input("Enter number of containers:", "", key="cont")
if st.button("Calculate Containers"):
    try:
        num = int(containers)
        price = num * 200_000
        st.session_state.calculation_result = {
            "material": "Containers",
            "quantity": num,
            "price": price
        }
        st.experimental_rerun()
    except ValueError:
        st.error("Enter valid number")

# المواد الخام
st.subheader("🏗️ Raw Materials")
models = st.text_input("Enter number of models:", "", key="raw")
if st.button("Calculate Raw Materials"):
    try:
        num = int(models)
        price = num * 75_000
        st.session_state.calculation_result = {
            "material": "Raw Materials",
            "quantity": num,
            "price": price
        }
        st.experimental_rerun()
    except ValueError:
        st.error("Enter valid number")

# عرض التاريخ
if st.session_state.history:
    st.subheader("📜 History")
    for i, h in enumerate(st.session_state.history, 1):
        st.write(f"{i}. {h['material']} – {h['quantity']} → {h['price']} IQD")
