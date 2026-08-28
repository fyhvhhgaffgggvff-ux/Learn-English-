import streamlit as st
from google import genai

# إعداد واجهة الصفحة
st.set_page_config(page_title="المعلم الذكي | English & Arabic", page_icon="🤖", layout="centered")

st.title("🤖 المعلم الذكي للغة الإنجليزية والعربية")
st.write("أدخل أي كلمة، جملة، أو مصطلح (تقني، هندسي، أو عام) لتشريح معناها وأمثلة عليها فوراً بالذكاء الاصطناعي.")

# الاتصال بـ API باستخدام المكتبة الرسمية الجديدة
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error("يرجى التأكد من إضافة GEMINI_API_KEY داخل Secrets في Streamlit.")

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
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            st.success("تم التحليل بنجاح!")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"حدث خطأ أثناء الاتصال بالذكاء الاصطناعي: {e}")
