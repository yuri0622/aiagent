# 분류 모델 웹앱 만들기

import streamlit as st

# 1. 기계학습 모델 파일 로드


# 2. 모델 설명
st.title('기업을 위한 나이,성별에 따른 SNS 사용 시간 예측 에이전트')
st.subheader('모델 설명')
st.write(' - 기계학습 알고리즘 : 선형 회귀 ')
st.write(' - 학습 데이터 출처 : https://www.kaggle.com/datasets/imyjoshua/average-time-spent-by-a-user-on-social-media')
st.write(' - 훈련    데이터 : 700건')
st.write(' - 테스트 데이터 : 300건')
st.write(' - 인공지능 모델 정확도 : ?')

# 3. 데이터시각화
col1, col2, col3 = st.columns(3)  
with col1:
      st.subheader('데이터시각화1')
      st.image('시각화1.png' )   # 이미지 불러오기
with col2:
      st.subheader('데이터시각화2')
      st.image('시각화2.png' )   # 이미지 불러오기
with col3:
      st.subheader('데이터시각화3')
      st.image('시각화3.png')   # 이미지 불러오기

# 4. 모델 활용
st.subheader('모델 활용')
st.write('**** 당신의 성별을 선택하고, 나이를 입력해주세요 ')
a = st.number_input(' 나이 입력 ', value=0) 
b = st.selectbox('성별 선택(남자:0, 여자:1, 기타:2' [0,1,2])
