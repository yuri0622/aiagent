# 분류 모델 웹앱 만들기

import streamlit as st

# 1. 기계학습 모델 파일 로드
import joblib
model = joblib.load('pppp.pkl')

# 2. 모델 설명
st.title('다양한 변수에 따른 SNS 사용 시간 예측 에이전트')
st.subheader('모델 설명')
st.write(' - 기계학습 알고리즘 : 선형 회귀 ')
st.write(' - 학습 데이터 출처 : https://www.kaggle.com/datasets/imyjoshua/average-time-spent-by-a-user-on-social-media')
st.write(' - 훈련    데이터 : 700건')
st.write(' - 테스트 데이터 : 300건')
st.write(' - 인공지능 모델 정확도 : -0.02')

# 3. 데이터시각화
col1, col2 = st.columns(2)  
with col1:
      st.subheader('데이터시각화1')
      st.image('visualize_1.png' )   # 이미지 불러오기
with col2:
      st.subheader('데이터시각화2')
      st.image('visualize_income.png' )   # 이미지 불러오기

# 4. 모델 활용
st.subheader('모델 활용')
st.write('**** 소득과 나이를 입력하고, 성별을 선택해주세요! ')

a = st.number_input(' 나이 입력 ', value=0) 
b = st.number_input('소득 입력',value=0)
c = st.selectbox('성별 선택' male:0, female:1, non-binary:2, [0,1,2])

if st.button('사용시간 예측'): 
        input_data = [[a,b,c]]
        p = model.predict(input_data)
        st.write('인공지능의 예측 사용 시간은', p)
