# %% [markdown]
# # Extracting attributes from timedelta columns, like weeks or days via a ColumnTransformation plugin
#
# inspired by the following stackoverflow question:
# https://stackoverflow.com/questions/38355816/pandas-add-timedelta-column-to-datetime-column-vectorized

# %%
import pandas as pd
import bamboolib as bam

df = pd.DataFrame([['2016-01-10',28],['2016-05-11',28],['2016-02-23',15],['2015-12-08',30]], 
                      columns = ['date','timedelta'])

df['date'] = pd.to_datetime(df['date'])
df['timedelta'] = pd.to_timedelta(df['timedelta'], 'd')

# %%
df

# %%
# # goal is to extract the number of weeks based on the timedelta column, for example:
# df['weeks'] = df['timedelta'] / np.timedelta64(1, 'W')

# %%
import ipywidgets as widgets

from bamboolib.plugins import ColumnTransformationPlugin, DF_OLD, SelectizeDropdown


class TimedeltaExtractAttribute(ColumnTransformationPlugin):

    name = "Timedelta: extract attribute"

    def __init__(self, *args, column=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.column = column

        # based on https://docs.scipy.org/doc/numpy/reference/arrays.datetime.html#datetime-units
        self.attribute = SelectizeDropdown(
            options=[
                ("year", "Y"),
                ("month", "M"),
                ("week", "W"),
                ("day", "D"),
                ("hour", "h"),
                ("minute", "m"),
                ("second", "s"),
            ],
            value="D",
        )
        self.new_column_name = widgets.Text(value=self.column)

    def render(self):
        self.set_title("Extract attribute")
        self.set_content(
            widgets.HTML(f"Convert <b>{self.column}</b> to"),
            self.attribute,
            widgets.HTML("New column name:"),
            self.new_column_name,
        )

    def get_description(self):
        return (
            f"Extract timedelta attribute {self.attribute.label} from '{self.column}'"
        )

    def get_code(self):
        return f"""{DF_OLD}['{self.new_column_name.value}'] = {DF_OLD}['{self.column}'] / np.timedelta64(1, '{self.attribute.value}')"""



# %% [markdown]
# The plugin is shown in bamboolib when clicking on the column header of timedelta

# %%
df

# %%
