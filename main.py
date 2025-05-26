import streamlit as st
import pandas as pd
import plotly.express as px

# Google Drive의 CSV 파일 URL
CSV_URL = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

@st.cache_data
def load_data():
    df = pd.read_csv(CSV_URL)
    return df

# Streamlit 앱 제목
st.title("📊 Google Drive CSV Plotly 시각화 앱")

# 데이터 불러오기
df = load_data()

# 데이터 미리보기
st.subheader("데이터 미리보기")
st.dataframe(df)

# 컬럼 선택
st.subheader("Plotly 그래프 만들기")
numeric_cols = df.select_dtypes(include=["int", "float"]).columns.tolist()
all_cols = df.columns.tolist()

x_col = st.selectbox("X축", all_cols)
y_col = st.selectbox("Y축", numeric_cols)

chart_type = st.radio("그래프 유형", ["산점도", "선그래프", "막대그래프"])

# 그래프 그리기
if chart_type == "산점도":
    fig = px.scatter(df, x=x_col, y=y_col, title=f"{y_col} vs {x_col}")
elif chart_type == "선그래프":
    fig = px.line(df, x=x_col, y=y_col, title=f"{y_col} vs {x_col}")
else:
    fig = px.bar(df, x=x_col, y=y_col, title=f"{y_col} vs {x_col}")

st.plotly_chart(fig)
