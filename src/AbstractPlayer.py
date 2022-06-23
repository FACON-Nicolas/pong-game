from abc import ABC
from cmath import sqrt
import os
from typing import overload

import pygame

class AbstractPlayer(ABC):

    pong_path = "resources/pong.png"
    speed = 4

    def __init__(self) -> None:
        AbstractPlayer.create_pong()
        self._pong = pygame.image.load(AbstractPlayer.pong_path).convert_alpha()
        self._rect = self._pong.get_rect()
        self._score = 0

    @staticmethod
    def create_pong() -> None:
        if not os.path.exists(AbstractPlayer.pong_path):
            window_tmp = pygame.Surface((20, 80))
            pygame.draw.rect(window_tmp, (200,200,200), pygame.Rect(0, 0, 20, 80))
            pygame.image.save(window_tmp, AbstractPlayer.pong_path)

    def update_score(self, value: int=1) -> None:
        if value <= 0: raise ValueError("value must be greater than 0.")
        self._score += value

    def move_pong(self, sens: int, delta_time: float) -> None:
        self._rect.y += (sens * delta_time * AbstractPlayer.speed)

    def isCollidingObject(self, object: pygame.Surface) -> bool:
        rect = object.get_rect()
        x, y = abs((self._rect.x-rect.x)**2), abs((self._rect.y-rect.y)**2)
        return x < self._rect.w and y < self._rect.h

