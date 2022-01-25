from peewee import *

db=SqliteDatabase("diario.db")


class Entrada(Model):
    #contenido
    #timesramp

    class Meta:
        databaase=db

def menu_loop():
    """Show Menu"""

def add_entrada():
    """Add Entrada"""

def ver_entradas():
    """Ver todas las entradas"""

def borrar_entrada(entrada):
    """Borrar Entrada"""

