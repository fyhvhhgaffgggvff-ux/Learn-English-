import streamlit as st
from supabase import create_client, Client

st.set_page_config(page_title="تعلم اللغة الإنجليزية والعربية", layout="centered")

# الاتصال بـ Supabase
@st.cache_resource
def init_supabase():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

try:
    supabase = init_supabase()
except Exception as e:
    st.warning("يرجى إضافة مفاتيح Supabase في Advanced Settings -> Secrets.")

st.title("📚 منصة تعلم اللغة الإنجليزية والعربية")

st.sidebar.header("التصنيفات")
category = st.sidebar.selectbox("اختر التصنيف", ["الكل", "محادثات", "مصطلحات تقنية", "قواعد"])

try:
    query = supabase.table("words").select("*")
    if category != "الكل":
        query = query.eq("category", category)
    
    response = query.execute()
    words = response.data

    if words:
        for item in words:
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**العربية:** {item.get('word_ar', '')}")
                with col2:
                    st.write(f"**English:** {item.get('word_en', '')}")
                st.divider()
    else:
        st.info("لا توجد كلمات متاحة في هذا التصنيف حالياً.")
except Exception as e:
    st.info("قم بإضافة الكلمات إلى جدول words في Supabase لتبدأ بالظهور هنا.")

