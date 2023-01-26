__all__ = [
    "EventDataRequestStartGame",
    "EventDataGameplayUIUpdate",
    "EvtDataSetControlledActor"
]


class EventData:
    counter = 0

    def __init__(self) -> None:
        super().__init__()

    @property
    def name(self) -> str:
        return self.__name__

    @staticmethod
    def generate_guid() -> int:
        EventData.counter += 1
        return EventData.counter


class EventDataRequestStartGame(EventData):
    event_type: int = EventData.generate_guid()


class EventDataGameplayUIUpdate(EventData):
    event_type: int = EventData.generate_guid()


class EvtDataSetControlledActor(EventData):
    event_type: int = EventData.generate_guid()
