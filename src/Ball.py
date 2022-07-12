from math import sqrt, sin
import pygame

class Ball:

    DEFAULT_SPEED = 500

    def __init__(self, x: int, y: int, speed: int, max_x: int, max_y:int) -> None:
        self._speed = speed
        self._ball = pygame.transform.scale(pygame.image.load('resources/ball.png').convert_alpha(), (50, 50))
        self.rect = self._ball.get_rect()
        self._vx = -1
        self._vy = 1
        self._min = 0
        self.rect.x = x
        self.rect.y = y
        self._max_x = max_x
        self._max_y = max_y
        self._collide = None
        self._goal = False

    def reset(self, x: int, window: pygame.Surface):
        self.rect.x = window.get_rect().w / 2
        self.rect.y = window.get_rect().h / 2
        self._collide = None
        self._vx = 1 if x < window.get_rect().w / 2 else -1
        self._vy = 1 if x < window.get_rect().h / 2 else -1

    def move(self, delta_time: float):
        self.rect.x += (delta_time * self._vx * self._speed)
        self.rect.y += (delta_time * self._vy * self._speed)

    def show_ball(self, window: pygame.Surface):
        window.blit(self._ball, self.rect)

    def update(self, delta_time: float, window: pygame.Surface, players):
        self.move(delta_time)
        self.show_ball(window)
        if self.collide_wall(): self.bounce()
        if self.collide_player(players): self.bounce(self.collide_player(players))
        if (self.goal()): self._goal = True

    def collide_wall(self):
        return self.rect.y <= 0 or self.rect.y + self.rect.h >= self._max_y

    def collide_player(self, players):
        player = None
        for p in players:
            if (p.is_collinding_object(self)):
                player = p
        return player

    def goal(self):
        return self.rect.x+self.rect.w < 0 or self.rect.x >= self._max_x

    def bounce(self, player=None):
        if (self.is_collide_okay()):
            if player is None: 
                self.bounced(0, False)
                self.set_collide("wall")
            else:
                difference = self.rect.y - player.center_y()
                self.set_collide("player")
                self.bounced(difference, True)

    def is_collide_okay(self):
        return self._vy <= 0 and self._collide == "down-wall" \
            or self._vy > 0 and self._collide == "top-wall" \
            or self._vx <= 0 and self._collide == "right-player" \
            or self._vx > 0 and self._collide == "left-player"\
            or self._collide is None 

    def set_wall_collide(self):
        self._collide = "top-wall" if self._vy > 0 else "down-wall"

    def set_player_collide(self):
        self._collide = "right-player" if self._vx > 0 else "left-player"

    def set_collide(self, collide):
        if "wall" in collide: self.set_wall_collide()
        else: self.set_player_collide()

    def bounced(self, difference: float, is_collinding_player: bool):
        alpha = 63+difference
        ab = self._vy if not is_collinding_player else self._vx
        ac = ab*sin(alpha)
        bc = sqrt(ac**2+ab**2)
        if is_collinding_player: 
            self._vx = bc if self._vx < 0 else -bc
        else: 
            self._vy = bc if self._vy < 0 else -bc


