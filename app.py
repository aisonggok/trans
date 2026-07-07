import streamlit as st
from deep_translator import GoogleTranslator

# 앱 제목 설정
st.title("🌐 간단한 다국어 번역기")
st.write("한국어를 입력하면 영어, 일본어, 중국어로 번역해 줍니다!")

# 사용자로부터 한국어 텍스트 입력받기
user_input = st.text_input("번역할 한국어 문장을 입력하세요:", placeholder="예: 안녕하세요, 오늘 날씨가 참 좋네요!")

# 번역 버튼 만들기
if st.button("번역하기"):
    if user_input:
        with st.spinner('번역 중입니다...'):
            try:
                # 영어, 일본어, 중국어(간체) 번역 수행
                en_translation = GoogleTranslator(source='ko', target='en').translate(user_input)
                ja_translation = GoogleTranslator(source='ko', target='ja').translate(user_input)
                zh_translation = GoogleTranslator(source='ko', target='zh-CN').translate(user_input)
                
                # 결과 출력
                st.subheader("번역 결과")
                
                st.success(f"🇺🇸 **영어:** {en_translation}")
                st.info(f"🇯🇵 **일본어:** {ja_translation}")
                st.warning(f"🇨🇳 **중국어:** {zh_translation}")
                
            except Exception as e:
                st.error(f"번역 중 오류가 발생했습니다: {e}")
    else:
        st.warning("번역할 문장을 먼저 입력해 주세요!")
