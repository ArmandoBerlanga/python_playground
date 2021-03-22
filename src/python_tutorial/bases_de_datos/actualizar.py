import mysql.connector as mysqlc

conx = mysqlc.connect(host = "localhost",
                      user = "root",
                      passwd = "",
                      database = "pruebas_ibd")

cursor = conx.cursor()
consulta = "UPDATE libro SET titulo = %s, editorial = %s, area = %s WHERE IDLibro = %s"

valores = ("Leyes maximopoder II", "Casa de Melissa", "No tan derecho", 234)

cursor.execute(consulta, valores) # lo unico que cambia es que ahora se usa executemany
conx.commit() # para insertar informacion en la base de datos

cont = cursor.rowcount # para saber cuantos inserts se han realizado
print (f"Registros actualizados: {cont}") 

cursor.close()
conx.close()