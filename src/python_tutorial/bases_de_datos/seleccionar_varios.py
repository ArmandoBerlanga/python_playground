import mysql.connector as mysqlc

conx = mysqlc.connect(host = "localhost",
                      user = "root",
                      passwd = "",
                      database = "pruebas_ibd")

cursor = conx.cursor()
consulta = "SELECT * FROM autor WHERE IDautor IN %s"
at_comp = ((1,2,3),) # se indican cuales son los ID que se igualaran en la parte de IN %s

cursor.execute(consulta % at_comp) # se pasa como parametro los ID o param a igualar con el signo % y no ,
registros = cursor.fetchall() # se usa un fetchall por que pueden ser varios

print ("\nConsultas que cumplan con alguno de los siguientes IDAutor: \n")
for fila in registros: # se itera y acomoda por atributo y mensaje
    print ("IDautor: " + str(fila[0]))
    print ("Nombre: " + str(fila[1]))
    print ("Pais: " + str(fila[2]) + "\n")

cursor.close()
conx.close()