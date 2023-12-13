import pygame
import sys
from pygame.locals import *
import random

WIDTH = 800
HEIGHT = 600
FPS = 60
SIZE_SCREEN = (WIDTH, HEIGHT)
GRAVITY =1
CENTER_SCREEN = (WIDTH//2,HEIGHT//2)
WIDTH_PLAYER = 50
HEIGHT_PLAYER = 50

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


fondo = pygame.transform.scale(pygame.image.load(r"Clase23 Video copy 2\assets\images\fondo-antiguo-pueblo-medieval_1639-40118.jpg"),(WIDTH,HEIGHT))
imagen_parlante = pygame.image.load(r"Parcial Entrega\Imagenes\parlantito-removebg-preview.png")
imagen_parlante_reescalada = pygame.transform.scale(imagen_parlante, (70, 70))
imagen_dragon_fondo = pygame.transform.scale(pygame.image.load(r"Clase23 Video copy 2\assets\images\dragon verde.jpg"),(WIDTH,HEIGHT))
imagen_platform = pygame.image.load(r"Clase23 Video copy 2\assets\images\2dplatform.png")
imagen_instrucciones = pygame.transform.scale(pygame.image.load(r"Clase23 Video copy 2\assets\images\instrucciones (1).jpg"),(WIDTH,HEIGHT))
imagen_muerte = pygame.transform.scale(pygame.image.load(r"Clase23 Video copy 2\assets\images\dragon.png"),(WIDTH,HEIGHT))
imagen_victory = pygame.transform.scale(pygame.image.load(r"Clase23 Video copy 2\assets\images\dragon victory.jpg"),(WIDTH,HEIGHT))

def terminar():
    """Termina el programa

    Args:
        None

    Returns:
        None
    """
    pygame.quit()  # desconectar pygame
    sys.exit()  # terminar el proceso

def mostrar_texto(superficie,texto,fuente,coordenadas,color_fuente,color_fondo=BLACK):
    """Mustra un texto a mostrar en la pantalla de mi juego

    Args:
        superficie: donde
        texto: texto a mostrar
        fuente : tipo de letra
        coordenas : lugar en pantalla
        color_fuente : color de las letras
        color_fondo : color del fondo del texto

    Returns:
        None
    """
    sup_texto = fuente.render(texto,True,color_fuente,color_fondo)
    rect_texto = sup_texto.get_rect()
    rect_texto.center = coordenadas
    superficie.blit(sup_texto,rect_texto)

def wait_user():
    """Espera a que se presione una tecla para continuar el programa

    Args:
        None

    Returns:
        None
    """
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # desconectar pygame
                sys.exit()  # terminar el proceso

            if event.type == KEYDOWN: #evento presionar tecla
                if event.key == K_ESCAPE:
                    terminar()  

                return
            
def color_random(lista_colores):
    """Selecciona un color random de mi lista de colores

    Args:
        lista_colores = lista con mis colores

    Returns:
        None
    """
    from random import randrange
    
    return lista_colores[randrange(len(lista_colores))]

def color_aleatorio():
    """Crear un color aleatorio en base a r,g,b

    Args:
        None

    Returns:
        None
    """
    from random import randrange
    r = randrange(256)
    g = randrange(256)
    b = randrange(256)
    
    return (r, g, b)

def crear_bloque(imagen = None,left=0,top=0,ancho=100,alto=100,color = (255,255,255), dir = 3,
borde = 0, radio = -1, speed_x = 5 , speed_y = 5):
    """Crea un bloque en base a mis especificaciones

    Args:
        imagen = imagen que se le bliteara al bloque
        left = donde aparece en x
        top = donde aparece en y
        ancho = ancho del bloque
        alto = alto del bloque
        color = color si no le asigno imagen
        dir = direccion en la que aparece
        borde = grosor del borde de mi bloque
        randio = circunferencia del bloque
        speed_x = velocidad a la que se movera el bloque en el eje x
        speed_y = velocidad a la que se movera el bloque en el eje y

    Returns:
        None
    """

    rec = pygame.Rect(left,top,ancho,alto)

    if imagen:
        imagen = pygame.transform.scale(imagen,(ancho,alto))

    return {"rect": rec,"color": color,"dir": dir ,"borde": borde, "radio" : radio,"speed_x":speed_x,"speed_y": speed_y, "img" : imagen}


def mostrar_texto_boton(superficie,texto,x,y,font_size=36,color=BLACK):
    """muestra el texto que contendra el boton

    Args:
        superficie : donde (pantalla)
        texto : texto literal que contendra el boton
        x : coordena en x
        y : coordena en y
        font_size : tamaño de la fuente
        color : color de la fuente
    """
    fuente = pygame.font.SysFont("comicsans",font_size)
    render = fuente.render(texto,True,color)
    rectangulo_texto = render.get_rect(center=(x,y))
    superficie.blit(render,rectangulo_texto)

def crear_boton(screen,rect,texto,color_normal,color_hover):
    """Crea un boton en pantalla

    Args:
        screen : pantalla donde lo quuiero crear
        rect : rectangulo del boton
        texto : texto que contendra
        color_normal : color que se muestra en pantalla
        color_hover : color que se muestra si el cursor esta encima de el
    """
    cursor_mouse = pygame.mouse.get_pos()
    
    if rect.collidepoint(cursor_mouse):
        pygame.draw.rect(screen,color_hover,rect,border_radius=10)
    else:
        pygame.draw.rect(screen,color_normal,rect,border_radius=10) # pygame.draw.rect(donde? ,color ? ,rect ,[borde])
    mostrar_texto_boton(screen,texto,rect.centerx,rect.centery)