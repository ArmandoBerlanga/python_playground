# Diccionarios, son lo mismo que los HashMaps en Java
digits = {
    1 : "uno",
    2 : "dos",
    3 : "tres",
    4 : "cuatro",
    5 : "cinco",
    6 : "seis",
    7 : "siete",
    8 : "ocho",
    9 : "nueve",
    0 : "cero"
}

value = int (input ("Inserte un valor numertico: "))

concat = ""
for c in str(value):
    concat += (digits [int(c)]) + " "

print (concat)
'''
Puedes usar el metodo get en lugar del [key] para añadir parametros y/o que no se genere error
No se ocupan metodos especficios par asignar solo usa el [] y dale nuevos valores
'''

emojis = {
    ":)" : "😀",
    ":(" : "💩"
}

message = input("> ")

for s in message.split(" "):
    print (emojis.get(s, s) + " ", end = " ")




