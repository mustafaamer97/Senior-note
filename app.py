import os
import streamlit as st
from streamlit_mic_recorder import mic_recorder

# إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="Senior Note | المساعد الذكي للأطباء",
    page_icon="🩺",
    layout="wide"
)

# تصميم الواجهة الرئيسية
st.title("🩺 Senior Note: المنصة الطبية الذكية والمحلية")
st.markdown("---")

# القائمة الجانبية لإدارة المراجع والملفات
with st.sidebar:
    st.header("📚 المكتبة والمراجع الطبية")
    st.markdown("رفع البروتوكولات الخاصة أو تصفح المراجع المضافة مسبقاً.")
    
    uploaded_files = st.file_uploader(
        "رفع ملفات الأبحاث أو البروتوكولات (PDF)", 
        type=["pdf"], 
        accept_multiple_files=True
    )
    
    if uploaded_files:
        st.success(f"تم رفع {lenس(uploaded_files)} ملف بنجاح!")
        # هنا سيتم ربط الملفات بقاعدة المعرفة المحلية (RAG)

    st.markdown("---")
    st.markdown("### 🔒 وضع الخصوصية")
    st.info("النظام يعمل محلياً، ولا يتم رفع بيانات المرضى أو الملفات الحساسة لأي سحابة خارجية.")

# تقسيم الشاشة إلى قسمين رئيسيين (البحث الذكي + المساعد الصوتي)
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("💬 استعلامات البروتوكولات والأبحاث")
    user_query = st.text_input("اسأل عن أي بروتوكول، جرعة، أو حالة طبية (مثلاً: ما هي خطوات التعامل مع صدمة الحساسية الحادة؟)")
    
    if user_query:
        # محاكاة رد الذكاء الاصطناعي بناءً على المراجع المضافة
        st.info("جاري البحث في مراجع وبروتوكولات المستشفى...")
        st.write("**الإجابة السريرية:** (هنا سيظهر الرد الموثق مع أرقام الصفحات والمراجع المعتمدة بناءً على الملفات المرفوعة).")

with col2:
    st.subheader("🎙️ المساعد الصوتي (Scribe)")
    st.markdown("سجل ملاحظات الحالة بعد الفحص مباشرة:")
    
    # زر التسجيل الصوتي عبر المتصفح
    audio_data = mic_recorder(
        start_prompt="🔴 ابدأ التسجيل الصوتي",
        stop_prompt="⏹️ إيقاف التسجيل",
        key='medical_voice_note'
    )
    
    if audio_data:
        st.audio(audio_data['bytes'])
        st.success("تم التقاط الصوت! جاري التفريغ محلياً وصياغة التقرير...")
        # هنا سيتم تمرير الصوت لمحرك Whisper المحلي لتوليد التقرير الطبي المنظم

# قسم عرض التقرير الإكلينيكي الناتج
st.markdown("---")
st.subheader("📋 مسودة التقرير الإكلينيكي / الملخص")
st.text_area("التقرير الجاهز للنسخ إلى السجل الطبي (EMR):", placeholder="سيظهر التقرير الطبي المرتب هنا تلقائياً بعد المعالجة...", height=150)
