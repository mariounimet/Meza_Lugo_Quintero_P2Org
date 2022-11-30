from consulta import buscar
from funciones import save_db, clear
def gestion(dbe, codigo_lista, nombre_lista):
    while True:
        clear()
        
        print('\n********GESTION********\n')
        print('Escoja el número de la operación que desea realizar\n')
        print('1===> Poner en Mantenimiento \n2===> Poner en exposicion \n3===> Eliminar Pintura \n4===> Salir de Gestion')
        try:
            opcion = int(input('\n\n===>'))
        except:
            input('opción inválida\npresione ENTER para volver al menú principal')
            continue
        
        if opcion == 4:
            save_db(dbe)
            return dbe

        index = buscar(dbe, codigo_lista, nombre_lista)
        if index == -1:
            input('La pintura no fue encontrada\nPRESIONE ENTER PARA CONTINUAR')
            continue

        if opcion < 1 or opcion > 4:
            input('opcion inválida\npresione ENTER para volver al menú principal')
        elif opcion == 1:
            if dbe[index]["status"] == 'M':
                input('La pintura ya se encuentra en estado de mantenimiento \nPRESIONE ENTER PARA CONTINUAR')
                continue
            else:
                dbe[index]["status"] = "M"
                input("Cambio realizado con exito \nPRESIONE ENTER PARA CONTINUAR")
        elif opcion == 2:
            if dbe[index]["status"] == 'E':
                input('La pintura ya se encuentra en estado de exhibicion \nPRESIONE ENTER PARA CONTINUAR')
                continue
            else:
                dbe[index]["status"] = "E"
                input("Cambio realizado con exito \nPRESIONE ENTER PARA CONTINUAR")

        elif opcion == 3:
            dbe[index]["deleted"] = True
            input("Eliminación exitosa\nPresione ENTER para continuar")

