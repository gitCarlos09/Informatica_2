"""
edad=input("ingrese edad: ")
edad=int(edad)

if (edad >= 18):
    print("La persona es mayor de edad")
else:
    print("La persona es menor de edad")


num1= input(("Ingrese el primer número: "))
num2= input(("Ingrese el segundo número: "))

if (num1>num2):
    print("El primero es mayor al segundo")
elif (num2>num1):
    print("El segundo es mayor al primero")
else:
    print("Ambos son iguales")

"""
#Ejercicio 1
""" a) Pedir al usuario que ingrese su edad, luego imprimir en pantalla si es mayor o menor de edad 
    b) Pedir al usuario que ingrese su salario, luego imprimir si su salario es alto o bajo, salario alto > $5000000
    c) Pedir al usuario que ingrese 3 notas, luego avisar si aprueba o reprueba la materia 
        (Aprueba con promedio mayor o igual a 3.0) """
"""
# a)
edad=input("ingrese su edad: ")
edad=int(edad)

if (edad >= 18):
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")

# b)
salario=input("ingrese su salario: ")

if (edad >= 5000000):
    print("Su salario es alto")
else:
    print("Su salario es bajo")

# c)
nota1= input(("Ingrese la primera nota: "))
nota2= input(("Ingrese la segunda nota: "))
nota3= input(("Ingrese la tercera nota: "))
promedio = ((nota1 + nota2 + nota3)/3)

if (promedio>=3):
    print("Usted ha aprobado la materia")
else:
    print("Usted ha reprobado la materia")
"""
#Ejercicio 2
""" a) Dados 2 números, desarrolle un programa que determine , ¿que número es menor?
    b) Dados 3 números, desarrolle un programa que determine, ¿que número es mayor? """
"""
#a
núm1=input("Ingrese el primer número: ")
núm2=input("Ingrese el segundo número: ")

if (núm1>núm2):
    print(núm2, " es menor que ", núm1)
elif (núm2>núm1): 
    print(núm1, " es menor que ", núm2)
else: 
    print(núm1, " es igual que ", núm2)

#b
núm1=input("Ingrese el primer número: ")
núm2=input("Ingrese el segundo número: ")
núm3=input("Ingrese el tercer número: ")

if (núm1>núm2 and núm1>núm3):
    print(núm1, "es mayor que", núm2, "y", núm3)
elif (núm2>núm1 and núm2>núm3): 
    print(núm2, "es mayor que", núm1, "y", núm3)
elif (núm3>núm2 and núm3>núm1): 
    print(núm3, "es mayor que", núm1, "y", núm2)
else: 
    print("Todos son iguales")
"""
#Ejercicio 3