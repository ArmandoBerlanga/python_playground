import mysql.connector as mysqlc

conx = mysqlc.connect(host="localhost",
                      user="root",
                      passwd="",
                      database="pruebas_ibd")

cursor = conx.cursor()
consulta = "SELECT * FROM autor WHERE IDautor = %s"
at_comp = (1,)

cursor.execute(consulta, at_comp)
registros = cursor.fetchone() # fetch one regresa una lista unica con el atributo deseado a comparar

print ("\nConsultas que cumplan con alguno de los siguientes IDAutor: ")
for r in registros:
    print (r)

cursor.close()
conx.close()