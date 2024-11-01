import pandas as pd

class Helper():
# Time
  def seperate_time(self, time_str):
    dt = pd.to_datetime(time_str)
    return [dt.year*100000+dt.day_of_year*100+dt.hour, dt.day_of_week, dt.year, dt.month, dt.day, dt.hour]

  def encode_time(self, filepath="", column="time_id", save_to=None):
    df = pd.read_csv(filepath)
    data = [self.seperate_time(time_str) for time_str in df[column]]
    df_time = pd.DataFrame(data, columns=["time_id", "day", "year", "month", "date", "hour"])
    df[column] = df_time["time_id"]
    # df.to_csv(filepath, index=False)
    df_time = df_time.drop_duplicates(subset=[column], keep="first")
    if(save_to): df_time.to_csv(save_to, index=False)
    return df_time

# Concat
  def concat_csv(self, filepaths, save_to=None, index=False):
    dfs = [pd.read_csv(filepath) for filepath in filepaths]
    df_concat = pd.concat(dfs)
    if(save_to): df_concat.to_csv(save_to, index=index)
    return df_concat
  
  def concat_fact(self):
    self.concat_csv([
      "references/daily/daily-2018.csv",
      "references/daily/daily-2020.csv",
      "references/daily/daily-2022.csv",
      "references/daily/daily-2024.csv",
    ], "data/fact_daily_summary.csv", True)
    
    self.concat_csv([
      "references/hourly/hourly-2018.csv",
      "references/hourly/hourly-2019.csv",
      "references/hourly/hourly-2020.csv",
      "references/hourly/hourly-2021.csv",
      "references/hourly/hourly-2022.csv",
      "references/hourly/hourly-2023.csv",
      "references/hourly/hourly-2024.csv",
    ], "data/fact_weather.csv", True)

    print(f"[JV] Concatenated successfully!")

# Ae chạy hàm ni để concatnate lại bảng fact
Helper().concat_fact()


# df = pd.read_csv("data/dim_time.csv")
# df = df.drop(df.columns[0], axis=1)
# df.to_csv("data/dim_time.csv", index=False)

# Helper().encode_time(
#   "references/hourly/hourly-2018.csv",
#   save_to="data/dim_time_2018.csv")

# Helper().encode_time(
#   "references/daily/daily-2018.csv")

# Helper().concat_csv(filepaths=[
#   "data/dim_time_2018.csv",
#   "data/dim_time_2019.csv",
#   "data/dim_time_2020.csv",
#   "data/dim_time_2021.csv",
#   "data/dim_time_2022.csv",
#   "data/dim_time_2023.csv",
#   "data/dim_time_2024.csv",
# ], save_to="data/dim_time.csv")