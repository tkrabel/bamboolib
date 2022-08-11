# %%
import ipywidgets as widgets

# %%
from bamboolib.plugins import TransformationPlugin, DF_OLD, Singleselect, Multiselect


# %%
class CalculateIndexReturn(TransformationPlugin):

    name = "Calculate index return"
    description = "BR function: calculate the index return of a column."

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        numeric_columns = list(self.get_df().select_dtypes(include=["number"]).columns)

        self.value_column_input = Singleselect(
            options=numeric_columns, placeholder="Choose column", focus_after_init=True
        )
        self.groupby_columns_input = Multiselect(
            options=list(self.get_df().columns),
            placeholder="Choose column(s) (optional)",
        )

    def render(self):
        self.set_title("Calculate Index Return")
        self.set_content(
            widgets.HTML("Calculate the index return of"),
            self.value_column_input,
            widgets.HTML("For each group in (optional)"),
            self.groupby_columns_input,
        )

    def get_code(self):
        return f"""{DF_OLD} = br.add_index_return({DF_OLD}, '{self.value_column_input.value}', {self.groupby_columns_input.value})"""
