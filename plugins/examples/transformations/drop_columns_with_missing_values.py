# %% [markdown]
# # Drop columns that only contain missing values

# %%
import pandas as pd
import bamboolib as bam

titanic_df = bam.get_titanic_df()
titanic_df["na_column"] = pd.NA

# %%
# Solution:
# titanic_df_cleaned = titanic_df.dropna(how="all", axis=1)

# %%
from bamboolib.plugins import TransformationPlugin, DF_OLD, DF_NEW, Singleselect
import ipywidgets as widgets


DROP_NA_COLUMNS_OPTIONS = (
    ("only missing values", "all"),
    ("at least 1 missing value", "any")
)


class DropColumnsWithMissingValues(TransformationPlugin):

    name = "Drop columns with missing values"
    description = "Drop columns that contain at least one missing value or only missing values"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.drop_na_option = Singleselect(
            options=DROP_NA_COLUMNS_OPTIONS,
            placeholder="Choose ...",
            focus_after_init=True,
            set_soft_value=True
        )

    def render(self):
        self.set_title("Drop columns with missing values")
        self.set_content(
            widgets.HTML("Drop all columns that contain"),
            self.drop_na_option,
            self.rename_df_group,
        )

    def get_code(self):
        return f"{DF_NEW} = {DF_OLD}.dropna(how='{self.drop_na_option.value}', axis=1)"

# %% [markdown]
# **Hint:** You can find the plugin by searching "drop columns". 

# %%
titanic_df

# %%
