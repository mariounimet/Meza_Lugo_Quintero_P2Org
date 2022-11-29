import sys
from funciones import clear, load_db, save_db, crear_listas, ordenar
from insercion import insercion
from consulta import buscar
from gestion import gestion
from compactar import compactar


def main():
    # importar base de datos
    db = load_db()
    auxiliares = crear_listas(db)
    aux_cota = auxiliares[0]
    aux_nombre = auxiliares[1]

    aux_cota = ordenar(aux_cota, "cota")
    aux_nombre = ordenar(aux_nombre, "nombre")

    # menu principal
    while True:
        #clear()

        print('\n********LOUVRE ADMINISTRATOR********\n')
        print('Escoja el número de la operación que desea realizar\n')
        print('1===> Registrar pintura \n2===> Buscar pintura \n3===> Gestionar pinturas \n4===> Compactar base de datos \n5===> Salir el sistema')

        try:
            opcion = int(input('\n\n===>'))
        except:
            input('opción inválida\npresione ENTER para volver al menú principal')
            continue

        if opcion < 1 or opcion > 5:
            input('opcion inválida\npresione ENTER para volver al menú principal')
        elif opcion == 1:
            inserciones = insercion(db, aux_cota, aux_nombre)
            db = inserciones[0]
            aux_cota = inserciones[1]
            aux_nombre = inserciones[2]

        elif opcion == 2:
            buscar(db, aux_cota, aux_nombre)

        elif opcion == 3:
            gestion()

        elif opcion == 4:
            compactar()

        else:
            sys.exit()


main()
