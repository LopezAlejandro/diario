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

def ver_entradas(search_query = None):
    """Ver todas las entradas"""
    entradas =  Entrada.select().order_by(Entrada.timestamp.desc())

    if search_query:
        entradas = entradas.where(Entrada.contenido.contains(search_query))

    for entrada in entradas:
        timestamp = entrada.timestamp.strftime("%A %B %d,%Y %I:%m%p")
        print(timestamp)
        print("+"*len(timestamp))
        print(entrada.contenido)
        print("(n) Next entrada")
        print("(q) Quit")

        next_action = input("Action: ").lower().strip()
        if next_action == "q":
            break


def search_entradas():
    """Search Entradas"""
    search_query = input("Search query: ").strip()
    ver_entradas(search_query)

def borrar_entrada():
    """Borrar Entrada"""
    print("borrar")

menu = OrderedDict([
    ("a",add_entrada),
    ("v",ver_entradas),
    ("s",search_entradas),
    ("b",borrar_entrada)
])

if __name__ == "__main__":
    create_and_connect()
    menu_loop()
