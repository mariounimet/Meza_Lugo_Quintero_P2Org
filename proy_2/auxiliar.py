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
        lista_tot.append(codigo_lista and nombre_lista)
    else:
        lista_tot.append(codigo_lista and nombre_lista)
    return lista_tot