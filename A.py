from matplotlib import pyplot
import random

n = 3
tam_tablero=2**n

tablero = [[0 for x in range(tam_tablero)] for y in range(tam_tablero)]
tablero[0][0] = -1

num=0


pyplot.figure(figsize=(5,5))
pyplot.imshow(tablero)
pyplot.show()

#x_esq y y_esq son las coordenada x de la esquina superior izquierda
#x_esp y y_esp son las coordenadas de cuadrado especial
#tam es el tamaño del cuadrado
def proceso(x_esq,y_esq,tam,x_esp, y_esp)
        #Caso base
        if(tam==2):
                return
        else:   
                mitad = tam // 2
                posicion = esta_cuadrado_especial(x_esq, y_esq, x_esp, y_esp, mitad)
                match (posicion):
                        case 1: 
                                #Dibujar la l en el centro y hacer la recursion en todos los cuadros
                        case 2:
                        case 2:
                        case 4:
                        case _:
                        




                

                proceso(x,y,mitad)
                proceso(x+mitad, y, mitad)
                proceso(x,y+mitad, mitad)
                proceso(x+mitad, y+mitad, mitad)

#Funcion para saber donde esta el cuadrado especial
def esta_cuadrado_especial(x_esq, y_esq, x_esp, y_esp, mitad)
        if (x_esp <=x_esq+mitad):
                if (y_esp <= y_esq+mitad):
                        return 1 #Esta en el cuadrado sup izq
                else:
                        return 2 #Esta en el cuadrado inferior izq
        else:
                if(y_esp <= y_esq + mitad):
                        return 3 #Esta en el cuadrado superior derecho
                else:
                        return 4 #Esta en el cuadrado inferior derecho


"""data = [[random.randint(a=2,b=3) for x in range(0,8)], # hilera 1
        [random.randint(a=4,b=5) for x in range(0,8)], # hilera 2
        [random.randint(a=6,b=7) for x in range(0,8)], # hilera 3
        [random.randint(a=0,b=1) for x in range(0,8)], # hilera 4
        [random.randint(a=0,b=1) for x in range(0,8)], # hilera 5
        [random.randint(a=0,b=1) for x in range(0,8)], # hilera 6
        [random.randint(a=5,b=9) for x in range(0,8)], # hilera 7
        [random.randint(a=0,b=1) for x in range(0,8)]] # hilera 8
# mostrar la matriz de datos 2d

pyplot.figure(figsize=(5,5))
pyplot.imshow(data)
pyplot.show()"""