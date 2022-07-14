import pygame


class Audio:

    def __init__(self, fx_volume: float) -> None:
        pygame.mixer.init()
        self._fx_volume = fx_volume

    def play_sound(self, sound_searched: str) -> None:
        path = self.__get_sound(sound_searched)
        sound = pygame.mixer.Sound(path)
        sound.set_volume(self._fx_volume)
        sound.play()

    def __get_sound(self, sound_searched: str) -> str:
        return "resources/"+sound_searched+".mp3" 

    def update(self, fx_volume):
        self._fx_volume = fx_volume
