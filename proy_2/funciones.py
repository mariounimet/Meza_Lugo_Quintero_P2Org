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
