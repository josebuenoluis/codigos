import csv

#Datos de prueba
data = [
    {
        "dni":"12345678",
        "nombre":"jose bueno"
    },
    {
        "dni":"12345678",
        "nombre":"jose bueno"
    }
]

def exportarCSV(data:list[dict]) -> None:
    """Funcion para exportar CSV, desde
    una lista de diccionarios"""
    #Obtenemos los encabezados de los datos recibidos
    # para el csv
    headers = [
        header for header in data[0].keys()
    ]
    with open("utils/prueba.csv","w") as file:
        writer = csv.DictWriter(file,fieldnames=headers,delimiter=";",lineterminator="\n")
        writer.writeheader()
        writer.writerows(data)


