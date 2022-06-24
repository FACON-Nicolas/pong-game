from xml.dom import NotFoundErr
import pygame
import pygame_gui
from AbstractPlayer import AbstractPlayer
from ArtificialPlayer import ArtificialPlayer
from Ball import Ball
from Human import Human
from Scene import Scene

class Display:

    scene_names = ['menu', 'settings', 'pause', 'main']

    def __init__(self, width: int, height: int) -> None:
        pygame.display.init()
        self._height = height
        self._width = width
        self._surface = pygame.display.set_mode((width, height))
        self._menu_scene = Scene('resources/wallpaper.jpg', 'resources/menu_scene.json', width, height)
        self._main_scene = Scene('resources/main_bg.png', 'resources/main_scene.json', width, height)
        self._pause_scene = Scene('resources/main_bg.png', 'resources/pause_scene.json', width, height)
        self._scenes = [self._menu_scene, self._main_scene, self._pause_scene]
        self._ball = Ball(800, 425, 500, 1600, 900)
        self._human = Human()
        self._ai = ArtificialPlayer(self._ball, self._surface)
        self._menu_scene.enable()

    def process(self, event: pygame.surface) -> None:
        for s in self._scenes:
            if(s.is_enabled()):
                s.process_scene(event)

    def update_menu(self) -> None:
        self._menu_scene.update_scene(self._surface)

    def search_button(self, txt: str, scene_name: str) -> pygame_gui.elements.UIButton:
        if scene_name is None: return self._search_button(txt)
        if scene_name not in Display.scene_names:
            raise ValueError("This scene does not exist")
        if scene_name=="menu": return self._menu_scene.get_specific_button(txt)
        if scene_name=="pause": return self._pause_scene.get_specific_button(txt)
        if scene_name=="settings": pass


    def _search_button(self, txt: str) -> pygame_gui.elements.UIButton:
        for s in self._scenes:
            try:
                return s.get_specific_button(txt)
            except NotFoundErr:
                pass
        raise NotFoundErr("The button searched does not exist")

    def disable_scene(self, scene_name: str) -> None:
        if scene_name not in Display.scene_names:
            raise ValueError("This scene does not exist")
        if scene_name=="menu": self._menu_scene.disable()
        if scene_name=="pause": self._pause_scene.disable()
        if scene_name=="settings": pass
        if scene_name=="main": self._main_scene.disable()

    def enable_scene(self, scene_name: str) -> None:
        if scene_name not in Display.scene_names:
            raise ValueError("This scene does not exist")
        for s in self._scenes:
            if s.is_enabled():
                s.disable()
        if scene_name=="menu": self._menu_scene.enable()
        if scene_name=="pause": self._pause_scene.enable()
        if scene_name=="settings": pass
        if scene_name=="main": self._main_scene.enable()

    def show(self, object: pygame.Surface, position: tuple) -> None:
        self._surface.blit(object, position)

    def update(self, delta_time, key: pygame.key) -> None:
        for s in self._scenes:
            s.update_scene(self._surface)
        if (self._main_scene.is_enabled()):
            self._ball.update(delta_time, self._surface, [self._human, self._ai])

        if (self._main_scene.is_enabled()):
            self._human.update(key, delta_time, 0, self._surface.get_rect().h, self._surface)
            self._ai.update(self._surface)

    def is_scene_enabled(self, scene_name: str) -> bool:
        if scene_name not in Display.scene_names:
            raise ValueError("This scene does not exist")
        if scene_name=="menu": return self._menu_scene.is_enabled()
        if scene_name=="pause": return self._pause_scene.is_enabled()
        if scene_name=="settings": pass
        if scene_name=="main": return self._main_scene.is_enabled()