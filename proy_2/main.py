import sys
from funciones import clear, load_db, save_db, crear_listas
from insercion import insercion
from consulta import consulta
from gestion import gestion
from compactar import compactar


def main():
    # importar base de datos
    db = load_db()
    auxiliares = crear_listas(db)
    aux_cota = auxiliares[0]
    aux_nombre = auxiliares[1]
    # menu principal
    while True:
        clear()

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
            insercion(db)

        elif opcion == 2:
            consulta()

        elif opcion == 3:
            gestion()

        elif opcion == 4:
            compactar()

        else:
            sys.exit()


main()
