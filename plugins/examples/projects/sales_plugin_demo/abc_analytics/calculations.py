import pandas as pd
import bamboolib as bam


def compute_revenue_share(df, groupby_columns):
    shares = df.groupby(groupby_columns).agg({"total_revenue": "sum"}).reset_index()
    shares["total_revenue_share"] = shares["total_revenue"] / shares["total_revenue"].sum() * 100
    shares = shares.drop(columns=["total_revenue"])
    return shares


def load_data_from_database_table(*args, **kwargs):
    df = bam.get_sales_df()
    return df