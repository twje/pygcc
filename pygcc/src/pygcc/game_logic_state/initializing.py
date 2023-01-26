from .game_logic_state import GameLogicState

__all__ = ["Initializing"]


class Initializing(GameLogicState):
    def update(self):
        from . import BaseGameState
        self.game.change_state(BaseGameState.BGS_MainMenu)
