# %%
import pandas as pd
# spark - available within Databricks by default

# %%
def load_ticker(ticker_list):
    df_list = []
    for ticker_name in ticker_list:
        ticker_df = spark.table(ticker_name).toPandas()
        df_list.append(ticker_df)
    df = pd.concat(df_list, axis=0, ignore_index=True)
    return df


# %%
def add_index_return(df, value_column, groupby_columns):
    df["price_return"] = df.groupby(groupby_columns)[value_column].transform(
        "pct_change"
    )
    df["index_return"] = df["price_return"].add(1)
    df["index_return"] = df.groupby(groupby_columns)["index_return"].cumprod().fillna(1)
    return df
