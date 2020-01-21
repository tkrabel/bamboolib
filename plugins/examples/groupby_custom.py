# %%
import pandas as pd
import bamboolib as bam
bam.enable()

# %%
df_test = pd.DataFrame({'id': [1,2,3,4,5,6],
              'ab': ['tet', 'tet', 'tet', 'erm' ,'erm' ,'erm'],
              'ab_code': ['AB1', 'AB1', 'AB1', 'AB2', 'AB2', 'AB2', ]})
df_test

# %%
df_test.groupby('ab').agg(lambda x: list(x))


# %%
def custom(x):
    #display(x)
    #display(type(x))
    return list(x)


# %%
import ipywidgets as widgets

from bamboolib.plugins import (
    TransformationPlugin,
    DF_OLD,
    DF_NEW,
    SelectizeWidget,
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
        return f"{DF_NEW} = {DF_OLD}.groupby({self.groupby_columns.value}).agg({self.custom_function_text.value})"



# %%
df_test

# %%
