from typing import Callable
from pygcc.base.base_game import BaseGame
from pygcc.views.game_view import GameView
from pygcc.timestep import Timestep
from pygcc.config import *
from pygcc.event_manager import EventManager
from pygcc.views.teaport_wars_human_view import TeaportWarsHumanView
from pygcc.events import EventData
from pygcc.events import EventDataRequestStartGame
from pygcc import game_logic_state as gls
from pygame.event import Event


__all__ = ["TeapotWarsGame"]


#StateFactoryType = Callable[[], gls.GameLogicState]


# ----------------
# Game Logic Layer
# ----------------
class TeapotWarsGame(BaseGame):  # TeapotWarsLogic
    from pygcc import game_logic_state as gls

    def __init__(self) -> None:
        super().__init__()
        self.register_all_delegates()

    def post_init(self):
        pass

    def register_all_delegates(self):
        event_manager = EventManager.instance
        event_manager.add_listener(
            self.request_start_game_delegate,
            EventDataRequestStartGame.event_type
        )

    # =========
    # Delegates
    # =========
    def request_start_game_delegate(self, event: EventData):
        self.change_state(gls.BaseGameState.BGS_WaitingForPlayers)
