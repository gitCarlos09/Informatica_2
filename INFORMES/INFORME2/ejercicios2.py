"""
 Recomendaciones:
 - Recuerde almacenar las respuestas tal como se pide en cada ejercicio
 - Para los ejercicios 3,4 y 5 se pide crear funciones, 
   asi que entregue funciones, no valores
 """

nombre_completo = "Jhanth Carlo Castillo Perez"    #Por favor ingrese su nombre en las comillas

# ------------------------ EJERCICIO 1 --------------------------------
""" Dados los siguientes puntos geométricos:
"P1" ==> (5, 2, 3)             P11 ==>  (2, 2, 3)
"P2" ==> (4, 1, 3)             P12 ==>  (2, 3, 4)
"P3" ==> (2.5, 1, 0)           P13 ==>  (1, 1, 3)
"P4" ==> (0.5, 0.5, 2)         P14 ==>  (4, 4, 4)
"P5" ==> (1, 2, 1)             P15 ==>  (5, 5, 1)
"P6"  ==> (6, 2, 1)            P16 ==>  (1, 0.5, 1)
"P7"  ==> (3, 2, 0.5)          P17 ==>  (3, 4, 5)
"P8"  ==> (2, 6, 1)            P18 ==>  (3, 1, 2)
"P9"  ==> (0, 0, 0)            P19 ==>  (3, 9, 1)
"P10" ==> (2, 0, 0.5)          P20 ==>  (0.5, 0.5, 6)
Determine el par de puntos que se encuentran más cercanos.
Almacene la respuesta en un string llamado parCercano. Ejemplo:
parCercano = "P3-P10" """
"""
puntos = {"P1": (5, 2, 3),    "P2": (4, 1, 3),   "P3": (2.5, 1, 0), "P4": (0.5, 0.5, 2), "P5": (1, 2, 1),
          "P6": (6, 2, 1),    "P7": (3, 2, 0.5), "P8": (2, 6, 1),   "P9": (0, 0, 0),    "P10": (2, 0, 0.5),
         "P11": (2, 2, 3),   "P12": (2, 3, 4),  "P13": (1, 1, 3),  "P14": (4, 4, 4),    "P15": (5, 5, 1),
         "P16": (1, 0.5, 1), "P17": (3, 4, 5),  "P18": (3, 1, 2),  "P19": (3, 9, 1),    "P20": (0.5, 0.5, 6)}

parCercano = ""
distanciaMinima = float('inf')

for punto1 in puntos:
    for punto2 in puntos:
        if punto1 != punto2:
            distancia = (((puntos[punto1][0] - puntos[punto2][0])**2 + 
                          (puntos[punto1][1] - puntos[punto2][1])**2 + 
                          (puntos[punto1][2] - puntos[punto2][2])**2)**0.5)
            if distancia < distanciaMinima:
                distanciaMinima = distancia
                parCercano = punto1 + "-" + punto2


print("El par mas cercano son los puntos", parCercano)
"""


# ------------------------ EJERCICIO 2 --------------------------------
""" El costo de las entradas a cine es el siguiente:
                          ----------- 2D ------------        ---------- 3D -------------
                          ----NIÑO----  ----ADULTO---        ---NIÑO----  ----ADULTO----
 precio (Lunes-viernes)       $4000          $7000              $7000         $11000
 precio (Sabado, domingo)     $6000          $8000              $8000         $14000

Las ventas de boletas en el intervalo de una semana, se registraron de la siguiente manera:
ventas = [
("2D_5NIÑOS_LUNES", "2D_2ADULTOS_LUNES"),("2D_0NIÑOS_LUNES", "2D_1ADULTOS_LUNES"),("2D_0NIÑOS_LUNES", "2D_3ADULTOS_LUNES"),
("3D_0NIÑOS_LUNES", "3D_1ADULTOS_LUNES"),("2D_2NIÑOS_LUNES", "2D_1ADULTOS_LUNES"),("2D_0NIÑOS_LUNES", "2D_2ADULTOS_LUNES"),
("2D_0NIÑOS_LUNES", "2D_2ADULTOS_LUNES"),("3D_0NIÑOS_LUNES", "3D_3ADULTOS_LUNES"),("3D_3NIÑOS_LUNES", "3D_4ADULTOS_LUNES"),
("2D_2NIÑOS_LUNES", "2D_4ADULTOS_LUNES"),
("2D_1NIÑOS_MARTES","2D_4ADULTOS_MARTES"),("3D_3NIÑOS_MARTES", "3D_2ADULTOS_MARTES"),
("2D_3NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),
("3D_0NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),
("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_3ADULTOS_MARTES"),("3D_3NIÑOS_MARTES", "3D_4ADULTOS_MARTES"),
("2D_2NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_1NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),
("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_3NIÑOS_MARTES", "3D_2ADULTOS_MARTES"),("2D_3NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),
("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),
("2D_2NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),
("3D_0NIÑOS_MARTES", "3D_3ADULTOS_MARTES"),("3D_3NIÑOS_MARTES", "3D_4ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),
("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_1NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),
("3D_3NIÑOS_MARTES", "3D_2ADULTOS_MARTES"),("2D_3NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),
("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),
("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_3ADULTOS_MARTES"), 
("3D_3NIÑOS_MARTES", "3D_4ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),
("3D_1NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),
("3D_0NIÑOS_MIERCOLES", "3D_3ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),
("3D_1NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("2D_1NIÑOS_MIERCOLES", "2D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),
("3D_0NIÑOS_MIERCOLES", "3D_3ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("2D_1NIÑOS_MIERCOLES", "2D_1ADULTOS_MIERCOLES"),
("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),
("3D_1NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_0NIÑOS_MIERCOLES", "3D_3ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),
("3D_1NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("2D_1NIÑOS_MIERCOLES","2D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),
("3D_0NIÑOS_MIERCOLES", "3D_3ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("2D_1NIÑOS_MIERCOLES", "2D_1ADULTOS_MIERCOLES"),
("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),
("3D_1NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),
("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_1ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_1ADULTOS_MIERCOLES"),
("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_1ADULTOS_MIERCOLES"),
("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),
("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),
("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_2NIÑOS_JUEVES", "3D_1ADULTOS_JUEVES"),
("3D_0NIÑOS_JUEVES", "3D_3ADULTOS_JUEVES"),("2D_3NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),
("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_0ADULTOS_JUEVES"),
("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),
("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),
("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),
("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_2NIÑOS_JUEVES", "3D_1ADULTOS_JUEVES"),
("3D_0NIÑOS_JUEVES", "3D_3ADULTOS_JUEVES"),("2D_3NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),
("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),
("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),
("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_0ADULTOS_JUEVES"),
("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),
("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_2NIÑOS_JUEVES", "3D_1ADULTOS_JUEVES"),
("3D_0NIÑOS_JUEVES", "3D_3ADULTOS_JUEVES"),("2D_3NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),
("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),
("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),
("2D_1NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),("3D_2NIÑOS_JUEVES", "3D_1ADULTOS_JUEVES"),("3D_0NIÑOS_JUEVES", "3D_3ADULTOS_JUEVES"),
("2D_3NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_0ADULTOS_JUEVES"),
("2D_2NIÑOS_VIERNES", "2D_1ADULTOS_VIERNES"),("3D_1NIÑOS_VIERNES", "3D_1ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES","2D_2ADULTOS_VIERNES"),
("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_1ADULTOS_VIERNES"),("3D_1NIÑOS_VIERNES", "3D_1ADULTOS_VIERNES"),
("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("3D_0NIÑOS_VIERNES", "3D_3ADULTOS_VIERNES"),
("3D_3NIÑOS_VIERNES", "3D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_1NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),
("2D_2NIÑOS_VIERNES", "2D_0ADULTOS_VIERNES"),("3D_1NIÑOS_VIERNES", "3D_1ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),
("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("3D_0NIÑOS_VIERNES", "3D_3ADULTOS_VIERNES"),("3D_3NIÑOS_VIERNES", "3D_4ADULTOS_VIERNES"),
("2D_2NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_1NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_1ADULTOS_VIERNES"),
("3D_1NIÑOS_VIERNES","3D_1ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_0ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),
("3D_0NIÑOS_VIERNES", "3D_3ADULTOS_VIERNES"),("3D_3NIÑOS_VIERNES", "3D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),
("2D_1NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("3D_0NIÑOS_VIERNES", "3D_3ADULTOS_VIERNES"),("3D_3NIÑOS_VIERNES", "3D_4ADULTOS_VIERNES"),
("2D_2NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_1NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),
("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),
("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_0ADULTOS_SABADO"),
("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),
("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),
("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),
("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_4ADULTOS_SABADO"),("3D_1NIÑOS_SABADO", "3D_1ADULTOS_SABADO"),
("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),
("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_4ADULTOS_SABADO"),
("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),
("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_0ADULTOS_SABADO"),
("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),
("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),
("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),
("2D_1NIÑOS_SABADO", "2D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),
("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),
("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),
("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO","3D_4ADULTOS_SABADO"),
("2D_1NIÑOS_DOMINGO", "2D_0ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),
("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),
("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"), ("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),
("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),
("2D_1NIÑOS_DOMINGO", "2D_3ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),
("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),
("2D_3NIÑOS_DOMINGO","2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),
("3D_0NIÑOS_DOMINGO", "3D_0ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),
("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),
("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),
("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),
("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),
("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO","2D_3ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),
("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),
("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),
("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),
("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),
("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),
("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO","2D_1ADULTOS_DOMINGO"),
("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),
("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_3ADULTOS_DOMINGO"),
("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_0ADULTOS_DOMINGO"),
("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),
("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),
("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),
("2D_1NIÑOS_DOMINGO","2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),
("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),
("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),
("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),
("2D_1NIÑOS_DOMINGO", "2D_3ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),
("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO","3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),
("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),
("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_0ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),
("2D_3NIÑOS_DOMINGO","2D_4ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_9ADULTOS_DOMINGO")]

Calcule el numero de boletas vendidas (boletasVendidas) y el dinero recaudado por el cine (dineroRecaudado)
Presente la respuesta de la siguiente manera:
    reporteCine = [boletasVendidas, dineroRecaudado]
"""



# ------------------------ EJERCICIO 3 --------------------------------

"""Desarrolle las siguientes funciones:
    
    NOMBRE DE LA FUNCION     PROBLEMA                                                    TIPO DE ENTRADA            RETORNO                        NOTA
    obtenerMultiplos        * Funcion que retorne los primeros 10 multiplos de un numero  * Entero (un numero)     * Lista con los multiplos       *El cero no se tendrá en cuenta como un múltiplo
    obtenerDivisores        * Función que retorne los divisores de un numero              * Entero (un numero)     * Lista con los divisores       *El numero 1, ni el mismo numero de entrada, se considerarán divisores
    obtenerNesimoFibonacci  * Función que retorne el n-esimo numero fibonacci             * Entero (un numero)     * Entero (numero fibonacci)     *El 1er numero de la serie es 0, el 2do es 1, el 3ro es 1, el 4to es 2 ==> 0,1,1,2,3,5,8...
Almacene su respuesta en un listado llamado funciones, de la siguiente manera:
    funciones = [obtenerMultiplos, obtenerDivisores, obtenerNesimoFibonacci]
"""
"""
numero_pedido = int(input("Ingrese un número entero positivo: "))

def obtenerMultiplos (numero_pedido):
    multiplos = []
    for i in range (1, 11):
        n_multiplo = numero_pedido * i
        multiplos.append(n_multiplo)
    return multiplos
obtenerMultiplos = obtenerMultiplos(numero_pedido)

def obtenerDivisores (numero_pedido):
    divisores = []
    for i in range (2, numero_pedido - 1):
        if numero_pedido % i == 0:
            divisores.append(i)
    return divisores
obtenerDivisores = obtenerDivisores(numero_pedido)


def fibonacci (numero_pedido):
    fibo = 1
    back = -1
    for i in range(numero_pedido):
        fibo = fibo + back
        back = fibo - back
    return fibo
obtenerNesimoFibonacci = fibonacci (numero_pedido)

funciones = [obtenerMultiplos, obtenerDivisores, obtenerNesimoFibonacci]
print(funciones)
"""

# ------------------------ EJERCICIO 4 --------------------------------
"""El precio de venta de los artículos de una empresa es el siguiente:
                    Codigo      Precio unitario
                     A001          $ 31 000
                     A011          $ 25 000
                     A032          $ 43 000
                     A125          $ 55 000
                     B001          $ 10 000
                     B005          $ 20 000
                     P009          $ 30 000
                     P019          $ 49 000
                     R001          $ 60 000
                     W307          $ 90 000
                     Z052          $ 35 000
                     Z025          $ 27 000
                     Z278          $ 65 000
   Las ventas a lo largo de un día se ha registrado en la siguiente base de datos:
   ventas = ["A032-52Unidades", "B001-29Unidades", "A125-15Unidades", "A032-22Unidades", "P009-25Unidades", "B005-20Unidades", "B001-19Unidades", "P009-31Unidades", "B005-22Unidades", "W307-15Unidades", "A011-31Unidades", "P019-18Unidades", "A011-20Unidades", "R001-20Unidades", "P019-19Unidades", "A001-12Unidades", "A125-20Unidades", "R001-31Unidades", "Z052-52Unidades", "W307-31Unidades", "Z025-42Unidades", "Z052-10Unidades", "Z278-30Unidades", "Z025-24Unidades", "Z278-21Unidades", "A001-31unidades"]
   Cree una función llamada => calcularVentas,
   que reciba  => ventas
   que retorne => el dinero recaudado a lo largo del día
   """



# ------------------------ EJERCICIO 5 --------------------------------

""" El salario de un empleado de una empresa se calcula, utilizando como base $ 1'200.000 
    Además se paga una comisión de acuerdo a las ventas de los siguientes productos:
                                           precio     comisión
                             Zapatos:    $ 50.000        5%
                             Tenis:      $ 70.000        4%  
                             Camisa:     $ 40.000        6%
                             Corbata:    $ 25.000        7%
                             Pantalon:   $ 35.000        5%
                             Blusa:      $ 80.000        3%
                             Vestido:    $ 95.000        2%
 
    Realice una función llamada => calcularSalario 
    Que reciba los parametros =>   * nombre. (string con el nombre del empleado)
                                   * unidades_vendidas. (lista [zapatos, tenis, camisas, corbatas, pantalones, blusas, vestidos] 
                                                              eje: [10, 14, 13, 0, 20, 13, 8])
    Que retorne => Un diccionario con el nombre y el salario obtenido, por ejemplo: 
                   {"nombre": "Cristian Pachon", "salario" : 2000000}
                   #(conserve las claves "nombre" y "salario") 
"""