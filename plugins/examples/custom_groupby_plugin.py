import ipywidgets as widgets

from bamboolib.plugins import (
    TransformationPlugin,
    DF_OLD,
    DF_NEW,
    SelectizeWidget,
    list_to_string,
)


class GroupbyCustomFunction(TransformationPlugin):

    name = "Groupby with custom function"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.groupby_columns = SelectizeWidget(
            options=list(self.get_df().columns), placeholder="Choose column(s)"
        )

        self.custom_function_text = widgets.Text(
            placeholder="lambda expression or function name", value="lambda x: min(x)"
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
        columns_list = list_to_string(self.groupby_columns.value, quoted=True)
        return f"{DF_NEW} = {DF_OLD}.groupby([{columns_list}]).agg({self.custom_function_text.value})"
