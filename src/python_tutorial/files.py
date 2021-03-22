# try:

#     file = open ("Archivo.txt", "w")
#     file.write("Hola como estas")
#     file.write("\nYo muy bien perrillo y tu?")
    
# except Exception as e:
#     print(e)
# finally:
#     file.close()


try:

    file = open ("Archivo.txt", "r")
    # print (file.read()) #lee todo
    # print(file.read(12)) # lee por nums de chars
    # print(file.readline()) # lee 1 solo linea
    # print(file.readlines()) # regresa una lista con todas las lineas

    for line in file:
        print (line)
    
except Exception as e:
    print(e)
finally:
    file.close()

    '''
    "r" - Read - Default value. Opens a file for reading, error if the file does not exist
    "a" - Append - Opens a file for appending, creates the file if it does not exist
    "w" - Write - Opens a file for writing, creates the file if it does not exist
    "x" - Create - Creates the specified file, returns an error if the file exist

    Se pude leer por rutas
    con w+ se puede leer y escribir informacion
    '''
