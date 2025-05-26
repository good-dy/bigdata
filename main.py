import pandas as pd
import plotly.express as px
import streamlit as st

# GitHub에서 데이터 로드
@st.cache
def load_data():
    url = 'https://raw.githubusercontent.com/<username>/<repo-name>/main/data.csv'  # GitHub raw URL
    df = pd.read_csv(url)  # CSV 파일을 pandas 데이터프레임으로 읽어오기
    return df

# 데이터프레임 로드
df = load_data()

# 데이터 미리보기
st.write("### Data Overview", df.head())

# Plotly 시각화 (예시: 데이터에서 'column1'과 'column2'가 있다고 가정)
fig = px.scatter(df, x='column1', y='column2', title='Scatter Plot of Column1 vs Column2')

# Plotly 시각화 표시
st.plotly_chart(fig)
