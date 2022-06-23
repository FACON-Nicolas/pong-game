from operator import truediv
import pygame
import random

class Ball:

    def __init__(self, x: int, y: int, speed: int, max_x: int, max_y:int) -> None:
        self._speed = speed
        self._ball = pygame.transform.scale(pygame.image.load('resources/ball.png').convert_alpha(), (50, 50))
        self.rect = self._ball.get_rect()
        self._vx = 1
        self._vy = -1
        self._min = 0
        self.rect.x = x
        self.rect.y = y
        self._max_x = max_x
        self._max_y = max_y

    def move(self, delta_time: float):
        self.rect.x += (delta_time * self._vx * self._speed)
        self.rect.y += (delta_time * self._vy * self._speed)

    def show_ball(self, window: pygame.Surface):
        window.blit(self._ball, self.rect)

    def update(self, delta_time: float, window: pygame.Surface, players):
        self.move(delta_time)
        self.show_ball(window)
        if self.collide_wall(): self.set_vy()
        if self.collide_player(players): self.set_vx()
        if self.goal(): self._vx, self._vy, self.rect.x, self.rect.y = 0,0,800,425

    def collide_wall(self):
        return self.rect.y <= 0 or self.rect.y + self.rect.h >= self._max_y

    def collide_player(self, players):
         for p in players:
            if (p.isCollidingObject(self)):
                return True
         return False

    def goal(self):
        return self.rect.x <= 0 or self.rect.x + self.rect.w >= self._max_x

    def set_vx(self):
        self._vx = -1 if self._vx >= 0 else 1
        self._vx *= random.randint(1, 4)

    def set_vy(self):
        self._vy = -1 if self._vy >= 0 else 1
        self._vy *= random.randint(1, 4)