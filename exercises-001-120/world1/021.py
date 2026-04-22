import pygame

pygame.mixer.init()

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()

input("Press Enter to stop the music")
