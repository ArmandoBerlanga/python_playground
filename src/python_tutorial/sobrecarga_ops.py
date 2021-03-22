class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre (self):
        return self.__nombre

    def set_nombre (self, nombre):
        self.__nombre = nombre

    def __add__ (self, otro):
        return self.__nombre + otro.__nombre

    '''
    Sirve para la sobrecarga de los diferentes operadores segun la clase, hacemos que se soporten
    Podria funcionar tambien que uses el metodo __str__
    add para suma
    sub para resta
    mul para multiplicacion
    truediv para division decimal
    floordiv para la division entera
    mod para el modulo
    pow para exponente

    puede haber sobreesctiruta de todo el __gt__ y el __lt__ o el __eq__ son ejemplos
    Con estos metodos sobreescritos podemos hacer uso de la comapracion de objetos
    '''


if __name__ == '__main__':
    p1 = Persona ("Carlos")
    p2 = Persona ("Juana")

    print (p1 + p2)
    
    