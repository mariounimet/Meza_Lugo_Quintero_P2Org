import os

#limpia el terminal
def clear():  #codigo de función obtenido de: https://micro.recursospython.com/recursos/como-limpiar-la-consola.html
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def load_db():
    file = open('proy_2/db.txt', 'r')

    

    return file
