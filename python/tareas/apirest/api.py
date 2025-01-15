import json
from urllib import request,error
import sys
from datetime import datetime

try:
    fecha = sys.argv[1]

    fecha_datetime = datetime.strptime(fecha, "%d/%m/%Y").timestamp()

    response = request.urlopen(f"https://mempool.space/api/v1/historical-price?currency=EUR&timestamp={fecha_datetime}")

    resultado = json.loads(response.read().decode("utf-8"))

    fecha = datetime.fromtimestamp(float(resultado["prices"][0]["time"])).strftime("%d/%m/%y")

    print(f"\nEl valor del Bitcoin el {fecha} era de {resultado["prices"][0]["EUR"]}€")

except IndexError:
    print("\nDebe ingresar una fecha valida.\n")
except ValueError:
    print("\nDebe ingresar una fecha en el formato <dia>/<mes>/<año>")
except error.URLError:
    print("\nError de conexion")
except Exception as error:
    print(f"Otro error {error} tipo {type(error)}")