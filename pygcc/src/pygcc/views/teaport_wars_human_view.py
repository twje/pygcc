from .human_view import HumanView
from pygcc.events import EventData
from pygcc.event_manager import EventManager
from pygcc.events import EventDataGameplayUIUpdate
from pygcc.events import EvtDataSetControlledActor
from pygcc.timestep import Timestep

__all__ = ["MainMenuView"]


class TeaportWarsHumanView(HumanView):
    def __init__(self, renderer) -> None:
        super().__init__(renderer)
        self.register_all_delegates()

    def destroy(self):
        self.remove_all_delegates()

    def register_all_delegates(self):
        event_manager = EventManager.instance

        event_manager.add_listener(
            self.gameplay_ui_update_delegate,
            EventDataGameplayUIUpdate.event_type
        )
        event_manager.add_listener(
            self.set_controlled_actor_delegate,
            EvtDataSetControlledActor.event_type
        )

    def remove_all_delegates(self):  # todo: implement
        pass

    def update(self, ts: Timestep):
        super().update(ts)

    # ==========
    # View Logic
    # ==========

    # =========
    # Delegates
    # =========
    def gameplay_ui_update_delegate(self, event: EventData):
        pass

    # todo: ActorManager.lua (work out how it calls this event)
    def set_controlled_actor_delegate(self, event: EventData):
        pass
