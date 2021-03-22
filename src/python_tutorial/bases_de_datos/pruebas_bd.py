import mysql.connector as mysqlc

# primeramente se inicializa un objeto conexion para poder conectarse a la BD
conx = mysqlc.connect(host="localhost",
                      user="root",
                      passwd="",
                      database="pruebas_ibd")

cursor = conx.cursor() # luego con el objeto cursor lo que podemos hacer es hacer consultas
consulta = "SELECT * FROM autor"  # establecemos la consulta
cursor.execute(consulta)  # se la pasamos a nuestro cursos 
registros = cursor.fetchall() # con este metodo se nos regresa una lista de tuplas de los datos

print("\nInformacion de la base de datos")
for r in registros:
    print(r)

cursor.close()  # se cierran los repsectivos objetos
conx.close()
