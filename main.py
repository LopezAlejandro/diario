import datetime
import sys

from peewee import *
from collections import OrderedDict

db = SqliteDatabase('diario.db')

class Entrada(Model):
    # contenido
    # timesramp
    contenido = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now())

    class Meta:
        database = db


def create_and_connect():
    """Se conecta y crea la base de datos"""

    db.connect()
    db.create_tables([Entrada])


def menu_loop():
    """Show Menu"""
    choice = None
    while choice != "q":
        print("Pulse q para salir")
        for key, value in menu.items():
            print("{}) {}".format(key, value.__doc__))
        choice= input("Action: ").lower().strip()

        if choice in menu:
            menu[choice]()


def add_entrada():
    """Add Entrada"""
    print("Ingrese su contenido. CTRL + D para terminar")
    data = sys.stdin.read().strip()

    if data:
       # if input('Quiere guardar su entrada? [SN]').lower().strip() != 'n':
       Entrada.create(contenido=data)
       print("Su entrada ha sido guardada")

def ver_entradas():
    """Ver todas las entradas"""
    print("Ver")


def borrar_entrada():
    """Borrar Entrada"""
    print("borrar")

menu = OrderedDict([
    ("a",add_entrada),
    ("v",ver_entradas),
    ("b",borrar_entrada)
])

if __name__ == "__main__":
    create_and_connect()
    menu_loop()
