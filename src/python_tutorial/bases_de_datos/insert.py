import mysql.connector as mysqlc

conx = mysqlc.connect(host = "localhost",
                      user = "root",
                      passwd = "",
                      database = "pruebas_ibd")

cursor = conx.cursor()
consulta = "INSERT INTO autor (nombre, pais) VALUES (%s, %s)"

valores = ("Carlos Lopez Guatemalo", "Japon")
cursor.execute(consulta, valores)

cont = cursor.rowcount # para saber cuantos inserts se han realizado
print (cont) 

conx.commit() # para insertar informacion en la base de datos
cursor.close()
conx.close()