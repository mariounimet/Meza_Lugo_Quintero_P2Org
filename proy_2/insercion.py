from funciones import clear, save_db, consulta, ordenar

def print_error_cota():
    error = '\nPor favor ingrese la cota con un formato adecuado. Por ejemplo: "ABCD1345"'
    return print(error)


def print_error_cota_repetida():
    error_name = '\nError, la cota que intentas ingresar ya se encuentra en la base de datos.'
    return print(error_name)


def insercion(dbe, auxCota, auxNombre):
    clear()
    while True:
        control = True

        cota = input('Para registrar una nueva pintura, por favor indique la cota: ')

        # Chequea si es menor a 8 caracteres
        if (len(cota) != 8):
            input('\nLa cota tiene que tener ocho caracteres.\npresione ENTER')
            clear()
            continue
        else:
            # Chequea si los primeros 4 caracteres son letras
            for i in range(0, 4):
                if not cota[i].isalpha():
                    input('\nPor favor ingrese la cota con un formato adecuado. Por ejemplo: "ABCD1345"\npresione ENTER')
                    control = False
                    break
            if not control:
                clear()
                continue

            # Chequea si los ultimos 4 caracteres son numeros
            for j in range(4, 8):
                if not cota[j].isnumeric():
                    input('\nPor favor ingrese la cota con un formato adecuado. Por ejemplo: "ABCD1345"\npresione ENTER')
                    control = False
                    break
            if not control:
                clear()
                continue

            cota = cota.upper()
            # Chequea si la cota ingresada ya se encuentra en la bde
            verificacion = consulta(auxCota, "cota", cota)
            if verificacion[0]:
                input('\nError, la cota que intentas ingresar ya se encuentra en la base de datos.\npresione ENTER')
                clear()
                continue
        # Ya pasaron todos los chequeos para la cota

        # NOMBRE
        nombre = input("\nIngrese el nombre de la pintura (máximo 30 caracteres): ")

        # Chequeo si el tamaño del nombre es mayor a 30 caracteres
        if (len(nombre) > 30):
            input("Error, los nombres solo pueden tener máximo 30 caracteres\npresione ENTER")
            clear()
            continue
        nombre = nombre.lower()
        # Chequeo si la pintura ya se encuentra en la base de datos

        verificacion = consulta(auxNombre, "nombre", nombre)
        if verificacion[0]:
            input("Error, la pintura ingresada ya se encuentra en la base de datos.\npresione ENTER")
            clear()
            continue
        # PRECIO
        try:
            precio = float(input('\nIngrese el precio de la obra: '))
        except:
            input('\nEl precio tiene que ser un numero.\npresione ENTER')
            clear()
            continue

        if precio < 0:
            input('\nEl precio no puede ser un numero negativo.\npresione ENTER')
            clear()
            continue

        # STATUS
        try:
            status_input = int(input('\nPara el status ingrese:\n1==> EN EXHIBICIÓN\n2==> EN MANTENIMIENTO\n> '))
        except:
            input('Por favor, ingrese un numero\npresione ENTER')
            clear()
            continue

        if status_input not in range(1, 3):
            input('Por favor, ingrese un numero entre el 1 o el 2\npresione ENTER')
            clear()
            continue

        if status_input == 1:
            status = 'E'
        else:
            status = 'EN MANTENIMIENTO'

        # DELETED

        deleted = False

        # Agregar a la bde
        pintura = {
            "cota": cota.upper(),
            "nombre": nombre,
            "precio": precio,
            "status": status,
            "deleted": False,
        }

        dbe.append(pintura)
        auxCota.append({"cota": cota, "index": len(dbe)-1})
        auxCota = ordenar(auxCota, "cota")
        auxNombre.append({"nombre": cota, "index": len(dbe)-1})
        auxNombre = ordenar(auxNombre, "nombre")

        save_db(dbe)
        input("\n¡Pintura agregada con exito!\npresione ENTER para volver al menu principal")
        clear()
        return [dbe, auxCota, auxNombre]
