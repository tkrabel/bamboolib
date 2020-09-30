# %% [markdown]
# # Demo for loading dummy data
# - This is the actual code that is also used inside bamboolib. You find the UI when you type "bam" in a cell and execute the cell
# - You can use this template to write your own data loader from your custom sources

# %%
import bamboolib as bam

# %%
bam

# %% [markdown]
# If you adjust the code of the DummyData class below, you will also adjust the default behavior of bamboolib because the LoaderPlugin overrides the previous plugin with the same name

# %%
import ipywidgets as widgets
from bamboolib.plugins import LoaderPlugin, DF_NEW, Singleselect

class DummyData(LoaderPlugin):

    name = "Load dummy data"
    new_df_name_placeholder = "df"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        data_options = [
            {
                "label": "Titanic dataset",
                "value": "pd.read_csv(bam.titanic_csv)",
                "description": "Each row is a passenger on the Titanic - often used for classifications",
            },
            {
                "label": "Sales dataset",
                "value": "pd.read_csv(bam.sales_csv)",
                "description": "Timeseries dataset - each row is a monthly sales figure for various products",
            },
        ]
        self.dataset = Singleselect(
            options=data_options, value=data_options[0]["value"], width="xl"
        )

    def render(self):
        self.set_title("Load dummy data")
        self.set_content(
            widgets.HTML("Load a dummy data set for testing bamboolib"),
            self.dataset,
            self.new_df_name_group,
            self.execute_button,
        )

    def get_code(self):
        return f"""
                    import pandas as pd
                    {DF_NEW} = {self.dataset.value}
                """


# %% [markdown]
# When you adjusted the class, you can also debug and view the plugin UI via executing `DummyData()`. This saves you the time of navigating to the plugin in the UI in order to view your changes.

# %%
DummyData()

# %%
