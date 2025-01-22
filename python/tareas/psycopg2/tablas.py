import psycopg2

def crear_tablas(conexion):
    """Funcion para crear las tablas de la base de datos si no existen."""
    try:
        cursor = conexion.cursor()
        command = """
        CREATE TYPE artist_type as (
            nombre text,
            apellido text,
            nacionalidad text
        );

        CREATE TYPE sale_date as (
            fecha date
        );

        CREATE TYPE items_purchased as (
            id INTEGER,
            articulos_comprados text[]
        );

        CREATE TYPE sale_info as (
            customer_name VARCHAR(100),
            fecha_venta sale_date,
            discos_vendidos items_purchased
        );

        CREATE TABLE discos (
            id SERIAL PRIMARY KEY,
            titulo text UNIQUE,
            año_lanzamiento int,
            generos_musicales text[],
            artistas_involucrados int[]
        );

        CREATE TABLE artistas (
            id SERIAL PRIMARY KEY,
            datos artist_type NOT NULL
        );

        CREATE TABLE ventas (
            id SERIAL PRIMARY KEY,
            datos_venta sale_info NOT NULL
        );
    """
        cursor.execute(command)

        conexion.commit()

        cursor.close()

        print("Tablas y tipos creados correctamente!")


    except psycopg2.OperationalError as error:
        print(f"\nFallo al conectar con la base de datos: {error}")
        
    except psycopg2.IntegrityError as error:
        print(f"Error de integridad en la base de datos: {error}")

    except psycopg2.errors.DuplicateObject:
        print(f"Hay tablas y tipos duplicados.")