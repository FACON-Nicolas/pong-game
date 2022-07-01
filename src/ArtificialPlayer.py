import pygame
from AbstractPlayer import AbstractPlayer
from Ball import Ball

class ArtificialPlayer(AbstractPlayer):

    def __init__(self, ball: Ball, window: pygame.Surface) -> None:
        super().__init__()
        self._ball = ball
        self._rect.x = window.get_rect().w-self._rect.w


    def update(self, window: pygame.Surface, delta_time: float, ) -> None:
        direction = -1 if self._ball.rect.y <= self._rect.y else 1
        self.move_pong(direction, delta_time, 0, window.get_rect().h)
        if self._ball.rect.x + self._ball.rect.w >= self._ball._max_x: self.update_score() 
        window.blit(self._pong, self._rect)
