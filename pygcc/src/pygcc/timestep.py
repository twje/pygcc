from dataclasses import dataclass


__all__ = ["Timestep"]

@dataclass
class Timestep:
    __milliseconds: float = 0

    @property
    def seconds(self):
        return self.__milliseconds / 1000

    @property
    def milliseconds(self):
        return self.__milliseconds

    def set_time_from_seconds(self, seconds: float):
        self.__milliseconds = seconds * 1000

    def set_time_from_milliseconds(self, milliseconds: float):
        self.__milliseconds = milliseconds

    