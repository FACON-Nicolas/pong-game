from faulthandler import is_enabled
from turtle import st
import pygame
import pygame_gui


class Scene:

    def __init__(self, background_path: str) -> None:
        self._background = pygame.image.load(background_path).convert_alpha()
        self._rect = self._background.get_rect()
        self._buttons = list(pygame_gui.elements.UIButton)
        self._is_enabled = False

    def is_enabled(self) -> bool: 
        return self._is_enabled

    def set_enabled(self, is_enabled: bool) -> None:
        self._is_enabled = is_enabled

    is_enabled_property = property(is_enabled, set_enabled)

    def add_button(self, button: pygame_gui.elements.UIButton) -> None:
        if button not in self._buttons:
            self._buttons.append(button)

    def del_button(self, button: pygame_gui.elements.UIButton) -> None:
        if button in self._buttons:
            self._buttons.remove(button)

    @staticmethod
    def from_json_to_scene(json_file: str):
        pass

    @staticmethod
    def from_tuple_to_button(button_infos: tuple) -> pygame_gui.elements.UIButton:
        pass

    @staticmethod
    def from_tuple_to_slider(slider_infos: tuple) -> pygame_gui.elements.UIHorizontalSlider:
        pass

    @staticmethod
    def from_tuple_to_label(label_infos: tuple) -> pygame_gui.elements.UILabel:
        pass