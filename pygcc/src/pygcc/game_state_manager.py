from typing import Optional
from pygcc.game_logic_state import BaseGameState
from pygcc.game_logic_state import GameLogicState


__all__ = ["GameStateManager"]

StateFactoryType = dict[BaseGameState, GameLogicState]


class GameStateManager:
    def __init__(self, initial_state_id: BaseGameState) -> None:
        self.state_factories: Optional[StateFactoryType] = None
        self.state_id: BaseGameState = initial_state_id
        self.__state: Optional[GameLogicState] = None

    def get_state(self) -> GameLogicState:
        if self.__state is None:
            self.__state = self.state_factories[self.state_id]()
        return self.__state

    def change_state(self, state_id: BaseGameState):
        self.state_id = state_id
        self.__state = self.state_factories[state_id]()
        self.__state.on_enter()
