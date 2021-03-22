import mysql.connector as mysqlc

conx = mysqlc.connect(host = "localhost",
                      user = "root",
                      passwd = "",
                      database = "pruebas_ibd")

cursor = conx.cursor()
consulta = "INSERT INTO autor (nombre, pais) VALUES (%s, %s)"

valores = (("Carlos Lopez Guatemalo", "Japon"), 
           ("Fernanda Alvarez Jimena", "How to be A dumb Ass"),
           ("Fresia Milipza Perez Garza", "Econocosas"),)

cursor.executemany(consulta, valores) # lo unico que cambia es que ahora se usa executemany
conx.commit() # para insertar informacion en la base de datos

cont = cursor.rowcount # para saber cuantos inserts se han realizado
print (cont) 

cursor.close()
conx.close()