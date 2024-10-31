import pandas as pd

class Helper():
# Time
  def seperate_time(self, time_str):
    dt = pd.to_datetime(time_str)
    return [dt.year*100000+dt.day_of_year*100+dt.hour, dt.day_of_week, dt.year, dt.month, dt.day, dt.hour]

  def encode_time(self, filepath="", column="time", save_to=None):
    df = pd.read_csv(filepath)[:100]
    data = [self.seperate_time(time_str) for time_str in df[column]]
    df_time = pd.DataFrame(data, columns=["time_id", "day", "year", "month", "date", "hour"])
    if(save_to): df_time.to_csv(save_to, index=False)
    df[column] = df_time["time_id"]
    # print(df.head(10))
    df.to_csv(filepath, index=False)
    return df_time

# Concat
  def concat_csv(self, filepaths, save_to=None):
    dfs = [pd.read_csv(filepath) for filepath in filepaths]
    df_concat = pd.concat(dfs)
    if(save_to): df_concat.to_csv(save_to, index=False)
    return df_concat

# Helper().encode_time("data/open-meteo-21.00N105.88E19m.csv", save_to="data/dim_time/dim_time.csv")
# Helper().concat_csv(filepaths=[
#   "data/dim_time/dim_time_1.csv",
#   "data/dim_time/dim_time_2.csv",
# ], save_to="data/dim_time/dim_time.csv")