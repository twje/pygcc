from abc import ABC
from abc import abstractmethod
from pygcc.timestep import Timestep
from pygame.event import Event


class ScreenElement(ABC):
    @abstractmethod
    def on_event(self, event: Event):
        pass

    @abstractmethod
    def update(self, ts: Timestep):
        pass

    @abstractmethod
    def render(self):
        pass
