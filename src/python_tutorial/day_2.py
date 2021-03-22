# while loops

command = ""
started = False
while True:
    command = input("Ingrese el comando: ").lower()
    if command == "quit":
        print("bye bye bro")
        break

    elif command == "start":
        if not started:
            started = True
            print("car started")
        else:
            print ("car already started")

    elif command == "stop":
        print("car stopped")

    else:
        print("I dont understnad bro")

else:
    print ("Is not working ur program") # solo funciona cuandoe sale del loop 

'''
 En este lenguaje se puede usar un else en los While
'''

# for loops