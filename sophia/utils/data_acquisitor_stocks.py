import numpy as np
import pandas as pd
import sqlite3
from prophet import Prophet
from matplotlib import pylab as plt

csv_path = r"/workspaces/sophia/toyota.csv"
db_path = r"/workspaces/sophia/stocks.db"
conn = sqlite3.connect(db_path)

df=pd.read_csv(csv_path)
# df.to_sql("toyota",if_exists="replace",con=conn,index=False)

df=pd.read_sql_query("select date as ds,close as y from toyota",con=conn)
model = Prophet()
model.fit(df)

future_data = model.make_future_dataframe(periods=5, freq="y")
forecast_data = model.predict(future_data)

model.plot_components(forecast_data)
model.plot(forecast_data)

df["y"]=(np.log(df["y"]-np.log(df["y"].shift())))

model = Prophet()
model.fit(df)

future_data = model.make_future_dataframe(periods=5, freq="y")
forecast_data = model.predict(future_data)

model.plot_components(forecast_data)
model.plot(forecast_data)