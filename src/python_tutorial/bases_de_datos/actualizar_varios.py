import mysql.connector as mysqlc

conx = mysqlc.connect(host="localhost",
                      user="root",
                      passwd="",
                      database="pruebas_ibd")

cursor = conx.cursor()
consulta = "UPDATE libro SET titulo = %s, editorial = %s, area = %s WHERE IDLibro = %s"

# 1, 101, 234

values = (
    ("Libro actualizado 1", "casita", "ksitas", 1),
    ("Libro actualizado 2", "casita2", "ksitas2", 101),
    ("Libro actualizado 3", "casita3", "ksitas3", 234)
)

cursor.executemany(consulta, values) # lo unico que cambia es que ahora se usa executemany
conx.commit() 

cont = cursor.rowcount 
print (f"Registros actualizados: {cont}") 

cursor.close()
conx.close()
