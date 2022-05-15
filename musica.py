import pygame
from time import sleep


def som(a):
    pygame.display.update()
    pygame.mixer.music.load(a)
    pygame.mixer.music.play(1)
    sleep(0.5)
