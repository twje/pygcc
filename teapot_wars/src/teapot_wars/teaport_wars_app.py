from pygcc.views.main_menu_view import MainMenuView
from pygcc.base.base_game_app import BaseGameApp
from teapot_wars.teaport_wars_game import TeapotWarsGame

__all__ = ["TeapotWarsApp"]


# -----------------
# Application Layer
# -----------------
class TeapotWarsApp(BaseGameApp):
    def register_engine_events(self):
        pass

    def register_game_events(self):
        pass

    def create_game_and_view(self) -> BaseGameApp:
        game = TeapotWarsGame()
        game.post_init()

        menu_view = MainMenuView()
        game.add_view(menu_view)

        return game
