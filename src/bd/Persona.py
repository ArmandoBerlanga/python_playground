import sys
from os.path import dirname, abspath
dir = dirname(dirname(abspath(__file__)))
sys.path.append(dir)

from utils.modulos.db_module import ConexionBD

class Persona:
    
    def __init__(self, id : int, nombre : str, apellido_paterno: str, apellido_materno : str, edad : int):
        self.__id = id
        self.__nombre = nombre
        self.__apellido_paterno = apellido_paterno
        self.__apellido_materno = apellido_materno
        self.__edad = edad

    def set_id (self, id : int):
        self.__id = id

    def get_id (self, id : int):
        return self.__id

    def set_nombre (self, nombre : str):
        self.__nombre = nombre

    def get_nombre (self):
        return self.__nombre

    def set_apellido_paterno (self, apellido_paterno : str):
        self.__apellido_paterno = apellido_paterno

    def get_apellido_paterno (self):
        return self.__apellido_paterno

    def set_apellido_materno (self, apellido_materno : str):
        self.__apellido_paterno = apellido_materno

    def get_apellido_materno (self):
        return self.__apellido_materno

    def set_edad (self, edad : int):
        self.__edad = edad

    def get_edad (self):
        return self.__edad

    def __str__(self):
        return f"{self.__nombre} {self.__apellido_paterno} {self.__apellido_materno} [{self.__edad} años]"


if __name__ == '__main__':
    p1 = Persona (None, "Jose", "Beralnga", "Mendoza", 19)
    p2 = Persona (None, "Armando", "Mendoza", "Sanchez", 29)
    p3 = Persona (None, "Jose", "Lorenzo", "Mendoza", 24)
    p4 = Persona (None, "Pepe", "Beralnga", "Chavez", 49)

    ppl = [p1, p2, p3, p4]
