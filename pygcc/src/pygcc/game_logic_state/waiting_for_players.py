from .game_logic_state import GameLogicState

__all__ = ["WaitingForPlayers"]


class WaitingForPlayers(GameLogicState):
    def on_enter(self):
        pass
        #     # todo: complete multiplayer implementation
        #     from pygcc.teapot_wars import TeapotWars
        #     players_view = TeaportWarsHumanView(TeapotWars.instance.renderer)
        #     self.add_view(players_view)

    def update(self):
        from . import BaseGameState
        self.game.change_state(BaseGameState.BGS_LoadingGameEnvironment)
