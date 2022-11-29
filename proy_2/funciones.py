import os
import json

#limpia el terminal
def clear():  #codigo de función obtenido de: https://micro.recursospython.com/recursos/como-limpiar-la-consola.html
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def load_db():
    with open('proy_2/db.json') as db:
        database = json.load(db)
    return database

def save_db(db):
    database = json.dumps(db, indent=4)
    with open('proy_2/db.json', 'w') as file:
        file.write(database)

def crear_listas(dbe):
    #Verificar que la base de datos no este vacia
            #Listas vacias e inicializacion de contador
    cont = 0
    #La lista tot hace referencia a una lista auxiliar con la lista de codigos y la lista de los nombres
    lista_tot = []
    codigo_lista = []
    nombre_lista = []
    if len(dbe) != 0:
        #iteracion en la base de datos
        for pintura in dbe:
            dic_cod = {"cota": pintura["cota"],
                        "index":cont}
            dic_name = {"nombre": pintura["nombre"],
                        "index":cont}
            codigo_lista.append(dic_cod)
            nombre_lista.append(dic_name)
        lista_tot.append(codigo_lista)
        lista_tot.append(nombre_lista)
    else:
        lista_tot.append(codigo_lista)
        lista_tot.append(nombre_lista)
    return lista_tot

def ordenar(lista, clave):
    return sorted(lista, key=lambda pintura: pintura[clave])

def consulta(lista, clave, parametroBuscado):
    if len(lista) == 0:
        return [False, []]
    if len(lista) == 1:
        if lista[0][clave] == parametroBuscado:
            return [True, lista[0]]
        else:
            return [False, []]
    else:
        pivot_index = len(lista) // 2
        pivot = lista[pivot_index]
        if pivot[clave] == parametroBuscado:
            return [True, pivot]
        elif pivot[clave] < parametroBuscado:
            return consulta(lista[pivot_index:], clave, parametroBuscado)
        elif pivot[clave] > parametroBuscado:
            return consulta(lista[:pivot_index], clave, parametroBuscado)