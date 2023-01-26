from .screen_element import ScreenElement
from .button import Button
from pygcc.timestep import Timestep
from pygcc.event_manager import EventManager
from pygcc.events import EventDataRequestStartGame
from pygame.rect import Rect
from pygame.event import Event


__all__ = ["MainMenuUI"]


RED = (255, 0, 0)


class MainMenuUI(ScreenElement):
    def __init__(self) -> None:
        super().__init__()
        self.start_button = Button(Rect(0, 0, 100, 100), RED, self.start_game)

    def start_game(self):
        event_manager = EventManager.instance
        event_manager.queue_event(EventDataRequestStartGame())

    def on_event(self, event: Event):
        self.start_button.on_event(event)

    def update(self, ts: Timestep):
        pass

    def render(self):
        self.start_button.render()
