from abc import ABC
from cmath import sqrt
import os
import pygame

from Ball import Ball

class AbstractPlayer(ABC):

    pong_path = "resources/pong.png"
    speed = 500

    def __init__(self) -> None:
        AbstractPlayer.create_pong()
        self._pong = pygame.image.load(AbstractPlayer.pong_path).convert_alpha()
        self._rect = self._pong.get_rect()
        self._score = 0

    @staticmethod
    def create_pong() -> None:
        if not os.path.exists(AbstractPlayer.pong_path):
            window_tmp = pygame.Surface((20, 120))
            pygame.draw.rect(window_tmp, (55, 55, 55), pygame.Rect(0, 0, 20, 120))
            pygame.image.save(window_tmp, AbstractPlayer.pong_path)

    def update_score(self, value: int=1) -> None:
        if value <= 0: raise ValueError("value must be greater than 0.")
        self._score += value

    def move_pong(self, sens: int, delta_time: float, min: int, max: int) -> None:
        value_to_add = (sens * delta_time * AbstractPlayer.speed)
        if (min <= self._rect.y + value_to_add <= max - self._rect.h): 
            self._rect.y += value_to_add

    def is_collinding_object(self, object: Ball) -> bool:
        rect = object.rect
        if self._rect.x >= 800:
            is_okay_x = 0 <= rect.x - self._rect.x+rect.h <= self._rect.w
            is_okay_y = 0 <= rect.y - self._rect.y+rect.w <= self._rect.h
        else:
            is_okay_x = self._rect.x <= rect.x <= self._rect.x+self._rect.w
            is_okay_y = self._rect.y-rect.h <= rect.y <= self._rect.y+self._rect.h
        return is_okay_x and is_okay_y

    def was_colliding_object(self, object: Ball) -> bool:
        x, y, vx, vy = object.rect.x, object.rect.y, -object._vx, -object._vy
        for i in range(1, object._speed+1):
            object.rect.x, object.rect.y = object.rect.x + vx, object.rect.y + vy
            if self.is_collinding_object(object): return True
        object.rect.x, object.rect.y = x, y
        return False

    def center_y(self):
        return self._rect.y + (self._rect.h // 2)

    def get_score(self):
        return self._score