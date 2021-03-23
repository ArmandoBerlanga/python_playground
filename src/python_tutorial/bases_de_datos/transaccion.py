import mysql.connector as mysqlc

conexion = mysqlc.connect(host = "localhost",
                      user = "root",
                      passwd = "",
                      database = "pruebas_ibd")

try:
    cursor = conexion.cursor()

    consulta = "INSERT INTO autor (nombre, pais) VALUES (%s, %s)"
    valores = ("Guillermo del Toro", "México")
    cursor.execute(consulta, valores)
    conexion.commit() 

    consulta = "DELETE FROM autor WHERE IDautor = %s"
    valores = (74,)
    cursor.execute(consulta, valores)
    conexion.commit() 

except Exception as e:
    conexion.rollback() # sirve para retroceder a antes de la transaccion (no se ejectuan las op pendientes)
    print (f"Ocrrio un error SOS: {e}")

finally:
    cursor.close()
    conexion.close()