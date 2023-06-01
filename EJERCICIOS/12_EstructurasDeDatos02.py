# Veamos la estructura tipo serie
# Es un arreglo unidimensional tipo lista y diccionario 

import pandas

#Serie de número de días de los meses del año
data1  = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
index1 = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
serieDiasPorMes = pandas.Series(data=data1, index=index1)

#Serie de número atomico de 8 elementos
data2  = [1, 2, 3, 4, 5, 6, 7, 8]
index2 = ["Hidrogeno", "Helio", "Litio", "Berilio", "Boro", "Carbono", "Nitrogeno", "Oxigeno"]
serieNumAtom = pandas.Series(data=data2, index=index2)

# Buscar funciones que me permitan calcular sobre las series 
# - La suma de cada serie
# - La media de cada serie
# - La desviación estándar de cada serie

print ("Suma días:", serieDiasPorMes.sum())
print ("Suma números atomicos:", serieNumAtom.sum())

print ("Media dias:", serieDiasPorMes.mean())
print ("Media números atomicos:", serieNumAtom.mean())

print ("Desviacion dias:", serieDiasPorMes.std())
print ("Desviacion números atomicos:", serieNumAtom.std())

# Extraer los dias del mes de mayo
# Extraer número atomico del oxigeno
# Ext

print ("Dias de Mayo:", serieDiasPorMes["May"])
print ("Numero atomico oxigeno:", serieNumAtom["Oxigeno"])

#-----------------------EJERCICIO----------------------

#crear una serie con los siguientes datos: 

"""
  Nombre              Salario   
  Cristian Pachon     $ 3.200.000
  Daniela Pineda      $ 4.300.000
  Esteban Murcia      $ 4.600.000
  Jose Guzman         $ 3.900.000
  Camilo Rodriguez    $ 1.200.000
  Mariana Londoño     $ 1.100.000
  Estefania Muñoz     $ 1.700.000
  Cristian Rodriguez  $ 3.100.000
  Natalia Alzate      $ 2.200.000
  Juan Sanabria       $ 5.100.000
  Juanita Calderon    $ 1.300.000
  Laura Quintero      $ 2.500.000
  Viviana Quesada     $ 1.500.000"""

#Luego:
#Extraer el salario de Estefania Muñoz
#Extraer el salario de Mariana Londoño
#Extraer el salario mas alto 
#Extraer el salario más bajo
#Extraer los nombres de los trabajadores con salario mayor a 4 millones
#Extraer los nombres de los trabajadores con salario menor a 1.5 milones
#Determinar la media de los salarios
#Determinal la desviacion estandar de los salarios

data3 = [3_200_000, 4_300_000, 4_600_000, 3_900_000, 1_200_000, 1_100_000, 1_700_000,
         3_100_000, 2_200_000, 5_100_000, 1_300_000, 2_500_000, 1_500_000]

index3 = ["Cristian Pachon", "Daniela Pineda", "Esteban Murcia", "Jose Guzman", "Camilo Rodriguez", "Mariana Londoño", "Estefania Muñoz",
          "Cristian Rodriguez", "Natalia Alzate", "Juan Sanabria", "Juanita Calderon", "Laura Quintero", "Viviana Quesada"]

serieNombreSalario = pandas.Series(data=data3, index=index3)

print ("Salario Estefania Muñoz:", serieNombreSalario["Estefania Muñoz"])
print ("Salario Mariana Londoño:", serieNombreSalario["Mariana Londoño"])
print ("Salario más alto:", serieNombreSalario.max())
print ("Salario más bajo:", serieNombreSalario.min())

salariosaltos = serieNombreSalario[serieNombreSalario > 4_000_000]
print ("salarios mayores a 4 millones:", list(salariosaltos.index))

salariosbajos = serieNombreSalario[serieNombreSalario < 1_500_000]
print ("salarios menores a 1.5 milones:", list(salariosbajos.index))

print ("Media del salario:", serieNombreSalario.mean())
print ("Desviación del salario:", serieNombreSalario.std())

# Dibujar y describir la serie salarios

serieNombreSalario.plot()