import pygame

class Label():

    def __init__(self, text: str, scale_text: int, width: int, height: int, x: int=0, y=0, pos: int=1):
        self._scale_text = scale_text
        self._x = x
        self._y = y
        self._pos = pos
        self.rect = None
        self._text = None
        if (self._x != 0 and self._pos == 1): raise ValueError("x should be equal to 0 if center is True")
        self.init_text(text)
        self.init_pos(width, height)

    def init_text(self, text: str) -> None:
        font = pygame.font.SysFont(None, self._scale_text)
        self._text = font.render(text, True, (255, 255, 255))

    def init_pos(self, width: int, height: int):
        self.rect = self._text.get_rect()
        if self._pos == 1: self.rect.x = (width - self.rect.w) // 2
        else : self.rect.x = self._x
        self.rect.y = self._y

