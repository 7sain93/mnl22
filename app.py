import streamlit as st
import math
from datetime import datetime

# صفحة مهيأة للعرض في المنتصف
st.set_page_config(page_title="Materials Calculator", layout="centered")

# -------------------------
# CSS للتنسيق (توسيط + حجم أكبر)
# -------------------------
st.markdown(
    """
    <style>
    .block-container {
        max-width: 760px;
        margin: 0 auto;
        padding-top: 40px;
    }
    h1, h2, h3 { text-align: center; }
    .big-btn .stButton>button {
        font-size: 20px !important;
        height: 60px !important;
        border-radius: 10px !important;
    }
    .wide-input .stNumberInput>div>div>input, .wide-input .stTextInput>div>div>input {
        font-size: 18px !important;
        height: 48px !important;
        text-align:center;
    }
    .centered {
        display:flex;
        justify-content:center;
        align-items:center;
        flex-direction:column;
    }
    .grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 16px;
        max-width: 700px;
        margin: 0 auto;
    }
    .result-box {
        border-radius: 10px;
        padding: 18px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        max-width: 600px;
        margin: 0 auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# تهيئة session state
# -------------------------
if "page" not in st.session_state:
    st.session_state.page = "select"   # نفتح مباشرة على صفحة الاختيار
if "material" not in st.session_state:
    st.session_state.material = None
if "calc_pending" not in st.session_state:
    st.session_state.calc_pending = None   # سيتم تخزين نتيجة مؤقتاً قبل التأكيد
if "history" not in st.session_state:
    st.session_state.history = []          # سجل العمليات (محلي بالجلسة)

# -------------------------
# دوال حسابات
# -------------------------
def calc_trucks_from_tons(tons):
    # توقع أن tons عدد صحيح (طن)
    # أقل واحد شاحنة إذا الوزن > 0
    if tons <= 0:
        return 1
    return math.ceil(tons / 40)

def price_for_wood(trucks):
    return trucks * 200_000

def price_for_iron(trucks):
    return trucks * 150_000

def price_for_container(n):
    return n * 200_000

def price_for_raw(n):
    return n * 75_000

# -------------------------
# سايد بار (يظهر دائماً الآن لأن لا تسجيل دخول)
# -------------------------
with st.sidebar:
    st.title("☰ Menu")
    if st.button("🏠 Home"):
        st.session_state.page = "select"
        st.experimental_rerun()
    st.write("---")
    if st.button("📊 Reports"):
        st.session_state.page = "reports"
        st.experimental_rerun()
    if st.button("🎨 Design"):
        st.session_state.page = "design"
        st.experimental_rerun()
    if st.button("📞 Support"):
        st.session_state.page = "support"
        st.experimental_rerun()
    st.write("---")
    if st.button("🚪 Logout / Reset"):
        # إعادة ضبط بسيطة (لا يوجد users الآن)
        st.session_state.page = "select"
        st.session_state.material = None
        st.session_state.calc_pending = None
        st.session_state.history = []
        st.experimental_rerun()

# -------------------------
# صفحة: اختيار المادة
# -------------------------
def page_select():
    st.header("WELCOME TO OUR CALCULATOR!")
    st.write("Choose a material to calculate:")
    st.markdown("<div class='grid'>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌲 WOOD", key="btn_wood", use_container_width=True):
            st.session_state.material = "WOOD"
            st.session_state.page = "input"
            st.experimental_rerun()
    with col2:
        if st.button("🔩 IRON", key="btn_iron", use_container_width=True):
            st.session_state.material = "IRON"
            st.session_state.page = "input"
            st.experimental_rerun()

    col3, col4 = st.columns(2)
    with col3:
        if st.button("📦 CONTAINER", key="btn_container", use_container_width=True):
            st.session_state.material = "CONTAINER"
            st.session_state.page = "input"
            st.experimental_rerun()
    with col4:
        if st.button("🏗️ RAW MATERIALS", key="btn_raw", use_container_width=True):
            st.session_state.material = "RAW MATERIALS"
            st.session_state.page = "input"
            st.experimental_rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# صفحة: إدخال القيم (باستخدام form => Enter يعمل كـ submit)
# -------------------------
def page_input():
    material = st.session_state.material
    st.header(f"Enter {material}")
    st.markdown("<div class='centered'>", unsafe_allow_html=True)

    # نستخدم form حتى Enter يرسل (submit) مباشرة عند ضغط Enter داخل الحقل
    with st.form(key="input_form", clear_on_submit=False):
        if material in ["WOOD", "IRON"]:
            # نستخدم Tons كقيمة صحيحة بدون كسور
            tons = st.number_input("Weight (tons)", min_value=0, step=1, format="%d", key="tons")
            submitted = st.form_submit_button("CALCULATE")
            if submitted:
                trucks = calc_trucks_from_tons(int(tons))
                price = price_for_wood(trucks) if material == "WOOD" else price_for_iron(trucks)
                st.session_state.calc_pending = {
                    "material": material,
                    "input": int(tons),
                    "trucks": trucks,
                    "price": int(price),
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                st.session_state.page = "result"
                st.experimental_rerun()

        elif material == "CONTAINER":
            cnt = st.number_input("Number of containers", min_value=0, step=1, format="%d", key="containers")
            submitted = st.form_submit_button("CALCULATE")
            if submitted:
                price = price_for_container(int(cnt))
                st.session_state.calc_pending = {
                    "material": material,
                    "input": int(cnt),
                    "price": int(price),
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                st.session_state.page = "result"
                st.experimental_rerun()

        elif material == "RAW MATERIALS":
            qty = st.number_input("Number of models", min_value=0, step=1, format="%d", key="models")
            submitted = st.form_submit_button("CALCULATE")
            if submitted:
                price = price_for_raw(int(qty))
                st.session_state.calc_pending = {
                    "material": material,
                    "input": int(qty),
                    "price": int(price),
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                st.session_state.page = "result"
                st.experimental_rerun()

    st.markdown("</div>", unsafe_allow_html=True)
    if st.button("⟲ Back to materials"):
        st.session_state.page = "select"
        st.session_state.material = None
        st.experimental_rerun()

# -------------------------
# صفحة: النتيجة + حفظ
# -------------------------
def page_result():
    data = st.session_state.calc_pending
    if not data:
        st.error("No calculation found.")
        if st.button("Back"):
            st.session_state.page = "select"
            st.experimental_rerun()
        return

    st.header("Preview Result")
    st.markdown("<div class='result-box'>", unsafe_allow_html=True)

    st.write(f"**Material:** {data['material']}")
    st.write(f"**Input:** {data['input']}")
    if data["material"] in ["WOOD", "IRON"]:
        st.write(f"**Trucks:** {data['trucks']} 🚛")
    st.write(f"**Price:** {data['price']:,} IQD")
    st.write(f"**Time:** {data['time']}")

    st.markdown("</div>", unsafe_allow_html=True)

    cols = st.columns([1,1,1])
    with cols[0]:
        if st.button("✅ Confirm & Save"):
            # حفظ مؤقت في الجلسة
            st.session_state.history.append(data.copy())
            st.session_state.calc_pending = None
            st.success("Saved successfully!")
            st.session_state.page = "select"
            st.session_state.material = None
            st.experimental_rerun()
    with cols[1]:
        if st.button("✖ Cancel"):
            st.session_state.calc_pending = None
            st.session_state.page = "select"
            st.session_state.material = None
            st.experimental_rerun()
    with cols[2]:
        if st.button("↩ Back"):
            st.session_state.page = "input"
            st.experimental_rerun()

# -------------------------
# صفحة: التقارير (عرض السجل المحفوظ)
# -------------------------
def page_reports():
    st.header("Reports / Saved Calculations")
    if not st.session_state.history:
        st.info("No saved operations yet.")
    else:
        # جدول مبسط
        rows = []
        for i, rec in enumerate(st.session_state.history, 1):
            rows.append({
                "No": i,
                "Material": rec["material"],
                "Input": rec["input"],
                "Trucks": rec.get("trucks", ""),
                "Price (IQD)": rec["price"],
                "Time": rec["time"]
            })
        import pandas as pd
        df = pd.DataFrame(rows)
        st.dataframe(df)

    if st.button("Back to Home"):
        st.session_state.page = "select"
        st.experimental_rerun()

# -------------------------
# صفحة: design (placeholder)
# -------------------------
def page_design():
    st.header("Design Settings")
    st.info("Design settings placeholder — you can change theme/colors later.")
    if st.button("Back to Home"):
        st.session_state.page = "select"
        st.experimental_rerun()

# -------------------------
# صفحة: support
# -------------------------
def page_support():
    st.header("Support")
    st.write("Call / WhatsApp: 07725406386")
    if st.button("Back to Home"):
        st.session_state.page = "select"
        st.experimental_rerun()

# -------------------------
# Router
# -------------------------
def router():
    page = st.session_state.page
    if page == "select":
        page_select()
    elif page == "input":
        page_input()
    elif page == "result":
        page_result()
    elif page == "reports":
        page_reports()
    elif page == "design":
        page_design()
    elif page == "support":
        page_support()
    else:
        page_select()

# -------------------------
# تشغيل
# -------------------------
router()
