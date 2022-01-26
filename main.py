from peewee import *
import datetime

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


def add_entrada():
    """Add Entrada"""


def ver_entradas():
    """Ver todas las entradas"""


def borrar_entrada(entrada):
    """Borrar Entrada"""


if __name__ == "__main__":
    create_and_connect()
    menu_loop()
