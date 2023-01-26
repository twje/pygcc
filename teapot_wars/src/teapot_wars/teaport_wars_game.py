from pygcc.base.base_game import BaseGame
from pygcc.base.base_game import StateFactoryType
from pygcc.config import *
from pygcc.event_manager import EventManager
from pygcc.events import EventData
from pygcc.events import EventDataRequestStartGame
from pygcc import game_logic_state as gls


__all__ = ["TeapotWarsGame"]


# ----------------
# Game Logic Layer
# ----------------
class TeapotWarsGame(BaseGame):  # TeapotWarsLogic
    def __init__(self) -> None:
        super().__init__()
        self.register_all_delegates()

    def specify_game_states(self) -> StateFactoryType:
        from teapot_wars.game_logic_states import replaced_states
        states = gls.states
        states.update(replaced_states)
        return states

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
