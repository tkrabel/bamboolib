from bamboolib.plugins import TransformationPlugin, DF_OLD, DF_NEW, Multiselect
import ipywidgets as widgets


class TotalRevenueShare(TransformationPlugin):

    name = "ABC Corp: Calculate Revenue Share"
    description = "This is an ABC corp internal function that computes the revenue share"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.groupby_columns = Multiselect(
            options=list(self.get_df().columns),
            placeholder="Choose column",
            focus_after_init=True
        )

    def render(self):
        self.set_title("Calculate Revenue Share")
        self.set_content(
            widgets.HTML("Compute the <b>total revenue share</b> for each value in"),
            self.groupby_columns,
            self.rename_df_group,
        )

    def get_code(self):
        return f"{DF_NEW} = abc.compute_revenue_share({DF_OLD}, {self.groupby_columns.value})"
