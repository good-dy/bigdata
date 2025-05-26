import streamlit as st
import pandas as pd
import plotly.express as px

CSV_URL = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

@st.cache_data
def load_data():
    df = pd.read_csv(CSV_URL)
    return df

st.title("📊 Google Drive CSV Plotly 시각화 앱")

df = load_data()
st.subheader("데이터 미리보기")
st.dataframe(df)

# 모든 수치형 컬럼 대상으로 X, Y축 선택
numeric_cols = df.select_dtypes(include=["int", "float"]).columns.tolist()
x_col = st.selectbox("X축", numeric_cols)
y_col = st.selectbox("Y축", numeric_cols)

chart_type = st.radio("그래프 유형", ["산점도", "선그래프", "막대그래프"])

# 정렬된 데이터프레임 사용
df_sorted = df.sort_values(by=x_col)

# 그래프 생성
if chart_type == "산점도":
    fig = px.scatter(df_sorted, x=x_col, y=y_col, title=f"{y_col} vs {x_col}")
elif chart_type == "선그래프":
    fig = px.line(df_sorted, x=x_col, y=y_col, title=f"{y_col} vs {x_col}")
else:
    fig = px.bar(df_sorted, x=x_col, y=y_col, title=f"{y_col} vs {x_col}")

st.plotly_chart(fig)
