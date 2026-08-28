import streamlit as st
from google import genai

st.set_page_config(page_title="المعلم الذكي | English & Arabic", page_icon="🤖", layout="centered")

st.title("🤖 المعلم الذكي للغة الإنجليزية والعربية")
st.write("أدخل أي كلمة، جملة، أو مصطلح (تقني، هندسي، أو عام) لتشريح معناها وأمثلة عليها فوراً بالذكاء الاصطناعي.")

# الاتصال بالعميل الجديد
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error("يرجى التأكد من إضافة GEMINI_API_KEY داخل Secrets في Streamlit.")

user_input = st.text_input("اكتب الكلمة أو الجملة هنا:", placeholder="مثال: Porosity, Permeability, Reservoir...")

if st.button("شرح وترجمة ✨") and user_input:
    with st.spinner("جاري التحليل..."):
        prompt = f"""
        أنت معلم ومترجم خبير.
        النص المدخل: "{user_input}"
        
        قم بتقديم شرح منظم باللغة العربية يشمل:
        1. الترجمة الدقيقة.
        2. النطق الصوتي التوضيحي.
        3. مثالين عمليين في جمل مع ترجمتهما.
        4. المعنى التخصصي (إن كان مصطلحاً هندسياً/تقنياً مثل المسامية Porosity).
        """
        
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            st.success("تم التحليل بنجاح!")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"حدث خطأ أثناء الاتصال بالذكاء الاصطناعي: {e}")
