import bamboolib.views.plot_creator as pc


class XAxisForRevenueShare(pc.XAxisWithMaybeSortColumn):
    default_value = "region"


class YAxisForRevenueShare(pc.YAxisWithMultipleColumns):
    default_value = ["total_revenue_share"]


class ColorForRevenueShare(pc.Color):
    default_value = "sales_channel"


class FiureThemeForRevenueShare(pc.FigureTheme):
    default_value = "seaborn"


class TitleForRevenueShare(pc.FigureTitle):
    value = "Revenue Share (%) by Region and Channel"


class ABCRevenueShareBarPlot(pc.BarPlot):
    name = "ABC: plot revenue share"
    recommended_configs = [
        XAxisForRevenueShare,
        YAxisForRevenueShare,
        ColorForRevenueShare,
        FiureThemeForRevenueShare,
        TitleForRevenueShare,
    ]
    # optional_configs = []
