# Programa creado por José Armando Berlanga Mendoza
# Creado el 17 de febrero de 2021
# Descripción: ejercicio sobre recursividad

def voltear_palabra (s): # metodo para voltear una palabra u oracion completamente
    l = len(s)
    if (l == 0):
        return ""
    else:
        return s[l-1:] + voltear_palabra (s[0:l-1])

def es_palindrome (s): # metodo para evaluar si una palabra u oracion es palindrome (que estan iguales al derecho y al reves)
    if (len(s) > 1):
        if s[len(s)-1] == s [0]:
            return es_palindrome (s [1 : len(s)-1])
        else:
            return False
    else:
        return True

def imprimir_pino (reglon, cont): # metodo para la impresion de un pino centrado
    if (reglon == 0):
        return ""
    else:
        for i in range (reglon, 0, -1):
            print (" ", end = "")
            if i == 0:
                break
        for i in range (cont+1, 0, -1):
            print ("*", end = "")
            if i == 0:
                break

        print()
        return imprimir_pino(reglon-1, cont+2)

def formatear_palabra (s): # metodo de formateo
    acentos = "áéíóú"
    sinAcentos = "aeiou"

    s = s.lower().replace(" ", "").replace(".", "").replace(",", "")
    for char in s:
        pos = acentos.find(char)
        if pos != -1:
            s = s.replace(acentos[pos], sinAcentos[pos])

    return s

# Given a string s, find the length of the longest substring without repeating characters.
def longest_substring(s):

    if len(s) == 1:
        return 1

    elif s == "":
        return 0
    
    conts = []
    for i in range (len(s)-1):
        chars = []
        cont = 0
        j = i
        while s[j] not in chars and j < len(s)-1:
            cont+=1
            chars.append(s[j])
            j+=1
        
        conts.append(cont)

    return max (conts)

if __name__ == '__main__':

    option = -1
    while (option == -1):
        print ("\n[1] Voltear el orden de una palabra u oracion\n[2] Evaluar si una palabra o frase es palindrome\n[3] Imprimir un pino")
 
        option = int (input("\nIngrese un numero segun las opciones dadas: "))
        if option != 1 and option != 2 and option != 3:
            print("\nNo has ingresado un num valido, vuelve a ingresarlo")
            option = -1

    if option == 1:
        s = input("\nIngrese el texto a voltear: ")
        print("\nResultado: " + voltear_palabra(s))

    elif option == 2:
        s = input("\nIngrese el texto a evaluar: ")
        # s = "A mamá Roma le aviva el amor a papá y a papá Roma le aviva el amor a mamá."
        print ("\n\"" + s +"\"" + ", es palindrome" if (es_palindrome(formatear_palabra(s))) else ", no es Palindrome")
        
    else:
        pisos = int (input("\nIngrese el numero de pisos de la piramide: "))
        print()
        imprimir_pino(pisos, 0)
        print()
