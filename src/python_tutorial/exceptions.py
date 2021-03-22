
salida = True
while salida:
    try :
        age = int(input("\nDame tu edad: "))
        print (age)
        salida = False
        
    except ValueError:
        print("\nERROR: has ingresado un valor no valido")
        

salida = True
while salida:
    try :
        num = int(input("\nDame un numero para dividir: "))
        print (10000/num)
        salida = False
        
    except ZeroDivisionError:
        print("\nERROR: has ingresado un valor igual a 0, no se puede usar como divisor")
