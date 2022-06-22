__author__ = 'FACON Nicolas'
__version__ = '1.0.0'
__date__ = '2022-06-20'

import pygame
from pygame.locals import *
from pygame_gui._constants import *
from Display import Display

UI_BUTTON_PRESSED = 1025 # pygame_gui.UI_BUTTON_PRESSED doesn't work anymore, so I gave it a value

class Main():

    clock = pygame.time.Clock()
    
    def __init__(self) -> None:
        Main.clock.tick(60)
        self._display = Display(1600, 900)
        self._is_running = True
        self.run()

    def run(self):
        while self._is_running:
            self.event()
            self._display.show(pygame.image.load('resources/wallpaper.jpg').convert(), (0,0))
            self._display.update_menu()
            pygame.display.flip()

    def event(self):
        for event in pygame.event.get():
            if event.type == QUIT: self._is_running=False
            elif event.type == UI_BUTTON_PRESSED:
                self.button_pressed(event)
            self._display.process_menu(event)
        
    def button_pressed(self, event) -> None:
        if self._display.search_button("QUIT", "menu").process_event(event) and self._display.search_button("QUIT", "menu").is_enabled: self._is_running=False
        elif self._display.search_button("START", "menu").process_event(event) and self._display.search_button("START", "menu").is_enabled: self._display.disable_scene("menu")

m=Main()