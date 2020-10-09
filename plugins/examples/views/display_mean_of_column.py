# %% [markdown]
# # Viewplugin demo - computing and displaying the mean of a column
# This little demo shows the basics of how to write a Viewplugin.  
#
# **Goal of the plugin**   
# For a user specified column, display its mean. If the mean cannot be computed (e.g. because it's a string column), show the user a message.
#
# **Need help?**  
# If you have any questions or need help, please <a href="mailto:support+viewplugin_demo_mean_of_column@8080labs.com">reach out</a>.

# %% [markdown]
# **Your turn**   
# Run the code below. After that, you can call the plugin in two ways:
# 1. **For the end user:** open bamboolib by calling `df_titanic` and search for the plugin by its name (or description)
# 2. **During development:** call the plugin directly with `ComputeMeanOfColumn(df=df_titanic)`

# %%
import bamboolib as bam
import pandas as pd

# For this demo, we work with the titanic data set that comes pre-installed with bamboolib
df_titanic = pd.read_csv(bam.titanic_csv)

import ipywidgets as widgets  # We use that to display e.g. HTML

from bamboolib.plugins import ViewPlugin, Singleselect, Button


class ComputeMeanOfColumn(ViewPlugin):

    # You will find the plugin via it's name and/or description.
    name = "Compute mean of a column"
    description = "Compute the mean of a selected column"

    def render(self):
        column_names = list(self.get_df().columns)

        self.column_input = Singleselect(
            options=column_names,
            placeholder="Choose column",
            focus_after_init=True,
        )
        
        self.execute_button = Button(
            description="Compute mean", 
            style="primary",  # Make the button green.
            # Whenever user clicks on self.execute_button, we call update_output.
            # For more info, type `help(Button)`
            on_click=self.update_output  
        )
        
        self.output = widgets.VBox([])
        
        self.set_title("Compute mean of column")
        self.set_content(
            widgets.HTML("Column"),
            self.column_input,
            self.execute_button,
            self.output,
        )
    
    def update_output(self, button):  # button is a required argument (convention by ipywidgets).
        selected_column_name = self.column_input.value
        selected_series = self.get_df()[selected_column_name]
        
        try:
            result = selected_series.mean()
            message = f"Mean of <b>{selected_column_name}</b>: {result:.2f}"
        except:
            # Fails e.g. if column is not numeric.
            message = f"Couldn't compute the mean for column <b>{selected_column_name}</b>"
            
        # This re-renders self.output.
        self.output.children = [widgets.HTML(message)]  # Need to use ipywidgets.


# %% [markdown]
# When you adjusted the class, you can also debug and view the plugin UI via executing `ComputeMeanOfColumn(df=df_titanic)`. This saves you the time of navigating to the plugin in the UI in order to view your changes.

# %%
ComputeMeanOfColumn(df=df_titanic)

# %% [markdown]
# Your users can find the plugin by searching for it's name (or description) inside of bamboolib.

# %%
# Run cell and search for "mean" in the bamboolib search bar.
df_titanic

# %% [markdown]
# **Do you have any questions or feedback?**  
# We're happy to hear it! Please <a href="mailto:bamboolib+viewplugin_demo_mean_of_column@8080labs.com">shoot us a message</a>.
