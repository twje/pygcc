from pygcc.game_logic_state import BaseGameState
from .main_menu import MainMenu
from .waiting_for_players import WaitingForPlayers


replaced_states = {
    BaseGameState.BGS_MainMenu: MainMenu,
    BaseGameState.BGS_WaitingForPlayers: WaitingForPlayers
}
