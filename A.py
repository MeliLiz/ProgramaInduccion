from matplotlib import pyplot
import random
import sys

if len(sys.argv)<2 :
        print("Modo de uso: python3 A.py <Numero n para hacer el tablero de 2^n>")
        sys.exit(0)

r=sys.argv[1]

try:
        n=int(r)
except:
        print ("El argumento proporcionado debe ser un entero")
        sys.exit(0)


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

                return num + 1
        else:   
                pyplot.figure(figsize=(5,5))
                pyplot.imshow(tablero)
                pyplot.show()
                mitad = tam // 2
                posicion = esta_cuadrado_especial(x_esq, y_esq, x_esp, y_esp, mitad)

                if(posicion == 1): #Cuadradito especial en el cuadrado sup. izquierdo

                        #Dibujar la L en el centro
                        tablero[x_esq + mitad][y_esq+mitad - 1] = num #Cuadradito en el cuadrado sup der
                        tablero[x_esq + mitad - 1][y_esq + mitad] = num #Cuadradito en el cuadrado inf izq
                        tablero[x_esq+mitad][y_esq +mitad] = num #Cuadradito en el cuadrado inf der


                        num+=1

                        #Llamadas a proceso con las coordenadas del cuadrito especial en el cuadrado sup izq
                        num_a= proceso(x_esq, y_esq, mitad, x_esp, y_esp, num)# proceso en el cuadrado sup izq
                        #print(a)
                        num_b = proceso(x_esq + mitad, y_esq, mitad, x_esq+mitad , y_esq+mitad - 1,num_a) #proceso en el cuadrado sup der
                        num_c = proceso(x_esq, y_esq + mitad, mitad, x_esq+mitad - 1, y_esq+mitad,num_b) #proceso en el cuadrado inferior izquierdo
                        num_d = proceso(x_esq + mitad, y_esq + mitad, mitad, x_esq+mitad, y_esq+mitad,num_c) #proceso en el cuadrado inferior derecho
                        return num_d

                elif(posicion==2): #Cuadaradito especial en el cuadrado inferior izquierdo
                                
                        #Dibujar la L en el centro
                        tablero[x_esq + mitad - 1][y_esq+mitad -1] = num #Cuadradito en el cuadrado sup izq
                        tablero[x_esq+mitad][y_esq+mitad - 1] = num #Cuadradito en el cuadrado sup der
                        tablero[x_esq+mitad][y_esq+mitad] = num #Cuadradito en el cuadrado inf der

                        num+=1

                        #Llamadas a proceso con las coordenadas del cuadrito especial en el cuadrado inferior izquierdo
                        num_a = proceso(x_esq, y_esq, mitad, x_esq+mitad - 1, y_esq+mitad - 1,num)# proceso en el cuadrado sup izq
                        num_b = proceso(x_esq + mitad, y_esq, mitad, x_esq+mitad , y_esq+mitad - 1,num_a) #proceso en el cuadrado sup der
                        num_c = proceso(x_esq, y_esq + mitad, mitad, x_esp, y_esp,num_b) #proceso en el cuadrado inferior izquierdo
                        num_d = proceso(x_esq + mitad, y_esq + mitad, mitad, x_esq+mitad, y_esq+mitad,num_c) #proceso en el cuadrado inferior derecho
                        return num_d

                elif(posicion==3): #Cuadradito especial en el cuadrado superior derecho
                                
                        #Dibujar la L en el centro y hacer la recursion en todos los cuadros
                        tablero[x_esq+mitad - 1][y_esq +mitad - 1] = num #Cuadradito en el cuadrado sup izq
                        tablero[x_esq+mitad - 1][y_esq + mitad] = num #Cuadradito en el cuadrado inf izq
                        tablero[x_esq + mitad][y_esq + mitad] = num #Cuadradito en el cuadrado inf der

                        num+=1

                        #Llamadas a proceso con las coordenadas del cuadrito especial en el cuadrado superior derecho
                        num_a = proceso(x_esq, y_esq, mitad, x_esq+mitad - 1, y_esq+mitad - 1,num) # proceso en el cuadrado sup izq
                        num_b = proceso(x_esq + mitad, y_esq, mitad, x_esp , y_esp,num_a) #proceso en el cuadrado sup der
                        num_c = proceso(x_esq, y_esq + mitad, mitad, x_esq+mitad-1, y_esq+mitad,num_b) #proceso en el cuadrado inferior izquierdo
                        num_d = proceso(x_esq + mitad, y_esq + mitad, mitad, x_esq+mitad, y_esq+mitad,num_c) #proceso en el cuadrado inferior derecho
                        return num_d

                elif(posicion==4): #Cuadradito en el cuadrado inferior derecho
                        tablero[x_esq+mitad][y_esq+mitad - 1] = num #Cuadradito en el cuadrado sup der
                        tablero[x_esq+mitad - 1][y_esq+mitad] = num #Cuadradito en el cuadrado inf izq
                        tablero[x_esq+mitad - 1][y_esq + mitad - 1] = num #Cuadradito en el cuadrado sup izq

                        num+=1

                        #Llamadas a proceso con las coordenadas del cuadrito especial en el cuadrado inferior derecho
                        num_a = proceso(x_esq, y_esq, mitad, x_esq+mitad - 1, y_esq+mitad - 1,num) # proceso en el cuadrado sup izq
                        num_b = proceso(x_esq + mitad, y_esq, mitad, x_esq+mitad , y_esq+mitad - 1,num_a) #proceso en el cuadrado sup der
                        num_c = proceso(x_esq, y_esq + mitad, mitad, x_esq+mitad-1, y_esq+mitad,num_b) #proceso en el cuadrado inferior izquierdo
                        num_d = proceso(x_esq + mitad, y_esq + mitad, mitad, x_esp, y_esp,num_c) #proceso en el cuadrado inferior derecho
                        return num_d
                else:
                        print("Este caso no deberia ser posible")
                        
        


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

pyplot.figure(figsize=(5,5))
pyplot.imshow(tablero)
pyplot.show()