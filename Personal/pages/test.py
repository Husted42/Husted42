import streamlit as st
import pandas as pd
from pages.plots import dailies_heatmap, training_barchart
from pages.utils import build_daily_task_frame

#### ----- Variables ----- #####
daily_tasks = ["Use Habitica", "Up before 8", "Creatin", "Vitamin", "10 min oprydning"]
WEEK_NUMBER = 41
YEAR = 2026


#### ----- Read data ----- #####
data_history = pd.read_csv("data/habitica_task_history.csv")
df_daily = build_daily_task_frame(data_history, daily_tasks, YEAR)

st.set_page_config(
    page_title="Personal Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("Personal Dashboard")
st.caption("Weekly report based on habitica data")

##### ----- Page row 1 ----- #####
col1_1, col1_2 = st.columns([1.4, 1])
height_1 = 400
with col1_1:
    st.subheader(f"Dailies - Week {WEEK_NUMBER}, {YEAR}")
    heatmap = dailies_heatmap(df_daily, WEEK_NUMBER, YEAR, daily_tasks, height=height_1)
    st.altair_chart(heatmap, width='stretch')
with col1_2:
    st.subheader(f"Training - Week {WEEK_NUMBER}, {YEAR}")
    exercise_task = ['Exercise']
    chart = training_barchart(df_daily, WEEK_NUMBER, YEAR, exercise_task, height=height_1)
    st.altair_chart(chart, width='stretch')


##### ----- Side bar ----- #####
with st.sidebar:
    st.title("Navigation")
    st.radio(
        "Select page",
        ["Overview", "Weekly", "Monthly"]
    )
