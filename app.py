import streamlit as st
import pandas as pd
from datetime import date

# 1. 제목 및 설명
st.title("📘 수학교사 진로 데이터 대시보드")
st.write("""
이 대시보드는 수학교사를 목표로 하는 학생을 위해 만든 것입니다.
한국 교육 통계를 기반으로 교사 관련 현황을 보여주고,
본인의 역량을 직접 입력해볼 수 있습니다.
""")

# 2. 교원 수 & 학생 수 통계 (교육부)
# GitHub raw URL로 수정
url_stats = "https://raw.githubusercontent.com/hungang1001/-/main/korea_teacher_stats.csv"

try:
    df_stats = pd.read_csv(url_stats)
    st.subheader("🇰🇷 한국 교사·학생 연도별 통계")
    st.dataframe(df_stats)
    
    # 3. 주요 지표 (Metric)
    st.subheader("주요 교육 지표")
    pisa_top = 23  # OECD PISA 수학 상위권 비율
    st.metric("PISA 수학 상위권 비율 (한국)", f"{pisa_top}%", help="OECD 평균 9% 대비 높음")
    
    # 4. 차트 시각화
    st.subheader("📈 연도별 교사 수 변화")
    st.line_chart(df_stats, x="연도", y="교사수")

except Exception as e:
    st.error(f"데이터를 불러오는 데 오류가 발생했습니다: {e}")
    st.info("korea_teacher_stats.csv 파일의 GitHub URL을 확인해주세요.")


# 5. 입력 폼: 나의 수학교사 역량 체크
st.subheader("나의 수학교사 준비 상태 입력")

with st.form("교사역량체크"):
    math_ability = st.slider("수학 이해도 (1-10)", 1, 10, 7)
    teaching_interest = st.slider("교수 열정 (1-10)", 1, 10, 8)
    strong_area = st.text_input("잘하는 수학 분야", "")
    improvement = st.text_input("보완할 점", "")
    submitted = st.form_submit_button("제출")
    
    if submitted:
        st.success("입력해주셔서 감사합니다!")
        st.write("## 입력 결과")
        st.write("ㆍ수학 이해도:", math_ability)
        st.write("ㆍ교수 열정:", teaching_interest)
        st.write("ㆍ잘하는 분야:", strong_area)
        st.write("ㆍ보완할 점:", improvement)
