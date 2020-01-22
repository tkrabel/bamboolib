# %% [markdown]
# # Calculating the diff within groups via a TransformationPlugin
#
# inspired by Sailu and the following stackoverflow post:
# - https://stackoverflow.com/questions/20648346/computing-diffs-within-groups-of-a-dataframe
#
#
# __Goal:__ For each company, calculate the revenue diff to the previous month/row

# %%
import pandas as pd
import numpy as np

# %%
df = pd.DataFrame()

# %%
df["company"] = ["A", "A", "A", "A", "B", "B", "B", "B", "C", "C", "C", "C"]

# %%
df["month"] = [
    "Jan-19",
    "Feb-19",
    "Mar-19",
    "Apr-19",
    "Jan-19",
    "Feb-19",
    "Mar-19",
    "Apr-19",
    "Jan-19",
    "Feb-19",
    "Mar-19",
    "Apr-19",
]

# %%
df["revenue"] = [100, 200, 120, 220, 80, 75, 97, 123, 340, 98, 23, 124]

# %%
# # solution:
# df['diff'] = df.groupby(['company'])['revenue'].transform(lambda series: series.diff())

# %%
import ipywidgets as widgets

from bamboolib.plugins import (
    TransformationPlugin,
    DF_OLD,
    SelectizeWidget,
    SelectizeDropdown,
)


class DiffWithinGroups(TransformationPlugin):

    name = "Diff within groups"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        columns = list(self.get_df().columns)

        self.groupby_columns = SelectizeWidget(
            options=columns, placeholder="Choose groupby column(s)"
        )

        self.value_column = SelectizeDropdown(
            options=columns, placeholder="Choose value column"
        )

        self.new_column_name = widgets.Text(
            value="diff", placeholder="Name of diff column"
        )

    def render(self):
        self.set_title("Diff within groups")
        self.set_content(
            widgets.HTML("Groupby:"),
            self.groupby_columns,
            widgets.HTML("Calculate diff of:"),
            self.value_column,
            widgets.HTML("Call result column:"),
            self.new_column_name,
        )

    def get_code(self):
        return f"{DF_OLD}['{self.new_column_name.value}'] = {DF_OLD}.groupby({self.groupby_columns.value})['{self.value_column.value}'].transform(lambda series: series.diff())"


# %%
df

# %%
