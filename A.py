from matplotlib import pyplot
# a continuación, estableceré una matriz 2d de 8 x 8, con bits aleatorios como elementos (0 o 1);
# para la aleatorización de enteros (0 o 1) utilizo el módulo aleatorio en Python;
# para construir cada fila en la matriz 2d, uso la comprensión de listas en Python
import random
data = [[random.randint(a=0,b=1) for x in range(0,8)], # hilera 1
        [random.randint(a=0,b=1) for x in range(0,8)], # hilera 2
        [random.randint(a=0,b=1) for x in range(0,8)], # hilera 3
        [random.randint(a=0,b=1) for x in range(0,8)], # hilera 4
        [random.randint(a=0,b=1) for x in range(0,8)], # hilera 5
        [random.randint(a=0,b=1) for x in range(0,8)], # hilera 6
        [random.randint(a=0,b=1) for x in range(0,8)], # hilera 7
        [random.randint(a=0,b=1) for x in range(0,8)]] # hilera 8
# mostrar la matriz de datos 2d

pyplot.figure(figsize=(5,5))
pyplot.imshow(data)
pyplot.show()