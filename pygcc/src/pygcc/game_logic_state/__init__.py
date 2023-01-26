from enum import Enum
from enum import auto

# ----------------
# Base Game States
# ----------------
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


states = {
    BaseGameState.BGS_Initializing: Initializing,
    BaseGameState.BGS_MainMenu: MainMenu,
    BaseGameState.BGS_WaitingForPlayers: WaitingForPlayers,
    BaseGameState.BGS_LoadingGameEnvironment: LoadingGameEnvironment,
}
