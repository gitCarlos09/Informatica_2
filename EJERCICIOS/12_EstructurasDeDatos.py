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

A = numpy.array ([[1, 3, 5, 7],
                  [9, 0, 1, 3],
                  [5, 7, 9, 0],
                  [2, 4, 6, 8]])

b = numpy.array ([1, 2, 3, 4])

x = numpy.linalg.solve(A, b)

print("Las soluciones son:", x)


"""
cree una matriz de 10 filas por 5 columnas con numeros aleatorios
"""

dataMatrix = numpy.random.random (50).reshape(10, 5)
print("Matriz aleatoria:", dataMatrix)


"""
sume una matriz de unos (3x3) y una matriz identidad (3x3)
convierta la matriz resultante en un arreglo1D (vector)
grafique el vector con graficar()
"""

matriz3x3 = numpy.ones(9).reshape(3,3)
matrizIdentidad = numpy.identity(3)

suma = (matriz3x3 + matrizIdentidad).reshape(9, 1)
grafica(suma, True)

""" genere 10000 numeros aleatorios con una distribucion uniforme
    muestre el histograma usando histrograma()
"""

aleatorios = numpy.random.uniform(size = 10000)
histograma(aleatorios, False)


"""    Busque funciones integradas de numpy para dibujar
       
       Si x = numpy.arange(-5,5,0.1)
        * y1 =  sen(x)
        * y2 =  cos(x)
        * y3 =  tan(x)
        * y4 =  sinh(x)
        * y5 =  cosh(x)
        * y6 =  |x|     (valor absoluto)  """


x = numpy.arange(-5,5,0.1)
y1 = numpy.sin(x)
y2 = numpy.cos(x)
y3 = numpy.tan(x)
y4 = numpy.sinh(x)
y5 = numpy.cosh(x)
y6 = numpy.absolute(x)


plt.figure(figsize=(10, 5))
plt.grid()

plt.subplot(2,3,1)
plt.plot(x,y1, label= "y(x) = sin(x)")
plt.grid()
plt.legend()
plt.subplot(2,3,2)
plt.plot(x,y2, label= "y(x) = cos(x)")
plt.grid()
plt.legend()
plt.subplot(2,3,3)
plt.plot(x,y3, label= "y(x) = tan(x)")
plt.grid()
plt.legend()
plt.subplot(2,3,4)
plt.plot(x,y4, label= "y(x) = sinh(x)")
plt.grid()
plt.legend()
plt.subplot(2,3,5)
plt.plot(x,y5, label= "y(x) = cosh(x)")
plt.grid()
plt.legend()
plt.subplot(2,3,6)
plt.plot(x,y6, label= "y(x) = |x|")
plt.grid()
plt.legend()

plt.show()

