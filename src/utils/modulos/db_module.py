import mysql.connector as mysqlc

class ConexionBD:
    def __init__(self, host, user, passwd, db_name):
        self.__host = host
        self.__user = user
        self.__passwd = passwd
        self.__db_name = db_name
        self.__conexion = None
        self.__cursor = None
    
    def obtener_conexion (self):
        if self.__conexion is None:
            try:

                self.__conexion = mysqlc.connect(host = self.__host, user = self.__user, 
                    passwd = self.__passwd, database = self.__db_name)

                return self.__conexion

            except Exception as e:
                print(f"Error al conectar en la base de datos \n{e}")
        else:
            return self.__conexion

    
    def obtener_cursor (self):
        if self.__cursor is None:

            try:

                self.__cursor = self.obtener_conexion().cursor()
                return self.__cursor

            except Exception as e:
                print(f"Error al crear el cursor en la base de datos \n{e}")

        else:
            return self.__cursor


    def cerrar_objetos(self):
        if self.__cursor is not None:
            try:

                self.__cursor.close()
                self.__conexion.close()

            except Exception as e:
                print(f"Error al cerrar los objetos cursor y conexion \n{e}")
            

if __name__ == '__main__':
    bd = ConexionBD ("localhost", "root", "", "pruebas_ibd")
    print(bd.obtener_conexion())
    print(bd.obtener_cursor())
    bd.cerrar_objetos()
