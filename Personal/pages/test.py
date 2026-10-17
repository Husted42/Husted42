import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Personal Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("Personal Dashboard")
st.caption("Your personal analytics hub")

# Sidebar
with st.sidebar:
    st.title("Navigation")
    st.radio(
        "Select page",
        ["Overview", "Habitica", "Statistics"]
    )

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Tasks Completed", 24, "+5")

with col2:
    st.metric("Completion Rate", "82%", "+4%")

with col3:
    st.metric("Current Streak", "12 days")

# Example chart
st.subheader("Weekly Activity")

df = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Completed": [5, 7, 4, 8, 6, 9, 7]
})

st.bar_chart(df, x="Day", y="Completed")

st.subheader("Task History")
st.dataframe(df, use_container_width=True)