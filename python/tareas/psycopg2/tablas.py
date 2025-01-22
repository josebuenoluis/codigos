import psycopg2

# a) Catálogo de discos: Registra información como el título, año de lanzamiento, 
# géneros musicales y artistas involucrados. 
# b) Gestión de artistas: Almacena información sobre los artistas, como nombre, 
# apellido y nacionalidad. 
# c) Registro de ventas: Incluye información sobre el cliente, la fecha de la venta y 
# los discos vendidos. 

# Tipos Compuestos: 
# a) Define un tipo compuesto artist_type para representar la información de los 
# artistas. 
# b) Define un tipo compuesto sale_info para registrar información de las ventas. 

# Arrays: 
# a) Usa arrays para asociar varios géneros musicales a un disco. 
# b) Usa arrays para manejar las relaciones entre discos y artistas.

def crear_tablas():
    try:
        conexion = psycopg2.connect(host="localhost",dbname="musica",
                        user="alumno",password="alumno")
        
        cursor = conexion.cursor()

        command = """
        CREATE TYPE artist_type as (
            nombre text,
            apellido text,
            nacionalidad text
        );

        CREATE TYPE sale_info as (
            dni_cliente text,
            fecha_venta date,
            discos_vendidos text[]
        );

        CREATE TABLE discos (
            titulo text PRIMARY KEY,
            año_lanzamiento int,
            generos_musicales text[],
            artistas_involucrados int[]
        );

        CREATE TABLE artista (
            id int PRIMARY KEY,
            datos artist_type
        );
    """
        cursor.execute(command)
        conexion.commit()
        print("Tablas y tipos creados correctamente!")
    except psycopg2.OperationalError as error:
        print(f"\nFallo al conectar con la base de datos: {error}")
    except psycopg2.IntegrityError as error:
        print(f"Error de integridad en la base de datos: {error}")
crear_tablas()