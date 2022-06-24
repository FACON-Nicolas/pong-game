import pygame
from pygame.locals import *
from AbstractPlayer import AbstractPlayer

class Human(AbstractPlayer):

    def __init__(self) -> None:
        super().__init__()

    def update(self, key: pygame.key, delta_time: float, min:int, max: int, window: pygame.Surface) -> None:
        assert(min < max), "min must be less than max"
        if key == K_DOWN: self.move_pong(1, delta_time, min, max)
        elif key == K_UP: self.move_pong(-1, delta_time, min, max)
        window.blit(self._pong, self._rect)