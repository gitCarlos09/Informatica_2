#==>  EJERCICIO 1 
""" Dada una cantidad de segundos, realice un algoritmo que los convierta a unidades horas,minutos
mostrando en pantalla en formato "horas:minutos"  """

#Segundos=input("ingrese # de segundos:")
#Segundos=int(Segundos)
#horas=Segundos//3600
#sobrante1=Segundos%3600
#minutos=sobrante1//60
#sobrante2=sobrante1%60
#print(horas, minutos, sep=":")

segundos = 240
horas = segundos // 3600
minutos = (segundos % 3600) // 60
print(horas,":", minutos) 

#==>  EJERCICIO 2 
""" ¿Qué radio debe tener una esfera, para que su volumen sea el mismo al de un cubo de lado 5 cm? """

r = 5 * ((3/(4*3.141592)) ** (1/3))
print("radio => ", r)

#==>  EJERCICIO 4 
""" Realice un código, que permita la conversión de millas a km y km a millas """

millas = 2.5
km = millas * 1.609
print("millas : ", millas,"=====", "kilometros : ", km)

#==>  EJERCICIO 5 
""" Dadas las coordenadas P1(5,4,5) y P2(0,10,9).
Realice un codigo que determine la distancia entre ambos puntos """

x1, y1, z1 = 5,4,5
x2, y2, z2 = 0,10,9

distancia = ( (x1-x2)**2 + (y1-y2)**2 + (z1-z2) ** 2 ) ** (1/2)
print("distancia: ", distancia)

#==>  EJERCICIO 6 
""" La calificación de informatica se encuentra en el intervalo [0,5] y se calcula tomando 4 notas, 
con porcentajes de 15%, 25%, 20% y 40%. Si un estudiante tiene las primeras 3 calificaciones definidas.
Realice un algoritmo que calcule la nota necesaria de la última nota para pasar la materia. """

nota1 = 1 
nota2 = 2
nota3 = 2
nota4 = (3 -(nota1 * 0.15 + nota2 * 0.25 + nota3* 0.20)) /  0.4
print("nota 4 necesaria: ", nota4)

#==>  EJERCICIO 11 
""" Un auto acelera de manera uniforme 0.5 km/s², 
a) ¿cuantas horas deben pasar para alcanzar la velocidad de la luz?
b) ¿qué distancia se habrá recorrido? (suponga que es posible alcanzar la velocidad de la luz) """

a = 0.5 # km/s²
vi = 0
vf = 300000 #km/s

t = (vf - vi)/a
t_horas = t * (1/3600)
print("horas necesarias para igualar la velocidad luz", t_horas)
x = (1/2) * a * (t ** 2)
print("distancia recorrida por el auto: ", x)

#==>  EJERCICIO 12 
""" Un proyectil es lanzado verticalmente hacia arriba, calcule la velocidad inicial que debe tener para 
alcanzar una altura dada. """

h = 10 #m
g = 9.8 #m/s²
v = (2 * h * g) ** (1/2)
print("Velocidad necesaria: ", v, "m/s")

#==>  EJERCICIO 15 
""" Dos automoviles realizan una carrera. El primero de ellos acelera a razón constante de 3m/s², el segundo 
a razón de 5m/s². Si el segundo de ellos empieza su recorrido 10 segundos después que el primero ha empezado.
¿Cuanto tiempo habrá transcurrido cuando ambos se encuentran? """

#====================== EJERCICIOS OPERADORES ====================
#==> Ejercicio 1 
""" Realice las siguientes operaciones mentalmente. Intente determinar la respuesta, luego verifique en python
   1 + 3 - 5      "cristian" + "Unal"     [1,2,3] + [4,5,6]    True and False          5 > 3          1 in [1,2,3]
   13 / 2         "Unal" * 5              [1,2] * 4            1 and 2                 2 != 2            "A" in ("A", "B", "C")   
   19 // 6                                (1,2,3) + (4,5,6)    5 and True              3 == "3"          1 not in ["A", "B", "C"]    
   31 % 3                                 (1,2) * 4            False and 5             5 > True          "A" in {"A", "B", "C"} 
   2 ** 5                                                      [] and "resultado"      True < 0
   16 ** 0.5                                                   True and (2,3,4)        True != False
                                                               False or True           "abc" < "bcd"
                                                               0 or 5
                                                               True or 5
                                                               "resultado" or False
   """

#==> EJERCICIO 3 
""" De los operadores *, /, +. ¿Cual tiene mayor prioridad?
=> 3 / 2 * 5  compare con 3 * 2 / 5
=> 3 / 2 + 5  compare con 3 + 2 / 5
=> 3 * 2 + 5  compare con 3 + 2 * 5  """

#==> EJERCICIO 4 
""" De los operadores *, **. ¿Cual tiene mayor prioridad?
=> 3 * 2 ** 5  compare con 3 ** 2 * 5
=> 2 * 2 ** 3  compare con 2 ** 2 * 3
=> 2 ** 2 ** 3 ¿Qué sucede en este caso? """

#==> EJERCICIO 5 
""" De los operadores *, /, //, % ¿cual tiene mayor prioridad?:
=> 13 // 6 * 2 compare con 27 // 6 * 2
=> 13 / 6 // 2 compare con 13 // 6 / 2
=> 13 * 6 % 2 compare con 13 % 6 * 2 """

#==> EJERCICIO 6 
""" Realice las siguientes operaciones, y determine:
¿Cuál es el orden de prioridades de los operadores not, and, or?
=> not True and False
=> True and not False
=> True and False or False
=> True or False and False """

#==> EJERCICIO 7
""" Intente determinar mentalmente la salida de las siguientes operaciones
 1 and 2 and 3     1 or 2 or 3
 1 and 0 and 3     1 or 0 or 3
 0 and 2 and 3     0 or 1 or 2
 """


cadena = "hola mundo cruel"
print("mayusculas =>", cadena.upper())
print("capitalizar =>", cadena.capitalize())
print("capitalizar =>", cadena.title())
print("conteo =>", cadena.count("o"))
print("verificar =>", "12345".isdecimal())