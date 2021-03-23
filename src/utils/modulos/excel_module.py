import pandas as pd

def crear_excel (data : dict, file_name : str):
    df = pd.DataFrame(data, columns = data.keys())
    df.to_excel(file_name + ".xlsx", sheet_name = "Hoja 1")


def leer_excel (file_name : str, keys):
    df = pd.read_excel(file_name + ".xlsx")

    return df

if __name__ == '__main__':
    data = {
        "nombre" : ["Armando", "Jose",],
        "correo" : ["Jose.berlangam@udem.edu", "ArmandoBerlanga2708@gmail,com",]
    }

    # crear_excel(data, "Ejemplo")
    df = leer_excel("mails_github", keys = ["Nombre", "Correo"])

    for name in df["Nombre"]:
        print (name)

