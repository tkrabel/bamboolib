# Databricks notebook source
import bamboolib as bam
import br_analytics as br

# COMMAND ----------

import pandas as pd; import numpy as np
df = br.load_ticker(['goog_ticker_clean', 'aapl_ticker_clean'])
# Step: Calculate index return
df = br.add_index_return(df, 'close', ['label'])

# COMMAND ----------

import plotly.express as px
fig = px.line(df.sort_values(by=['date'], ascending=[True]), x='date', y='index_return', color='label')
fig.update_layout(xaxis_rangeslider_visible=True)
fig.update_layout(xaxis_rangeselector_buttons=list([
                dict(label="1m", count=1, step="month", stepmode="backward"),
                dict(label="6m", count=6, step="month", stepmode="backward"),
                dict(label="YTD", count=1, step="year", stepmode="todate"),
                dict(label="1y", count=1, step="year", stepmode="backward"),
                dict(step="all")
            ]))
fig
