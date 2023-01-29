from typing import Optional
from abc import ABC
from abc import abstractmethod
import json
import logging

from pygcc.level_manager import LevelManager
from pygcc.views.game_view import GameView
from pygcc.timestep import Timestep
from pygcc.game_logic_state import BaseGameState
from pygcc.game_state_manager import GameStateManager
from pygcc.game_state_manager import StateFactoryType
from pygame.event import Event
from pygcc.events import EventData
from pygcc.config import *

__all__ = ["BaseGame"]

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


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
        with open(level_resource, "r") as fp:
            root = json.load(fp)

        pre_load_script, post_load_script = self.load_pre_and_post_load_scripts(
            root,
            level_resource
        )

        print(pre_load_script, post_load_script)

    def load_pre_and_post_load_scripts(self, root: dict, level_resource: str) -> tuple[Optional[str], Optional[str]]:
        pre_load_script, post_load_script = None, None
        if "Scripts" not in root:
            logger.info(f"Unable to load scripts from {level_resource}")
            return pre_load_script, post_load_script

        pre_load_script = self.load_script(root, "PreLoad", level_resource)
        post_load_script = self.load_script(root, "PostLoad", level_resource)

        return pre_load_script, post_load_script

    def load_script(self, root: dict, script_id: str, level_resource: str) -> Optional[str]:
        assert "Scripts" in root
        scripts = root["Scripts"]

        if script_id not in root["Scripts"]:
            logger.info(
                f"Unable to load script {script_id} from {level_resource}")
            return
        script_resource_path = scripts[script_id]

        try:
            with open(script_resource_path, "r") as fp:
                return fp.read()
        except FileNotFoundError:
            logger.info(f"Script '{script_resource_path}' not found.")

    def load_game_delegate(self, foo) -> bool:
        return True

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

    # ---------
    # Delegates
    # ---------
    def request_new_actor_delegate(self, event: EventData):
        # set as a callback in void BaseGameLogic::VSetProxy()
        pass
