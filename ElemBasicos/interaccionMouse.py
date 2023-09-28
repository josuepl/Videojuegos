import pygame
from pygame.locals import *
import sys
 
pygame.init()
display = pygame.display.set_mode((300, 300))
relojFPS = pygame.time.Clock()
 
cont =0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Boton pulsado ",pygame.mouse.get_pressed())
    btnIzq, btnMed, btnDer = pygame.mouse.get_pressed()
    if btnIzq:
        print("Se ha presionado el boton izquierdo: ",cont)
        cont += 1
    elif btnMed:
        print("Se ha presionado el boton central: ",cont)
        cont += 1
    elif btnDer:
        print("Se ha presionado el boton derecho: ",cont)
        cont += 1
    pygame.display.update()
    relojFPS.tick(10)