from __future__ import annotations

from typing import Callable
from collections import defaultdict
from collections import deque
from pygcc.events import EventData

__all__ = ["EventManager"]

ListenerType = Callable[[EventData], None]


class EventManager:
    instance: EventManager = None

    def __init__(self) -> None:
        assert EventManager.instance is None
        self.listeners: dict[int, list[ListenerType]] = defaultdict(list)
        self.queue: deque[EventData] = deque()

    def add_listener(self, listener: ListenerType, event_type: int):
        listener_list = self.listeners[event_type]
        assert listener not in listener_list, "Listener already registered"
        listener_list.append(listener)

    def queue_event(self, event: EventData):
        self.queue.append(event)

    def update(self):
        while len(self.queue) > 0:
            event = self.queue.popleft()
            for listener in self.listeners[event.event_type]:
                listener(event)

        self.queue.clear()


EventManager.instance = EventManager()
