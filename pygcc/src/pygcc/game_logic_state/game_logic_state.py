from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pygcc.base.base_game import BaseGame


__all__ = ["GameLogicState"]


class GameLogicState:
    def __init__(self) -> None:
        from pygcc.base.base_game_app import BaseGameApp
        self.game: BaseGame = BaseGameApp.instance.game

    def on_enter(self):
        pass

    def update(self):
        pass
