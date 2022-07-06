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
        self._ball = Ball(800, 425, Ball.DEFAULT_SPEED, 1600, 900)
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
        self.update_scenes()
        if self._ball._goal:
            print(self._human.get_score(), " - ", self._ai.get_score())
            self._main_scene._labels[0].set_text(str(self._human.get_score()) + " - " + str(self._ai.get_score()))
            self._ball._goal = False
        self.update_ball_and_players(delta_time, key)

        #if self._ball.x >= 1600: self._human.update_score()
        #elif self._ball.x == 0: self._ai.update_score()
        #self._main_scene._labels[0].set_text(str(self._human.get_score()) + '-' + str(self._ai.get_score()))

    def is_scene_enabled(self, scene_name: str) -> bool:
        if scene_name not in Display.scene_names:
            raise ValueError("This scene does not exist")
        if scene_name=="menu": return self._menu_scene.is_enabled()
        if scene_name=="pause": return self._pause_scene.is_enabled()
        if scene_name=="settings": pass
        if scene_name=="main": return self._main_scene.is_enabled()

    def update_scenes(self):
        for s in self._scenes:
            s.update_scene(self._surface)

    def update_ball_and_players(self, delta_time: float, key: pygame.key):
        if (self._main_scene.is_enabled()):
            self._ball.update(delta_time, self._surface, [self._human, self._ai])
            self._human.update(key, delta_time, 0, self._surface.get_rect().h, self._surface)
            self._ai.update(self._surface, delta_time)
