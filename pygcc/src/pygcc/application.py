import sys
from pygcc.timestep import Timestep
from pygcc.application_listener import ApplicationListener
from pygcc.config import *
import pygame
from pygame.locals import *


__all__ = ["Application"]

pygame.init()


class Application:
    def __init__(self, listener: ApplicationListener) -> None:
        self.listener = listener
        self.timestep = Timestep()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.listener.post_init()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                self.listener.on_event(event)

            self.screen.fill(BACKGROUND_COLOR)
            self.listener.update(self.timestep)
            pygame.display.flip()

            delta = self.clock.tick(FPS)
            self.timestep.set_time_from_milliseconds(delta)
