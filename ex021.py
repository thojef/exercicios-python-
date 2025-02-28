# Exercício Python 21: Faça um programa em Python que abra e 
# reproduza o áudio de um arquivo MP3.

import pygame

pygame.init()

arquivo = r'C:\Users\T\Music\among us imposter sound effect.mp3'
pygame.mixer.music.load(arquivo)

pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue

