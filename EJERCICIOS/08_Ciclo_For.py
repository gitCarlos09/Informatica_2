#=============== EJERCICIOS CICLO FOR===================

#==> EJERCICIO 1
""" Realice los siguientes programas:
      a) Programa que calcule los primeros 100 terminos de la serie de fibonacci
      b) Programa que determine todos los divisores de un numero n
      c) Programa que determine si un número n es primo
      d) Programa que sume los digitos de un numero cualquiera. Ejemplo: numero=> 8791, rta=> 25 
      e) Programa que sume los digitos pares de un numero cualquiera """
"""

print("\n----- EJERCICIO 1 -----")

# --- A ---
print("--- A ---")
fib1, fib2 = 1, 1
print(fib1, fib2, sep = "-", end="-")
for turno in range(98):
      fib1, fib2 = fib2, fib1 + fib2
      print(fib2, end = "-")

# --- B ---
print("--- B ---")
n = int(input("Ingrese un número entero positivo: "))

for divisor in range(1, n+1):
      residuo = n % divisor
      if residuo == 0:
            print(divisor,end= "-")

# --- C ---
print("--- C ---")
numero = int(input("Ingrese un número entero positivo: "))

for divisor in range(2, numero-1):
    residuo = numero % divisor
    if residuo == 0:
          print("\n", numero, "==> No es un numero primo")
          break   # rompe el ciclo for cuando sea primo
else:
      print("\n", numero, "==> Es un numero primo")

# --- D ---
print("--- D ---")
numeroCualquiera = int(input("Ingrese un número entero positivo: "))
stringNumeroCualquiera = str(numeroCualquiera)

suma = 0
for caracter in stringNumeroCualquiera:
    digito = int(caracter)
    suma += digito

print("original==>", numeroCualquiera, "suma => ", suma)

# --- E ---
print("--- E ---")
numeroCualquiera = int(input("Ingrese un número entero positivo: "))
stringNumeroCualquiera = str(numeroCualquiera)
suma = 0
for caracter in stringNumeroCualquiera:
    digito = int(caracter)
    if digito % 2 == 0:
        suma += digito

print("original==>", numeroCualquiera, "suma => ", suma)
"""

#==> EJERCICIO 2 
"""
Dados los siguientes puntos geométricos:
"P1" ==> (2, 2, 3)              "P6"  ==> (1, 0.5, 1)
"P2" ==> (2, 3, 4)              "P7"  ==> (3, 2, 0.5)
"P3" ==> (1, 1, 3)              "P8"  ==> (3, 1, 2)
"P4" ==> (0.5, 0.5, 2)          "P9"  ==> (0, 0, 0)
"P5" ==> (1, 2, 1)              "P10" ==> (2, 0, 0.5) 
Determine el par de puntos que se encuentran más cercanos.
Almacene la respuesta en un string llamado parCercano. Ejemplo:
parCercano = "P2-P3" 
"""

puntos = {'P1': (2, 2, 3), 'P2': (2, 3, 4), 'P3': (1, 1, 3), 'P4': (0.5, 0.5, 2), 'P5': (1, 2, 1), 
'P6': (1, 0.5, 1), 'P7': (3, 2, 0.5), 'P8': (3, 1, 2), 'P9': (0, 0, 0), 'P10': (2, 0, 0.5)}

dist_minima = ((puntos['P2'][0] - puntos['P1'][0])**2 + (puntos['P2'][1] - puntos['P1'][1])**2 + (puntos['P2'][2] - puntos['P1'][2])**2)**0.5
punto1 = 'P1'
punto2 = 'P2'

for i in puntos:
    for j in puntos:
        if i != j:
            dist_actual = ((puntos[j][0] - puntos[i][0])**2 + (puntos[j][1] - puntos[i][1])**2 + (puntos[j][2] - puntos[i][2])**2)**0.5
            if dist_actual < dist_minima:
                dist_minima = dist_actual
                punto1 = i
                punto2 = j

print("La distancia mínima entre dos puntos es:", dist_minima)
print("Los puntos correspondientes son:", punto1, "y", punto2)

#==> EJERCICIO 3 
"""
matrix = [[1,  2,  3, 50],
          [6,  7,  8, 10],
          [2,  4,  6, 11]]
Programa que imprima matrix de la siguiente manera
porfilas =>    1-2-3-50-6-7-8-10-2-4-6-11-
porColumnas => 1-6-2-2-7-4-3-8-6-50-10-11-
"""
"""
print("\n----- EJERCICIO 2 -----")

# Por filas
print("--- Por filas ---")
def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print()

matriz_1 = [[1, 2, 3, 50], [6, 7, 8, 10], [2, 4, 6, 11]]
imprimir_matriz(matriz_1)

# Por columnas
print("--- Por columnas ---")
def imprimir_matriz(matriz):
    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            print(matriz[j][i], end=" ")
        print()

matriz_2 = [[1, 6, 2], [2, 7, 4], [3, 8, 6], [50, 10, 11]]
imprimir_matriz(matriz_2)
"""
#==> EJERCICIO 3
""" El rendimiento de los empleados de una empresa es el siguiente:
--------------  Emplea_1  Emplea_2  Emplea_3  Emplea_4  Emplea_5  Emplea_6  Emplea_7  Emplea_8  Emplea_9  Emplea_10  Emplea_11  Emplea_12  Emplea_13  Emplea_14  Emplea_15  Emplea_16  Emplea_17  Emplea_18  Emplea_19  Emplea_20  Emplea_21  Emplea_22  Emplea_23  Emplea_24  Emplea_25  Emplea_26  Emplea_27 
Rendimiento --    "C"       "B"      "B"        "B"        "C"      "B"      "A"        "C"       "B"        "A"        "C"       "B"        "B"        "B"         "B"        "A"       "B"        "A"         "A"        "C"       "B"        "B"        "B"         "B"         "C"       "A"       "C"   
Donde "A" es alto, "B" aceptable  y "C"  insuficiente. 
Determine ¿cuales empleados pueden solicitar un aumento salarial y cuáles pueden ser despedidos? """