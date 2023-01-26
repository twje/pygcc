from abc import ABC
from abc import abstractmethod
from pygcc.level_manager import LevelManager
from pygcc.views.game_view import GameView
from pygcc.timestep import Timestep
from pygcc.game_logic_state import BaseGameState
from pygcc.game_state_manager import GameStateManager
from pygcc.game_state_manager import StateFactoryType
from pygame.event import Event
from pygcc.config import *

__all__ = ["BaseGame"]


class BaseGame(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.games_views: list[GameView] = []
        self.level_manager = LevelManager()
        self.state_manager = GameStateManager(BaseGameState.BGS_Initializing)

    def post_init(self):
        self.state_manager.state_factories = self.specify_game_states()

    @abstractmethod
    def specify_game_states(self) -> StateFactoryType:
        """Allow client to extend game states"""
        pass

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
        state = self.state_manager.get_state()
        state.update()

    def render(self):
        for view in self.games_views:
            view.render()

    def change_state(self, state_id: BaseGameState):
        self.state_manager.change_state(state_id)
