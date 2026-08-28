import streamlit as st
import google.generativeai as genai

# إعداد واجهة الصفحة
st.set_page_config(page_title="المعلم الذكي | English & Arabic", page_icon="🤖", layout="centered")

st.title("🤖 المعلم الذكي للغة الإنجليزية والعربية")
st.write("أدخل أي كلمة، جملة، أو مصطلح (تقني، هندسي، أو عام) لتشريح معناها وأمثلة عليها فوراً بالذكاء الاصطناعي.")

# إعداد مفتاح API لـ Gemini
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("يرجى إضافة GEMINI_API_KEY في Advanced Settings -> Secrets داخل Streamlit.")

# واجهة المدخلات
user_input = st.text_input("اكتب الكلمة أو الجملة هنا:", placeholder="مثال: Reservoir, Streamlit, أو جملة كاملة...")

if st.button("شرح وترجمة ✨") and user_input:
    with st.spinner("جاري التحليل واستخراج الأمثلة..."):
        prompt = f"""
        أنت معلم لغة إنجليزية وعربية محترف وخبير.
        قام المستخدم بإدخال الكلمة أو النص التالي: "{user_input}"
        
        يرجى تقديم رد منظم باللغة العربية يحتوي على:
        1. الترجمة الدقيقة (English -> Arabic or Arabic -> English).
        2. نطق الكلمة الصوتية بالرموز أو بالحروف العربية التوضيحية.
        3. مثالين عمليين في جملتين مفيدتين (مع ترجمتهما).
        4. إذا كان النص مصطلحاً تقنياً أو هندسياً، وضح معناه التخصصي باختصار.
        """
        
        try:
            response = model.generate_content(prompt)
            st.success("تم التحليل بنجاح!")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"حدث خطأ أثناء الاتصال بالذكاء الاصطناعي: {e}")
