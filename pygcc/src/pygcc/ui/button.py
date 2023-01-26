from typing import Callable
from .screen_element import ScreenElement
from pygcc.timestep import Timestep
from pygame.color import Color
from pygame.rect import Rect
from pygame.event import Event
import pygame


__all__ = ["Button"]


class Button(ScreenElement):
    def __init__(self, rect: Rect, color: Color, callback: Callable) -> None:
        super().__init__()
        self.rect = rect
        self.color = color
        self.callback = callback
        self.screen = pygame.display.get_surface()

    def on_event(self, event: Event):
        if event.type == pygame.MOUSEBUTTONUP:
            position = pygame.mouse.get_pos()
            if self.rect.collidepoint(position[0], position[1]):
                self.callback()

    def update(self, ts: Timestep):
        pass

    def render(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
