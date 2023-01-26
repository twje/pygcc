from .human_view import HumanView
from pygcc.timestep import Timestep
from pygcc.ui.main_menu_ui import MainMenuUI

__all__ = ["MainMenuView"]


class MainMenuView(HumanView):
    def __init__(self) -> None:
        super().__init__(None)
        self.main_menu_ui = MainMenuUI()
        self.push_element(self.main_menu_ui)
