import psycopg2
from conexion import conexion
from tablas import crear_tablas


# Se debe crear un sistema para gestionar la información de una tienda de 
# música. Este sistema permitirá registrar discos, artistas, géneros musicales y 
# las ventas realizadas. Cada disco puede involucrar varios artistas y estar 
# clasificado en múltiples géneros. Además, las ventas deben incluir información 
# sobre los clientes y los discos vendidos.

def insertarArtista(cursor) -> bool:
    """Funcion para insertar un nuevo artista con
    un tipo de dato compuesto artist_type"""
    pass

def insertarDisco(cursor) -> bool:
    """Funcion para insertar un nuevo disco con arrays que
    contendran datos para relacionar estos discos con otros datos"""
    pass

def registrarVenta(cursor) -> bool:
    """Funcion para registrar una venta con tipos de 
    datos compuestos y un array para almacenar los id de discos"""
    pass

def eliminarArtista(cursor) -> bool:
    """Funcion para eliminar un artista por su id."""
    pass

def eliminarDisco(cursor) -> bool:
    """Funcion para eliminar un dico por su id."""
    pass



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
        
        match user:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                print("\nSaliendo del programa!\n")
                db.close()
                break