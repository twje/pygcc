from abc import ABC
from typing import Optional
from pygcc.level_manager import LevelManager
from pygcc.game_logic_state import game_logic_state as gls
from pygcc.views.game_view import GameView
from pygcc.timestep import Timestep
from pygcc import game_logic_state as gls
from pygame.event import Event
from pygcc.config import *

__all__ = ["BaseGame"]


class BaseGame(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.games_views: list[GameView] = []
        self.level_manager = LevelManager()
        self.__state_id: gls.BaseGameState = gls.BaseGameState.BGS_Initializing
        self.__state: Optional[gls.GameLogicState] = None

    @property
    def state(self) -> gls.GameLogicState:
        if self.__state is None:
            instance = gls.BaseGameStateFactory.create_state(self.__state_id)
            self.__state = instance
        return self.__state

    def load_game(self, level_resource: str) -> bool:
        print(level_resource)

    def add_view(self, view: GameView, actor_id: int = INVALID_ACTOR_ID):
        view_id = len(self.games_views)
        self.games_views.append(view)

        view.on_attach(view_id, actor_id)
        view.on_restore()

    def on_event(self, event: Event):
        for view in reversed(self.games_views):
            view.on_event(event)

    def update(self, ts: Timestep):
        self.state.update()

    def render(self):
        for view in self.games_views:
            view.render()

    def change_state(self, state_id: gls.BaseGameState):
        self.__state_id = state_id
        self.__state = None
        self.state.on_enter()
