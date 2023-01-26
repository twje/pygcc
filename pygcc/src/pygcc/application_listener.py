from abc import ABC
from abc import abstractmethod
from .timestep import Timestep
from pygame.event import Event

__all__ = ["ApplicationListener"]


class ApplicationListener(ABC):
    @abstractmethod
    def post_init(self):
        pass

    @abstractmethod
    def on_event(self, event: Event):
        pass

    @abstractmethod
    def update(self, ts: Timestep):
        pass
