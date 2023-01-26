from typing import Optional
from pygame.event import Event
from pygcc.application_listener import ApplicationListener
from pygcc.timestep import Timestep
from pygcc.event_manager import EventManager
from pygcc.base.base_game import BaseGame
from pygame.event import Event

__all__ = ["BaseGameApp"]


class BaseGameApp(ApplicationListener):
    instance = None

    def __init__(self) -> None:
        assert BaseGameApp.instance is None
        BaseGameApp.instance = self
        super().__init__()
        self.game: Optional[BaseGame] = None
        self.renderer = None

    def post_init(self):  # GameCodeApp::InitInstance (todo - check if there is a deregister event)
        """
        initialize game once all sub-systems are initialized  (i.e. OpenGL graphics context)
        """
        self.register_engine_events()
        self.register_game_events()

        self.game = self.create_game_and_view()

    def on_event(self, event: Event):
        self.game.on_event(event)

    def update(self, ts: Timestep):
        event_manager = EventManager.instance

        event_manager.update()
        self.game.update(ts)
        self.game.render()

    # =====
    # Hooks
    # =====
    def create_game_and_view(self) -> BaseGame:
        assert False

    def load_game(self) -> bool:
        return self.game.load_game("new.xml")

    def register_engine_events(self):
        pass

    def register_game_events(self):
        pass
