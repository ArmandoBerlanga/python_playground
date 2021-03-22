import sys
from os.path import dirname, abspath
dir = dirname(dirname(abspath(__file__)))
sys.path.append(dir)

from utils.mail_module import send_complex
from utils.excel_module import leer_excel

def format_name (name : str): # recibe un nombre de n lugares y solo usa el primer nombre 
    firstname = name.split(" ")[0]
    firstname = firstname.lower()
    firstname = firstname[0].upper() + firstname[1:]
    return firstname

def mandar_mails ():
    info = leer_excel("src/files/mails_github", ["Nombre", "Correo"]) # lee 2 slots de un excel donde estaran el nombre y el correo
    files = ["src/files/Guia instalacion git Windows.pdf", # se almacena la direccion de los files
            "src/files/Guia taller github.pdf"]

    subject = "Liga para ingresar al Taller de GitHub 2021 | SAITC"

    for i in range(len(info["Nombre"])):
        name_receiver = info["Nombre"].get(i)
        mail_receiver = info["Correo"].get(i)

        body = f'''Bienvenido {format_name(name_receiver)},

        mensaje

        '''

        send_complex(mail_receiver, subject, body, True, files)

if __name__ == '__main__':
    mandar_mails()