import pygame
from AbstractPlayer import AbstractPlayer
from Ball import Ball

class ArtificialPlayer(AbstractPlayer):

    def __init__(self, ball: Ball, window: pygame.Surface) -> None:
        super().__init__()
        self._ball = ball
        self._rect.x = window.get_rect().w-self._rect.w


    def update(self, window: pygame.Surface) -> None:
        window.blit(self._pong, self._rect)
