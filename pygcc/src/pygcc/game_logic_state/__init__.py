from enum import Enum
from enum import auto
from .game_logic_state import GameLogicState
from .initializing import Initializing
from .main_menu import MainMenu
from .waiting_for_players import WaitingForPlayers
from .loading_game_environment import LoadingGameEnvironment


class BaseGameState(Enum):
    BGS_Initializing = auto()
    BGS_MainMenu = auto()
    BGS_WaitingForPlayers = auto()
    BGS_LoadingGameEnvironment = auto()


class BaseGameStateFactory:
    factories = {
        BaseGameState.BGS_Initializing: Initializing,
        BaseGameState.BGS_MainMenu: MainMenu,
        BaseGameState.BGS_WaitingForPlayers: WaitingForPlayers,
        BaseGameState.BGS_LoadingGameEnvironment: LoadingGameEnvironment,
    }

    @classmethod
    def override_factory(cls, state_id: BaseGameState, factory: GameLogicState):
        cls.factories[state_id] = factory

    @classmethod
    def create_state(cls, state_id: BaseGameState) -> GameLogicState:
        return cls.factories[state_id]()
