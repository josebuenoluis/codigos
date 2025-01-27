import psycopg2
from conexion import conexion
from tablas import crear_tablas


def insertarArtista(database):
    """Función para insertar un nuevo artista con un tipo de dato compuesto artist_type."""
    try:
        cursor = database.cursor()
        nombre = input("\nIngrese nombre del artista: ").strip()
        apellido = input("\nIngrese apellido del artista: ").strip()
        nacionalidad = input("\nIngrese nacionalidad: ").strip()

        if not (nombre and apellido and nacionalidad):
            print("\nLos campos no pueden estar vacíos.")
            return

        # Inserta el artista usando un tipo compuesto
        command = """INSERT INTO artistas(datos)
                     VALUES (ROW(%s, %s, %s)::artist_type);"""
        cursor.execute(command, (nombre, apellido, nacionalidad))
        database.commit()
        print("\nArtista insertado correctamente.")
    except Exception as e:
        database.rollback()
        print(f"\nError al insertar artista: {e}")
    finally:
        cursor.close()


def insertarPrueba(database):
    """Función de prueba para insertar un registro en la tabla nombre."""
    try:
        cursor = database.cursor()
        nombre = input("\nIngrese nombre: ").strip()

        if not nombre:
            print("\nEl campo nombre no puede estar vacío.")
            return

        # Asegúrate de que esta tabla exista
        command = """INSERT INTO nombre(id, nombre) VALUES (1, %s);"""
        cursor.execute(command, (nombre,))
        database.commit()
        print("\nRegistro insertado correctamente en la tabla 'nombre'.")
    except Exception as e:
        database.rollback()
        print(f"\nError al insertar prueba: {e}")
    finally:
        cursor.close()


def insertarDisco(database):
    """Función para insertar un nuevo disco con arrays."""
    try:
        cursor = database.cursor()
        titulo = input("\nIngrese título del disco: ").strip()
        año = input("\nIngrese año de lanzamiento: ").strip()
        generos = input("\nIngrese géneros musicales separados por comas: ").strip()
        artistas = input("\nIngrese artistas involucrados separados por comas: ").strip()

        if not (titulo and año and generos and artistas):
            print("\nTodos los campos son obligatorios.")
            return

        # Convierte géneros y artistas en arrays
        generos_array = generos.split(',')
        artistas_array = artistas.split(',')

        command = """INSERT INTO discos(
                        titulo, "año_lanzamiento", generos_musicales, artistas_involucrados)
                     VALUES (%s, %s, ARRAY[%s], ARRAY[%s]);"""
        cursor.execute(command, (titulo, año, generos_array, artistas_array))
        database.commit()
        print("\nDisco insertado correctamente.")
    except Exception as e:
        database.rollback()
        print(f"\nError al insertar disco: {e}")
    finally:
        cursor.close()


def registrarVenta(database):
    """Función para registrar una venta con tipos de datos compuestos y arrays."""
    try:
        cursor = database.cursor()
        cliente = input("\nIngrese nombre del cliente: ").strip()
        fecha = input("\nIngrese la fecha de la venta (YYYY-MM-DD): ").strip()
        discos = input("\nIngrese IDs de discos vendidos separados por comas: ").strip()

        if not (cliente and fecha and discos):
            print("\nTodos los campos son obligatorios.")
            return

        discos_array = discos.split(',')

        command = """INSERT INTO ventas(
                        datos_venta)
                     VALUES (ROW(%s, ROW(%s)::sale_date, ROW(ARRAY[%s])::items_purchased));"""
        cursor.execute(command, (cliente, fecha, discos_array))
        database.commit()
        print("\nVenta registrada correctamente.")
    except Exception as e:
        database.rollback()
        print(f"\nError al registrar venta: {e}")
    finally:
        cursor.close()


def main():
    """Función principal que ejecuta el programa."""
    menu = """\n    1. Insertar artista.
    2. Insertar disco.
    3. Registrar venta.
    4. Salir.\n"""

    try:
        db = conexion()
        crear_tablas(db)

        while True:
            print(menu)
            opcion = input("\nIngrese una opción: ").strip()
            if opcion == "1":
                insertarArtista(db)
            elif opcion == "2":
                insertarDisco(db)
            elif opcion == "3":
                registrarVenta(db)
            elif opcion == "4":
                print("\nSaliendo del programa!\n")
                db.close()
                break
            else:
                print("\nOpción inválida. Intente nuevamente.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
