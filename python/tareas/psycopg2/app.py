import psycopg2
from conexion import conexion
from tablas import crear_tablas


# Se debe crear un sistema para gestionar la información de una tienda de 
# música. Este sistema permitirá registrar discos, artistas, géneros musicales y 
# las ventas realizadas. Cada disco puede involucrar varios artistas y estar 
# clasificado en múltiples géneros. Además, las ventas deben incluir información 
# sobre los clientes y los discos vendidos.

def insertarArtista() -> bool:
    """Funcion para insertar un nuevo artista con
    un tipo de dato compuesto artist_type"""
    nombre = input("\nIngrese nombre del artista: ")
    apellido = input("\nIngrese apellido del artista: ")
    nacionalidad = input("\nIngrese nacionalidad: ")
    if nombre != "" and apellido != "" and nacionalidad != "":
        command = f"""INSERT INTO artistas(datos)
        VALUES (({nombre},{apellido},{nacionalidad})::artist_type);"""
        cursor = db.cursor()
        cursor.execute(command)
        db.commit()
        cursor.close()
    else:
        print("\nLos campos no pueden estar vacios.")

def insertarDisco(cursor) -> bool:
    """Funcion para insertar un nuevo disco con arrays que
    contendran datos para relacionar estos discos con otros datos"""
    command = """INSERT INTO public.discos(
	titulo, "año_lanzamiento", generos_musicales, artistas_involucrados)
	VALUES (%s,%s,ARRAY[%s], ARRAY[%s]);"""

def registrarVenta(cursor) -> bool:
    """Funcion para registrar una venta con tipos de 
    datos compuestos y un array para almacenar los id de discos"""
    command = """INSERT INTO public.ventas(
	datos_venta)
	VALUES (ROW(%s,ROW(%s)::sale_date,
	ROW(ARRAY[%s])::items_purchased));"""
    
def eliminarArtista(cursor) -> bool:
    """Funcion para eliminar un artista por su nombre."""
    command = """DELETE FROM public.artistas
	WHERE id = %s;"""

def eliminarDisco(cursor) -> bool:
    """Funcion para eliminar un dico por su nombre."""
    command = """DELETE FROM public.discos
	WHERE id = %s;"""


if __name__ == '__main__':

    db = conexion()
    
    crear_tablas(db)

    menu = """\n    1. Insertar artista.
    2. Insertar disco.
    3. Registrar venta.
    4. Salir.\n"""
    while True:
        print(menu)
        user = input("\nIngrese una opcion: ")
        cursor = db.cursor()
        match user:
            case "1":
                if insertarArtista():
                    print("\nArtista insertado correctamente!")
                else:
                    print("\nNo se ha podido insertar el artista...")
            case "2":
                if insertarDisco(cursor):
                    print("\nDisco insertado correctamente!")
                else:
                    print("\nNo se ha podido insertar el disco...")
            case "3":
                if registrarVenta(cursor):
                    print("\nVenta registrada correctamente!")
                else:
                    print("\nNo se ha podido registrar la venta...")
            case "4":
                print("\nSaliendo del programa!\n")
                db.close()
                break