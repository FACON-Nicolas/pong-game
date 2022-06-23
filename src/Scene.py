import json
from xml.dom import NotFoundErr
import pygame
import pygame_gui

from Label import Label


class Scene:

    tick = 60

    def __init__(self, background_path: str,  file: str, width: int, height: int) -> None:
        pygame.init()
        pygame.display.init()
        self._manager = pygame_gui.UIManager((width, height))
        self._background = pygame.transform.scale(pygame.image.load(background_path).convert_alpha(), (width, height))
        self._rect = self._background.get_rect()
        self._buttons = list()
        self._labels = list()
        self._sliders = list()
        self._is_enabled = False
        self._width = width
        self._height = height
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

    def add_label(self, label: pygame_gui.elements.UILabel) -> None:
        if label not in self._labels:
            self._labels.append(label)

    def del_button(self, button: pygame_gui.elements.UIButton) -> None:
        if button in self._buttons:
            self._buttons.remove(button)

    def from_json_to_scene(self, json_file: str) -> None:
        with open(json_file, 'r') as f:
            infos = json.load(f)
            for b in infos["buttons"]: self.add_button(self.from_str_to_button(b))
            for l in infos['labels']: self.add_label(self.from_str_to_label(l))

    
    def from_str_to_button(self, button_infos: str) -> pygame_gui.elements.UIButton:
        text, x, y, size_x, size_y = button_infos.split(".")
        x, y, size_x, size_y = int(x), int(y), int(size_x), int(size_y)
        button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y), (size_x, size_y)), text=text, manager=self._manager)
        return button

    def from_str_to_slider(self, slider_infos: str) -> pygame_gui.elements.UIHorizontalSlider:
        pass

    def from_str_to_label(self, label_infos: str) -> pygame_gui.elements.UILabel:
        text_, x, y, s, pos, visibility = label_infos.split('.')
        x, y, s, pos, visibility = int(x), int(y), int(s), int(pos), bool(int(visibility))
        return Label(text_, s, self._width, x, y, pos, visibility)

    def process_scene(self, event: pygame.event) -> None:
        if (self._is_enabled): 
            self._manager.process_events(event)

    def update_scene(self, window: pygame.Surface) -> None:
        if (self._is_enabled):
            window.blit(self._background, self._rect)
            for l in self._labels: l.update(window)
            self._manager.update(1)
            self._manager.draw_ui(window)

    def get_specific_button(self, txt: str) -> pygame_gui.elements.UIButton:
        for b in self._buttons:
            if b.text==txt: return b
        raise NotFoundErr("the button searched does not exist.")

    def disable(self) -> None:
        if not self._is_enabled: raise ValueError("The Scene is already disabled")
        for b in self._buttons:
            b.disable()
        self.set_enabled(False)

    def enable(self) -> None:
        for b in self._buttons:
            b.enable()
        self.set_enabled(True)
