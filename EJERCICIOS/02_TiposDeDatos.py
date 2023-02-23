# Imprimir en la terminal:

# Dos enteros en una misma linea
# Dos flotantes en una misma linea
# Dos booleanos en una misma linea
# Dos listas en una misma linea
# Un diccionario 

# SOLUCION:

print(23,17)
print(12.45,67.5436)
print(True,False)
print([1,2,3],["Uno","Dos","Tres"])
print({"Four":"4"})
# Imprimir que tipo de dato son los
# siguientes datos:

# 100000001
# 0.00000000000001
# [0,0,0,0]
# {1,2,3}

#SOLUCION

print(type(100000001))
print(type(0.0000000000001))
print(type([0,0,0,0]))
print(type({1,2,3}))

# Crear variables y asignarles los siguientes tipos de datos:
# Enteros: 1,2,3 999
# Luego reste sucesivamente del ultimo al primero y almacenelo en una variable llamada resultado1 

# Flotantes: 15.2, 29.5, 18.28
# Luego divida sucesivamente del primero al ultimo
# y almacenelo en una variable llamada resultado2

# Strings: "123", "Cristian" 
# Luego sume ambas variables y determine si la operacion es posible, si asi es almacenelo en una variable de su eleccion

# Solucion

a=1
b=2
c=3
d=999
resultado1=d-c-b-a
print(resultado1)

e=15.2
f=29.5
g=18.28
resultado2=e/f/g
print(resultado2)

S1="123"
S2="Cristian"

SString=S1+S2
print(SString)

###### Para pensar ######

# Busque una manera de convertir:
# un entero a un flotante
# un flotante a un entero
# un string a un entero y flotante
# un numero a un string

#Solucion

A=21
B=28.0816
C="911"

float(A)
print(float(A))

int(B)
print(int(B))

int(C)
float(C)
print(int(C))
print(float(C))

str(A)
str(B)
print(str(A))
print(str(B))