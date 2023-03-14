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
"""Desarrolle un programa que calcule el descuento salarial que hace una empresa a sus empleados, por motivos de pandemia. 
El programa debe solicitar el salario recibido por el trabajador (input) y luego debe imprimir el descuento realizado (print).
Si el empleado gana menos de $ 900.000 se le descuenta el 15%, luego si devenga hasta $2.500.000 se le descuenta el 20%. Por último si 
gana por encima de este último valor se le descuenta el 25% de su salario."""

salario = 1_000_000 # debe ser un input el valor ingresado

if (salario < 900_000):
       descuento = salario * 0.15
elif (salario >= 900_000) and (salario <= 2_500_000):
       descuento = salario*0.20
else:
       descuento = salario*0.25
print("EL DESCUENTO ES DE ==> ", descuento)


#Ejercicio 4 
"""Los estudiantes del curso de matematicas obtuvieron las siguientes calificaciones definitivas (cada una de las notas equivale al 25%):
         Nota1  Nota2  Nota3  Nota4
Camila    1.0    2.3    5.0    5.0
Maria     5.0    3.5    2.5    3.2
José      2.2    4.0    3.2    4.1
Daniela   5.0    0.5    1.0    0.2
Esteban   4.0    5.0    0.0    0.0
El director del grupo preparará una salida académica, en caso de que se hayan cumplido las siguientes condiciones:
   * El 60% del grupo debe aprobar la materia
   * Por lo menos dos notas del grupo, deben tener un promedio mayor a 3.0
   * El promedio de los que perdieron la materia debe ser mayor a 2
¿Habrá salida académica?"""

#------------ condicion1----------------
definitiva_Camila   = (1.0 + 2.3 + 5.0 + 5.0)/4
definitiva_Maria    = (5.0 + 3.5 + 2.5 + 3.2)/4
definitiva_José     = (2.2 + 4.0 + 3.2 + 4.1)/4
definitiva_Daniela  = (5.0 + 0.5 + 1.0 + 0.2)/4
definitiva_Esteban  = (4.0 + 5.0 + 0.0 + 0.0)/4 

reporte_Camila   = definitiva_Camila >= 3
reporte_Maria    = definitiva_Maria >= 3
reporte_José     = definitiva_José >= 3
reporte_Daniela  = definitiva_Daniela >= 3
reporte_Esteban  = definitiva_Esteban >= 3

porcentajeAprobados = ((reporte_Camila + reporte_Maria + reporte_José + reporte_Daniela + reporte_Esteban) / 5) * 100

condicion1 = porcentajeAprobados >= 60
print("condicion1 ==>", condicion1)

#------------ condicion2------------

nota1Grupo = (1.0+5.0+2.2+5.0+4.0) / 5
nota2Grupo = (2.3+3.5+4.0+0.5+5.0) / 5
nota3Grupo = (5.0 +2.5 +3.2+ 1.0+ 0.0) / 5
nota4Grupo = (5.0+3.2+4.1+0.2+0.0) / 5

ReporteNota1Grupo = (nota1Grupo >= 3.0)
ReporteNota2Grupo = (nota2Grupo >= 3.0)
ReporteNota3Grupo = (nota3Grupo >= 3.0)
ReporteNota4Grupo = (nota4Grupo >= 3.0)

numeroNotasGrupoAprobadas = (ReporteNota1Grupo+ReporteNota2Grupo+ReporteNota3Grupo+ReporteNota4Grupo) 

condicion2 = (numeroNotasGrupoAprobadas >=2)
print("condicion2 =>", condicion2)

#------------ condicion3--------------

definitiva_Camila   = (1.0 + 2.3 + 5.0 + 5.0)/4
definitiva_Maria    = (5.0 + 3.5 + 2.5 + 3.2)/4
definitiva_José     = (2.2 + 4.0 + 3.2 + 4.1)/4
definitiva_Daniela  = (5.0 + 0.5 + 1.0 + 0.2)/4
definitiva_Esteban  = (4.0 + 5.0 + 0.0 + 0.0)/4 

EsCamilaMayorA2 =  round(definitiva_Camila)   >= 2
EsMariaMayorA2 =  round(definitiva_Maria)     >= 2
EsJoséMayorA2 =  round(definitiva_José)       >= 2
EsDanielaMayorA2 =  round(definitiva_Daniela) >= 2
EsEstebanMayorA2 =  round(definitiva_Esteban) >= 2

SonMayoresA2Todos = ((EsCamilaMayorA2+EsMariaMayorA2+EsJoséMayorA2+EsDanielaMayorA2+EsEstebanMayorA2)==5)
condicion3 = SonMayoresA2Todos

print("condicion3", condicion3)

if (condicion1 and condicion2 and condicion3):
   print("Habrá salida académica")
else:
   print(" No Habrá salida académica")
