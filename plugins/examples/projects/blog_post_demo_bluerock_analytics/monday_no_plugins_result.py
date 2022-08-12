# Databricks notebook source
import pandas as pd; import numpy as np
aapl = spark.table("ticker_aapl").limit(100000).toPandas()


# COMMAND ----------

import pandas as pd; import numpy as np
goog = spark.table("ticker_goog").limit(100000).toPandas()
# Step: Concatenate dataframes vertically
stocks = pd.concat([goog, aapl], axis=0, ignore_index=True)

# Step: Sort column(s) date ascending (A-Z)
stocks = stocks.sort_values(by=['date'], ascending=[True])

# Step: Drop rows where date < 2018-01-01
stocks = stocks.loc[~(stocks['date'] < '2018-01-01')]

# Step: Percentage change
stocks['price_return'] = stocks.groupby(['label'])['close'].transform('pct_change')

# Step: Create new column 'index_return' from formula 'price_return + 1'
stocks['index_return'] = stocks['price_return'] + 1

# Step: Replace missing values
stocks[['index_return']] = stocks[['index_return']].fillna(1)

# Step: Cumulative product
stocks['index_return'] = stocks.groupby(['label'])['index_return'].cumprod()



# COMMAND ----------

import plotly.express as px
fig = px.line(stocks.sort_values(by=['date'], ascending=[True]), x='date', y='index_return', color='label')
fig.update_layout(xaxis_rangeselector_buttons=list([
                dict(label="1m", count=1, step="month", stepmode="backward"),
                dict(label="6m", count=6, step="month", stepmode="backward"),
                dict(label="YTD", count=1, step="year", stepmode="todate"),
                dict(label="1y", count=1, step="year", stepmode="backward"),
                dict(step="all")
            ]))
fig.update_layout(xaxis_rangeslider_visible=True)
fig

# COMMAND ----------


