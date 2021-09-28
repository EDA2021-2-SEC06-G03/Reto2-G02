"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from prettytable import PrettyTable

assert cf

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Seleccionar el tipo de algoritmo de ordenamiento iterativo")
    print("3- Req. 1. Listar cronológicamente los artistas")
    print("4- Req. 2. Listar cronológicamente las adquisiciones")
    print("5- Req. 3. Clasificar las obras de un artista por técnica")
    print("6- Req. 4. Clasificar las obras por la nacionalidad de sus creadores")
    print("7- Req. 5. Transportar obras de un departamento")
    print("8- Req. 6. Proponer una nueva exposición en el museo")
    print("9- (MAP) N obras mas antiguas por tecnica")
    print("10- Salir del Menu")


def initCatalog(Tipo_Arreglo):
    return controller.initCatalog(Tipo_Arreglo)


def loadData(catalog):
    controller.loadData(catalog)


catalog = None


def imprimirArtistasCrono(lista):
    listaImprimir = primerosYUltimos(lista)

    #IMPRESION NORMAL
    # print('Nombre ---', 'Año nacimiento ---', 'Año fallecimiento ----', 'Nacionalidad ----', 'Genero')
    # for i in range(1, lt.size(listaImprimir) + 1):
    #     print([lt.getElement(listaImprimir, i).get('DisplayName'), lt.getElement(listaImprimir, i).get('BeginDate'),
    #                lt.getElement(listaImprimir, i).get('EndDate'), lt.getElement(listaImprimir, i).get('Nationality'),
    #                lt.getElement(listaImprimir, i).get('Gender')])

    #IMPRESION CON PRETTY TABLE
    x = PrettyTable()
    x.field_names = ['Nombre', 'Año nacimiento', 'Año fallecimiento', 'Nacionalidad', 'Genero']
    for i in range(1, lt.size(listaImprimir) + 1):
        x.add_row([lt.getElement(listaImprimir, i).get('DisplayName'), lt.getElement(listaImprimir, i).get('BeginDate'),
                   lt.getElement(listaImprimir, i).get('EndDate'), lt.getElement(listaImprimir, i).get('Nationality'),
                   lt.getElement(listaImprimir, i).get('Gender')])
    print(x)


def imprimirObrasCrono(lista):
    listaImprimir = primerosYUltimos(lista)
    x = PrettyTable()
    x.field_names = ['Titulo', 'Artista(s)', 'Fecha', 'Medio', 'Dimensiones']
    for i in range(1, lt.size(listaImprimir) + 1):
        x.add_row([lt.getElement(listaImprimir, i).get('Title'), lt.getElement(listaImprimir, i).get('Artist'),
                   lt.getElement(listaImprimir, i).get('Date'), lt.getElement(listaImprimir, i).get('Medium'),
                   lt.getElement(listaImprimir, i).get('Dimensions')])
    print(x)


def imprimirObrasTecnica(lista):
    x = PrettyTable()
    x.field_names = ['Titulo', 'Fecha', 'Medio', 'Dimensiones']
    for i in range(1, lt.size(lista) + 1):
        x.add_row([lt.getElement(lista, i).get('Title'), lt.getElement(lista, i).get('Date'),
                   lt.getElement(lista, i).get('Medium'), lt.getElement(lista, i).get('Dimensions')])
    print(x)


def imprimirObrasTransportar(lista):
    x = PrettyTable()
    x.field_names = ['Titulo', 'Artista (s)', 'Clasificación', 'Fecha de la obra', 'Medio', 'Dimensiones', 'Costo']

    for i in range(1, lt.size(lista) + 1):
        x.add_row([lt.getElement(lista, i).get('Title'), lt.getElement(lista, i).get('Artist'),
                   lt.getElement(lista, i).get('Classification'), lt.getElement(lista, i).get('Date'),
                   lt.getElement(lista, i).get('Medium'), lt.getElement(lista, i).get('Dimensions'),
                   lt.getElement(lista, i).get('Transport')])
    print(x)


def primeros5Lista(lista):
    lista5primeros = lt.newList()
    lt.addLast(lista5primeros, lt.getElement(lista, 1))
    lt.addLast(lista5primeros, lt.getElement(lista, 2))
    lt.addLast(lista5primeros, lt.getElement(lista, 3))
    lt.addLast(lista5primeros, lt.getElement(lista, 4))
    lt.addLast(lista5primeros, lt.getElement(lista, 5))
    return lista5primeros


def ultimos5Lista(lista):
    lista5ultimos = lt.newList()
    lt.addLast(lista5ultimos, lt.getElement(lista, lt.size(lista)))
    lt.addLast(lista5ultimos, lt.getElement(lista, lt.size(lista) - 1))
    lt.addLast(lista5ultimos, lt.getElement(lista, lt.size(lista) - 2))
    lt.addLast(lista5ultimos, lt.getElement(lista, lt.size(lista) - 3))
    lt.addLast(lista5ultimos, lt.getElement(lista, lt.size(lista) - 4))
    return lista5ultimos


def primerosYUltimos(lista):
    listaImprimir = lt.newList()
    tam_lista = lt.size(lista)
    lt.addLast(listaImprimir, lt.getElement(lista, 1))
    lt.addLast(listaImprimir, lt.getElement(lista, 2))
    lt.addLast(listaImprimir, lt.getElement(lista, 3))
    lt.addLast(listaImprimir, lt.getElement(lista, tam_lista - 2))
    lt.addLast(listaImprimir, lt.getElement(lista, tam_lista - 1))
    lt.addLast(listaImprimir, lt.getElement(lista, tam_lista))
    return listaImprimir


def resp_req1():
    fecha_inicial = input("Ingresa el año inicial: ")
    fecha_final = input("Ingresa el año final: ")
    lista_artistas, tiempo = controller.listarCronoArtistas(fecha_inicial, fecha_final, catalog)
    tam_lista = lt.size(lista_artistas)
    print("============ Respuesta Requerimiento 1 ============")
    print("Tiempo procesamiento: " + str(round(tiempo, 2)) + " milseg")
    print("La cantidad de artistas nacidos entre " + fecha_inicial + " y " + fecha_final + " es de " + str(tam_lista))
    print("Los primeros 3 y los ultimos 3 artistas en este rango son: ")
    imprimirArtistasCrono(lista_artistas)


def resp_req2():
    fecha_inicial = input("Ingresa la fecha inicial (AAAA-MM-DD): ")
    fecha_final = input("Ingresa la fecha final (AAAA-MM-DD): ")
    lista_obras, cont = controller.listarCronoObras(fecha_inicial, fecha_final, catalog)
    tam_lista = lt.size(lista_obras)
    print("============ Respuesta Requerimiento 2 ============")
    print("Obras adquiridas entre " + fecha_inicial + " y " + fecha_final + " es de " + str(tam_lista))
    print("La cantidad de obras adquiridas mediante compras es de " + str(cont))
    print("Las primeras 3 y los ultimas 3 obras en este rango son: ")
    imprimirObrasCrono(lista_obras)


def resp_req3():
    nombre = input("Ingresa el nombre del artista: ")
    cantidadObras, cantidadTecnicas, idArtista, tecnicaMayor, cantidadTecnicaMayor, listaDeObrasMayor = controller.totalObras(
        nombre, catalog)
    print("============ Respuesta Requerimiento 3 ============")
    print("El total de la obras del artista " + nombre + " identificado con el ID " + idArtista + " es de: " + str(
        cantidadObras))
    print("El total de tecnicas utilizadas son de: " + str(cantidadTecnicas))
    print("La tecnica mas utilizada es la de: " + tecnicaMayor + " y su cantidad de obras con esta tecnica es de: " + str(
        cantidadTecnicaMayor))
    imprimirObrasTecnica(listaDeObrasMayor)


def resp_req5():
    departamento = input("Ingresa el departamento a consultar: ")
    cantidadObras, listaOrdenada, peso, listaTransporteOrdenada, totalTransporte = controller.obrasDepartamento(departamento, catalog)
    print("============ Respuesta Requerimiento 5 ============")
    print("Cantidad de obras a transportar: " + str(cantidadObras))
    print("Peso aproximado de las obras (kg): " + str(round(peso, 3)))
    print("Valor aproximado del transportes (USD): " + str(round(totalTransporte, 3)))
    print("----- Obras mas caras de transportar ------")
    imprimirObrasTransportar(ultimos5Lista(listaTransporteOrdenada))
    print("----- Obras mas antiguas ------")
    imprimirObrasTransportar(primeros5Lista(listaOrdenada))

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar: ')
    if int(inputs) == 1:
        tipo_Arreglo = ""
        opcion = int(input("Elige la opción 1.ArrayList 2.SingleLinked : "))
        if opcion == 1:
            tipo_Arreglo = "ARRAY_LIST"
        else:
            tipo_Arreglo = "SINGLE_LINKED"
        print("Cargando información de los archivos ....")
        catalog = initCatalog(tipo_Arreglo)
        loadData(catalog)

        catalog['years'] = mp.newMap(2, maptype='PROBING', loadfactor=0.5)
        print(catalog['years'])
        mp.put(catalog['years'], 15, 'novecientos')
        mp.put(catalog['years'], 618513, 'gerard')
        mp.put(catalog['years'], 12, 'Camilo')
        print(catalog['years'])
        print(mp.get(catalog['years'], 15))
        print(mp.get(catalog['years'], 15)['value'])
        print(catalog['years'])
        print('Artistas cargados: ' + str(lt.size(catalog['artist'])))
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))

    elif int(inputs) == 2:
        tipo_Algoritmo = input("Elige la opción Insertion, Shell, Merge o Quick Sorts: ")
        ordenado = controller.AlgoritmoIterativo(tipo_Algoritmo, catalog)
        print("Para el catálogo con el tipo de ordenamiento:", tipo_Algoritmo, "el tiempo de procesamiento es:",
              round(ordenado, 2), " milisegundos")

    elif int(inputs) == 3:
        resp_req1()

    elif int(inputs) == 4:
        resp_req2()

    elif int(inputs) == 5:
        resp_req3()

    elif int(inputs) == 6:
        print("Obras por la nacionalidad de sus creadores: ")

    elif int(inputs) == 7:
        resp_req5()

    elif int(inputs) == 8:
        A_IO = input("Ingresa el año inicial de las obras: ")
        A_FO = input("Ingresa el año final de las obras: ")
        Area_D = input("Ingresa el área disponible: ")
        print("Propuesta de una nueva exposición:  ")

    elif int(inputs) == 9:
        print("Hola")
    else:
        sys.exit(9)
sys.exit(0)
