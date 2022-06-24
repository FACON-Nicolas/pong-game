from abc import ABC
from cmath import sqrt
import os
from typing import overload

import pygame

from Ball import Ball

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

    def move_pong(self, sens: int, delta_time: float, max: int, min: int) -> None:
        value_to_add = (sens * delta_time * AbstractPlayer.speed)
        if (min < self._rect.y + value_to_add < max): self._rect.y += value_to_add

    def isCollidingObject(self, object: Ball) -> bool:
        rect = object.rect
        x, y = abs(self._rect.x-rect.x), abs(self._rect.y-rect.y)
        return x < self._rect.w and y < self._rect.h

    def center_y(self):
        return self._rect.y + (self._rect.h // 2)