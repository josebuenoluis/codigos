import psycopg2


def conexion():
    """Funcion para crear la conexion con la base de datos."""
    try:
        conexion = psycopg2.connect(host="localhost",dbname="musica",
                            user="alumno",password="alumno")
        
    except psycopg2.OperationalError as error:
        print(f"\nFallo al conectar con la base de datos: {error}")
        conexion = None
    except psycopg2.IntegrityError as error:
        print(f"Error de integridad en la base de datos: {error}")
        conexion = None

    return conexion