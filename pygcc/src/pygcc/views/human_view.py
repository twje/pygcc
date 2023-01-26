from .game_view import GameView
from pygcc.renderer import Renderer
from pygcc.timestep import Timestep
from pygcc.ui.screen_element import ScreenElement
from pygame.event import Event

__all__ = ["HumanView"]


class HumanView(GameView):
    def __init__(self, renderer: Renderer) -> None:
        super().__init__()
        self.renderer = renderer
        self.screen_elements: list[ScreenElement] = []
        self.view_id: int = 0
        self.actor_id: int = 0

    def destroy(self):
        pass

    def push_element(self, element: ScreenElement):
        self.screen_elements.append(element)

    def on_attach(self, view_id, actor_id):
        self.view_id = view_id
        self.actor_id = actor_id

    def on_restore(self):
        pass

    def on_event(self, event: Event):  # VOnMsgProc
        for element in reversed(self.screen_elements):
            element.on_event(event)

    def update(self, ts: Timestep): 
        for element in self.screen_elements:
            element.update(ts)

    def render(self):  # GameCodeApp::OnD3D11FrameRender
        for element in self.screen_elements:
            element.render()
