import sys
from os.path import dirname, abspath
dir = dirname(dirname(abspath(__file__)))
sys.path.append(dir)

from utils.modulos.db_module import ConexionBD
from Persona import Persona

class PersonaDAO:
    __bd = ConexionBD ("localhost", "root", "", "pruebas")
    
    def __init__(self):
        self.__select = "SELECT * FROM persona ORDER BY id_persona"
        self.__delete = "DELETE FROM persona WHERE id_persona = %s"

    def select_from (self):
        cursor = self.__bd.obtener_cursor()
        cursor.execute(self.__select)
        registros = cursor.fetchall()

        ppl = []
        for r in registros:
            p = Persona (r[0], r[1], r[2], r[3], r[4])
            ppl.append(p)

        return ppl

    def delete_from (self):
        pass

if __name__ == '__main__':
    pdao = PersonaDAO ()
    ppl = pdao.select_from()

    for p in ppl:
        print (p)