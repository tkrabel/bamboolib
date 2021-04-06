# %%
from bamboolib.plugins import LoaderPlugin, DF_NEW, Singleselect

# %%
import ipywidgets as widgets


# %%
class LoadDatabaseTable(LoaderPlugin):

    name = "ABC Corp: Load data from database"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        tables_option = ["Sales Data", "Meta data", "Production data"]
        self.table_input = Singleselect(options=tables_option, value="", width="xl", placeholder="Choose table...")

    def render(self):
        self.set_title("Load data from database")
        self.set_content(
            widgets.HTML("Load data from table"),
            self.table_input,
            self.new_df_name_group,
            self.execute_button,
        )

    def get_code(self):
        return f"""{DF_NEW} = abc.load_data_from_database_table("{self.table_input.value}")"""
    
    
    
