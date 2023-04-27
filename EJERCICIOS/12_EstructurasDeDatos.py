import numpy
import pandas
import matplotlib.pyplot as plt

def grafica (y, encendido):
    plt.figure()
    x = range(len(y))
    plt.plot (x, y)
    if encendido == True:
        plt.show()
    else:
        plt.close()

def histograma (data, encendido):
    plt.figure()
    plt.hist(data)
    if encendido == True:
        plt.show()
    else:
        plt.close()
"""
arreglo1D = numpy.array([3, 5, 7, 2])

arreglo2D = numpy.array ([[1, 2, 3],
                         [4, 5 ,6],
                         [7, 8, 9]])

array1D = numpy.arange(10, 15, 0.5)
array2D = array1D.reshape((2, 5))

print(array1D)
print(array2D)

aleatorios1D = numpy.random.random(50)
aleatorios2D = aleatorios1D.reshape((5, 10))

print("aleatorio 1D", aleatorios1D)
print("aleatorio 2D", aleatorios2D)

grafica(array1D, False)
grafica(aleatorios1D, False)

# Generar numeros aleatorios 
# Para las distribuciones normal, exponencial, logistica
# Dibujarlas en un histograma

dataNormal1D = numpy.random.normal(size=5000)
histograma(dataNormal1D, True)

dataExponencial1D = numpy.random.exponential(size = 5000)
histograma(dataExponencial1D, False)
dataLogistica1D = numpy.random.logistic(size=5000)
histograma(dataLogistica1D, False)

# arreglos de zeros, o unos
arrayCeros1D = numpy.zeros(50)  #50 datos
arrayUnos1D  = numpy.ones(50)   #50 datos

grafica(arrayCeros1D, False)
grafica(arrayUnos1D, False)
"""
"""crear una matriz cuadrada y el vector
    |1,3,5,7|      |1|
A = |9,0,1,3|    b=|2|
    |5,7,9,0|      |3|
    |2,4,6,8|      |4|
resuelva la ecuacion Ax = b
Utilizando la funcion numpy.linalg.solve()
"""
"""
A = numpy.array ([[1, 3, 5, 7],
                  [9, 0, 1, 3],
                  [5, 7, 9, 0],
                  [2, 4, 6, 8]])

b = numpy.array ([1, 2, 3, 4])

ecuacion = numpy.linalg.solve((A), (b))
print("Las soluciones son:", ecuacion)
grafica(ecuacion, True)
"""
"""
cree una matriz de 10 filas por 5 columnas con numeros aleatorios
"""

dataMatrix = numpy.random.random (size = 5)

print(dataMatrix)


"""
sume una matriz de unos (3x3) y una matriz identidad (3x3)
convierta la matriz resultante en un arreglo1D (vector)
grafique el vector con graficar()
"""




