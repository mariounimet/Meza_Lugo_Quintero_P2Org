from funciones import save_db
from funciones import imprimir_pintura


def compactar(db):

    contador = 0
    aux = []

    # Buscamos recorrer la base de datos para eliminar las pinturas con parametros "deleted = true"
    if (len(db) == 0):
        return print("\nLa base de datos se encuentra vacia")
    else:
        for i, pintura in enumerate(db):
            if pintura["deleted"] == True:
                contador += 1
                aux.append(db.pop(i))

        for i, pintura in enumerate(db):
            if pintura["deleted"] == True:
                contador += 1
                aux.append(db.pop(i))

        if (contador == 0):
            print("\nNo se encontraron elementos para compactar")
        else:
            # Salvamos la nueva base de datos actualizada
            save_db(db)
            print(
                "\n¡Base de datos compactada con éxito!\nLas pinturas borradas fueron:\n")
            for i, pintura in enumerate(aux):
                print(f'---- {i+1} ----')
                imprimir_pintura(pintura)

            aux.clear()

            # TODO - Codigo para la reorganización de nuestras listas indexadas
