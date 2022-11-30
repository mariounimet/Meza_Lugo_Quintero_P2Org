from funciones import clear, consulta, imprimir_pintura

def buscar(db, auxCota, auxNombre):
    clear()
    while True:
        print('Escoja el número de la operación que desea realizar\n')
        print('1===> Buscar por cota \n2===> Buscar por nombre \n3===> Volver a menu principal ')

        try:
            opcion = int(input('\n\n===>'))
        except:
            input('opción inválida\npresione ENTER para volver al menú principal')
            clear()
            continue

        if opcion < 1 or opcion > 3:
            input('opcion inválida\npresione ENTER para volver al menú principal')
            clear()
            continue
        elif opcion == 1:
            cota = input("Ingrese la cota de la pintura buscada: ")
            pintura = consulta(auxCota, "cota", cota)
            if pintura[0] and not db[pintura[1]["index"]]["deleted"]:
                return pintura[1]["index"]
            else:
                input("Pintura no encontrada\npresione ENTER continuar")
        elif opcion == 2:
            nombre = input("Ingrese el nombre de la pintura buscada: ")
            pintura = consulta(auxNombre, "nombre", nombre)
            if pintura[0] and not db[pintura[1]["index"]]["deleted"]:
                return pintura[1]["index"]
            else:
                input("Pintura no encontrada\npresione ENTER continuar")
        else:
            break
        input("Presione ENTER para continuar")