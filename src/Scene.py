from faulthandler import is_enabled
import json
from os import system
import pygame
import pygame_gui


class Scene:

    tick = 60

    def __init__(self, background_path: str,  file: str, width: int, height: int) -> None:
        print(system('pwd'))
        pygame.init()
        self._manager = pygame_gui.UIManager((width, height))
        #self._background = pygame.image.load(background_path).convert_alpha()
        #self._rect = self._background.get_rect()
        self._buttons = list()
        self._labels = list()
        self._sliders = list()
        self._is_enabled = False
        self.from_json_to_scene(file)

    def is_enabled(self) -> bool: 
        return self._is_enabled

    def set_enabled(self, is_enabled: bool) -> None:
        self._is_enabled = is_enabled

    is_enabled_property = property(is_enabled, set_enabled)

    def add_button(self, button: pygame_gui.elements.UIButton) -> None:
        if button not in self._buttons:
            button.enable()
            self._buttons.append(button)

    def del_button(self, button: pygame_gui.elements.UIButton) -> None:
        if button in self._buttons:
            self._buttons.remove(button)

    def from_json_to_scene(self, json_file: str) -> None:
        with open(json_file, 'r') as f:
            infos = json.load(f)
            for b in infos["buttons"]: self.add_button(self.from_str_to_button(b))

    
    def from_str_to_button(self, button_infos: str) -> pygame_gui.elements.UIButton:
        text, x, y, size_x, size_y = button_infos.split(".")
        x, y, size_x, size_y = int(x), int(y), int(size_x), int(size_y)
        return pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y), (size_x, size_y)), text=text, manager=self._manager)

    @staticmethod
    def from_tuple_to_slider(slider_infos: tuple) -> pygame_gui.elements.UIHorizontalSlider:
        pass

    @staticmethod
    def from_tuple_to_label(label_infos: tuple) -> pygame_gui.elements.UILabel:
        pass

s = Scene(None, 'resources/menu_scene.json', 1600, 900)