from xml.dom import NotFoundErr
import pygame
from Scene import Scene

class Display:

    scene_names = ['menu', 'settings', 'pause', 'main']

    def __init__(self, width: int, height: int) -> None:
        self._height = height
        self._width = width
        self._surface = pygame.display.set_mode((width, height))
        self._menu_scene = Scene('resources/wallpaper.jpg', 'resources/menu_scene.json', width, height)
        self._scenes = [self._menu_scene]
        self._menu_scene.enable()

    def process_menu(self, event):
        self._menu_scene.process_scene(event)

    def update_menu(self):
        self._menu_scene.update_scene(self._surface)

    def search_button(self, txt: str, scene_name: Scene=None):
        if Scene is None: return self._search_button(txt)
        if scene_name not in Display.scene_names:
            raise ValueError("This scene does not exist")
        if scene_name=="menu": return self._menu_scene.get_specific_button(txt)
        if scene_name=="pause": pass
        if scene_name=="settings": pass
        if scene_name=="main": pass


    def _search_button(self, txt: str):
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
        if scene_name=="pause": pass
        if scene_name=="settings": pass
        if scene_name=="main": pass

    def enable_scene(self, scene_name: str) -> None:
        if scene_name not in Display.scene_names:
            raise ValueError("This scene does not exist")
        for s in Display.scene_names: self.disable_scene(scene_name)
        if scene_name=="menu": self._menu_scene.enable()
        if scene_name=="pause": pass
        if scene_name=="settings": pass
        if scene_name=="main": pass

    def show(self, object: pygame.Surface, position: tuple) -> None:
        self._surface.blit(object, position)