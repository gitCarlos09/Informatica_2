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
fibonacci = [0, 1]

for i in range(2, 100):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print(fibonacci)

# --- B ---
print("--- B ---")
n = int(input("Ingrese un número entero positivo: "))
divisores = []

for i in range(1, n+1):
    if n % i == 0:
        divisores.append(i)

print("Los divisores de", n, "son:", divisores)

# --- C ---
print("--- C ---")
def es_primo(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

numero1 = int(input("Ingrese un número entero positivo: "))
if es_primo(numero1):
    print(numero1, "es un número primo")
else:
    print(numero1, "no es un número primo")

# --- D ---
print("--- D ---")
def suma_digitos(numero2):
    suma = 0
    while numero2 > 0:
        digito = numero2 % 10
        suma += digito
        numero2 //= 10
    return suma

numero2 = int(input("Ingrese un número entero: "))

resultado = suma_digitos(numero2)
print("La suma de los dígitos de", numero2, "es", resultado)

# --- E ---
print("--- E ---")
def suma_digitos_pares(numero3):
    suma = 0
    while numero3 > 0:
        digito = numero3 % 10
        if digito % 2 == 0:
            suma += digito
        numero3 //= 10
    return suma

numero3 = int(input("Ingrese un número entero: "))

resultado = suma_digitos_pares(numero3)
print("La suma de los dígitos pares de", numero3, "es", resultado)
"""

#==> EJERCICIO 2 
"""
matrix = [[1,  2,  3, 50],
          [6,  7,  8, 10],
          [2,  4,  6, 11]]
Programa que imprima matrix de la siguiente manera
porfilas =>    1-2-3-50-6-7-8-10-2-4-6-11-
porColumnas => 1-6-2-2-7-4-3-8-6-50-10-11-
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

#==> EJERCICIO 3
""" El rendimiento de los empleados de una empresa es el siguiente:
--------------  Emplea_1  Emplea_2  Emplea_3  Emplea_4  Emplea_5  Emplea_6  Emplea_7  Emplea_8  Emplea_9  Emplea_10  Emplea_11  Emplea_12  Emplea_13  Emplea_14  Emplea_15  Emplea_16  Emplea_17  Emplea_18  Emplea_19  Emplea_20  Emplea_21  Emplea_22  Emplea_23  Emplea_24  Emplea_25  Emplea_26  Emplea_27 
Rendimiento --    "C"       "B"      "B"        "B"        "C"      "B"      "A"        "C"       "B"        "A"        "C"       "B"        "B"        "B"         "B"        "A"       "B"        "A"         "A"        "C"       "B"        "B"        "B"         "B"         "C"       "A"       "C"   
Donde "A" es alto, "B" aceptable  y "C"  insuficiente. 
Determine ¿cuales empleados pueden solicitar un aumento salarial y cuáles pueden ser despedidos? """