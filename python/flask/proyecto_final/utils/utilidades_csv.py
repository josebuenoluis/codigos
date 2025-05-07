import csv

#Datos de prueba
data = [
    {
        "dni":"12345678",
        "nombre":"jose bueno"
    }
]

# Funcion para exportar CSV
def exportarCSV(data) -> None:
    headers = ["dni","nombre"]
    # writer = csv.DictWriter("",headers,dialect="csv")
    file = open("C:/Users/jose_/Documents/codigos/python/flask/proyecto_final/utils/prueba.csv")
    writer = csv.writer(
        file,
        delimiter=","
    )
    writer.writerow(("hola"))
    # writer.writeheader()

exportarCSV(data)