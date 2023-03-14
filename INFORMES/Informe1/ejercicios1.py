"""Recomendaciones:
 - Recuerde almacenar las respuestas tal como se pide en cada ejercicio
 - Se resuelve de manera individual, la copia será anulada.
 - Muestre sus procedimientos de manera clara"""

# nombre_completo = "Jhanth Carlo Castillo Perez"    #Por favor ingrese su nombre en las comillas

#------------------------ EJERCICIO 1 --------------------------------
"""
Cree los siguientes rangos (tipo range()): 
   rango1 => 334, 331, 328, 325, ... 4, 1
   rango2 => -5,-3,-1, 1, 3, 5, ... 999
   rango3 => -50, -55, -60, -65, -70, ... -195, -200
Después de obtener los rangos, almacenelos de la siguiente manera:
listaDeRangos = [rango1, rango2, rango3]
"""
print("\n----- EJERCICIO 1 -----")

rango1= range(334, 0,-3)
rango2= range(-5, 1000, 2)
rango3= range(-50, -201, -5)

listaDeRangos = [rango1, rango2, rango3]
print(listaDeRangos)

#------------------------ EJERCICIO 2 --------------------------------
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
print("\n----- EJERCICIO 2 -----")

"distancia = ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**(1/2)"

# Se calcula la distancia entre cada punto.
"Con respecto al P1"
D1_2=((2-2)**2+(2-3)**2+(3-4)**2)**1/2
D1_3=((2-1)**2+(2-1)**2+(3-3)**2)**1/2
D1_4=((2-0.5)**2+(2-0.5)**2+(3-2)**2)**1/2
D1_5=((2-1)**2+(2-2)**2+(3-1)**2)**1/2
D1_6=((2-1)**2+(2-0.5)**2+(3-1)**2)**1/2
D1_7=((2-3)**2+(2-2)**2+(3-0.5)**2)**1/2
D1_8=((2-3)**2+(2-1)**2+(3-2)**2)**1/2
D1_9=((2-0)**2+(2-0)**2+(3-0)**2)**1/2
D1_10=((2-2)**2+(2-0)**2+(3-0.5)**2)**1/2

"Con respecto al P2"
D2_3=((2-1)**2+(3-1)**2+(4-3)**2)**1/2
D2_4=((2-0.5)**2+(3-0.5)**2+(4-2)**2)**1/2
D2_5=((2-1)**2+(3-2)**2+(4-1)**2)**1/2
D2_6=((2-1)**2+(3-0.5)**2+(4-1)**2)**1/2
D2_7=((2-3)**2+(3-2)**2+(4-0.5)**2)**1/2
D2_8=((2-3)**2+(3-1)**2+(4-2)**2)**1/2
D2_9=((2-0)**2+(3-0)**2+(4-0)**2)**1/2
D2_10=((2-2)**2+(3-0)**2+(4-0.5)**2)**1/2

"Con respecto al P3"
D3_4=((1-0.5)**2+(1-0.5)**2+(3-2)**2)**1/2
D3_5=((1-1)**2+(1-2)**2+(3-1)**2)**1/2
D3_6=((1-1)**2+(1-0.5)**2+(3-1)**2)**1/2
D3_7=((1-3)**2+(1-2)**2+(3-0.5)**2)**1/2
D3_8=((1-3)**2+(1-1)**2+(3-2)**2)**1/2
D3_9=((1-0)**2+(1-0)**2+(3-0)**2)**1/2
D3_10=((1-2)**2+(1-0)**2+(3-0.5)**2)**1/2

"Con respecto al P4"
D4_5=((0.5-1)**2+(0.5-2)**2+(2-1)**2)**1/2
D4_6=((0.5-1)**2+(0.5-0.5)**2+(2-1)**2)**1/2
D4_7=((0.5-3)**2+(0.5-2)**2+(2-0.5)**2)**1/2
D4_8=((0.5-3)**2+(0.5-1)**2+(2-2)**2)**1/2
D4_9=((0.5-0)**2+(0.5-0)**2+(2-0)**2)**1/2
D4_10=((0.5-2)**2+(0.5-0)**2+(2-0.5)**2)**1/2

"Con respecto al P5"
D5_6=((1-1)**2+(2-0.5)**2+(1-1)**2)**1/2
D5_7=((1-3)**2+(2-2)**2+(1-0.5)**2)**1/2
D5_8=((1-3)**2+(2-1)**2+(1-2)**2)**1/2
D5_9=((1-0)**2+(2-0)**2+(1-0)**2)**1/2
D5_10=((1-2)**2+(2-0)**2+(1-0.5)**2)**1/2

"Con respecto al P6"
D6_7=((1-3)**2+(0.5-2)**2+(1-0.5)**2)**1/2
D6_8=((1-3)**2+(0.5-1)**2+(1-2)**2)**1/2
D6_9=((1-0)**2+(0.5-0)**2+(1-0)**2)**1/2
D6_10=((1-2)**2+(0.5-0)**2+(1-0.5)**2)**1/2

"Con respecto al P7"
D7_8=((3-3)**2+(2-1)**2+(0.5-2)**2)**1/2
D7_9=((3-0)**2+(2-0)**2+(0.5-0)**2)**1/2
D7_10=((3-2)**2+(2-0)**2+(0.5-0.5)**2)**1/2

"Con respecto al P8"
D8_9=((3-0)**2+(1-0)**2+(2-0)**2)**1/2
D8_10=((3-2)**2+(1-0)**2+(2-0.5)**2)**1/2

"Con respecto al P9"
D9_10=((0-2)**2+(0-0)**2+(0-0.5)**2)**1/2  # Para la distancia del punto 9-10 no es necesario una lista

"Listas de distancias asociadas a un punto"
list_D1=[D1_2, D1_3, D1_4, D1_5, D1_6, D1_7, D1_8, D1_9, D1_10]   
list_D2=[D2_3, D2_4, D2_5, D2_6, D2_7, D2_8, D2_9, D2_10]
list_D3=[D3_4,D3_5,D3_6,D3_7,D3_8,D3_9,D3_10]
list_D4=[D4_5,D4_6,D4_7,D4_8,D4_9,D4_10]
list_D5=[D5_6,D5_7,D5_8,D5_9,D5_10]
list_D6=[D6_7,D6_8,D6_9,D6_10]
list_D7=[D7_8,D7_9,D7_10]
list_D8=[D8_9,D8_10]

# Valor minimo de cada lista de distancias y se guardan en una nueva lista
list_min=[min(list_D1),min(list_D2),min(list_D3),min(list_D4),min(list_D5),min(list_D6),min(list_D7),min(list_D8),D9_10]
Geodesica=min(list_min)  # Saca la distancia minima de las distancias mas bajas encontradas

# Se busca los puntos que corresponden a esa distancia mínima
if Geodesica==(min(list_D1)):
    if Geodesica==(D1_2):
        parCercano="P1-P2"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D1_3):
        parCercano="P1-P3"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D1_4):
        parCercano="P1-P4"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D1_5):
        parCercano="P1-P5"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D1_6):
        parCercano="P1-P6"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D1_7):
        parCercano="P1-P7"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D1_8):
        parCercano="P1-P8"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D1_9):
        parCercano="P1-P9"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D1_10):
        parCercano="P1-P10"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)

if Geodesica==(min(list_D2)):
    if Geodesica==(D2_3):
        parCercano="P2-P3"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D2_4):
        parCercano="P2-P4"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D2_5):
        parCercano="P2-P5"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D2_6):
        parCercano="P2-P6"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D2_7):
        parCercano="P2-P7"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D2_8):
        parCercano="P2-P8"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D2_9):
        parCercano="P2-P9"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D2_10):
        parCercano="P2-P10"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)

if Geodesica==(min(list_D3)):
    if Geodesica==(D3_4):
        parCercano="P3-P4"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D3_5):
        parCercano="P3-P5"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D3_6):
        parCercano="P3-P6"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D3_7):
        parCercano="P3-P7"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D3_8):
        parCercano="P3-P8"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D3_9):
        parCercano="P3-P9"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D3_10):
        parCercano="P3-P10"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)

if Geodesica==(min(list_D4)):
    if Geodesica==(D4_5):
        parCercano="P4-P5"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D4_6):
        parCercano="P4-P6"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D4_7):
        parCercano="P4-P7"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D4_8):
        parCercano="P4-P8"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D4_9):
        parCercano="P4-P9"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D4_10):
        parCercano="P4-P10"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)

if Geodesica==(min(list_D5)):
    if Geodesica==(D5_6):
        parCercano="P5-P6"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D5_7):
        parCercano="P5-P7"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D5_8):
        parCercano="P5-P8"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D5_9):
        parCercano="P5-P9"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D5_10):
        parCercano="P5-P10"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)

if Geodesica==(min(list_D6)):
    if Geodesica==(D6_7):
        parCercano="P6-P7"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D6_8):
        parCercano="P6-P8"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D6_9):
        parCercano="P6-P9"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D6_10):
        parCercano="P6-P10"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)

if Geodesica==(min(list_D7)):
    if Geodesica==(D7_8):
        parCercano="P7-P8"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D7_9):
        parCercano="P7-P9"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D7_10):
        parCercano="P7-P10"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)

if Geodesica==(min(list_D8)):
    if Geodesica==(D8_9):
        parCercano="P8-P9"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
    elif Geodesica==(D8_10):
        parCercano="P8-P10"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)

if Geodesica==(D9_10):
    if Geodesica==(D9_10):
        parCercano="P9-P10"
        print("El par mas cercano es el punto",parCercano,"con",Geodesica)
parCercano=parCercano


#------------------------ EJERCICIO 3 --------------------------------
"""
La calificación de informatica se encuentra en el intervalo [0,5] y se calcula tomando 5 notas, 
con porcentajes de 10%, 20%, 15%, 20% y 35%. La materia se aprueba por encima de 3.0
Los siguientes estudiantes tienen las primeras 4 calificaciones definidas.
cod      Nombre          Nota1   Nota2  Nota3  Nota4  Nota 5
01    Miguel Pineda        1.0    1.1    2.3    1.1     ?
02    Maria Gonzalez       3.1    3.1    1.2    3.0     ?
03    Jose Nuñez           5.0    4.0    2.5    5.0     ?
04    Angelica Lozano      3.1    1.0    2.6    1.0     ?
05    Camilo Suarez        3.2    4.0    1.1    3.0     ?
06    Mariana Rosero       5.0    5.0    5.0    3.9     ?
07    Esteban Quesada      3.4    4.0    2.6    3.2     ?
08    Julia Quintero       2.0    2.2    2.1    4.2     ?
09    Mauricio Lizcano     3.7    4.1    4.7    4.0     ?
10    Angie Gomez          4.1    4.7    4.4    5.0     ?
11    Camilo Restrepo      5.0    5.0    1.0    3.2     ?
12    Mauricio Velazquez   5.0    4.2    2.1    5.0     ?
13    Esteban Rodriguez    3.2    4.1    2.2    3.3     ?
   Determine cuantos estudiantes pierden aúnque obtengan la mejor nota_5
   Determine cuantos estudiantes ganan aunque obtengan la peor nota_5
   Determine cuantos estudiantes tienen posibilidades de pasar
   Almacene sus resultados en una lista llamada estudiantes, tal como se muestra:
   estudiantes = [Cantidad_que_pierden, Cantidad_que_ganan, Cantidad_con_posibilidades]
"""

print("\n----- EJERCICIO 3 -----")

# Calcula la nota que lleva el alumno, sin contar la Nota 5
Stud_01=(1*0.10)+(1.1*0.20)+(2.3*0.15)+(1.1*0.20)
Stud_02=(3.1*0.10)+(3.1*0.20)+(1.2*0.15)+(3*0.20)
Stud_03=(5*0.10)+(4*0.20)+(2.5*0.15)+(5*0.20)
Stud_04=(3.1*0.10)+(1*0.20)+(2.6*0.15)+(1*0.20)
Stud_05=(3.2*0.10)+(4*0.20)+(1.1*0.15)+(3*0.20)
Stud_06=(5*0.10)+(5*0.20)+(5*0.15)+(3.9*0.20)
Stud_07=(3.4*0.10)+(4*0.20)+(2.6*0.15)+(3.2*0.20)
Stud_08=(2*0.10)+(2.2*0.20)+(2.1*0.15)+(4.2*0.20)
Stud_09=(3.7*0.10)+(4.1*0.20)+(4.7*0.15)+(4*0.20)
Stud_10=(4.1*0.10)+(4.7*0.20)+(4.4*0.15)+(5*0.20)
Stud_11=(5*0.10)+(5*0.20)+(1*0.15)+(3.2*0.20)
Stud_12=(5*0.10)+(4.2*0.20)+(2.1*0.15)+(5*0.20)
Stud_13=(3.2*0.10)+(4.1*0.20)+(2.2*0.15)+(3.3*0.20)

"Esta es la mejor nota 5"
nota_5=5*0.35    

# 1-1. Compara la nota final con la mejor nota 5 y si es verdadero, el alumno pierde la materia
B_nota_5_Stud_01 = Stud_01+nota_5 < 3
B_nota_5_Stud_02 = Stud_02+nota_5 < 3
B_nota_5_Stud_03 = Stud_03+nota_5 < 3
B_nota_5_Stud_04 = Stud_04+nota_5 < 3
B_nota_5_Stud_05 = Stud_05+nota_5 < 3
B_nota_5_Stud_06 = Stud_06+nota_5 < 3
B_nota_5_Stud_07 = Stud_07+nota_5 < 3
B_nota_5_Stud_08 = Stud_08+nota_5 < 3
B_nota_5_Stud_09 = Stud_09+nota_5 < 3
B_nota_5_Stud_10 = Stud_10+nota_5 < 3
B_nota_5_Stud_11 = Stud_11+nota_5 < 3
B_nota_5_Stud_12 = Stud_12+nota_5 < 3
B_nota_5_Stud_13 = Stud_13+nota_5 < 3

# 1-2. Para la condicion 1 si la nota final del alumno es verdad entonces pierde.
pierde=0   # Contador de los que pierden
if B_nota_5_Stud_01==True:
    pierde=1+pierde
if B_nota_5_Stud_02==True:
    pierde=1+pierde
if B_nota_5_Stud_03==True:
    pierde=1+pierde
if B_nota_5_Stud_04==True:
    pierde=1+pierde
if B_nota_5_Stud_05==True:
    pierde=1+pierde
if B_nota_5_Stud_06==True:
    pierde=1+pierde
if B_nota_5_Stud_07==True:
    pierde=1+pierde
if B_nota_5_Stud_08==True:
    pierde=1+pierde
if B_nota_5_Stud_09==True:
    pierde=1+pierde
if B_nota_5_Stud_10==True:
    pierde=1+pierde
if B_nota_5_Stud_11==True:
    pierde=1+pierde
if B_nota_5_Stud_12==True:
    pierde=1+pierde
if B_nota_5_Stud_13==True:
    pierde=1+pierde
Cantidad_que_pierden=pierde

# 2-1. Verifica quienes ganan la materia con la peor nota 5
P_nota5_Stud_01 = Stud_01 >=3
P_nota5_Stud_02 = Stud_02 >=3
P_nota5_Stud_03 = Stud_03 >=3
P_nota5_Stud_04 = Stud_04 >=3
P_nota5_Stud_05 = Stud_05 >=3
P_nota5_Stud_06 = Stud_06 >=3
P_nota5_Stud_07 = Stud_07 >=3
P_nota5_Stud_08 = Stud_08 >=3
P_nota5_Stud_09 = Stud_09 >=3
P_nota5_Stud_10 = Stud_10 >=3
P_nota5_Stud_11 = Stud_11 >=3
P_nota5_Stud_12 = Stud_12 >=3
P_nota5_Stud_13 = Stud_13 >=3

# 2-2. Para la condicion 2, si la nota final del alumno es verdadera, entonces gana la materia con la peor nota 5
ganan=0   # Contador de los que ganan

if P_nota5_Stud_01==True:
    ganan=1+ganan
if P_nota5_Stud_02==True:
    ganan=1+ganan
if P_nota5_Stud_03==True:
    ganan=1+ganan
if P_nota5_Stud_04==True:
    ganan=1+ganan
if P_nota5_Stud_05==True:
    ganan=1+ganan
if P_nota5_Stud_06==True:
    ganan=1+ganan
if P_nota5_Stud_07==True:
    ganan=1+ganan
if P_nota5_Stud_08==True:
    ganan=1+ganan
if P_nota5_Stud_09==True:
    ganan=1+ganan
if P_nota5_Stud_10==True:
    ganan=1+ganan
if P_nota5_Stud_11==True:
    ganan=1+ganan
if P_nota5_Stud_12==True:
    ganan=1+ganan
if P_nota5_Stud_13==True:
    ganan=1+ganan
Cantidad_que_ganan=ganan

# 3. Cuenta los demás estudiantes, es decir que tienen posibilidades
Cantidad_con_posibilidades=13-Cantidad_que_pierden-Cantidad_que_ganan

# 4. Almacen de los resultados
estudiantes=[Cantidad_que_pierden,Cantidad_que_ganan,Cantidad_con_posibilidades]
print("[pierden,ganan,posibilidades]")
print(estudiantes)


#------------------------ EJERCICIO 4 --------------------------------

""" Seis compañeros, contratan un taxi con el objeto de movilizarse juntos a la universidad. 
El contrato es de lunes a viernes, y deben pagar al taxista $15000 por cada trayecto. 
Se prestarán dos servicios al día, uno de ida y el otro de regreso.
Sin embargo, los seis no se movilizan juntos todos los dias. Por tanto, han planteado que la tarifa
debe dividirse entre el numero de compañeros que se movilicen en cada trayecto.En caso, de que ninguno
utilice el servicio. Deben pagar al taxista una tarifa de $10000, repartidos equitativamente entre todos.
A continueación veamos el uso del servicio por parte de los compañeros en la última semana de clases:
                            IDA                             |                       REGRESO
            LUNES   MARTES  MIERCOLES   JUEVES  VIERNES     |    LUNES   MARTES  MIERCOLES   JUEVES  VIERNES
JUAN          Si        Si        Si      Si      No        |      Si        Si        Si      No       No
CAMILA        Si        No        Si      No      Si        |      Si        No        No      No       No
JOSE          Si        No        Si      Si      No        |      Si        No        Si      Si       No
MARIA         Si        Si        Si      No      No        |      No        No        Si      No       No
ESTEBAN       Si        No        No      Si      Si        |      No        No        No      Si       No
ANGIE         Si        No        Si      No      No        |      Si        No        Si      No       No
¿Cuanto debe pagar cada estudiante? 
Almacene el resultado dentro de un diccionario llamado "diccionarioPagos"
las claves deben ser los nombres de los estudiantes (en strings)
y los valores deben ser el dinero total que pagó cada uno al terminar la semana (en flotantes)
"""

print("\n----- EJERCICIO 4 -----")

"Precio del taxi"
Pay=15000

# Calcula el precio del taxi por su uso
"Ida"
Mon_Ida= Pay/6
Tue_Ida= Pay/2
Wed_Ida= Pay/5
Thu_Ida= Pay/3
Fri_Ida= Pay/2
"Regreso"
Mon_Back= Pay/4
Tue_Back= Pay
Wed_Back= Pay/4
Thu_Ida=  Pay/2
Fri_Ida=  10000/6

# 1. A cada uno le calculamos lo que pagaron en la semana.
Juan    = Mon_Ida + Mon_Back + Tue_Ida + Tue_Back + Wed_Ida + Wed_Back + Thu_Ida + Fri_Ida
Camila  = Mon_Ida + Mon_Back + Wed_Ida + Fri_Ida  + Fri_Ida
Jose    = Mon_Ida + Mon_Back + Wed_Ida + Wed_Back + Thu_Ida + Thu_Ida + Fri_Ida
Maria   = Mon_Ida + Tue_Ida  + Wed_Ida + Wed_Back + Fri_Ida
Esteban = Mon_Ida + Thu_Ida  + Thu_Ida + Fri_Ida  + Fri_Ida
Angie   = Mon_Ida + Mon_Back + Wed_Ida + Wed_Back + Fri_Ida

# 2. Pago semanal en el diccionario pedido
diccionarioPagos={"Angie": Angie, "Camila": Camila, "Esteban": Esteban, "Jose": Jose, "Juan": Juan, "Maria": Maria}
print(diccionarioPagos)


#------------------------ EJERCICIO 5 --------------------------------

""" El salario mensual de un empleado se calcula solo teniendo en cuenta el numero de seguros vendidos,
    (el precio de cada seguro es de $120000)
    Para los primeros 20 seguros vendidos, la comisión es del 20%.
    Para los siguientes 100 seguros las comisión es del 30%.
    Para los siguientes seguros vendidos. La comisión es de 10%.
   El salario de 4 empleados es el siguiente:
    Empleado   empleado1   empleado2    empleado3   empleado4
    Salario   $ 7860000    $ 5520000   $ 3720000    $ 2280000
   Determine el numero de seguros vendidos por cada empleado.
   Almacene su respuesta en una lista llamada cantidadSegurosVendidos como muestra el ejemplo:
   cantidadSegurosVendidos = [10, 50, 80, 32]
   """

print("\n----- EJERCICIO 5 -----")

#Salario de los empleados
empleado_1=7860000
empleado_2=5520000
empleado_3=3720000
empleado_4=2280000

Seg1=20*120000          # salario que se gana por vender 20 seguros
Seg2=100*120000         # salario que se gana por vender otros 100 seguros

comi1=Seg1*0.20
comi2=Seg2*0.30

# Si la condicion se cumple se da por seguro que vendio mas de 120 seguros y solo hay que hallar la cantidad de seguros restantes

# Para el empleado 1
if empleado_1 > (comi1 + comi2):
    empleado_1= empleado_1 - (comi1 + comi2)
    Seg_V1= 20 + 100 + (empleado_1/(0.10*120_000))  # Si el N° de seguros vendidos > 120
elif (empleado_1 > comi1) and (empleado_1 <= comi1 + comi2): # Si no se asegura que vendio > 20
    empleado_1= empleado_1 - comi1
    Seg_V1= 20 + (empleado_1/(0.3*120000))   # N° de seguros vendidos <= 120 y > 20
else:
    Seg_V1= empleado_1/(0.2*120000)  # N° de seguros vendidos < 20

# Para el empleado 2
if empleado_2 > (comi1+comi2):
    empleado_2= empleado_2 -(comi1 + comi2)
    Seg_V2=20+100+(empleado_2/(0.10*120_000))  
elif (empleado_2 > comi1) and (empleado_2 <= comi1 + comi2):  
    empleado_2= empleado_2 - comi1
    Seg_V2=20+(empleado_2/(0.3*120_000))   
else:
    Seg_V2= empleado_2/(0.2*120_000)  

# Para el empleado 3
if empleado_3 > (comi1+comi2):
    empleado_3= empleado_3 - (comi1+comi2)
    Seg_V3= 20 + 100 + (empleado_3/(0.10*120_000))  
elif (empleado_3 > comi1) and (empleado_3 <= comi1 + comi2): 
    empleado_3= empleado_3 - comi1
    Seg_V3= 20 + (empleado_3/(0.3*120_000))   
else:
    Seg_V3= empleado_3/(0.2*120_000) 

# Para el empleado 4
if empleado_4 > (comi1 + comi2):
    empleado_4= empleado_4-(comi1 + comi2)
    Seg_V4=20 + 100 + (empleado_4/(0.10*120_000))  
elif (empleado_4 > comi1) and (empleado_4 <= comi1 + comi2):  
    empleado_4= empleado_4 - comi1
    Seg_V4= 20 + (empleado_4/(0.3*120_000))   
else:
    Seg_V4= empleado_4/(0.2*120_000)  

# Un paso intermedio para asegurar que la cantidad de seguros sea entera
Seg_V1= int(Seg_V1)
Seg_V2= int(Seg_V2)
Seg_V3= int(Seg_V3)
Seg_V4= int(Seg_V4)

# 1. Se guarda en una lista la cantidad de seguros vendidos por los empleados
cantidadSegurosVendidos=[Seg_V1,Seg_V2,Seg_V3,Seg_V4]
print("Cantidad de seguros vendidos: [empleado 1, empleado 2, empleado 3, Empleado 4]")
print(cantidadSegurosVendidos)

