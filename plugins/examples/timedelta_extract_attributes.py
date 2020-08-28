# %% [markdown]
# # Extracting attributes from timedelta columns via a TransformationPlugin
#
# inspired by Sailu and the following stackoverflow question:
# - https://stackoverflow.com/questions/38355816/pandas-add-timedelta-column-to-datetime-column-vectorized
#
# __Goal:__ extract the number of weeks as float based on the timedelta column

# %%
import pandas as pd
import numpy as np
import bamboolib as bam

# %%
df = pd.DataFrame()

# %%
df["date"] = ["2016-01-10", "2016-05-11", "2016-02-23", "2015-12-08"]
df["date"] = pd.to_datetime(df["date"])

# %%
df["days"] = [28, 7, 15, 30]
df["days"] = pd.to_timedelta(df["days"], "d")

# %%
# # solution:
# df['weeks'] = df['days'] / np.timedelta64(1, 'W')

# %%
import ipywidgets as widgets

from bamboolib.plugins import TransformationPlugin, DF_OLD, Singleselect, Text


class TimedeltaExtractAttribute(TransformationPlugin):

    name = "Timedelta: extract attribute"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.column = Singleselect(
            options=list(self.get_df().columns), focus_after_init=True
        )

        # based on https://docs.scipy.org/doc/numpy/reference/arrays.datetime.html#datetime-units
        self.attribute = Singleselect(
            options=[
                ("years", "Y"),
                ("months", "M"),
                ("weeks", "W"),
                ("days", "D"),
                ("hours", "h"),
                ("minutes", "m"),
                ("seconds", "s"),
            ],
            value="D",
        )
        self.new_column_name = Text(
            description="New column name", width="lg", execute=self
        )

    def render(self):
        self.set_title("Extract attribute")
        self.set_content(
            widgets.HTML("Convert"),
            self.column,
            widgets.HTML("to"),
            self.attribute,
            self.new_column_name,
        )

    def get_description(self):
        return f"Extract timedelta attribute {self.attribute.label} from '{self.column.value}'"

    def get_code(self):
        return f"{DF_OLD}['{self.new_column_name.value}'] = {DF_OLD}['{self.column.value}'] / np.timedelta64(1, '{self.attribute.value}')"


# %% [markdown]
# __Hint:__ The plugin is shown in bamboolib when searching for "Timedelta: extract attribute"

# %%
df

# %%
