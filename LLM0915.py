import streamlit as st

st.title("War News Bias Analyzer")
st.write("전쟁 뉴스의 언론사별 보도 관점을 비교·분석합니다.")

# UI 요소 1 : 국가 선택
country = st.selectbox(
    "비교할 국가를 선택하세요",
    ["이스라엘", "미국", "팔레스타인", "이집트"]
)

# UI 요소 2 : 분석할 기사 입력
article = st.text_area(
    "분석할 뉴스 기사를 입력하세요",
    placeholder="뉴스 기사의 내용을 붙여넣으세요."
)

# UI 요소 3 : 분석 버튼
if st.button("기사 분석하기"):
    st.subheader("분석 결과")

    st.write("선택한 국가:", country)
    st.write("기사의 표현과 관점을 분석합니다.")