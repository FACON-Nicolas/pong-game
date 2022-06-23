__author__ = 'FACON Nicolas'
__version__ = '1.0.0'
__date__ = '2022-06-20'

from time import time
import pygame
from pygame.locals import *
from pygame_gui._constants import *
from Display import Display
from AbstractPlayer import AbstractPlayer

UI_BUTTON_PRESSED = 1025 # pygame_gui.UI_BUTTON_PRESSED doesn't work anymore, so I gave it a value
delta = 0

class Main():

    clock = pygame.time.Clock()
    delta = 0
    
    def __init__(self) -> None:
        self._display = Display(1600, 900)
        self._is_running = True
        self.run()

    def run(self):
        while self._is_running:
            t = time()
            self.event()
            self._display.update_menu()
            pygame.display.flip()
            Main.delta = time() - t

    def event(self):
        for event in pygame.event.get():
            if event.type == QUIT: self._is_running=False
            elif event.type == UI_BUTTON_PRESSED:
                self.button_pressed(event)
            self._display.process_menu(event)
        
    def button_pressed(self, event) -> None:
        if self.is_okay_button_pressed("QUIT", "menu", event): self._is_running=False
        elif self.is_okay_button_pressed("START", "menu", event): self._display.disable_scene("menu")
        elif self.is_okay_button_pressed("SETTINGS", "menu", event): self._display.enable_scene("settings")

    def is_okay_button_pressed(self, button_name: str, scene_name: str, event: pygame.event):
        button = self._display.search_button(button_name, scene_name)
        return button.process_event(event) and button.is_enabled

m=Main()