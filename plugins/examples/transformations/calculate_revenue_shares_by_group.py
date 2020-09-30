# %% [markdown]
# # Calculating the revenue share of regions via a TransformationPlugin
#
# __Goal:__ For each **region**, we want to compute the revenue share (i.e. the percentage of our global revenue coming from that region)

# %%
import pandas as pd
import bamboolib as bam

# %%
sales_df = bam.get_sales_df()


# %%
# Custom function used in Plugin
def compute_share(df, groupby_column, value_column):
    shares = df.groupby(groupby_column).agg({value_column: "sum"}).reset_index()
    shares[value_column + "_share"] = shares[value_column] / shares[value_column].sum() * 100
    shares = shares.drop(columns=[value_column])
    return shares


# %%
# Solution:
# revenue_shares_df = compute_share(sales_df, 'region', 'total_revenue')

# %%
import ipywidgets as widgets

from bamboolib.plugins import TransformationPlugin, DF_OLD, DF_NEW, Singleselect


class TotalRevenueShare(TransformationPlugin):

    name = "Compute total revenue share"
    description = "This is a custom plugin that computes the total revenue share"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.groupby_column = Singleselect(
            options=list(self.get_df().columns),
            placeholder="Choose column",
            focus_after_init=True
        )

    def render(self):
        self.set_title("Total revenue share")
        self.set_content(
            widgets.HTML("Compute the <b>total revenue share</b> for each value in"),
            self.groupby_column,
            self.rename_df_group,
        )

    def get_code(self):
        return f"{DF_NEW} = compute_share({DF_OLD}, '{self.groupby_column.value}', 'total_revenue')"


# %% [markdown]
# **Hint:** You can find the plugin by searching "total revenue"

# %%
sales_df

# %% [markdown]
# **Inspiration:** Can you extend the plugin so that the user can choose which column she wants to compute the shares from?

# %%
