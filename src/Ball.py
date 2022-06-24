from math import sqrt, sin
import pygame

class Ball:

    def __init__(self, x: int, y: int, speed: int, max_x: int, max_y:int) -> None:
        self._speed = speed
        self._ball = pygame.transform.scale(pygame.image.load('resources/ball.png').convert_alpha(), (50, 50))
        self.rect = self._ball.get_rect()
        self._vx = -1.1
        self._vy = 1.1
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
        if self.collide_wall(): self.bounced(0, False)
        if self.collide_player(players): self.bounce(self.collide_player(players))
        if self.goal(): self._vx, self._vy, self.rect.x, self.rect.y = 0,0,800,425

    def collide_wall(self):
        return self.rect.y <= 0 or self.rect.y + self.rect.h >= self._max_y

    def collide_player(self, players):
         for p in players:
            if (p.isCollidingObject(self)):
                return p
         return None

    def goal(self):
        return self.rect.x <= 0 or self.rect.x + self.rect.w >= self._max_x

    def bounce(self, player=None):
        if player is None: self.bounced(0, False)
        else: 
            difference = self.rect.y - player.center_y()
            self.bounced(difference, True)

    def bounced(self, difference: float, is_collinding_player: bool):
        alpha = 63+difference
        ab = self._vy if not is_collinding_player else self._vx
        ac = ab*sin(alpha)
        bc = sqrt(ac**2+ab**2)
        if is_collinding_player: self._vx = bc
        else: 
            self._vy = bc if self._vy < 0 else -bc


