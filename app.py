import streamlit as st
import math

st.set_page_config(page_title="Calculator", page_icon="🧮", layout="centered")

# ----------------------------
# إعداد الحالة
# ----------------------------
if "page" not in st.session_state:
    st.session_state.page = "login"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "role" not in st.session_state:
    st.session_state.role = "user"  # user or admin

# ----------------------------
# دوال الحساب
# ----------------------------
def calc_wood(weight):
    trucks = math.ceil(weight / 40) if weight > 0 else 1
    price = trucks * 200_000
    return trucks, price

def calc_iron(weight):
    trucks = math.ceil(weight / 40) if weight > 0 else 1
    price = trucks * 150_000
    return trucks, price

def calc_container(num):
    price = num * 200_000
    return num, price

def calc_raw(num):
    price = num * 75_000
    return num, price

# ----------------------------
# سايد منيو
# ----------------------------
with st.sidebar:
    if st.session_state.logged_in:
        st.title("☰ Menu")
        st.toggle("Dark mode")  # مجرد placeholder
        support = st.selectbox("Support", ["Choose", "Call", "WhatsApp"])
        if st.button("Logout"):
            st.session_state.page = "login"
            st.session_state.logged_in = False
            st.rerun()
        # صلاحيات الادمن
        if st.session_state.role == "admin":
            st.write("---")
            st.subheader("Admin Options")
            st.button("Create User")
            st.button("Reports")
            st.button("Analytics")

# ----------------------------
# تسجيل الدخول
# ----------------------------
if st.session_state.page == "login":
    st.title("Login")
    username = st.text_input("Username", "")
    password = st.text_input("Password", "", type="password")

    if st.button("Login") or st.session_state.get("enter_pressed") == "login":
        if username == "user" and password == "123":
            st.session_state.logged_in = True
            st.session_state.role = "admin"  # مثال نخلي user هو admin
            st.session_state.page = "select"
            st.rerun()
        else:
            st.error("Invalid credentials")

# ----------------------------
# اختيار المواد
# ----------------------------
elif st.session_state.page == "select":
    st.title("WELCOME TO OUR CALCULATOR!")
    st.write("Choose a material:")
    if st.button("WOOD") or st.session_state.get("enter_pressed") == "wood":
        st.session_state.page = "wood_input"
        st.rerun()
    if st.button("IRON") or st.session_state.get("enter_pressed") == "iron":
        st.session_state.page = "iron_input"
        st.rerun()
    if st.button("CONTAINER") or st.session_state.get("enter_pressed") == "container":
        st.session_state.page = "container_input"
        st.rerun()
    if st.button("RAW MATERIALS") or st.session_state.get("enter_pressed") == "raw":
        st.session_state.page = "raw_input"
        st.rerun()

# ----------------------------
# WOOD
# ----------------------------
elif st.session_state.page == "wood_input":
    st.title("WOOD")
    weight = st.number_input("Enter weight in tons:", min_value=0.0, format="%.2f")
    if st.button("Calculate") or st.session_state.get("enter_pressed") == "wood_calc":
        trucks, price = calc_wood(weight)
        st.session_state.result = (trucks, price, "WOOD")
        st.session_state.page = "result"
        st.rerun()

# ----------------------------
# IRON
# ----------------------------
elif st.session_state.page == "iron_input":
    st.title("IRON")
    weight = st.number_input("Enter weight in tons:", min_value=0.0, format="%.2f")
    if st.button("Calculate") or st.session_state.get("enter_pressed") == "iron_calc":
        trucks, price = calc_iron(weight)
        st.session_state.result = (trucks, price, "IRON")
        st.session_state.page = "result"
        st.rerun()

# ----------------------------
# CONTAINER
# ----------------------------
elif st.session_state.page == "container_input":
    st.title("CONTAINER")
    num = st.number_input("Enter number of containers:", min_value=0, step=1)
    if st.button("Calculate") or st.session_state.get("enter_pressed") == "container_calc":
        count, price = calc_container(num)
        st.session_state.result = (count, price, "CONTAINER")
        st.session_state.page = "result"
        st.rerun()

# ----------------------------
# RAW MATERIALS
# ----------------------------
elif st.session_state.page == "raw_input":
    st.title("RAW MATERIALS")
    num = st.number_input("Enter number of models:", min_value=0, step=1)
    if st.button("Calculate") or st.session_state.get("enter_pressed") == "raw_calc":
        count, price = calc_raw(num)
        st.session_state.result = (count, price, "RAW MATERIALS")
        st.session_state.page = "result"
        st.rerun()

# ----------------------------
# صفحة النتيجة
# ----------------------------
elif st.session_state.page == "result":
    count, price, material = st.session_state.result
    st.title("Result")
    st.write(f"**Material:** {material}")
    if material in ["WOOD", "IRON"]:
        st.write(f"Trucks: **{count}**")
    else:
        st.write(f"Count: **{count}**")
    st.write(f"Total Price: **{price:,} IQD**")

    if st.button("✅ Save"):
        st.success("Saved successfully!")
        st.session_state.page = "select"
        st.rerun()
