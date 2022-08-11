from bamboolib.plugins import LoaderPlugin, DF_NEW, Multiselect

import ipywidgets as widgets


class LoadTickerData(LoaderPlugin):

    name = "BR: Load ticker data"
    new_df_name_placeholder = "df"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        ticker_options = [
            {"label": "Google/Alphabet (GOOG)", "value":"goog_ticker_clean"},
            {"label": "Apple (AAPL)", "value":"aapl_ticker_clean"},
            {"label": "Microsoft (MSF)", "value":"msf_ticker_clean"},
            {"label": "Amazon (AMZ)", "value":"amz_ticker_clean"},
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


class LoadGoogleSpreadsheetData(LoaderPlugin):
    name = "BR: Google Spreadsheet - load data"
    # TODO: to be implemented with your credentials etc

class LoadBigQueryData(LoaderPlugin):
    name = "BR: BigQuery - load data"
    # TODO: to be implemented with your credentials etc

class LoadSnowflakeData(LoaderPlugin):
    name = "BR: Snowflake - load data"
    # TODO: to be implemented with your credentials etc
