from .game_logic_state import GameLogicState

__all__ = ["LoadingGameEnvironment"]

# when state is entered it reads xml file and regiosteres delegate set_controlled_actor_delegate


class LoadingGameEnvironment(GameLogicState):
    def on_enter(self):
        from pygcc.base.base_game_app import BaseGameApp
        instance = BaseGameApp.instance
        instance.load_game()
