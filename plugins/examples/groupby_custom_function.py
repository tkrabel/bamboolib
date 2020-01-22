# %% [markdown]
# # Using custom groupby functions via a TransformationPlugin
#
# inspired by Harneet, Will and Zach
#
# __Goal:__ Groupby a column and execute either a lambda function or a custom function

# %%
import pandas as pd
import bamboolib as bam

# %%
df = pd.DataFrame()

# %%
df["group"] = ["A", "A", "A", "B", "B", "B"]

# %%
df["item"] = ["x", "y", "z", "x", "y", "z"]

# %%
df["number"] = [1, 2, 3, 4, 5, 6]


# %%
def my_custom_function(series):
    return min(series)


# %%
# # Solution 1:
# df.groupby('group').agg(lambda x: min(x))

# %%
# # Solution 2:
# df.groupby('group').agg(my_custom_function)

# %%
import ipywidgets as widgets

from bamboolib.plugins import TransformationPlugin, DF_OLD, DF_NEW, SelectizeWidget


class GroupbyCustomFunction(TransformationPlugin):

    name = "Groupby with custom function"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        columns = list(self.get_df().columns)

        self.groupby_columns = SelectizeWidget(
            options=columns, placeholder="Choose column(s)"
        )

        self.custom_function_text = widgets.Text(
            value="lambda x: min(x)", placeholder="lambda expression or function name"
        )

    def render(self):
        self.set_title("Groupy with custom function")
        self.set_content(
            widgets.HTML("Groupby:"),
            self.groupby_columns,
            self.spacer,
            widgets.HTML("Aggregation:"),
            self.custom_function_text,
            self.rename_df_group,
            self.code_preview_group,
        )

    def get_code(self):
        return f"{DF_NEW} = {DF_OLD}.groupby({self.groupby_columns.value}).agg({self.custom_function_text.value})"


# %%
df

# %%
