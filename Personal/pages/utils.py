import pandas as pd


def build_daily_task_frame(
	data_history: pd.DataFrame, tasks: list[str], year: int
) -> pd.DataFrame:
	history_days = data_history.loc[
		data_history["task_name"].isin(tasks), ["task_name", "date"]
	].copy()
	history_days["date"] = (
		pd.to_datetime(history_days["date"], utc=True)
		.dt.tz_localize(None)
		.dt.normalize()
	)
	history_days = history_days.drop_duplicates(["task_name", "date"])
	history_days["done"] = True

	days = pd.date_range(f"{year}-01-01", f"{year}-12-31", freq="D")
	data_spine = pd.MultiIndex.from_product(
		[tasks, days], names=["task_name", "date"]
	).to_frame(index=False)
	df_daily = data_spine.merge(
		history_days, on=["task_name", "date"], how="left"
	)
	df_daily["done"] = df_daily["done"].fillna(False).astype(bool)
	return df_daily
