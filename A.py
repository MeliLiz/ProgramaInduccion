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
                                #Dibujar la L en el centro y hacer la recursion en todos los cuadros
                                tablero[mitad + 1][mitad] = num #Cuadradito en el cuadrado sup der
                                tablero[mitad][mitad + 1] = num #Cuadradito en el cuadrado inf izq
                                tablero[mitad + 1][mitad + 1] = num #Cuadradito en el cuadrado inf der
                                num += 1
                                proceso(x_esq, y_esq, mitad, x_esp, y_esp)# proceso en el cuadrado sup izq
                                proceso(x_esq + mitad, y_esq, mitad, mitad + 1 , mitad) #proceso en el cuadrado sup der
                                proceso(x_esq, y_esq + mitad, mitad, mitad, mitad+1) #procceso en el cuadrado inferior izquierdo
                                proceso(x_esq + mitad, y_esq + mitad, mitad, mitad + 1, mitad + 1) #proceso en el cuadrado inferior derecho
                        case 2:
                                #Dibujar la L en el centro y hacer la recursion en todos los cuadros
                                tablero[mitad][mitad] = num #Cuadradito en el cuadrado sup izq
                                tablero[mitad+1][mitad] = num #Cuadradito en el cuadrado sup der
                                tablero[mitad + 1][mitad + 1] = num #Cuadradito en el cuadrado inf der
                                num += 1
                               
                        case 3:
                                #Dibujar la L en el centro y hacer la recursion en todos los cuadros
                                tablero[mitad][mitad] = num #Cuadradito en el cuadrado sup izq
                                tablero[mitad][mitad+1] = num #Cuadradito en el cuadrado inf izq
                                tablero[mitad + 1][mitad + 1] = num #Cuadradito en el cuadrado inf der
                                num += 1
                        case 4:
                                tablero[mitad + 1][mitad] = num #Cuadradito en el cuadrado sup der
                                tablero[mitad][mitad + 1] = num #Cuadradito en el cuadrado inf izq
                                tablero[mitad][mitad] = num #Cuadradito en el cuadrado sup izq
                                num += 1
                        
                proceso(x_esq, y_esq, mitad, x_esp, y_esp)# proceso en el cuadrado sup izq
                proceso(x_esq + mitad, y_esq, mitad, mitad + 1 , mitad) #proceso en el cuadrado sup der
                proceso(x_esq, y_esq + mitad, mitad, mitad, mitad+1) #proceso en el cuadrado inferior izquierdo
                proceso(x_esq + mitad, y_esq + mitad, mitad, mitad + 1, mitad + 1) #proceso en el cuadrado inferior derecho
        


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
