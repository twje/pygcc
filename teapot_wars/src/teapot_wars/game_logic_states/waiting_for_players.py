from pygcc import game_logic_state as gls

__all__ = ["WaitingForPlayers"]


class WaitingForPlayers(gls.WaitingForPlayers):
    def on_enter(self):
        super().on_enter()
        print("on_enter - WaitingForPlayers")

    def update(self):
        super().update()
        print("update - WaitingForPlayers")
