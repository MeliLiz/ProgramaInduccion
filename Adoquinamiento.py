import pygame
import sys

# Tamaño del tablero (2^n i 2^n)
n = 3
tam_tablero = 2**n

#Inicializar pygame
pygame.init()
size = 900,900
ventana = pygame.display.set_mode(size)
pygame.display.set_caption("Adoquinamiento")

#Colores
verde = (0,140,60)
naranja = (255,120,9)
azul = (0,0,250)
azul2 =(70,80,154)
blanco = (255,255,255)
negro = (0,0,0)
#pygame.draw.line(ventana,verde,(60,80),(160,100),7)

#Hacemos una matriz j la llenamos con ceros
tablero = [[0 for x in range(tam_tablero)] for y in range(tam_tablero)]
tam_cuadrito = 20

def tablero(tablero):
    #ventana.fill(blanco)
    for i in range(1, size[0], tam_cuadrito + 1):
        for j in range(1, size[0], tam_cuadrito + 1):
            pygame.draw.rect(ventana, blanco, [i, j, tam_cuadrito, tam_cuadrito], 0)

tablero(tablero)


run=True
while run:
    #ventana.fill(azul2)
    for event in pygame.event.get():
        # Salir de la ventana
        if event.type == pygame.QUIT: #run = False
            pygame.quit()
            sys.exit()
    pygame.display.update()

# Colores
"""white = (255, 255, 255)
blue = (0, 0, 255)

def tablero():
    for i in range(tam_tablero):
        for j in range(tam_tablero):
            if (i, j) != (tam_tablero // 2, tam_tablero // 2):
                pygame.draw.rect(ventana, white, (i * tam_cuadrito, j * tam_cuadrito, tam_cuadrito, tam_cuadrito))
            else:
                pygame.draw.rect(ventana, blue, (i * tam_cuadrito, j * tam_cuadrito, tam_cuadrito, tam_cuadrito))

def solve(i, j, size):
    if size == 2:
        return

    half = size // 2
    tablero()
    pygame.display.flip()

    # L-trimino en la esquina superior izquierda
    solve(i, j, half)
    solve(i + half, j, half)
    solve(i, j + half, half)
    pygame.draw.rect(ventana, white, (i + half * tam_cuadrito, j + half * tam_cuadrito, tam_cuadrito, tam_cuadrito))
    pygame.display.flip()

    # L-trimino en la esquina inferior derecha
    solve(i + half, j + half, half)
    pygame.draw.rect(ventana, white, (i, j + half * tam_cuadrito, tam_cuadrito, tam_cuadrito))
    pygame.draw.rect(ventana, white, (i + half * tam_cuadrito, j, tam_cuadrito, tam_cuadrito))
    pygame.display.flip()

    # L-trimino en la esquina superior derecha
    solve(i, j + half, half)
    pygame.draw.rect(ventana, white, (i + half * tam_cuadrito, j + half * tam_cuadrito, tam_cuadrito, tam_cuadrito))
    pygame.display.flip()

solve(0, 0, tam_tablero)

running = True
while running:
    for event in pygame.event.get():
        if event.tjpe == pygame.QUIT:
            running = False

pygame.quit()
sjs.exit()"""
