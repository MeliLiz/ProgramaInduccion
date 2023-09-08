from matplotlib import pyplot
import random

n = 4
tam_tablero=2**n

tablero = [[0 for x in range(tam_tablero)] for y in range(tam_tablero)]

#Numeros random para elegir las coordenadas del cuadradito especial
a = random.randint(0, tam_tablero - 1)
b = random.randint(0, tam_tablero - 1)
tablero[a][b] = -1

num = 1





#x_esq y y_esq son las coordenada x de la esquina superior izquierda
#x_esp y y_esp son las coordenadas de cuadrado especial
#tam es el tamaño del cuadrado
def proceso(x_esq,y_esq,tam,x_esp, y_esp,num):
        #Caso base
        if(tam==2):
                pyplot.figure(figsize=(5,5))
                pyplot.imshow(tablero)
                pyplot.show()

                llena_ultimo(num, x_esq, y_esq)

                pyplot.figure(figsize=(5,5))
                pyplot.imshow(tablero)
                pyplot.show()

                return num+1
        else:   
                pyplot.figure(figsize=(5,5))
                pyplot.imshow(tablero)
                pyplot.show()
                mitad = tam // 2
                posicion = esta_cuadrado_especial(x_esq, y_esq, x_esp, y_esp, mitad)

                match (posicion):
                        case 1: #Cuadradito especial en el cuadrado sup. izquierdo
                                #Dibujar la L en el centro
                                tablero[mitad][mitad - 1] = num #Cuadradito en el cuadrado sup der
                                tablero[mitad - 1][mitad] = num #Cuadradito en el cuadrado inf izq
                                tablero[mitad][mitad] = num #Cuadradito en el cuadrado inf der

                                num += 1

                                #Llamadas a proceso con las coordenadas del cuadrito especial en el cuadrado sup izq
                                num_a= proceso(x_esq, y_esq, mitad, x_esp, y_esp, num)# proceso en el cuadrado sup izq
                                num_b = proceso(x_esq + mitad, y_esq, mitad, mitad , mitad - 1,num_a) #proceso en el cuadrado sup der
                                num_c = proceso(x_esq, y_esq + mitad, mitad, mitad - 1, mitad,num_b) #proceso en el cuadrado inferior izquierdo
                                proceso(x_esq + mitad, y_esq + mitad, mitad, mitad, mitad,num_c) #proceso en el cuadrado inferior derecho

                        case 2: #Cuadaradito especial en el cuadrado inferior izquierdo
                                #Dibujar la L en el centro
                                tablero[mitad - 1][mitad -1] = num #Cuadradito en el cuadrado sup izq
                                tablero[mitad][mitad - 1] = num #Cuadradito en el cuadrado sup der
                                tablero[mitad][mitad] = num #Cuadradito en el cuadrado inf der

                                num += 1

                                #Llamadas a proceso con las coordenadas del cuadrito especial en el cuadrado inferior izquierdo
                                num_a = proceso(x_esq, y_esq, mitad, mitad - 1, mitad - 1,num)# proceso en el cuadrado sup izq
                                num_b = proceso(x_esq + mitad, y_esq, mitad, mitad , mitad - 1,num_a) #proceso en el cuadrado sup der
                                num_c = proceso(x_esq, y_esq + mitad, mitad, x_esp, y_esp,num_b) #proceso en el cuadrado inferior izquierdo
                                proceso(x_esq + mitad, y_esq + mitad, mitad, mitad, mitad,num_c) #proceso en el cuadrado inferior derecho
                               
                        case 3: #Cuadradito especial en el cuadrado superior derecho
                                #Dibujar la L en el centro y hacer la recursion en todos los cuadros
                                tablero[mitad - 1][mitad - 1] = num #Cuadradito en el cuadrado sup izq
                                tablero[mitad - 1][mitad] = num #Cuadradito en el cuadrado inf izq
                                tablero[mitad][mitad] = num #Cuadradito en el cuadrado inf der

                                num += 1

                                #Llamadas a proceso con las coordenadas del cuadrito especial en el cuadrado superior derecho
                                num_a = proceso(x_esq, y_esq, mitad, mitad - 1, mitad - 1,num) # proceso en el cuadrado sup izq
                                num_b = proceso(x_esq + mitad, y_esq, mitad, x_esp , y_esp,num_a) #proceso en el cuadrado sup der
                                num_c = proceso(x_esq, y_esq + mitad, mitad, mitad-1, mitad,num_b) #proceso en el cuadrado inferior izquierdo
                                proceso(x_esq + mitad, y_esq + mitad, mitad, mitad, mitad,num_c) #proceso en el cuadrado inferior derecho

                        case 4: #Cuadradito en el cuadrado inferior derecho
                                tablero[mitad][mitad - 1] = num #Cuadradito en el cuadrado sup der
                                tablero[mitad - 1][mitad] = num #Cuadradito en el cuadrado inf izq
                                tablero[mitad - 1][mitad - 1] = num #Cuadradito en el cuadrado sup izq

                                num += 1

                                #Llamadas a proceso con las coordenadas del cuadrito especial en el cuadrado inferior derecho
                                num_a = proceso(x_esq, y_esq, mitad, mitad - 1, mitad - 1,num) # proceso en el cuadrado sup izq
                                num_b = proceso(x_esq + mitad, y_esq, mitad, mitad , mitad - 1,num_a) #proceso en el cuadrado sup der
                                num_c = proceso(x_esq, y_esq + mitad, mitad, mitad-1, mitad,num_b) #proceso en el cuadrado inferior izquierdo
                                proceso(x_esq + mitad, y_esq + mitad, mitad, x_esp, y_esp,num_c) #proceso en el cuadrado inferior derecho
                        
        


#Funcion para saber donde esta el cuadrado especial
def esta_cuadrado_especial(x_esq, y_esq, x_esp, y_esp, mitad):
        if (x_esp <=x_esq + mitad - 1):
                if (y_esp <= y_esq + mitad -1):
                        return 1 #Esta en el cuadrado sup izq
                else:
                        return 2 #Esta en el cuadrado inferior izq
        else:
                if(y_esp <= y_esq + mitad -1):
                        return 3 #Esta en el cuadrado superior derecho
                else:
                        return 4 #Esta en el cuadrado inferior derecho
                
def llena_ultimo(num, x,y):
        if(tablero[x][y]==0):
                tablero[x][y]=num
        if(tablero[x+1][y]==0):
                tablero[x+1][y]=num
        if(tablero[x][y+1]==0):
                tablero[x][y+1]=num
        if(tablero[x+1][y+1]==0):
                tablero[x+1][y+1]=num


proceso(0,0,tam_tablero,a,b,num)