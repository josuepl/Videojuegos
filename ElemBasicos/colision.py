# Importar e inicializar Pygame.
import pygame

pygame.init()
tamPantalla = (400,300)#tupla
# Crear la ventana y poner el tamaño.
screen = pygame.display.set_mode(tamPantalla)
# Poner el título de la ventana.
pygame.display.set_caption("COLISION")

# Crear la superficie del fondo o background.
imgBackground = pygame.Surface(screen.get_size())
imgBackground = imgBackground.convert()
imgBackground.fill((0, 0, 0)) #rgb RED - GREEN - BLUE
# Inicializar las variables de control del game loop. 
clock = pygame.time.Clock()

salir = False
# Loop principal (game loop) del juego.
pos =[ 200, 150] #lista
velocidad=[-1,-2] #incremento en pixeles posicion
screen.blit(imgBackground, (0, 0))
while not salir:

    # Timer que controla el frame rate.
    clock.tick(30)

    # Procesar los eventos que llegan a la aplicación.
    for event in pygame.event.get():
        # Si se cierra la ventana se sale del programa.
        if event.type == pygame.QUIT:
           salir = True

        # Si se pulsa la tecla [Esc] se sale del programa.
        if event.type == pygame.KEYUP:
           if event.key == pygame.K_ESCAPE:
               salir = True

   # Actualizar la pantalla.
   
    screen.blit(imgBackground, (0, 0))
    pygame.draw.circle(screen, (0,255,0), pos, 20, 0)
    pygame.draw.circle(screen, (255, 0, 0), (150, 30),20, 0)
    pygame.draw.rect(screen,(255,255,255),((130,10),(40,40)),1)
    pos[1] = pos[1] + velocidad[1]
    pos[0] = pos[0] + velocidad[0]
    #print(pos)
    '''Validar las posiciones o limites de la pantalla y el objeto
    Limite de los laterales
    '''
    #pos[0] valor en X
    if(pos[0] < 20):
        velocidad[0] *= -1 
    if(pos[0]> tamPantalla[0] - 20):
        velocidad[0] *=  -1
    #Limites Superior Inferior
    #pos[1] valor en Y
    if(pos[1] < 20):
        velocidad[1] *= -1
    if(pos[1] > tamPantalla[1] - 20):
        velocidad[1] *= -1
    if (pos[0] + 20> 130 and pos[0]-20<170):
        if (pos[1] - 20 < 50):
            print("Has colisionado")
            print(pos)
            if(pos[0] -20 > 130):
                velocidad[0]*=-1
            velocidad[1]*=-1
   #pygame.draw.rect(screen, (255, 0, 0),[20|, 40], 0)
    pygame.display.flip()
# Cerrar Pygame y liberar los recursos que pidió el programa. pygame.quit()