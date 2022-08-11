# %%
import bamboolib.views.plot_creator as pc


# %%
class XAxisForStocks(pc.XAxisWithMaybeSortColumn):
    default_value = "date"


# %%
class YAxisForStocks(pc.YAxisWithMultipleColumns):
    default_value = ["index_return"]


# %%
class ColorForStocks(pc.Color):
    default_value = "label"


# %%
class BRLinePlotForStocks(pc.LinePlot):
    name = "BR: Line plot for stocks"
    recommended_configs = [
        XAxisForStocks,
        YAxisForStocks,
        ColorForStocks,
        pc.XAxisRangeSlider,
        pc.XAxisDefaultDateRangeSelectors,
    ]
    #optional_configs = []
