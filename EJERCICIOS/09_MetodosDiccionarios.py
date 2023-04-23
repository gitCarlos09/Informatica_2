########################
"""--------------diccionarios--------------
Extraccion: items(), keys(), values(), get(key)
Eliminar: pop(key)
Almacenamiento: clear(), copy()
Indexado: [key]"""
""" 
#Se compone por pares clave-valor 
#y se separa por comas

#Diccionario español-inglés
diccTraduccion = {"silla": "chair",
                  "cara": "face",
                  "amarillo": "yellow"}

#Diccionario con atomo-masa
diccAtomico = {"Hidrogeno":1,
               "Azufre"   :32,
               "Carbono"  :12,
               "Oxigeno"  :16}

#Diccionario con estudiantes-nota
diccEstudiantes = {"Juan Chica":       4.2,
                   "Manuela Segura":   3.5,
                   "Santiago Tabares": 3.0,
                   "Cristian Pachon":  2.0}

print("claves del diccAtomico  => ", diccAtomico.keys())
print("valores del diccAtomico => ", diccAtomico.values())
diccTraduccion.pop("amarillo")
print("eliminar amarillo de diccTraduccion => ", diccTraduccion)
print("indexado para diccEstudiantes => ", diccEstudiantes["Santiago Tabares"])


# Teniendo en cuenta los metodos anteriores, agregue 3 nuevos elementos a diccEstudiantes
diccEstudiantes["Miguel Gomez"] = 4.5
diccEstudiantes["Juan Aya"] = 3.9
diccEstudiantes["Carlos Castillo"] = 4.0

# Haga un ciclo for para recorrer todo diccEstudiantes 
# impriman los pares clave-valor

for clave in diccEstudiantes.keys():
    print(clave, "--", diccEstudiantes[clave])

for clave, valor in diccEstudiantes.items():
    print(clave, "---", valor)
"""

#====================== EJERCICIOS MÉTODOS DE DICCIONARIOS ====================

#==> EJERCICIO 1
""" Cree el siguiente diccionario =>
    Calificaciones = {"Juan": 5.0, "David": 2.4, "Maria": 2.9, "Esteban": 2.2, "Daniela": 2.0, "Mario": 3.1, "Juanita": 2.1, "José": 3.0, "Sebastian": 2.3, "Cristian": 2.0, "Alberto": 3.9, "Angélica": 4.2, "Angel": 2.0, "Marly": 2.5, "Mariana": 4.5, "Josefina": 2.7}
     
       a) Extraiga los keys y values del diccionario, almacenelos en las variables claves, valores, respectivamente
       b) Corrija en el diccionario las calificaciones de Marly (4.3), Angel (3.1) y Juanita (3.5)
       c) Elimine a les estudiantes Josefina y Juan.
       d) Cree una copia y llamela reprobados, elimine todos aquellos con calificación mayor o igual a 3
       e) Muestre en pantalla la mejor calificación, para ello utilice indexing
       f) Muestre en pantalla la peor calificación, para ello utilice indexing 
       g) Utilice indexing para agregar dos nuevos estudiantes: Marco(3.0) Alejandra(5.0)"""

Calificaciones = {"Juan": 5.0, "David": 2.4, "Maria": 2.9, "Esteban": 2.2, 
                "Daniela": 2.0, "Mario": 3.1, "Juanita": 2.1, "José": 3.0, 
                "Sebastian": 2.3, "Cristian": 2.0, "Alberto": 3.9, "Angélica": 4.2, 
                "Angel": 2.0, "Marly": 2.5, "Mariana": 4.5, "Josefina": 2.7}

# a)     
claves = Calificaciones.keys()
valores = Calificaciones.values()

# b)
Calificaciones["Marly"] = 4.3
Calificaciones["Angel"] = 3.1
Calificaciones["Juanita"] = 3.5

# c)
Calificaciones.pop("Josefina")
Calificaciones.pop("Juan")

# d)
copia = Calificaciones.copy()
reprobados = {}

for clave, valor in copia.items():
    if valor >= 3:
        reprobados.append(clave, valor)
        
print(reprobados)


#==> EJERCICIO 2
""" Utilizando diccionarios cree una base de datos de empleados de una empresa,
la base de datos se debe llamar empleadosMabe. Debe contener la siguiente información
Cod   Nombre               Cargo          Salario   
0001   Cristian Pachon     Ingeniero      $ 3.200.000
0002   Daniela Pineda      Programador    $ 4.300.000
0003   Esteban Murcia      Programador    $ 4.600.000
0004   Jose Guzman         Ingeniero      $ 3.900.000
0005   Camilo Rodriguez    Ensamblador    $ 1.200.000
0006   Mariana Londoño     Ensamblador    $ 1.100.000
0007   Estefania Muños     Ensamblador    $ 1.700.000
0008   Cristian Rodriguez  Ingeniero      $ 3.100.000
0009   Natalia Alzate      Ensamblador    $ 2.200.000
0010   Juan Sanabria       Diseñador      $ 5.100.000
0011   Juanita Calderon    Ensamblador    $ 1.300.000
0012   Laura Quintero      Administrador  $ 2.500.000
0013   Viviana Quesada     Guardia        $ 1.500.000
A partir de la base de datos, busque una manera de:
    a) Encontrar la persona con mayor salario
    b) Encontrar la persona con menor salario
    c) Calcular el gasto total de la empresa por motivo salarios
    d) Calcular el promedio de lo que ganan los programadores
    e) Calcular el promedio de lo que ganan los ensambladores"""

empleadosMabe = {"0001":  {"Nombre": "Cristian Pachon",    "Cargo": "Ingeniero",     "Salario": 3_200_000},
                 "0002":  {"Nombre": "Daniela Pineda",     "Cargo": "Programador",   "Salario": 4_300_000},
                 "0003":  {"Nombre": "Esteban Murcia",     "Cargo": "Programador",   "Salario": 4_600_000},
                 "0004":  {"Nombre": "Jose Guzman",        "Cargo": "Ingeniero",     "Salario": 3_900_000},
                 "0005":  {"Nombre": "Camilo Rodriguez",   "Cargo": "Ensamblador",   "Salario": 1_200_000},
                 "0006":  {"Nombre": "Mariana Londoño",    "Cargo": "Ensamblador",   "Salario": 1_100_000},
                 "0007":  {"Nombre": "Estefania Muños",    "Cargo": "Ensamblador",   "Salario": 1_700_000},
                 "0008":  {"Nombre": "Cristian Rodriguez", "Cargo": "Ingeniero",     "Salario": 3_100_000},
                 "0009":  {"Nombre": "Natalia Alzate",     "Cargo": "Ensamblador",   "Salario": 2_200_000},
                 "0010":  {"Nombre": "Juan Sanabria",      "Cargo": "Diseñador",     "Salario": 5_100_000},
                 "0011":  {"Nombre": "Juanita Calderon",   "Cargo": "Ensamblador",   "Salario": 1_300_000},
                 "0012":  {"Nombre": "Laura Quintero",     "Cargo": "Administrador", "Salario": 2_500_000},
                 "0013":  {"Nombre": "Viviana Quesada",    "Cargo": "Guardia",       "Salario": 1_500_000}}


#==> EJERCICIO 3
""" 
 Almacene en un diccionario la siguiente base de datos
 de calificaciones.
 Almacenelos de tal manera que sea posible acceder
 a la calificacion utilizando el nombre y la materia
                               Materias
    Nombre          Cuantica Etica Deportes Lenguas
Juan Gutierrez        2.0     5.0     1.3     3.2
Maria Snowden         3.1     4.9     2.2     1.1
Pedro Gonzalez        5.0     3.8     3.1     4.1
Angelica Lozano       2.1     2.7     4.1     3.2
Pablo Iglesias        3.2     1.6     5.0     1.2
Mariana Pajon         2.2     2.5     4.9     3.3
Esteban Loaiza        2.1     3.4     3.8     4.3
Daniela Pineda        5.0     4.3     2.7     1.2
Esteban Vazco         3.1     5.0     1.6     3.2
Enilse Lopez          5.0     2.2     2.5     5.0
Cristian Playonero    0.5     1.1     3.4     3.2
"""
    
cali_1 = {"Juan Gutierrez    ": {"Cuantica": 2.0, "Etica":  5.0, "Deportes": 1.3, "Lenguas":   3.2}, 
          "Maria Snowden     ": {"Cuantica": 3.1, "Etica":  4.9, "Deportes": 2.2, "Lenguas":   1.1},
          "Pedro Gonzalez    ": {"Cuantica": 5.0, "Etica":  3.8, "Deportes": 3.1, "Lenguas":   4.1},
          "Angelica Lozano   ": {"Cuantica": 2.1, "Etica":  2.7, "Deportes": 4.1, "Lenguas":   3.2},
          "Pablo Iglesias    ": {"Cuantica": 3.2, "Etica":  1.6, "Deportes": 5.0, "Lenguas":   1.2},
          "Mariana Pajon     ": {"Cuantica": 2.2, "Etica":  2.5, "Deportes": 4.9, "Lenguas":   3.3},
          "Esteban Loaiza    ": {"Cuantica": 2.1, "Etica":  3.4, "Deportes": 3.8, "Lenguas":   4.3},
          "Daniela Pineda    ": {"Cuantica": 5.0, "Etica":  4.3, "Deportes": 2.7, "Lenguas":   1.2},
          "Esteban Vazco     ": {"Cuantica": 3.1, "Etica":  5.0, "Deportes": 1.6, "Lenguas":   3.2},
          "Enilse Lopez      ": {"Cuantica": 5.0, "Etica":  2.2, "Deportes": 2.5, "Lenguas":   5.0},
          "Cristian Playonero": {"Cuantica": 0.5, "Etica":  1.1, "Deportes": 3.4, "Lenguas":   3.2}}