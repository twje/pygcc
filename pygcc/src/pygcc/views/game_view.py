from abc import ABC
from abc import abstractmethod
from pygcc.timestep import Timestep
from pygame.event import Event

__all__ = ["GameView"]


class GameView(ABC):
    @abstractmethod
    def destroy(self):
        pass

    @abstractmethod
    def on_attach(self, view_id, actor_id):
        pass

    @abstractmethod
    def on_restore(self):
        pass

    @abstractmethod
    def on_event(self, event: Event):
        pass

    @abstractmethod
    def update(self, ts: Timestep):
        pass

    @abstractmethod
    def render(self):
        pass
