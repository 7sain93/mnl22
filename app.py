import streamlit as st

st.set_page_config(page_title="Our Calculator", page_icon="🧮", layout="centered")

# CSS for styling
st.markdown("""
    <style>
        .centered {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            text-align: center;
        }
        .stButton>button {
            font-size: 20px;
            padding: 12px 30px;
            border-radius: 12px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #4CAF50;
            color: white;
            transform: scale(1.05);
        }
        .stNumberInput input {
            font-size: 18px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

with st.container():
    if not st.session_state.logged_in:
        st.markdown("<div class='centered'>", unsafe_allow_html=True)
        st.title("🔐 Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username == "user" and password == "123":
                st.session_state.logged_in = True
                st.success("Welcome ADMIN!")
            else:
                st.error("Invalid credentials")
        st.markdown("</div>", unsafe_allow_html=True)
        st.stop()

# Calculator
st.markdown("<div class='centered'>", unsafe_allow_html=True)
st.title("🧮 Main Calculator")

if st.button("🟤 Iron"):
    tons = st.number_input("Enter weight (tons):", min_value=0, step=1)
    if st.button("Calculate Iron"):
        price = tons * 200
        st.success(f"Price = {int(price)}")

if st.button("🚛 Trucks"):
    trucks = st.number_input("Enter number of trucks:", min_value=0, step=1)
    if st.button("Calculate Trucks"):
        price = trucks * 1000
        st.success(f"Price = {int(price)}")

if st.button("📦 Containers"):
    containers = st.number_input("Enter number of containers:", min_value=0, step=1)
    if st.button("Calculate Containers"):
        price = containers * 500
        st.success(f"Price = {int(price)}")

if st.button("🏗️ Raw Materials"):
    models = st.number_input("Enter number of models:", min_value=0, step=1)
    if st.button("Calculate Raw Materials"):
        price = models * 700
        st.success(f"Price = {int(price)}")

st.markdown("</div>", unsafe_allow_html=True)
