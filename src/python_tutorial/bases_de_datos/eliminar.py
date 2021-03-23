import mysql.connector as mysqlc

conx = mysqlc.connect(host = "localhost",
                      user = "root",
                      passwd = "",
                      database = "pruebas_ibd")

cursor = conx.cursor()
consulta = "DELETE FROM autor WHERE IDautor = %s"

valores = (3,)# solo borra los no relacionados
cursor.execute(consulta, valores) 

conx.commit() # para insertar informacion en la base de datos

eliminados = cursor.rowcount # para saber cuantos inserts se han realizado
print (f"eliminados {eliminados}") 

cursor.close()
conx.close()