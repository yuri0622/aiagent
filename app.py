# 분류 모델 웹앱 만들기

import streamlit as st

# 1. 기계학습 모델 파일 로드
import joblib
model = joblib.load('linear_regression_model.pkl')

import hashlib

def anonymize_user_id(user_id):

    # 사용자 ID를 해싱하여 익명화

    return hashlib.sha256(user_id.encode()).hexdigest()

# 예시 데이터

user_id = "user12345"

anonymized_id = anonymize_user_id(user_id)

print(f"익명화된 사용자 ID: {anonymized_id}")

# 2. 모델 설명
st.title('SNS 사용 시간 예측 에이전트')
st.subheader('모델 설명')
st.write(' - 기계학습 알고리즘 : 선형 회귀 ')
st.write(' - 학습 데이터 출처 : https://www.kaggle.com/datasets/imyjoshua/average-time-spent-by-a-user-on-social-media')
st.write(' - 훈련    데이터 : 700건')
st.write(' - 테스트 데이터 : 300건')
st.write(' - 인공지능 모델 정확도 : -0.01')

# 3. 데이터시각화
col1, col2 = st.columns(2)  
with col1:
      st.subheader('나이과 사용 시간')
      st.image('visualize_1.png' )   # 이미지 불러오기
with col2:
      st.subheader('소득과 사용 시간')
      st.image('visualize_income.png' )   # 이미지 불러오기

# 4. 모델 활용
st.subheader('모델 활용')
st.write('**** 아래의 정보를 입력해주세요! ')

a = st.number_input(' 나이 입력 ', value=0) 
b = st.number_input('소득 입력(단위: 달러)',value=0)

gender_dict = {'남성':0, '여성':1, '기타':2}
c = st.selectbox('성별 선택', list(gender_dict.keys()))
gender = gender_dict[c]

platform_dict = {'instagram':0, 'facebook':1, 'youtube':2}
d = st.selectbox('주요 사용 SNS 선택', list(platform_dict.keys()))
platform = platform_dict[d]

demographics_dict = {'도심':0, '부도심':1, '시골':2}
e = st.selectbox('거주지 특성', list(demographics_dict.keys()))
demographics = demographics_dict[e]

if st.checkbox('저희 기업은 개인정보 보호법 제17조제1항, 제28조의8제1항에서 지정한 범위에 한하여 정보를 제공합니다. 당신이 우리 기업의 정보를 이용한다면 개인정보 보호법 제18조의 제한을 받습니다. 이에 대해 동의하십니까?'):
    go = 1
else:
    go = 0


if st.button('사용시간 예측'): 
    if go==1:
        input_data = [[a,gender,b,platform,demographics]]
        p = model.predict(input_data)
        st.write('인공지능의 예측 사용 시간은 약', p)
    else:
        st.error('당신은 개인정보를 이용에 대해 책임질 준비가 되어있지 않군요! 당신에게는 정보를 제한합니다.')


# HTML과 CSS를 사용하여 배경색을 핑크색으로 변경
st.markdown(
    """
    <style>
        .stApp {
            background-color: pink;  # 배경 색을 핑크색으로 변경
        }
    </style>
    """,
    unsafe_allow_html=True
)
