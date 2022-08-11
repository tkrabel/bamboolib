from bamboolib.plugins import LoaderPlugin, DF_NEW, Multiselect

import ipywidgets as widgets


class LoadTickerData(LoaderPlugin):

    name = "BR: Load ticker data"
    new_df_name_placeholder = "df"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        ticker_options = [
            {"label": "Google/Alphabet (GOOG)", "value":"ticker_goog"},
            {"label": "Apple (AAPL)", "value":"ticker_aapl"},
            {"label": "Microsoft (MSF)", "value":"ticker_msf"},
            {"label": "Amazon (AMZ)", "value":"ticker_amz"},
        ]
        self.tickers_input = Multiselect(options=ticker_options, value="", width="xl")

    def render(self):
        self.set_title("Load ticker data")
        self.set_content(
            widgets.HTML("Load data for ticker(s)"),
            self.tickers_input,
            self.new_df_name_group,
            self.execute_button,
        )

    def get_code(self):
        return f"""{DF_NEW} = br.load_ticker({self.tickers_input.value})"""
