# IMPORTANTE: para correr el codigo es necesario la conexion a internet

import pandas as pd
import plotly.graph_objs as graf
import matplotlib.pyplot as plt
import json

from urllib.request import urlopen
with urlopen('https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/be6a6e239cd5b5b803c6e7c2ec405b793a9064dd/Colombia.geo.json') as CoordenadasColombia:
    departamentos = json.load(CoordenadasColombia)   # archivo que se encuentra en internet para usar las coordenadas de los departamentos mas eficientemente

archivo= 'INFORMES\PROYECTO\DosisCovid.xlsx'   # guarda la tabla de excel en archivo

Dosis=pd.read_excel(archivo)   # pandas lee el erchivo de excel y lo guarda en otra variable

print(Dosis)

locs = Dosis['Departamento']

condicion="Si"   # Haremos un ciclo para poder colocar lo que queremos ver

while condicion == "Si":
    print("\nDosis aplicadas de cada departamento de Colombia segun el mes para el COVID-19 (MAPA)")
    print("A continuacion se mostrara un mapa segun el mes seleccionado")
    opcion=int(input("Digite el numero de mes en el que desea ver las dosis aplicadas (1-24): ").strip())

    if (opcion >= 1) and (opcion <=24):
        MES=("MES"+" "+str(opcion))
        for loc in departamentos['features']:       # busca las localizaciones en features del documento que se extrae desde internet
            loc['id'] = loc['properties']['NOMBRE_DPT']
        fig = graf.Figure(graf.Choroplethmapbox(
                    geojson=departamentos,
                    locations=locs,
                    z=Dosis[MES],
                    colorscale='spectral',
                    colorbar_title=("Dosis aplicadas del"+" "+MES)))
        fig.update_layout(mapbox_style="carto-positron",
                        mapbox_zoom=3.4,
                        mapbox_center = {"lat": 4.570868, "lon": -74.297333})  # centramos para ver Colombia
        fig.show()
        
    else:
        print("¡El mes indicado no se encuentra en el rango estipulado!")

    condicion=str(input("¿Desea ver el mapa de las dosis aplicadas de otro mes? (Si/No)\n").strip().capitalize())
    if condicion=="No":
        print("Finalizacion de la vista del mapa")  

print("\n")

archivo2='PROYECTO\DosisCovid.xlsx'
DosisDepto=pd.read_excel(archivo2)   # pandas lee el erchivo de excel y lo guarda en otra variable
Dep=DosisDepto["Departamento"].to_list()  # guarda los departamentos en una lista

Dep[3]="SAN ANDRES"
Dep[26]="BOGOTA"

condicion3="Si"  # En esta parte se preguntara si quiere ver un histograma de las dosis segun el departamento

while condicion3=="Si":
    print(Dep)
    print("\nHistograma segun el departamento escogido (arriba se pueden ver los departamentos)")
    opcion2=str(input("ingrese el nombre del departamento de Colombia al que le desea ver su histograma: ").strip().upper())

    if condicion3 == "Si":
        DosisDeptoCopy=DosisDepto.drop(["Departamento"],axis=1)
        DosisDeptoCopy["SumaFilas"] = DosisDeptoCopy.sum(axis=1)  # Agrega una columna con la suma en filas
        Suma_fila=DosisDeptoCopy["SumaFilas"].to_list()  # guarda la suma de filas en una lista
        DosisDeptoCopy=DosisDeptoCopy.drop(["SumaFilas"],axis=1)  # elimina la columna añadida de suma total de fila
        Total={}  #Creamos una libreria vacia
        j=0      # contador de la lista de suma
        k=0
        Depto_Mes={}

        for i in Dep:
            Total[i]=Suma_fila[j]    # en el for agrega en el diccionario el departamento con su respectiva suma de meses
            j=j+1

            Depto_Mes[i]=DosisDeptoCopy.iloc[k].tolist()  # agrega en un diccionario el departamento junto al valor de dosis segun el mes
            k=k+1
        
        promedio=[]  # lista vacia para los promedios de dosis de los departamentos

        for k in Total.keys():      # aca se busca en el diccionario el valor de la suma de cada departamento
            promedio.append(Total[k]/24)    # toma el promedio del total de los meses segun el departamento
        if opcion2 in Total:
            # creamos el histograma segun el departamento:
            plt.figure(figsize=(10,6))
            plt.plot(DosisDeptoCopy.columns,Depto_Mes[opcion2],"d-b")
            plt.xlabel(opcion2,size=13)
            plt.ylabel("Cantidad de dosis",size=18)
            plt.title("Cantidad de dosis mensuales del departamento",color="blue",size=20, style="italic")
            plt.xticks(rotation=80,size=7)
            plt.grid()
            plt.show()
        else:
            print("¡El departamento ingresado es incorrecto!")   

    condicion3=str(input("¿Desea ingresar otro departamento? (Si/No) ").strip().capitalize())
    if condicion3 =="No":
            print("Finalizacion de la vista de histogramas por departamento\n")

opcion3=str(input("¿Desea ver el promedio de dosis de todos los departamentos en los 2 años? ").strip().capitalize())
if opcion3 == "Si":
    # creamos la grafica del promedio de los departamentos
    plt.figure(figsize=(10,6))
    plt.plot(Dep,promedio,"d-g",lw="1.5")
    plt.ylabel("Cantidad de dosis",size=15)
    plt.title("Promedio de dosis en los 2 años",size=25,color="blue",style="italic")
    plt.xticks(rotation=80,size=7)
    plt.grid()
    plt.show()


condicion2=str(input("¿Desea ver la grafica de las dosis de todos los meses? (Si/No) ").strip().capitalize())
if condicion2 == "Si":
    archivo='PROYECTO\DosisCovid.xlsx'   # guarda la tabla de excel en archivo
    Dosis=pd.read_excel(archivo)   # pandas lee el erchivo de excel y lo guarda en otra variable
    DosisCopy1=Dosis.copy()
    DosisSinDPTO=DosisCopy1.drop(["Departamento"],axis=1)   # Elimina la columna 1 para que no interfiera en la suma
    SumaDosis=DosisSinDPTO.sum()  # Suma la cantdad de dosis por mes convirtiendolo en serie

    x=SumaDosis.index  # x= numero de mes
    y=SumaDosis.values # y= cantidad de dosis

    # se crea la grafica de la cantidad de dosis suministradas por cada mes

    plt.figure(figsize=(10,6))
    plt.plot(x,y,"d-r",lw="1.5")
    plt.xticks(rotation=70,size=10)
    plt.ylim(top=9999999)
    plt.ylabel("Numero de dosis (millones)",color="blue",size="16")
    plt.title("Dosis aplicadas (Covid-19)",color="blue",size=25,style="italic")
    plt.grid()

    for i in range(len(x)):   # sirve para mostrar en cada punto el valor de este
        plt.text(x[i], y[i], f'( {y[i]})',va='baseline',size=8,rotation=45)

    plt.show()
