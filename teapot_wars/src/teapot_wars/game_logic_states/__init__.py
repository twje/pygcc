from pygcc import game_logic_state as gls
from .main_menu import MainMenu
from .waiting_for_players import WaitingForPlayers


def extend_base_game_states():
    gls.BaseGameStateFactory.override_factory(
        gls.BaseGameState.BGS_MainMenu,
        MainMenu
    )
    gls.BaseGameStateFactory.override_factory(
        gls.BaseGameState.BGS_WaitingForPlayers,
        WaitingForPlayers
    )
