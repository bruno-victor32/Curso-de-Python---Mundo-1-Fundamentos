#Faça um programa em Python que abra e reproduza o audio de um arquivo MP3

from pygame import mixer

mixer.init()
mixer.music.load('01. PAGODE RUSSO.mp3')
mixer.music.play()
input('Agora você escuta?')



