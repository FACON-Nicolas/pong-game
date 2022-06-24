__author__ = 'FACON Nicolas'
__version__ = '1.0.0'
__date__ = '2022-06-20'

import time
import pygame
from time import time as time_
from pygame.locals import *
from pygame_gui._constants import *
from Display import Display
from Human import Human

UI_BUTTON_PRESSED = 1025 # pygame_gui.UI_BUTTON_PRESSED doesn't work anymore, so I gave it a value
delta = 0

class Main():

    delta = 0
    
    def __init__(self) -> None:
        self._display = Display(1600, 900)
        self._is_running = True
        self._key = None
        self._is_paused_key_up = True
        self.run()

    def run(self) -> None:
        clock = pygame.time.Clock()
        t = time_()
        while self._is_running:
            clock.tick(60)
            self.update_delta(t)
            t = time_()
            self.event()
            self.update()
            self._display.update(Main.delta, self._key)
            pygame.display.flip()

    def update_delta(self, time : time) -> None:
        Main.delta = time_() - time

    def event(self) -> None:
        for event in pygame.event.get():
            if event.type == QUIT: self._is_running=False
            elif event.type == KEYDOWN and self._key is None: self._key = event.key
            elif event.type == KEYUP and self._key == event.key: self._key = None; self._is_paused_key_up = True
            elif event.type == UI_BUTTON_PRESSED:
                self.button_pressed(event)
            self._display.process(event)
        
    def button_pressed(self, event: pygame.event) -> None:
        if self.is_okay_button_pressed("QUIT", "menu", event): self._is_running=False
        elif self.is_okay_button_pressed("QUIT", "pause", event): self._is_running=False
        elif self.is_okay_button_pressed("START", "menu", event): self._display.enable_scene("main")
        elif self.is_okay_button_pressed("SETTINGS", "menu", event): self._display.enable_scene("settings")
        elif self.is_okay_button_pressed("RESUME", "pause", event): self._display.enable_scene("main")

    def is_okay_button_pressed(self, button_name: str, scene_name: str, event: pygame.event) -> bool:
        button = self._display.search_button(button_name, scene_name)
        return button.process_event(event) and button.is_enabled

    def update(self):
        if (self._key == K_ESCAPE and self._is_paused_key_up):
            self._is_paused_key_up = False
            print(self._display.is_scene_enabled("main"))
            if self._display.is_scene_enabled("main"): 
                self._display.enable_scene("pause")
            elif self._display.is_scene_enabled("pause"): 
                self._display.enable_scene("main")
        self._key == None


m=Main()