import pandas as pd
from datetime import date
import altair as alt

def dailies_heatmap(
    df_daily: pd.DataFrame, week_number: int, year: int, tasks: list[str], height: int = 200
):

    iso_dates = df_daily["date"].dt.isocalendar()
    selected_rows = (iso_dates["week"] == week_number) & (iso_dates["year"] == year)
    df_week = df_daily.loc[selected_rows].copy()
    df_week = df_week[df_week["date"].dt.dayofweek < 5].copy()
    df_week["day"] = df_week["date"].dt.strftime("%a %d-%m")

    day_order = df_week.sort_values("date")["day"].unique().tolist()
    heatmap = alt.Chart(df_week).mark_rect(stroke="gray").encode(
        x=alt.X("day:N", sort=day_order, title="Day"),
        y=alt.Y("task_name:N", sort=tasks, title="Task"),
        color=alt.Color(
            "done:N",
            scale=alt.Scale(domain=[True, False], range=["#2ecc71", "#e0e0e0"]),
            title="Completed",
        ),
    )
    return heatmap.properties(height=height)

def  training_barchart(
    df_daily: pd.DataFrame, week_number: int, year: int, tasks: list[str], height: int = 200
):


    iso_dates = df_daily["date"].dt.isocalendar()
    current_week_start = pd.Timestamp(date.fromisocalendar(year, week_number, 1))
    week_starts = pd.date_range(
        current_week_start - pd.Timedelta(weeks=4), periods=5, freq="W-MON"
    )

    df_training = df_daily[df_daily["task_name"].isin(tasks)].copy()
    df_training["week_start"] = df_training["date"] - pd.to_timedelta(
        df_training["date"].dt.dayofweek, unit="D"
    )
    df_training = df_training[
        df_training["week_start"].isin(week_starts)
        & (df_training["date"].dt.dayofweek < 5)
    ]

    weekly_counts = (
        df_training.groupby("week_start")["done"]
        .sum()
        .reindex(week_starts, fill_value=0)
        .rename_axis("week_start")
        .reset_index(name="completed_tasks")
    )
    weekly_counts["week"] = [
        f"{week_start.isocalendar().year}-W{week_start.isocalendar().week:02d}"
        for week_start in weekly_counts["week_start"]
    ]

    barchart = alt.Chart(weekly_counts).mark_bar(color="#2ecc71").encode(
        x=alt.X("week:N", sort=weekly_counts["week"].tolist(), title="Week"),
        y=alt.Y("completed_tasks:Q", title="Completed training tasks"),
        tooltip=["week:N", "completed_tasks:Q"],
    )
    return barchart.properties(height=height)