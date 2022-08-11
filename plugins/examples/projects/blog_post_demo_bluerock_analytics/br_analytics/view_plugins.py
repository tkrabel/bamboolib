from bamboolib.plugins import ViewPlugin
from bamboolib.helper import notification


class TrainXGBoostModel(ViewPlugin):

    name = "Train XGBoost model"
    description = "Machine learning (ML): train and score an XGBoost model."

    def render(self):
        self.set_title("Train XGBoost model")
        self.set_content(notification("Coming soon 🚀"))
