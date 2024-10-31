import pandas as pd

class Helper():
# Time
  def seperate_time(self, time_str):
    dt = pd.to_datetime(time_str)
    return []

  def encode_time(self, filepath="", column="time"):
    df = pd.read_csv(filepath)[:100]
    dt = 
    df[column] = df[column].apply(lambda x: )
    print(df.head(10))
    # return df


Helper.encode_time(filepath="data/open-meteo-21.00N105.88E19m.csv")