#  Strings
print ("\nEjemplo de Strng formateado")
name = "armando"
lastName = "Berlanga"
message = f"{name} tiene como apellido \"{lastName}\""

print (message + "\n")

print ("Ejemplo de metodos String")
phrase = "Fresia es el amor de mi vida"
length = len(phrase) # devuelve la longuitud de los Strings
print(length)

phrase = phrase.upper() # devuelve el string como mayus
print (phrase)

pos = phrase.find("E")
print (pos)

newPhrase = phrase.lower()
newPhrase = newPhrase.replace("fresia", "el mango") # remplazo de Strings por otros, tambien aplica en chars
print (newPhrase)

print ("mango" in newPhrase) # devuelve true si es que esta mango dentro, es un op booleano


print ("\n")

#Notas
'''
Se pueden usar comillas triples para poder usar un String multi linea
Hay indixes negativos para la consulta del String desde atras    
No hay metodo de Substring, se usa como un arreglo para charAt o rango s_var[0:2]

- Se puede usar el rango de la sigiente manera 
    [:x], de 0 a x o 
    [x:] de x hasta el final
    [:] para todos los caracteres

- Hay Strings con formato que usan poniendo un f minuscula
'''

