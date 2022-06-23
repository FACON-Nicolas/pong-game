import pygame

class Label():

    def __init__(self, text: str, scale_text: int, width: int, x: int, y: int, pos: int, isVisible: bool):
        self._scale_text = scale_text
        self._x = x
        self._y = y
        self._width = width
        self._pos = pos
        self._font = None
        self.rect = None
        self._text = None
        self._isVisible = isVisible
        if (self._x != 0 and self._pos == 1): raise ValueError("x should be equal to 0 if center is True")
        self.init(text)
        self.init_pos(width)

    def init(self, text: str) -> None:
        self._font = pygame.font.SysFont(None, self._scale_text)
        self._text = self._font.render(text, True, (255, 255, 255))

    def init_pos(self, width: int) -> None:
        self.rect = self._text.get_rect()
        if self._pos == 1: self.rect.x = (width - self.rect.w) // 2
        else : self.rect.x = self._x
        self.rect.y = self._y

    def set_text(self, text: str) -> None:
        self._text = text
        self.init_pos(self._width)

    def update(self, window: pygame.Surface):
        if (self._isVisible):
            window.blit(self._text, self.rect)