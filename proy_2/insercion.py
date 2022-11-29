from funciones import save_db


def print_error_cota():
    error = '\nPor favor ingrese la cota con un formato adecuado. Por ejemplo: "ABCD1345"'
    return print(error)


def print_error_cota_repetida():
    error_name = '\nError, la cota que intentas ingresar ya se encuentra en la base de datos.'
    return print(error_name)


def insercion(dbe):
    control = True

    while True:

        cota = input(
            'Para registrar una nueva pintura, por favor indique la cota: ')

        # Chequea si es menor a 8 caracteres
        if (len(cota) != 8):
            return print('\nLa cota tiene que tener ocho caracteres.')

        # Chequea si los primeros 4 caracteres son letras
        for i in range(0, 4):
            if not cota[i].isalpha():
                return print(
                    '\nSe han detectado numeros en los primeros 4 caracteres.\nPor favor ingrese la cota con un formato adecuado. Por ejemplo: "ABCD1345"')

        # Chequea si los ultimos 4 caracteres son numeros
        for j in range(4, 8):
            if not cota[j].isnumeric():
                return print(
                    '\nSe han detectado letras en los últimos 4 caracteres.\nPor favor ingrese la cota con un formato adecuado. Por ejemplo: "ABCD1345"')

        # Chequea si la cota ingresada ya se encuentra en la bde
        for k in dbe:
            if k["cota"].upper() == cota.upper():
                return print(
                    '\nError, la cota ingresada ya se encuentra en la base de datos. Abortando...')

        # NOMBRE
        nombre = input(
            "\nIngrese el nombre de la pintura (máximo 30 caracteres): ")

        # Chequeo si el tamaño del nombre es mayor a 30 caracteres
        if (len(nombre) > 30):
            return print("Error, los nombres solo pueden tener máximo 30 caracteres")

        # Chequeo si la pintura ya se encuentra en la base de datos
        for k in dbe:
            if k["nombre"].upper() == nombre.upper():
                return print(
                    "Error, la pintura ingresada ya se encuentra en la base de datos.")

        # PRECIO
        try:
            precio = int(input('\nIngrese el precio de la obra: '))
        except:
            return print('\nEl precio tiene que ser un numero.')

        if precio < 0:
            return print('\nEl precio no puede ser un numero negativo.')

        # STATUS
        try:
            status_input = int(input(
                '\nPara el status ingrese:\n1. EN EXHIBICIÓN\n2. EN MANTENIMIENTO\n> '))
        except:
            return print('Por favor, ingrese un numero')

        if status_input not in range(1, 3):
            return print('Por favor, ingrese un "1" o el "2"')

        if status_input == 1:
            status = 'EN EXHIBICION'
        else:
            status = 'EN MANTENIMIENTO'

        # Agregar a la bde
        pintura = {
            "cota": cota.upper(),
            "nombre": nombre,
            "precio": precio,
            "status": status,
            "deleted": False,
        }

        dbe.append(pintura)
        save_db(dbe)
        print("\n¡Pintura agregada con exito!")
        break
